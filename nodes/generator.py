
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
            logger.error(f"Function {func_name} not found in database")
            return {
                "messages": [AIMessage(content=f"Error: Function {func_name} not found in database.")],
                "next": "junction"
            }
    
    # Extract original function name
    if ":" in func_name:
        _, original_func_name = func_name.split(":", 1)
    else:
        original_func_name = func_name
    
    # Find implementations for dependencies
    dependency_implementations = {}
    
    # Extract function calls or dependencies
    function_calls = func_metadata.get("function_calls", [])
    if isinstance(function_calls, str):
        try:
            function_calls = json.loads(function_calls)
        except json.JSONDecodeError:
            # Fallback to splitting if JSON parsing fails
            function_calls = [call.strip() for call in function_calls.split(',')]
    
    # Find implementations for dependencies
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
        
        # Fallback search in code collection
        dep_result = code_collection.get(ids=[called_func], include=["documents", "metadatas"])
        if dep_result["ids"]:
            dependency_implementations[called_func] = {
                "code": dep_result["documents"][0],
                "metadata": dep_result["metadatas"][0]
            }
            logger.info(f"Found dependency {called_func} via direct lookup")
    
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
        # For initial generation, create a minimal harness focusing on function declaration and dependencies
        generator_prompt = f"""
        You are a specialized harness generator for CBMC verification.
        Create a MINIMAL verification harness for testing the function:

        Function Signature:
        ```c
        {func_metadata.get('return_type', 'void')} {original_func_name}({func_metadata.get('params', 'void')});
        ```

        CRITICAL INSTRUCTIONS:
        1. DO NOT include the full function implementation
        2. Always use the EXACT parameter names from the original function
        3. ALWAYS use "extern" keyword for function declarations to avoid redefinition conflicts
        4. NEVER redefine the function being tested
        5. Create a main() function that calls the target function
        6. Use __CPROVER_assume() for input constraints
        7. Use nondet functions for nondeterministic inputs
        8. ONLY include necessary header files from the standard library
        9. Ensure all declarations are complete and syntactically correct
        10. FOCUS on creating a verifiable function call scenario

        Function Dependencies:
        """
        
        # Add dependency declarations
        if dependency_implementations:
            generator_prompt += "\n// Function Dependencies to Declare\n"
            for dep_name, dep_info in dependency_implementations.items():
                # Extract function signature from metadata or existing implementations
                return_type = dep_info.get('metadata', {}).get('return_type', 'void')
                params = dep_info.get('metadata', {}).get('params', 'void')
                # Use extern and PRESERVE EXACT parameter names
                generator_prompt += f"extern {return_type} {dep_name}({params});\n"
        
        # Add main function template
        generator_prompt += f"""
        void main() {{
            // Nondeterministic input preparation
            // Assume constraints for inputs
            
            // Call the function under test with explicit parameter names
            {func_metadata.get('return_type', 'void')} result = {original_func_name}({
                ', '.join([f'nondet_{p.split()[-1]}()' if p.strip() != 'void' else '' 
                           for p in func_metadata.get('params', 'void').split(',')])
            });
            
            // Add verification assertions as needed
            __CPROVER_assert(/* add specific verification condition */, "Verification condition");
        }}
        """
        
        # Add clear instructions
        generator_prompt += """
        KEY VERIFICATION PRINCIPLES:
        - Use __CPROVER_assume() to set realistic input constraints
        - Add __CPROVER_assert() to check critical properties
        - Minimize the harness complexity
        - Focus on key function behaviors
        - ALWAYS use extern for function declarations
        - NEVER redeclare the function with different parameter names
        """
    
    else:
        # For refinement, focus on specific CBMC verification issues
        generator_prompt = f"""
        You are a specialized harness generator for CBMC verification.
        You need to REFINE a harness based on SPECIFIC CBMC verification failures.
        
        {improvement_recommendation}
        
        CRITICAL INSTRUCTIONS:
        1. DO NOT include the full function implementation
        2. Always use the EXACT parameter names from the original function
        3. ALWAYS use "extern" keyword for function declarations
        4. NEVER redefine the function being tested
        5. Modify the main() function to address specific CBMC failures
        6. Use __CPROVER_assume() to constrain inputs
        7. Use __CPROVER_assert() to validate key properties
        8. Address each specific issue from the previous verification
        9. Minimize the harness complexity
        10. FOCUS on the verification requirements
        """
        
        # Add dependency declarations
        if dependency_implementations:
            generator_prompt += "\n// Function Dependencies to Declare\n"
            for dep_name, dep_info in dependency_implementations.items():
                # Extract function signature from metadata or existing implementations
                return_type = dep_info.get('metadata', {}).get('return_type', 'void')
                params = dep_info.get('metadata', {}).get('params', 'void')
                generator_prompt += f"extern {return_type} {dep_name}({params});\n"
        
        # Add main function with specific refinement guidance
        generator_prompt += f"""
        void main() {{
            // Refined input preparation based on previous verification
            // More constrained and targeted input generation
            
            // Call the function under test with carefully prepared inputs
            {func_metadata.get('return_type', 'void')} result = {original_func_name}({
                ', '.join([f'nondet_{p.split()[-1]}()' if p.strip() != 'void' else '' 
                           for p in func_metadata.get('params', 'void').split(',')])
            });
            
            // Add specific verification conditions addressing previous failures
            __CPROVER_assert(/* refined verification condition */, "Refined verification condition");
        }}
        """
        
        # Add RAG-based recommendations if available
        if rag_recommendations and (rag_recommendations["has_similar_errors"] or 
                                   rag_recommendations["has_solutions"] or 
                                   rag_recommendations["has_matching_patterns"]):
            generator_prompt += "\n\n// RECOMMENDATIONS FROM KNOWLEDGE BASE:\n"
            
            if rag_recommendations["has_similar_errors"]:
                generator_prompt += "// Similar Errors Insights:\n"
                for error in rag_recommendations["similar_errors"][:2]:
                    generator_prompt += f"// - {error.get('error_message', 'Unspecified error')}\n"
            
            if rag_recommendations["has_solutions"]:
                generator_prompt += "// Successful Solution Patterns:\n"
                for solution in rag_recommendations["solutions"][:2]:
                    generator_prompt += "// Verification strategy hints:\n"
                    # Add specific hints about solution patterns
                    if solution.get('patterns_found', 0) > 0:
                        generator_prompt += "// Consider adding targeted assertions\n"
            
            if rag_recommendations["has_matching_patterns"]:
                generator_prompt += "// Matching Vulnerability Patterns:\n"
                for name, pattern in rag_recommendations["matching_patterns"].items():
                    generator_prompt += f"// - {pattern.get('description', 'Unspecified pattern')}\n"
        
        generator_prompt += """
        VERIFICATION REFINEMENT PRINCIPLES:
        - Precisely address the specific CBMC verification failures
        - Use more restrictive input constraints
        - Add targeted assertions
        - Minimize harness complexity
        - Focus on the specific verification requirements
        - ALWAYS use extern for function declarations
        - NEVER redeclare the function with different parameter names
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
        8. ALWAYS use "extern" for function declarations to avoid redefinition conflicts
        9. ALWAYS use the EXACT parameter names from the original function
        10. NEVER redefine the function being tested
        11. FOLLOW PROPER C CODE STRUCTURE:
           - Include directives first
           - Type definitions next
           - Function declarations next
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