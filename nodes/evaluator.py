"""
Harness evaluator node for CBMC harness generator workflow.
"""
import time
import sys
import re
import logging
from langchain_core.messages import AIMessage, HumanMessage
from core.embedding_db import code_collection

# Set up logging
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                   handlers=[logging.FileHandler("cbmc_evaluator.log"), logging.StreamHandler()])
logger = logging.getLogger("evaluator")

def harness_evaluator_node(state):
    """Evaluates the quality of generated harnesses based on CBMC output and suggests improvements."""
    evaluation_start = time.time()
    
    # SAFETY: Get and increment loop counter to prevent infinite recursion
    loop_counter = state.get("loop_counter", 0)
    logger.info(f"Evaluator node - function: {state.get('current_function', '')}, loop: {loop_counter}")
    
    func_name = state.get("current_function", "")
    harnesses = state.get("harnesses", {})
    cbmc_results = state.get("cbmc_results", {})
    
    # Get error tracking dictionaries
    cbmc_error_messages = state.get("cbmc_error_messages", {})
    harness_syntax_errors = state.get("harness_syntax_errors", {})
    parsing_issues = state.get("parsing_issues", {})
    verification_failures = state.get("verification_failures", {})
    
    # SAFETY: Initialize refinement_attempts if not present for this function
    refinement_attempts = state.get("refinement_attempts", {}).copy()
    if func_name not in refinement_attempts:
        refinement_attempts[func_name] = 0
    
    # Get current attempts count
    current_attempts = refinement_attempts.get(func_name, 0)
    logger.info(f"Current refinement attempts for {func_name}: {current_attempts}")
    
    # SAFETY: Force progression after max attempts regardless of other conditions
    max_refinements = 3
    if current_attempts >= max_refinements:
        processed_functions = state.get("processed_functions", []).copy()
        if func_name not in processed_functions:
            processed_functions.append(func_name)
            logger.info(f"Max refinements reached, marking {func_name} as processed")
        
        return {
            "messages": [AIMessage(content=f"Maximum refinement attempts ({max_refinements}) reached for {func_name}. Moving to next function.")],
            "refinement_attempts": refinement_attempts,
            "processed_functions": processed_functions,
            "loop_counter": loop_counter,
            "next": "junction"
        }
    
    # SAFETY: Handle missing data
    harness_code = harnesses.get(func_name, "")
    cbmc_result = cbmc_results.get(func_name, {})
    
    if not harness_code or not cbmc_result:
        # Mark this function as processed even if there was an error
        processed_functions = state.get("processed_functions", []).copy()
        if func_name and func_name not in processed_functions:
            processed_functions.append(func_name)
            logger.info(f"Missing harness/CBMC data, marking {func_name} as processed")
        
        return {
            "messages": [AIMessage(content=f"Error: Missing harness or CBMC result for function {func_name}. Marking as processed.")],
            "processed_functions": processed_functions,
            "loop_counter": loop_counter,
            "next": "junction"  # Move to next function
        }
    
    # Extract function details from code database
    function_result = code_collection.get(ids=[func_name], include=["documents", "metadatas"])
    if not function_result["ids"]:
        # Mark this function as processed even if there's an error
        processed_functions = state.get("processed_functions", []).copy()
        if func_name not in processed_functions:
            processed_functions.append(func_name)
            logger.info(f"Function metadata not found, marking {func_name} as processed")
        
        return {
            "messages": [AIMessage(content=f"Error: Function {func_name} metadata not found. Marking as processed.")],
            "processed_functions": processed_functions,
            "loop_counter": loop_counter,
            "next": "junction"
        }
    
    func_code = function_result["documents"][0]
    func_metadata = function_result["metadatas"][0]
    
    # Get CBMC output
    cbmc_stdout = cbmc_result.get("stdout", "")
    cbmc_stderr = cbmc_result.get("stderr", "")
    cbmc_status = cbmc_result.get("status", "UNKNOWN")
    verification_message = cbmc_result.get("message", "")
    suggestions = cbmc_result.get("suggestions", "")
    
    # Check for specific errors in STDERR
    include_errors = re.findall(r"function '([^']+)' is not declared", cbmc_stderr)
    syntax_errors = re.findall(r"file ([^\s]+) line (\d+) function ([^\s]+): (.+)", cbmc_stderr)
    nondet_errors = re.findall(r"function '(nondet_[^']+)' is not declared", cbmc_stderr)
    no_body_errors = re.findall(r"main symbol '([^']+)' has no body", cbmc_stderr)
    incompatible_types = re.findall(r"conversion from '([^']+)' to '([^']+)': incompatible pointer types", cbmc_stderr)
    
    # Set evaluation criteria for harness quality
    evaluation_criteria = {
        "has_nondet_inputs": "__CPROVER_" in harness_code and "nondet" in harness_code,
        "has_assertions": "__CPROVER_assert" in harness_code,
        "has_assumptions": "__CPROVER_assume" in harness_code,
        "checks_memory_leaks": "memory leak" in harness_code.lower() or "free" in harness_code,
        "checks_bounds": "bounds" in harness_code.lower() or "index" in harness_code.lower(),
        "checks_arithmetic": any(op in harness_code for op in ["overflow", "division", "zero"]),
        "addresses_cbmc_errors": False,
        "verification_passed": cbmc_status == "SUCCESS",
        "syntactically_valid": not "syntax error" in cbmc_stderr
    }
    
    # Calculate overall quality score
    quality_score = sum(1 for criterion, value in evaluation_criteria.items() if value) / len(evaluation_criteria)
    quality_score = round(quality_score * 100)
    
    # Build the improvement recommendation based on CBMC results
    improvement_recommendation = ""
    needs_improvement = False
    
    # Handle include errors
    if include_errors:
        needs_improvement = True
        missing_includes = {}
        for func in include_errors:
            if func == 'malloc' or func == 'free':
                missing_includes['stdlib.h'] = True
            elif func == 'memcpy' or func == 'memmove' or func == 'strncpy':
                missing_includes['string.h'] = True
            elif func.startswith('nondet_'):
                missing_includes['nondet functions'] = True
        
        include_suggestions = []
        if 'stdlib.h' in missing_includes:
            include_suggestions.append("Add #include <stdlib.h> for malloc/free")
        if 'string.h' in missing_includes:
            include_suggestions.append("Add #include <string.h> for string functions")
        if 'nondet functions' in missing_includes:
            include_suggestions.append("Add proper declarations for nondet functions. For example:\n" +
                                       "extern int __CPROVER_int_nondet();\n" +
                                       "#define nondet_int __CPROVER_int_nondet\n" +
                                       "extern size_t __CPROVER_size_t_nondet();\n" +
                                       "#define nondet_size_t __CPROVER_size_t_nondet")
        
        # First handle syntax or parsing errors
        improvement_recommendation = f"""
        Previous harness for {func_name} has missing include files or declarations that need to be fixed.
        
        CBMC errors:
        {', '.join([f"Function '{func}' is not declared" for func in include_errors])}
        
        Current harness:
        ```c
        {harness_code}
        ```
        
        Original function:
        ```c
        {func_code}
        ```
        
        Please fix the harness by adding the necessary includes and declarations:
        {', '.join(include_suggestions)}
        
        Generate a complete, syntactically valid harness that properly includes all necessary headers and declarations.
        """
    # Handle nondet function errors
    elif nondet_errors:
        needs_improvement = True
        nondet_types = [func.replace('nondet_', '') for func in nondet_errors]
        
        improvement_recommendation = f"""
        Previous harness for {func_name} is using nondet functions that are not properly declared.
        
        CBMC errors:
        {', '.join([f"Function '{func}' is not declared" for func in nondet_errors])}
        
        Current harness:
        ```c
        {harness_code}
        ```
        
        Please add the following declarations at the top of your harness:
        
        ```c
        // Add CBMC nondet function declarations
        {chr(10).join([f"extern {type}_t __CPROVER_{type}_t_nondet();" for type in nondet_types])}
        {chr(10).join([f"#define nondet_{type} __CPROVER_{type}_t_nondet" for type in nondet_types])}
        ```
        
        Generate a complete, syntactically valid harness with proper nondet function declarations.
        """
    # Handle no body errors
    elif no_body_errors:
        needs_improvement = True
        
        improvement_recommendation = f"""
        CBMC cannot find the implementation of function '{no_body_errors[0]}'. This means either:
        1. The function is not defined in the source files included in the verification, or
        2. The verification is targeting the wrong function.
        
        CBMC error: main symbol '{no_body_errors[0]}' has no body
        
        Current harness:
        ```c
        {harness_code}
        ```
        
        Please make sure your harness is designed to test the correct function. If needed, add a stub implementation or make sure the harness is properly designed to target the function you want to verify.
        
        Also, ensure you're using the main() function in your harness, not trying to directly verify the target function.
        """
    # Then handle other verification failures
    elif cbmc_status != "SUCCESS" and verification_failures:
        needs_improvement = True
        
        # Analyze memory issues
        memory_issues = []
        if "memory_leak" in verification_failures.get(func_name, []):
            memory_issues.append("Memory leaks detected - ensure all allocated memory is freed")
        if "null_pointer" in verification_failures.get(func_name, []):
            memory_issues.append("Null pointer dereferences - add null pointer checks")
            
        # Analyze arithmetic issues
        arithmetic_issues = []
        if "division_by_zero" in verification_failures.get(func_name, []):
            arithmetic_issues.append("Division by zero - add checks to ensure divisors are non-zero")
        if "arithmetic_overflow" in verification_failures.get(func_name, []) or "pointer_overflow" in verification_failures.get(func_name, []):
            arithmetic_issues.append("Arithmetic/pointer overflow - add bounds checking")
            
        # Analyze array bounds issues
        array_issues = []
        if "array_bounds" in verification_failures.get(func_name, []):
            array_issues.append("Array bounds violations - verify array indices are within bounds")
            
        # Analyze type conversion issues
        type_issues = []
        if "type_conversion" in verification_failures.get(func_name, []):
            type_issues.append("Type conversion problems - check for information loss in type conversions")
            
        improvement_recommendation = f"""
        Previous harness for {func_name} failed CBMC verification. Quality score: {quality_score}%.
        
        CBMC verification status: {cbmc_status}
        
        CBMC error message: {verification_message}
        
        Suggested fixes: {suggestions}
        
        CBMC output excerpt:
        {cbmc_stdout[:500] if len(cbmc_stdout) > 500 else cbmc_stdout}
        
        STDERR:
        {cbmc_stderr[:500] if len(cbmc_stderr) > 500 else cbmc_stderr}
        
        Current harness:
        ```c
        {harness_code}
        ```
        
        Original function:
        ```c
        {func_code}
        ```
        
        Please improve the harness to address the following issues:
        
        {', '.join(memory_issues) if memory_issues else ''}
        {', '.join(arithmetic_issues) if arithmetic_issues else ''}
        {', '.join(array_issues) if array_issues else ''}
        {', '.join(type_issues) if type_issues else ''}
        
        Generate a complete, working harness that properly tests the function and passes CBMC verification.
        
        Refinement attempt: {current_attempts + 1} of {max_refinements}
        """
    # Finally evaluate general harness quality
    else:
        # Determine if improvement is needed
        needs_improvement = (
            cbmc_status != "SUCCESS" or 
            quality_score < 70 or
            not evaluation_criteria["has_nondet_inputs"] or
            not evaluation_criteria["has_assertions"] or
            (func_metadata.get("has_malloc", False) and not evaluation_criteria["checks_memory_leaks"]) or
            not evaluation_criteria["syntactically_valid"] or
            include_errors or nondet_errors or no_body_errors
        )
        
        if needs_improvement:
            improvement_areas = []
            
            # Generate specific improvement suggestions
            if include_errors or nondet_errors:
                improvement_areas.append("Add necessary includes and function declarations")
            
            if not evaluation_criteria["has_nondet_inputs"]:
                improvement_areas.append("Use CBMC's nondet functions for inputs")
            
            if not evaluation_criteria["has_assertions"]:
                improvement_areas.append("Add CPROVER assertions to verify behavior")
            
            if not evaluation_criteria["has_assumptions"]:
                improvement_areas.append("Use CPROVER assumptions to constrain input values")
            
            if func_metadata.get("has_malloc", False) and not evaluation_criteria["checks_memory_leaks"]:
                improvement_areas.append("Add memory leak verification")
            
            improvement_recommendation = f"""
            Previous harness for {func_name} needs improvement. Quality score: {quality_score}%.
            
            CBMC verification status: {cbmc_status}
            STDERR output:
            {cbmc_stderr[:500] if len(cbmc_stderr) > 500 else cbmc_stderr}
            
            Current harness:
            ```c
            {harness_code}
            ```
            
            Original function:
            ```c
            {func_code}
            ```
            
            Identified issues:
            {', '.join(improvement_areas)}
            
            Please improve the harness to address these issues. Generate a complete, working harness that properly tests the function.
            
            Refinement attempt: {current_attempts + 1} of {max_refinements}
            """
    
    # Calculate evaluation time
    evaluation_time = time.time() - evaluation_start
    
    # Update function times dictionary
    function_times = state.get("function_times", {}).copy()
    if func_name not in function_times:
        function_times[func_name] = {}
    function_times[func_name]["evaluation"] = evaluation_time
    
    # CRITICAL: Update refinement attempts BEFORE returning
    # This ensures we don't get stuck in an infinite loop
    if needs_improvement:
        refinement_attempts[func_name] = current_attempts + 1
        logger.info(f"Incremented refinement attempts for {func_name} to {refinement_attempts[func_name]}")
    
    # CRITICAL: Mark as processed if NOT going to refine
    # This ensures forward progress in the workflow
    processed_functions = state.get("processed_functions", []).copy()
    if not needs_improvement:
        if func_name not in processed_functions:
            processed_functions.append(func_name)
            logger.info(f"No more improvements needed, marking {func_name} as processed")
    
    # CRITICAL: Return loop_counter to prevent recursive error
    return {
        "messages": [AIMessage(content=f"Evaluated harness for {func_name} in {evaluation_time:.2f}s. {cbmc_status}. {'Improvements needed.' if needs_improvement else 'No improvements needed.'}")],
        "refinement_attempts": refinement_attempts,
        "processed_functions": processed_functions,
        "improvement_recommendation": improvement_recommendation,
        "function_times": function_times,
        "loop_counter": loop_counter,  # Pass the loop counter to maintain recursion tracking
        "next": "generator" if needs_improvement else "junction"
    }

def route_from_evaluator(state):
    """Routes from evaluator to either generator (for refinement) or junction (for next function)."""
    return state.get("next", "junction")