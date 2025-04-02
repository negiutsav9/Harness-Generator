"""
Generator node for CBMC harness generator workflow with unified RAG enhancement.
"""
import time
import os
import re
import json
import logging
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from core.embedding_db import code_collection
from utils.metrics_utils import get_metrics_tracker
from utils.rag import get_unified_db

# Set up logging
logger = logging.getLogger("generator")

def generator_node(state):
    """Generates or refines CBMC-compatible harness for the current function using unified RAG."""
    # Get the global LLM instance
    from utils.llm_utils import setup_llm
    llm = setup_llm()

    # Start timing
    generation_start = time.time()
    
    func_name = state.get("current_function", "")
    logger.info(f"Generating harness for function: {func_name}")
    
    # Get result directories from state
    result_directories = state.get("result_directories", {})
    harnesses_dir = result_directories.get("harnesses_dir", "harnesses")
    
    # Get the unified RAG database
    rag_db = get_unified_db(os.path.join(result_directories.get("result_base_dir", "results"), "rag_data"))
    
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
    
    # Try to get function from unified database first
    function_data = rag_db.get_code_function(func_name)
    
    if function_data:
        func_code = function_data["code"]
        func_metadata = function_data["metadata"]
        logger.info(f"Found function {func_name} in unified RAG database")
    else:
        # Fall back to direct lookup from code_collection
        function_result = code_collection.get(ids=[func_name], include=["documents", "metadatas"])
        
        if function_result["ids"]:
            func_code = function_result["documents"][0]
            func_metadata = function_result["metadatas"][0]
            logger.info(f"Found function {func_name} via direct ID lookup")
            
            # Store in unified database for future use
            rag_db.add_code_function(func_name, func_code, func_metadata)
        else:
            # Strategy 2: Try parsing the function name 
            if ":" in func_name:
                # Try with file basename and function name
                file_basename, orig_func_name = func_name.split(":", 1)
                # Try searching for original function name 
                query_results = code_collection.query(
                    query_texts=[f"function {orig_func_name}"],
                    n_results=5
                )
                
                if query_results["ids"][0]:
                    for i, result_id in enumerate(query_results["ids"][0]):
                        # Look for exact matches first
                        if orig_func_name in result_id and not result_id.startswith("pattern:"):
                            match_result = code_collection.get(ids=[result_id], include=["documents", "metadatas"])
                            if match_result["ids"]:
                                func_code = match_result["documents"][0]
                                func_metadata = match_result["metadatas"][0]
                                logger.info(f"Found function {func_name} via name search: {result_id}")
                                
                                # Store in unified database for future use
                                rag_db.add_code_function(func_name, func_code, func_metadata)
                                break
            
            # Strategy 3: Last resort - fuzzy search
            if not func_code:
                # Try a more general search
                search_term = func_name.split(":")[-1] if ":" in func_name else func_name
                logger.info(f"Trying fuzzy search for {search_term}")
                
                query_results = code_collection.query(
                    query_texts=[search_term],
                    n_results=3
                )
                
                if query_results["ids"][0]:
                    result_id = query_results["ids"][0][0]  # Take the closest match
                    match_result = code_collection.get(ids=[result_id], include=["documents", "metadatas"])
                    if match_result["ids"]:
                        func_code = match_result["documents"][0]
                        func_metadata = match_result["metadatas"][0]
                        logger.info(f"Found potential match for {func_name} via fuzzy search: {result_id}")
                        
                        # Store in unified database for future use
                        rag_db.add_code_function(func_name, func_code, func_metadata)
    
    if not func_code:
        logger.error(f"Function {func_name} not found in database")
        return {
            "messages": [AIMessage(content=f"Error: Function {func_name} not found in database.")],
            "next": "junction"
        }
    
    # Extract function dependencies
    function_calls = []
    
    # First try from metadata
    calls_json = func_metadata.get("function_calls", "[]")
    try:
        if isinstance(calls_json, str):
            function_calls = json.loads(calls_json)
        else:
            function_calls = calls_json
    except json.JSONDecodeError:
        # Fallback: Extract from code directly
        function_calls = re.findall(r'\b(\w+)\s*\(', func_code)
        # Remove duplicates while preserving order
        function_calls = list(dict.fromkeys(function_calls))
    
    # Find implementations for dependencies
    dependency_implementations = {}
    
    for called_func in function_calls:
        # Skip standard library and control flow functions
        if called_func in ["if", "for", "while", "switch", "return", "malloc", "free",
                          "memset", "memcpy", "printf", "fprintf", "sprintf"]:
            continue
        
        # Try to find the dependency in the unified database first
        function_data = rag_db.get_code_function(called_func)
        if function_data:
            dependency_implementations[called_func] = {
                "code": function_data["code"],
                "metadata": function_data["metadata"]
            }
            logger.info(f"Found dependency {called_func} in unified RAG database")
            continue
        
        # Strategy 1: Direct lookup by name in same file
        if ":" in func_name:
            file_basename, _ = func_name.split(":", 1)
            direct_id = f"{file_basename}:{called_func}"
            
            dep_result = code_collection.get(ids=[direct_id], include=["documents", "metadatas"])
            if dep_result["ids"]:
                # Found direct match in same file
                dependency_implementations[called_func] = {
                    "code": dep_result["documents"][0],
                    "metadata": dep_result["metadatas"][0]
                }
                
                # Store in unified database for future use
                rag_db.add_code_function(direct_id, dep_result["documents"][0], dep_result["metadatas"][0])
                
                logger.info(f"Found dependency {called_func} in same file")
                continue
        
        # Strategy 2: Search for function pattern
        search_pattern = f"\\b{called_func}\\s*\\([^)]*\\)\\s*\\{{"
        logger.info(f"Searching for dependency: {search_pattern}")
        
        query_results = code_collection.query(
            query_texts=[search_pattern],
            n_results=5
        )
        
        if query_results["ids"][0]:
            for result_id in query_results["ids"][0]:
                # Skip pattern matches
                if result_id.startswith("pattern:"):
                    continue
                    
                match_result = code_collection.get(ids=[result_id], include=["documents", "metadatas"])
                if match_result["ids"]:
                    # Ensure this is a full implementation (not a declaration)
                    metadata = match_result["metadatas"][0]
                    if not metadata.get("is_declaration_only", True):
                        dependency_implementations[called_func] = {
                            "code": match_result["documents"][0],
                            "metadata": metadata
                        }
                        
                        # Store in unified database for future use
                        rag_db.add_code_function(result_id, match_result["documents"][0], metadata)
                        
                        logger.info(f"Found dependency {called_func} via pattern search: {result_id}")
                        break
        
        # Strategy 3: Look for function declaration as fallback
        if called_func not in dependency_implementations:
            # No implementation found, look for declaration as fallback
            decl_query_results = code_collection.query(
                query_texts=[f"declaration {called_func}"],
                n_results=3
            )
            
            if decl_query_results["ids"][0]:
                for result_id in decl_query_results["ids"][0]:
                    if "declaration:" in result_id and called_func in result_id:
                        decl_result = code_collection.get(ids=[result_id], include=["documents", "metadatas"])
                        if decl_result["ids"]:
                            dependency_implementations[called_func] = {
                                "code": decl_result["documents"][0],
                                "metadata": decl_result["metadatas"][0],
                                "is_declaration_only": True
                            }
                            logger.info(f"Found declaration for {called_func}: {result_id}")
                            break
    
    logger.info(f"Found {len(dependency_implementations)} function dependencies with implementations")
    
    # Special handling for improved missing function detection
    if is_refinement and cbmc_result:
        missing_functions = cbmc_result.get("missing_functions", set())
        if missing_functions:
            logger.info(f"Detected {len(missing_functions)} missing functions: {', '.join(missing_functions)}")
            
            # Look for these functions in the code database
            for missing_func in missing_functions:
                if missing_func in dependency_implementations:
                    logger.info(f"Already found implementation for {missing_func}")
                    continue
                    
                # Try to find implementation for missing function
                logger.info(f"Searching for implementation of missing function: {missing_func}")
                
                # Try direct match by function name
                query_results = code_collection.query(
                    query_texts=[f"function {missing_func}"],
                    n_results=5
                )
                
                # Check each result for an exact function match
                if query_results["ids"][0]:
                    for result_id in query_results["ids"][0]:
                        # Skip patterns and declarations
                        if result_id.startswith("pattern:") or result_id.startswith("declaration:"):
                            continue
                            
                        # Check if this is the function we're looking for
                        if missing_func in result_id:
                            match_result = code_collection.get(ids=[result_id], include=["documents", "metadatas"])
                            if match_result["ids"]:
                                metadata = match_result["metadatas"][0]
                                if not metadata.get("is_declaration_only", True):
                                    # Found the implementation
                                    logger.info(f"Found implementation for missing function {missing_func}: {result_id}")
                                    dependency_implementations[missing_func] = {
                                        "code": match_result["documents"][0],
                                        "metadata": metadata,
                                        "is_missing_function": True
                                    }
                                    
                                    # Store in unified database for future use
                                    rag_db.add_code_function(result_id, match_result["documents"][0], metadata)
                                    break
    
    # RAG Enhancement: Get recommendations from unified database for similar errors/solutions
    rag_recommendations = None
    
    if is_refinement and cbmc_result:
        logger.info(f"Querying unified RAG database for function {func_name}")
        
        # Get recommendations from unified database
        rag_recommendations = rag_db.get_recommendations(
            func_name, 
            func_code, 
            cbmc_result,
            previous_harness
        )
        
        # Log RAG findings
        if rag_recommendations:
            if rag_recommendations["has_similar_errors"]:
                logger.info(f"Found {len(rag_recommendations['similar_errors'])} similar errors in RAG database")
            if rag_recommendations["has_solutions"]:
                logger.info(f"Found {len(rag_recommendations['solutions'])} potential solutions in RAG database")
            if rag_recommendations["has_matching_patterns"]:
                logger.info(f"Found {len(rag_recommendations['matching_patterns'])} matching patterns in RAG database")
    
    # Build generator prompt with improved focus on dependencies and verification
    if not is_refinement:
        # For initial generation, create a focused prompt
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
        """
        
        # Add dependency section if we found implementations
        if dependency_implementations:
            generator_prompt += "\nFUNCTION DEPENDENCIES NEEDED:\n"
            generator_prompt += "The following functions are called by this function and need their implementations included:\n\n"
            
            for dep_name, dep_info in dependency_implementations.items():
                generator_prompt += f"Function: {dep_name}\n"
                generator_prompt += f"```c\n{dep_info['code']}\n```\n\n"
        
        # Add function metadata
        generator_prompt += f"""
        Function metadata:
        - Return type: {func_metadata.get("return_type", "void")}
        - Parameters: {func_metadata.get("params", "")}
        - Contains malloc: {"Yes" if "has_malloc" in func_metadata and func_metadata["has_malloc"] else "No"}
        - Contains free: {"Yes" if "has_free" in func_metadata and func_metadata["has_free"] else "No"}
        """
        
        # Add clear instructions
        generator_prompt += """
        CRITICAL INSTRUCTIONS:
        1. INCLUDE THE COMPLETE FUNCTION IMPLEMENTATION from above in your harness file
        2. Place the function implementation AFTER any necessary TYPE DEFINITIONS and DECLARATIONS but BEFORE the main() function
        3. ENSURE all necessary TYPE DEFINITIONS (enums, structs, etc.) come before any function that uses them
        4. DECLARE functions before calling them
        5. DO NOT duplicate function implementations - include the function code exactly ONCE
        6. INCLUDE ALL REQUIRED FUNCTION IMPLEMENTATIONS that were found and provided above
        7. ONLY include header files from the standard library (stdio.h, stdlib.h, string.h, etc.)
        8. DO NOT create mock implementations for any functions
        9. FOCUS ONLY on verifying actual properties of the function under test
        10. USE __CPROVER_assume() for input constraints
        11. USE nondet functions for inputs that need to be nondeterministic: nondet_int(), nondet_size_t(), etc.
        12. The function under test is '{func_name.split(":")[-1] if ":" in func_name else func_name}' - make sure to call this exact function
        
        Your harness must be minimal and focused - only create what's necessary to test the function.
        
        Provide only the minimal, focused harness code (including the function implementation) without explanation.
        """
    else:
        # For refinement, use the improvement recommendation and RAG enhancements
        generator_prompt = f"""
        You are a specialized harness generator for CBMC verification.
        You need to REFINE an existing harness based on SPECIFIC CBMC verification failures.
        
        {improvement_recommendation}
        
        IMPORTANT: You MUST include the function implementation in the harness:
        ```c
        {func_code}
        ```
        """
        
        # Add dependency section if we found implementations
        if dependency_implementations:
            generator_prompt += "\nFUNCTION DEPENDENCIES NEEDED:\n"
            generator_prompt += "The following functions are called by this function and need their implementations included:\n\n"
            
            for dep_name, dep_info in dependency_implementations.items():
                generator_prompt += f"Function: {dep_name}\n"
                generator_prompt += f"```c\n{dep_info['code']}\n```\n\n"
                
        # Add RAG recommendations if available
        if rag_recommendations and (rag_recommendations["has_similar_errors"] or 
                                   rag_recommendations["has_solutions"] or 
                                   rag_recommendations["has_matching_patterns"]):
            generator_prompt += "\nHISTORICAL KNOWLEDGE FROM SIMILAR FUNCTIONS:\n"
            
            # Add complete solution if one was found
            if rag_recommendations["has_solutions"]:
                best_solution = rag_recommendations["solutions"][0]
                generator_prompt += f"\nA similar function was successfully verified with this approach:\n```c\n"
                
                # Extract only the relevant parts (not the entire harness)
                harness_code = best_solution["harness_code"]
                
                # Try to extract just the main() function which contains the test strategy
                main_match = re.search(r'(void|int)\s+main\s*\([^{]*\{([^}]+)\}', harness_code, re.DOTALL)
                if main_match:
                    generator_prompt += f"// Main function from similar successful harness\n{main_match.group(0)}\n"
                else:
                    # Just include a portion to avoid too much code
                    lines = harness_code.split('\n')
                    relevant_lines = lines[max(0, len(lines)//2-15):min(len(lines), len(lines)//2+15)]
                    generator_prompt += f"// Relevant portion from similar successful harness\n" + '\n'.join(relevant_lines) + "\n"
                
                generator_prompt += "```\n"
            
            # Add matching patterns if found
            if rag_recommendations["has_matching_patterns"]:
                generator_prompt += "\nMatching vulnerability patterns:\n"
                
                for name, pattern_info in rag_recommendations["matching_patterns"].items():
                    generator_prompt += f"\n- {pattern_info['description']} (Severity: {pattern_info['severity']})"
                    generator_prompt += f"\n  Strategy: {pattern_info['verification_strategy']}\n"
        
        # Add critical instructions for refinement
        generator_prompt += """
        CRITICAL INSTRUCTIONS:
        1. KEEP THE COMPLETE FUNCTION IMPLEMENTATION in your harness file
        2. ADDRESS EACH SPECIFIC ISSUE mentioned in the error feedback
        3. Fix all identified errors and implement the suggested improvements
        4. If a memory leak is detected, ensure all allocated memory is freed
        5. If null pointer issues exist, add appropriate NULL checks
        6. If array bounds violations occur, add bounds checking
        7. If a function is missing, implement it using the provided code or create a minimal stub
        8. DO NOT create elaborate mock implementations - use only what is necessary
        9. Keep the harness minimal and focused on the specific verification issues
        10. Apply any relevant patterns from the historical knowledge section
        
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
        3. NEVER create mock implementations or stubs unless absolutely necessary
        4. ONLY include standard library headers
        5. AVOID creating any helper functions or utility code
        6. Create DIRECT tests of the function behavior with appropriate inputs
        7. FOCUS on real verification concerns, not artificial test scenarios
        8. ALWAYS include the original function implementation in the harness file
        9. FOLLOW PROPER C CODE STRUCTURE:
           - Include directives first
           - Type definitions next
           - Function declarations next
           - Function implementations next
           - Main function last
        """
        
        # Setup messages for the LLM based on the model type
        if "gemini" in model_name:
            # For Gemini, include the system prompt in the human message
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
                harness_code += "\n\nvoid main() {\n    // Auto-generated main function\n}"
        
        # Check for missing function dependencies in the harness
        for dep_name, dep_info in dependency_implementations.items():
            # Create a pattern to match the function signature
            dep_signature_pattern = rf"\b{re.escape(dep_name)}\s*\([^)]*\)\s*\{{"
            
            # Check if this function is already in the harness
            if not re.search(dep_signature_pattern, harness_code):
                logger.warning(f"Dependency {dep_name} not included in harness, adding it manually")
                
                # Find a suitable place to add it - after the target function impl but before main
                main_match = re.search(r"\b(?:void|int)\s+main\s*\([^)]*\)\s*\{", harness_code)
                if main_match:
                    main_pos = main_match.start()
                    # Add dependency before main
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
        generation_time_ms = int(generation_time * 1000)
        
        # Update function times
        function_times = state.get("function_times", {}).copy()
        if func_name not in function_times:
            function_times[func_name] = {}
        function_times[func_name]["generation"] = generation_time
        
        logger.info(f"Successfully {'refined' if is_refinement else 'generated'} harness for {func_name} in {generation_time:.2f}s")
        
        # Create message with RAG information if used
        message_content = f"{'Refined' if is_refinement else 'Generated'} minimal, focused harness for function {func_name} in {generation_time:.2f}s"
        if is_refinement and rag_recommendations:
            # Add info about RAG contributions
            if rag_recommendations["has_similar_errors"]:
                message_content += f"\nLeveraged {len(rag_recommendations['similar_errors'])} similar past errors from unified database"
            if rag_recommendations["has_solutions"]:
                message_content += f"\nApplied patterns from {len(rag_recommendations['solutions'])} successful solutions"
            if rag_recommendations["has_matching_patterns"]:
                message_content += f"\nIdentified {len(rag_recommendations['matching_patterns'])} relevant vulnerability patterns"
        
        # Get metrics tracker and update
        metrics_tracker = get_metrics_tracker()
        metrics = {
            "verification_status": "PENDING",
            "reachable_lines": 0,
            "covered_lines": 0,
            "coverage_pct": 0.0,
            "errors": 0
        }
        metrics_tracker.add_function_metrics(func_name, version_num, metrics, generation_time_ms)
        
        return {
            "messages": [AIMessage(content=message_content)],
            "harnesses": harnesses,
            "harness_history": harness_history,
            "improvement_recommendation": "",
            "function_times": function_times,
            "next": "cbmc"  # Proceed to CBMC verification
        }
        
    except Exception as e:
        # Error handling
        error_msg = str(e)
        error_type = type(e).__name__
        logger.error(f"Error ({error_type}) generating harness for {func_name}: {error_msg}")
        logger.error("Full traceback:", exc_info=True)
        print(f"\nERROR: API call failed when processing function {func_name}")
        print(f"Error type: {error_type}")
        print(f"Error message: {error_msg}")
        
        # Mark this function as failed to prevent repeated attempts
        failed_functions = state.get("failed_functions", [])
        if func_name not in failed_functions:
            failed_functions.append(func_name)
        
        # Get metrics tracker and update with error
        metrics_tracker = get_metrics_tracker()
        metrics = {
            "verification_status": "ERROR",
            "reachable_lines": 0,
            "covered_lines": 0,
            "coverage_pct": 0.0,
            "errors": 1,
            "error_categories": ["system_error"]
        }
        
        # Get refinement attempt number
        refinement_num = state.get("refinement_attempts", {}).get(func_name, 0)
        version_num = refinement_num + 1
        generation_time_ms = int((time.time() - generation_start) * 1000)
        
        metrics_tracker.add_function_metrics(func_name, version_num, metrics, generation_time_ms)
        
        # Return to junction to try next function
        return {
            "messages": [AIMessage(content=f"Error generating harness for {func_name}: {error_msg}. Skipping to next function.")],
            "failed_functions": failed_functions,
            "next": "junction"
        }

def route_from_generator(state):
    """Routes from generator to either cbmc or junction."""
    return state.get("next", "cbmc")