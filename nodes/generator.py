"""
Generator node for CBMC harness generator workflow.
"""
import time
import os
import re
import json
import logging
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from core.embedding_db import code_collection, query_pattern_db

# Set up logging
logger = logging.getLogger("generator")

def generator_node(state):
    """Generates or refines CBMC-compatible harness for the current function."""
    # Get the global LLM instance
    from utils.llm_utils import setup_llm
    llm = setup_llm()

    # Start timing
    generation_start = time.time()
    
    func_name = state.get("current_function", "")
    logger.info(f"Generating harness for function: {func_name}")
    
    # Get result directories from state
    result_directories = state.get("result_directories", {})
    harnesses_dir = result_directories.get("harnesses_dir", "harnesses")  # Default to "harnesses" if not found
    
    # Check if this is a refinement
    improvement_recommendation = state.get("improvement_recommendation", "")
    is_refinement = bool(improvement_recommendation)
    
    # Track harness history
    harness_history = state.get("harness_history", {})
    if func_name not in harness_history:
        harness_history[func_name] = []
    
    # Get previous harness if refining
    previous_harness = ""
    cbmc_result = {}
    if is_refinement and func_name in state.get("harnesses", {}):
        previous_harness = state.get("harnesses", {})[func_name]
        # Add to history if not already there
        if previous_harness not in harness_history[func_name]:
            harness_history[func_name].append(previous_harness)
        # Get the CBMC results for analysis
        cbmc_result = state.get("cbmc_results", {}).get(func_name, {})
    
    # Get function code
    function_result = code_collection.get(ids=[func_name], include=["documents", "metadatas"])
    
    if not function_result["ids"]:
        logger.error(f"Function {func_name} not found in database")
        return {
            "messages": [AIMessage(content=f"Error: Function {func_name} not found in database.")],
            "next": "junction"
        }
    
    func_code = function_result["documents"][0]
    func_metadata = function_result["metadatas"][0]
    
    # Extract function dependencies from metadata if available
    function_calls = func_metadata.get("function_calls", "[]")
    try:
        if isinstance(function_calls, str):
            function_calls = json.loads(function_calls)
        else:
            function_calls = []
    except json.JSONDecodeError:
        function_calls = []
    
    # Find and add implementations for function dependencies
    dependency_implementations = {}
    for called_func in function_calls:
        # Skip standard library functions and control flow statements
        if called_func in ["if", "for", "while", "switch", "return", "malloc", "free",
                          "memset", "memcpy", "printf", "fprintf", "sprintf"]:
            continue
            
        # Search for the function in the database
        dep_results = code_collection.query(
            query_texts=[called_func], 
            n_results=5
        )
        
        if dep_results["ids"] and len(dep_results["ids"][0]) > 0:
            for i, dep_id in enumerate(dep_results["ids"][0]):
                # Check if this is an exact match
                if called_func in dep_id:
                    dep_result = code_collection.get(ids=[dep_id], include=["documents", "metadatas"])
                    if dep_result["ids"]:
                        dep_code = dep_result["documents"][0]
                        dep_metadata = dep_result["metadatas"][0]
                        
                        # Check if this is just a declaration or a full implementation
                        if not dep_metadata.get("is_declaration_only", True):
                            logger.info(f"Found implementation for dependency: {called_func}")
                            dependency_implementations[called_func] = {
                                "code": dep_code,
                                "metadata": dep_metadata
                            }
                            break
                            
    logger.info(f"Found {len(dependency_implementations)} function dependencies with implementations")

    # ENHANCED HANDLING FOR "NO BODY FOR CALLEE" ERRORS
    if is_refinement:
        # Check if previous CBMC result had "no body for callee" errors
        missing_bodies = []
        if cbmc_result and cbmc_result.get("stdout", ""):
            # Extract all missing function bodies using regex
            cbmc_stdout = cbmc_result.get("stdout", "")
            no_body_matches = re.findall(r'no body for callee (\w+)', cbmc_stdout)
            missing_bodies = list(set(no_body_matches))  # Remove duplicates
        
        if missing_bodies:
            logger.info(f"Detected {len(missing_bodies)} missing function bodies: {', '.join(missing_bodies)}")
            # Find bodies for these missing functions
            missing_function_bodies = {}
            
            # Search for each missing function across all source files
            for missing_func in missing_bodies:
                logger.info(f"Searching for implementation of missing function: {missing_func}")
                
                # First, try direct match by function name
                try:
                    query_results = code_collection.query(
                        query_texts=[f"function {missing_func}"],
                        n_results=5
                    )
                    
                    # Check each result for exact function match
                    if query_results["ids"] and len(query_results["ids"][0]) > 0:
                        for i, result_id in enumerate(query_results["ids"][0]):
                            # Check if this is the function we're looking for
                            if missing_func in result_id and not result_id.startswith("declaration:"):
                                func_result = code_collection.get(ids=[result_id], include=["documents", "metadatas"])
                                if func_result["ids"]:
                                    # Found the implementation
                                    logger.info(f"Found implementation for {missing_func}: {result_id}")
                                    missing_function_bodies[missing_func] = {
                                        "id": result_id,
                                        "code": func_result["documents"][0],
                                        "is_implementation": True,
                                    }
                                    break
                except Exception as e:
                    logger.error(f"Error searching for {missing_func}: {str(e)}")
            
            # FIXED: Never attempt to generate a harness for missing functions
            # Just include the implementation directly in the current harness
            if missing_function_bodies:
                # Create function implementation section to include in prompt
                implementations_section = "\n\nIMPORTANT: Add these function implementations to your harness:\n\n"
                for missing_func_name, info in missing_function_bodies.items():
                    implementations_section += f"Function: {missing_func_name}\n```c\n{info['code']}\n```\n\n"
                    
                # Append this to the improvement recommendation
                improvement_recommendation += implementations_section
                logger.info(f"Added {len(missing_function_bodies)} missing function implementations to improvement recommendation")
            else:
                # If we couldn't find implementations, provide stub approach
                stub_section = """
                \nIMPORTANT: The following functions have no available implementations:
                """
                for func in missing_bodies:
                    stub_section += f"\n- {func}"
                    
                stub_section += """
                \nSince implementations are not available, you need to either:
                1. Create minimal stub implementations that satisfy CBMC verification
                2. Modify the harness to avoid calling these functions directly
                3. Use __CPROVER_assume() to constrain return values instead of calling functions

                Example approach for missing functions:
                ```c
                // Option 1: Minimal stub that satisfies CBMC verification
                HTTPStatus_t addHeader(HTTPRequestHeaders_t* pRequestHeaders, 
                                      const char* pName, size_t nameLen,
                                      const char* pValue, size_t valueLen) {
                    // Return a valid status without side effects
                    return HTTPSuccess;
                }

                // Option 2: Modify your test strategy to avoid the function call
                // Instead of: status = addHeader(...);
                // Do: 
                HTTPStatus_t status = nondet_HTTPStatus_t();
                __CPROVER_assume(status == HTTPSuccess || status == HTTPInvalidParameter);
                ```

                Choose the approach that best fits each missing function.
                """
                
                # Append this to the improvement recommendation
                improvement_recommendation += stub_section
                logger.info(f"Added stub approach suggestions for {len(missing_bodies)} missing functions")
    
    # Get pattern information
    patterns_result = query_pattern_db(func_code)
    
    # Analyze function properties
    has_malloc = "malloc(" in func_code
    has_free = "free(" in func_code
    has_array_access = "[" in func_code and "]" in func_code
    has_pointer_arithmetic = "*" in func_code or "->" in func_code
    has_division = "/" in func_code or "%" in func_code
    has_type_conversion = "(" in func_code and ")" in func_code and any(type_name in func_code for type_name in ["int", "char", "float", "double", "size_t", "unsigned", "long"])
    
    # Produce targeted verification guide
    verification_checks = []
    if has_malloc or has_free:
        verification_checks.append("--memory-leak-check: Verify memory is properly allocated and freed")
    if has_array_access:
        verification_checks.append("--bounds-check: Verify array accesses are within bounds")
    if has_pointer_arithmetic:
        verification_checks.append("--pointer-overflow-check: Verify pointer arithmetic is safe")
    if has_division:
        verification_checks.append("--div-by-zero-check: Verify divisors are non-zero")
    if has_type_conversion:
        verification_checks.append("--conversion-check: Verify type conversions are safe")
    
    # Construct verification guide
    if verification_checks:
        verification_guide = "Relevant CBMC Verification Checks for this function:\n" + "\n".join(verification_checks)
    else:
        verification_guide = "This function doesn't appear to need special CBMC verification checks beyond basic assertions."
    
    # Access the CBMC framework info from state
    cbmc_framework = state.get("cbmc_framework", {
        "has_framework": False,
        "utility_functions": {},
        "cbmc_headers": [],
        "harness_naming_patterns": {}
    })
    
    # Process CBMC framework information if available
    if cbmc_framework.get("has_framework", False):
        # Format CBMC headers information
        cbmc_headers_list = cbmc_framework.get("cbmc_headers", [])
        cbmc_headers_text = ""
        if cbmc_headers_list:
            cbmc_headers_text = "Available CBMC Headers:\n"
            for header in cbmc_headers_list:
                cbmc_headers_text += f"- {header}\n"
        
        # Format utility functions information
        utility_functions = cbmc_framework.get("utility_functions", {})
        utility_functions_text = ""
        if utility_functions:
            utility_functions_text = "Available CBMC Utility Functions:\n"
            for func_name, func_info in utility_functions.items():
                header = func_info.get("header", "unknown")
                utility_functions_text += f"- {func_name} (from {header})\n"
        
        # Determine appropriate harness naming pattern
        original_func_name = func_name.split(":")[-1] if ":" in func_name else func_name
        harness_name = f"{original_func_name}_harness"
        naming_patterns = cbmc_framework.get("harness_naming_patterns", {})
        if original_func_name in naming_patterns:
            harness_name = naming_patterns[original_func_name]
        
        # Create framework guidance
        framework_section = f"""
        CBMC verification framework detected. Use these resources for better verification:
        
        {cbmc_headers_text}
        {utility_functions_text}
        
        Recommended harness structure:
        1. Include the necessary CBMC headers listed above
        2. Use CBMC utility functions for memory allocation and validation
        3. Name your harness function: {harness_name}()
        4. Use "__CPROVER_assume()" for input constraints
        5. If the function has local implementations, provide them
        """
    else:
        # Standard guidance if no CBMC framework detected
        framework_section = """
        No specialized CBMC framework detected. Use standard CBMC harness approach:
        1. Create a main() function that calls the target function
        2. Use malloc() with appropriate size checks
        3. Use __CPROVER_assume() for input constraints
        4. Free any allocated memory
        """
    
    # Generate dependency information section
    dependency_section = ""
    if dependency_implementations:
        dependency_section = "FUNCTION IMPLEMENTATIONS NEEDED:\n"
        dependency_section += "The following functions are called by this function and need their implementations included:\n\n"
        
        for dep_name, dep_info in dependency_implementations.items():
            dependency_section += f"Function: {dep_name}\n"
            dependency_section += f"```c\n{dep_info['code']}\n```\n\n"
    
    # Get available headers from state
    available_headers = state.get("embeddings", {}).get("available_headers", [])
    
    # Build a clear list of available headers
    headers_section = "AVAILABLE HEADER FILES:\n"
    if available_headers:
        for header in available_headers:
            headers_section += f"- {header}\n"
    else:
        headers_section += "No header files found in the codebase. You will need to include standard library headers only.\n"
    headers_section += "\nNOTE: Only include header files that actually exist in the codebase or standard libraries."
    
    # Build generator prompt with focused verification and dependency info
    if not is_refinement:
        generator_prompt = f"""
        You are a specialized harness generator for CBMC verification.
        Create a MINIMAL, FOCUSED harness for the following function:

        ```c
        {func_code}
        ```

        IMPORTANT: You MUST include the function implementation itself in the harness file:
        ```c
        {func_code}
        ```
        
        {dependency_section}

        Function metadata:
        - Return type: {func_metadata.get("return_type", "void")}
        - Parameters: {func_metadata.get("params", "")}
        - Contains malloc: {has_malloc}
        - Contains free: {has_free}
        
        {headers_section}
        
        {framework_section}
        
        Matching vulnerability patterns:
        {json.dumps(patterns_result.get('matching_patterns', {}), indent=2)}
        
        {verification_guide}
        
        CRITICAL INSTRUCTIONS:
        1. INCLUDE THE COMPLETE FUNCTION IMPLEMENTATION from above in your harness file
        2. Place the function implementation AFTER any necessary TYPE DEFINITIONS and DECLARATIONS but BEFORE the main() function
        3. ENSURE all necessary TYPE DEFINITIONS (enums, structs, etc.) come before any function that uses them
        4. DECLARE functions before calling them (especially important for addHeader and similar functions)
        5. DO NOT duplicate function implementations - include the function code exactly ONCE
        6. INCLUDE ALL REQUIRED FUNCTION IMPLEMENTATIONS that were found and provided above
        7. ONLY include header files that actually exist in the codebase or standard libraries
        8. DO NOT create mock implementations for any functions - use the real implementations provided above
        9. If you need to call a function that isn't provided, use a standard library alternative
        10. FOCUS ONLY on verifying actual properties of the function under test
        11. USE __CPROVER_assume() only for realistic input constraints
        12. USE nondet functions for inputs that need to be nondeterministic: nondet_int(), nondet_size_t(), etc.
        13. The function under test is '{func_name}' - make sure to call this exact function with appropriate parameters
        
        Your harness must be minimal and focused - only create what's necessary to test the function.
        
        Provide only the minimal, focused harness code (including the function implementation) without explanation.
        """
    else:
        # For refinement, use a more targeted improvement guidance
        generator_prompt = f"""
        You are a specialized harness generator for CBMC verification.
        You need to REFINE an existing harness based on SPECIFIC CBMC verification failures.
        
        {improvement_recommendation}
        
        Previous harness code that you should improve:
        ```c
        {previous_harness}
        ```
        
        IMPORTANT: Make sure the original function implementation remains in the harness.
        If it's not present in the previous harness, add it at the beginning:
        ```c
        {func_code}
        ```
        
        {dependency_section}
        
        CRITICAL INSTRUCTIONS:
        1. ENSURE THE COMPLETE FUNCTION IMPLEMENTATION is present in your harness file
        2. Place the function implementation AFTER any necessary TYPE DEFINITIONS and DECLARATIONS but BEFORE the main() function 
        3. ENSURE all type definitions (enums, structs, etc.) come before any function that uses them
        4. DECLARE all helper functions before they are called
        5. DO NOT duplicate function implementations - include the function code exactly ONCE
        6. INCLUDE ALL REQUIRED FUNCTION IMPLEMENTATIONS that were found and provided above
        7. DO NOT create mock implementations of any functions - use the real implementations provided
        8. ADDRESS EACH SPECIFIC ISSUE mentioned in the evaluation feedback
        9. ADD all missing header files, function declarations, and constraints
        10. IMPLEMENT all suggested code changes precisely
        11. ENSURE proper memory management (allocation and freeing)
        12. FIX all pointer dereference issues with proper initialization and checks
        13. RESOLVE declaration errors by adding the necessary declarations
        14. NEVER implement stubs or mocks for functions that should exist in the codebase
        15. REMOVE any existing mock implementations or stubs you find in the previous harness
        16. Focus ONLY on creating a direct test of the function with appropriate inputs
        
        Make sure your harness is complete, properly formatted, and addresses ALL the specific issues mentioned in the feedback.
        
        Provide only the improved harness code without explanation.
        """
    
    # Generate the harness
    try:
        logger.info(f"Sending API request to generate harness for {func_name}")
        
        # Check for the LLM model type to handle system prompt correctly
        model_name = str(llm).lower()
        
        # Enhanced system prompt to strongly discourage mocks and stubs
        system_prompt = """
        You are a specialized harness generator for CBMC verification. Generate complete, correct, minimal code.

        IMPORTANT RULES:
        1. ALWAYS create a function named 'void main()' as the ONLY entry point
        2. DO NOT create functions named 'harness()', 'test_harness()', or any other entry point
        3. NEVER create mock implementations or stubs - use existing functions from the codebase
        4. ONLY include headers that actually exist in the codebase or standard libraries
        5. AVOID creating any helper functions or utility code
        6. Create DIRECT tests of the function behavior with appropriate inputs
        7. FOCUS on real verification concerns, not artificial test scenarios
        8. ALWAYS include the original function implementation in the harness file
        9. FOLLOW PROPER C CODE STRUCTURE:
           - Include directives first
           - Type definitions (typedef, enum, struct) next
           - Function declarations next
           - Function implementations next
           - Main function last
        10. DO NOT duplicate function implementations
        11. INCLUDE ALL REQUIRED FUNCTION IMPLEMENTATIONS that were found in the codebase

        Your code must be minimal, focused, and use ONLY 'void main()' as the entry point.
        """
        
        # Setup messages for the LLM based on the model type
        if "gemini" in model_name:
            # For Gemini, we need to include the system prompt in the human message
            response = llm.invoke([
                HumanMessage(content=f"{system_prompt}\n\n{generator_prompt}")
            ])
        else:
            # For Claude and OpenAI models, use separate system and human messages
            response = llm.invoke([
                SystemMessage(content=system_prompt),
                HumanMessage(content=generator_prompt)
            ])
            
        logger.info(f"Received API response for {func_name}")
        
        # Extract the harness code
        harness_code = response.content
        match = re.search(r'```(?:c)?\n(.+?)\n```', harness_code, re.DOTALL)
        if match:
            harness_code = match.group(1)
        
        # Validate harness completeness
        has_main = "void main(" in harness_code or "int main(" in harness_code
        balanced_braces = harness_code.count("{") <= harness_code.count("}")

        if not has_main or not balanced_braces:
            logger.warning(f"Incomplete harness for {func_name}, attempting to fix")
            
            # Fix incomplete harnesses
            if not balanced_braces:
                missing_braces = harness_code.count("{") - harness_code.count("}")
                if missing_braces > 0:
                    harness_code += "\n" + ("}" * missing_braces)
            
            # Make sure there's a main function
            if not has_main:
                # Always add a void main() function regardless of CBMC framework
                harness_code += "\n\nvoid main() {\n    // Auto-generated main function\n}"
            
        
        # Detect and remove potential stubs/mocks
        harness_lines = harness_code.split('\n')
        filtered_lines = []
        in_stub_implementation = False
        stub_markers = ["// Stub implementation", "/* Stub ", "/* Mock ",
                     "// Mock implementation", "// Mock function"]
        
        for line in harness_lines:
            # Check if this line starts a stub implementation
            if any(marker in line for marker in stub_markers) or (line.strip().startswith("//") and "stub" in line.lower()):
                in_stub_implementation = True
                continue
                
            # Check if we're at the end of a stubbed function
            if in_stub_implementation and "}" in line and not line.strip().startswith("//"):
                # This might be the end of a stub function
                in_stub_implementation = False
                continue
                
            # If we're not in a stub implementation, keep the line
            if not in_stub_implementation:
                filtered_lines.append(line)
        
        # Reconstruct the harness without stub implementations
        harness_code = '\n'.join(filtered_lines)
        
        # Check for non-existent headers
        available_headers = state.get("embeddings", {}).get("available_headers", [])
        standard_headers = ["stdio.h", "stdlib.h", "string.h", "stddef.h", "stdint.h", 
                           "stdbool.h", "math.h", "ctype.h", "time.h", "limits.h",
                           "assert.h", "errno.h", "float.h", "signal.h"]
        
        updated_lines = []
        for line in harness_code.split('\n'):
            if line.strip().startswith("#include"):
                include_match = re.search(r'#include\s+[<"]([^>"]+)[>"]', line)
                if include_match:
                    header_name = include_match.group(1)
                    # Keep the line if it's a standard header or in available headers
                    if header_name in standard_headers or header_name in available_headers:
                        updated_lines.append(line)
                    else:
                        # Skip the non-existent header
                        logger.warning(f"Removing non-existent header: {header_name}")
                        # Add comment explaining the removal
                        updated_lines.append(f"// Removed non-existent header: {header_name}")
                else:
                    # Keep the line if it doesn't match the pattern (unlikely)
                    updated_lines.append(line)
            else:
                # Keep all non-include lines
                updated_lines.append(line)
        
        # Reconstruct the harness without non-existent headers
        harness_code = '\n'.join(updated_lines)
        
        # Check for missing function dependencies in the harness
        # For each dependency, check if it's included in the harness
        for dep_name, dep_info in dependency_implementations.items():
            # Create a pattern to match the function signature (approximately)
            dep_signature_pattern = rf"\b{re.escape(dep_name)}\s*\([^)]*\)\s*\{{"
            
            # Check if this function is already in the harness
            if not re.search(dep_signature_pattern, harness_code):
                # If not, log the issue
                logger.warning(f"Dependency {dep_name} not included in harness, adding it manually")
                
                # Find a suitable place to add it - after the includes and declarations
                # but before the main function
                
                # First check for main function position
                main_match = re.search(r"\b(?:void|int)\s+main\s*\([^)]*\)\s*\{", harness_code)
                if main_match:
                    main_pos = main_match.start()
                    
                    # Find last function implementation before main
                    func_matches = list(re.finditer(r"\}\s*\n", harness_code[:main_pos]))
                    if func_matches:
                        last_func_end = func_matches[-1].end()
                        # Add dependency after last function before main
                        harness_code = harness_code[:last_func_end] + "\n" + dep_info["code"] + "\n\n" + harness_code[last_func_end:]
                    else:
                        # No other functions, add before main
                        harness_code = harness_code[:main_pos] + "\n" + dep_info["code"] + "\n\n" + harness_code[main_pos:]
                else:
                    # No main function found, add at end
                    harness_code += "\n\n" + dep_info["code"]
        
        # Save the new harness to history
        if harness_code not in harness_history[func_name]:
            harness_history[func_name].append(harness_code)
        
        # Update the harnesses dictionary
        harnesses = state.get("harnesses", {}).copy()
        harnesses[func_name] = harness_code
        
        # Determine version number for filename
        refinement_num = state.get("refinement_attempts", {}).get(func_name, 0)
        version_num = refinement_num + 1
        
        # Create function-specific directory in harnesses dir
        func_harness_dir = os.path.join(harnesses_dir, func_name)
        os.makedirs(func_harness_dir, exist_ok=True)
        
        # Save harness to file
        filename = os.path.join(func_harness_dir, f"v{version_num}.c")
        with open(filename, "w") as f:
            f.write(harness_code)
            f.flush()
            os.fsync(f.fileno())  # Force flush to disk
        
        # Calculate time
        generation_time = time.time() - generation_start
        
        # Update function times
        function_times = state.get("function_times", {}).copy()
        if func_name not in function_times:
            function_times[func_name] = {}
        function_times[func_name]["generation"] = generation_time
        
        logger.info(f"Successfully {'refined' if is_refinement else 'generated'} harness for {func_name} in {generation_time:.2f}s")
        return {
            "messages": [AIMessage(content=f"{'Refined' if is_refinement else 'Generated'} minimal, focused harness for function {func_name} in {generation_time:.2f}s")],
            "harnesses": harnesses,
            "harness_history": harness_history,
            "improvement_recommendation": "",
            "function_times": function_times,
            "next": "cbmc"  # Proceed to CBMC verification
        }
        
   # In the catch block of generator_node where errors are handled
    except Exception as e:
        # Enhanced error handling with more details
        error_msg = str(e)
        error_type = type(e).__name__
        logger.error(f"Error ({error_type}) generating harness for {func_name}: {error_msg}")
        logger.error(f"Full traceback:", exc_info=True)
        print(f"\nERROR: API call failed when processing function {func_name}")
        print(f"Error type: {error_type}")
        print(f"Error message: {error_msg}")
        
        # NEW: Mark this function as failed to prevent repeated attempts
        failed_functions = state.get("failed_functions", [])
        if func_name not in failed_functions:
            failed_functions.append(func_name)
        
        # Return to junction to try next function
        return {
            "messages": [AIMessage(content=f"Error generating harness for {func_name}: {error_msg}. Skipping to next function.")],
            "failed_functions": failed_functions,  # Add the new failed_functions state
            "next": "junction"
        }

def route_from_generator(state):
    """Routes from generator to either cbmc or junction."""
    return state.get("next", "cbmc")