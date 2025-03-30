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
    if is_refinement and func_name in state.get("harnesses", {}):
        previous_harness = state.get("harnesses", {})[func_name]
        # Add to history if not already there
        if previous_harness not in harness_history[func_name]:
            harness_history[func_name].append(previous_harness)
    
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
    
    # Get function dependencies
    func_dependencies = state.get("function_dependencies", {}).get(func_name, [])
    
    # Build dependency information for the generator
    dependency_info = []
    dependency_code_examples = []
    for dep_name in func_dependencies:
        # Query for the dependency by name
        dep_results = code_collection.query(
            query_texts=[dep_name], 
            n_results=1
        )
        
        if dep_results["ids"] and len(dep_results["ids"][0]) > 0:
            dep_id = dep_results["ids"][0][0]
            dep_result = code_collection.get(ids=[dep_id], include=["documents", "metadatas"])
            if dep_result["ids"]:
                dep_code = dep_result["documents"][0]
                dep_metadata = dep_result["metadatas"][0]
                
                # Extract function signature
                dep_return_type = dep_metadata.get("return_type", "unknown")
                dep_params = dep_metadata.get("params", "")
                
                # Add to dependencies list
                dep_info = {
                    "name": dep_name,
                    "id": dep_id,
                    "return_type": dep_return_type,
                    "params": dep_params,
                    "exists_in_codebase": True
                }
                dependency_info.append(dep_info)
                
                # Add example code showing how to call it
                # Extract minimal signature for reference
                dep_signature = f"{dep_return_type} {dep_name}({dep_params});"
                dependency_code_examples.append(dep_signature)
    
    # Create dependency section
    if dependency_info:
        dependency_section = "FUNCTION DEPENDENCIES:\nThe following functions are called by this function and are available in the codebase:\n"
        for dep in dependency_info:
            dependency_section += f"\n- {dep['return_type']} {dep['name']}({dep['params']})"
        
        # Add example code section if we have dependencies
        dependency_section += "\n\nFunction declarations (for reference only):\n"
        for example in dependency_code_examples:
            dependency_section += f"\n{example}"
    else:
        dependency_section = "FUNCTION DEPENDENCIES:\nNo external function dependencies found for this function in the codebase."
    
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

        Function metadata:
        - Return type: {func_metadata.get("return_type", "void")}
        - Parameters: {func_metadata.get("params", "")}
        - Contains malloc: {has_malloc}
        - Contains free: {has_free}
        
        {headers_section}
        
        {dependency_section}
        
        {framework_section}
        
        Matching vulnerability patterns:
        {json.dumps(patterns_result.get('matching_patterns', {}), indent=2)}
        
        {verification_guide}
        
        CRITICAL INSTRUCTIONS:
        1. INCLUDE THE COMPLETE FUNCTION IMPLEMENTATION from above in your harness file
        2. Place the function implementation BEFORE the main() function after the includes
        3. ONLY include header files that actually exist in the codebase or standard libraries
        4. DO NOT create mock implementations for any functions - use only real functions from the codebase
        5. If you need to call a function that isn't confirmed to exist, use a standard library alternative
        6. FOCUS ONLY on verifying actual properties of the function under test
        7. USE __CPROVER_assume() only for realistic input constraints
        8. USE nondet functions for inputs that need to be nondeterministic: nondet_int(), nondet_size_t(), etc.
        9. INCLUDE only headers that are definitely needed
        10. The function under test is '{func_name}' - make sure to call this exact function with appropriate parameters
        
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
        
        CRITICAL INSTRUCTIONS:
        1. ENSURE THE COMPLETE FUNCTION IMPLEMENTATION is present in your harness file
        2. Place the function implementation BEFORE the main() function after the includes
        3. DO NOT create mock implementations of any functions - all required functions already exist in the code database
        4. ADDRESS EACH SPECIFIC ISSUE mentioned in the evaluation feedback
        5. ADD all missing header files, function declarations, and constraints
        6. IMPLEMENT all suggested code changes precisely
        7. ENSURE proper memory management (allocation and freeing)
        8. FIX all pointer dereference issues with proper initialization and checks
        9. RESOLVE declaration errors by adding the necessary declarations
        10. NEVER implement stubs or mocks for functions that should exist in the codebase
        11. REMOVE any existing mock implementations or stubs you find in the previous harness
        12. Focus ONLY on creating a direct test of the function with appropriate inputs
        
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
        
        # Check if function implementation is included
        original_func_name = func_name.split(":")[-1] if ":" in func_name else func_name
        return_type = func_metadata.get("return_type", "").strip()
        params_text = func_metadata.get("params", "").strip()
        
        # Create a pattern that will match the function signature
        # Handle cases where return type might contain spaces (like "unsigned int")
        func_signature_pattern = rf"{return_type}\s+{re.escape(original_func_name)}\s*\(\s*{re.escape(params_text)}\s*\)"
        
        # Check if function implementation is included
        if not re.search(func_signature_pattern, harness_code):
            logger.warning(f"Function implementation not found in harness for {func_name}, adding it")
            
            # Add function at the beginning of the harness (before any includes)
            # Find the first include directive
            include_match = re.search(r'(#include\s+[<"][^>"]+[>"])', harness_code)
            if include_match:
                # Insert function before the first include
                include_pos = harness_code.find(include_match.group(1))
                harness_code = harness_code[:include_pos] + f"{func_code}\n\n" + harness_code[include_pos:]
            else:
                # No includes found, add to the beginning
                harness_code = f"{func_code}\n\n{harness_code}"
        
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
        
    except Exception as e:
        # Handle API errors
        error_msg = str(e)
        logger.error(f"Error generating harness for {func_name}: {error_msg}")
        print(f"\nERROR: API call failed when processing function {func_name}")
        print(f"Error message: {error_msg}")
        
        # Return to junction to try next function
        return {
            "messages": [AIMessage(content=f"Error generating harness for {func_name}: {error_msg}. Skipping to next function.")],
            "next": "junction"
        }

def route_from_generator(state):
    """Routes from generator to either cbmc or junction."""
    return state.get("next", "cbmc")