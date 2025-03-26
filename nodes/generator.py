"""
Generator node for CBMC harness generator workflow.
"""
import time
import os
import re
import json
import logging
from langchain_core.messages import AIMessage, HumanMessage
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
    
    # Get function code if not refining
    if not is_refinement:
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
        
        # Clear guidance about avoiding unnecessary mocks
        cbmc_verification_info = f"""
        {verification_guide}
        
        IMPORTANT GUIDELINES:
        
        1. Do NOT create mock implementations that aren't necessary for verification.
        2. Focus ONLY on testing the actual function behavior, not on artificial scenarios.
        3. Only implement verification checks that are relevant to this specific function.
        4. Avoid creating test cases for verification types that don't apply to this function.
        5. Keep the harness minimal and focused on real potential issues.
        
        The harness should:
        - Use __CPROVER_assert() only for properties that could actually fail in this function
        - Use __CPROVER_assume() to specify realistic input constraints
        - Use nondet functions like nondet_int() for inputs that need to be nondeterministic
        """
        
        # Build generator prompt with focused verification
        generator_prompt = f"""
        You are a specialized harness generator for CBMC verification.
        Create a MINIMAL, FOCUSED harness for the following function WITHOUT unnecessary mocks:
        
        ```c
        {func_code}
        ```
        
        Function metadata:
        - Return type: {func_metadata.get("return_type", "void")}
        - Parameters: {func_metadata.get("params", "")}
        - Contains malloc: {has_malloc}
        - Contains free: {has_free}
        
        Matching vulnerability patterns:
        {json.dumps(patterns_result.get('matching_patterns', {}), indent=2)}
        
        {cbmc_verification_info}
        
        CRITICAL INSTRUCTIONS:
        1. DO NOT create mock implementations of functions that aren't directly related to verification
        2. DO NOT implement stubs or test code just to satisfy CBMC checklist items
        3. ONLY verify properties that are relevant to this specific function
        4. DO NOT add checks for issues that cannot occur in this function
        5. Keep the harness SMALL and FOCUSED - don't add anything that isn't necessary
        6. If function dependencies are unavailable, minimize assumptions rather than creating elaborate mocks
        7. Follow CBMC's harness structure with a void main() function
        
        Provide only the minimal, focused harness code without explanation.
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
        
        CRITICAL INSTRUCTIONS:
        1. ADDRESS EACH SPECIFIC ISSUE mentioned in the evaluation feedback
        2. ADD all missing header files, function declarations, and constraints
        3. IMPLEMENT all suggested code changes precisely
        4. ENSURE proper memory management (allocation and freeing)
        5. FIX all pointer dereference issues with proper initialization and checks
        6. RESOLVE declaration errors by adding the necessary declarations
        7. IMPLEMENT stubs for functions with missing bodies if needed
        
        Make sure your harness is complete, properly formatted, and addresses ALL the specific issues mentioned in the feedback.
        
        Provide only the improved harness code without explanation.
        """
    
    # Generate the harness
    try:
        logger.info(f"Sending API request to generate harness for {func_name}")
        # Setup messages for the LLM
        response = llm.invoke([
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
                if "int main" not in harness_code and "void main" not in harness_code:
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
        
        # Create harness directory
        harness_base_dir = "harnesses"
        os.makedirs(harness_base_dir, exist_ok=True)
        
        func_harness_dir = os.path.join(harness_base_dir, func_name)
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