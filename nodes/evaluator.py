"""
Harness evaluator node for CBMC harness generator workflow.
"""
import time
import logging
from langchain_core.messages import AIMessage
from utils.cbmc_parser import generate_improvement_recommendation

# Set up logging
logger = logging.getLogger("evaluator")

def harness_evaluator_node(state):
    """Evaluates harnesses using CBMC output and generates improvement recommendations."""
    evaluation_start = time.time()
    
    func_name = state.get("current_function", "")
    loop_counter = state.get("loop_counter", 0)
    
    logger.info(f"Evaluating harness for {func_name}")
    
    harnesses = state.get("harnesses", {})
    cbmc_results = state.get("cbmc_results", {})

    # Initialization for function_times
    function_times = state.get("function_times", {}).copy()
    if func_name not in function_times:
        function_times[func_name] = {}
    
    # Safety: Initialize refinement_attempts if not present
    state_refinement_attempts = state.get("refinement_attempts", {}).copy()
    if func_name not in state_refinement_attempts:
        state_refinement_attempts[func_name] = 0
    
    current_attempts = state_refinement_attempts.get(func_name, 0)
    max_refinements = 3  # Reduced from 6 to be more focused
    
    # Get processed functions from state
    state_processed_functions = state.get("processed_functions", []).copy()
    
    # Force progression after max attempts
    if current_attempts >= max_refinements:
        if func_name not in state_processed_functions:
            state_processed_functions.append(func_name)
            logger.info(f"Max refinements reached for {func_name}, proceeding to next function")
        
        return {
            "messages": [AIMessage(content=f"Maximum refinement attempts ({max_refinements}) reached for {func_name}. Moving to next function.")],
            "refinement_attempts": state_refinement_attempts,
            "processed_functions": state_processed_functions,
            "loop_counter": loop_counter,
            "next": "junction"
        }
    
    # Safety: Handle missing data
    harness_code = harnesses.get(func_name, "")
    cbmc_result = cbmc_results.get(func_name, {})
    
    if not harness_code or not cbmc_result:
        if func_name and func_name not in state_processed_functions:
            state_processed_functions.append(func_name)
            logger.info(f"Missing data for {func_name}, proceeding to next function")
        
        return {
            "messages": [AIMessage(content=f"Error: Missing harness or CBMC result for function {func_name}. Marking as processed.")],
            "processed_functions": state_processed_functions,
            "loop_counter": loop_counter,
            "next": "junction"
        }
    
    # Get function code from CodeDB
    from core.embedding_db import code_collection
    function_result = code_collection.get(ids=[func_name], include=["documents", "metadatas"])
    if not function_result["ids"]:
        if func_name not in state_processed_functions:
            state_processed_functions.append(func_name)
            logger.info(f"Function {func_name} not found in database")
        
        return {
            "messages": [AIMessage(content=f"Error: Function {func_name} metadata not found. Marking as processed.")],
            "processed_functions": state_processed_functions,
            "loop_counter": loop_counter,
            "next": "junction"
        }
    
    func_code = function_result["documents"][0]
    
    # Check if verification was successful
    if cbmc_result.get("status") == "SUCCESS":
        # If verification was successful, skip further analysis and mark as processed
        if func_name not in state_processed_functions:
            state_processed_functions.append(func_name)
        logger.info(f"CBMC verification successful for {func_name}, marking as processed and moving to next function")
        
        return {
            "messages": [AIMessage(content=f"CBMC verification successful for {func_name}. Moving to next function.")],
            "refinement_attempts": state_refinement_attempts,
            "processed_functions": state_processed_functions,
            "function_times": function_times,
            "loop_counter": loop_counter,
            "next": "junction"
        }
    
    # Generate improvement recommendation
    cbmc_stdout = cbmc_result.get("stdout", "")
    cbmc_stderr = cbmc_result.get("stderr", "")
    
    # Determine if the harness needs improvement
    needs_improvement = cbmc_result.get("status") != "SUCCESS"
    
    # Generate the improvement recommendation
    if needs_improvement:
        # Use our simplified recommendation generator
        improvement_recommendation = generate_improvement_recommendation(harness_code, func_code, cbmc_result)
        logger.info(f"Generated improvement recommendation for {func_name}")
    else:
        improvement_recommendation = ""
        logger.info(f"No improvements needed for {func_name}")
    
    # Calculate evaluation time
    evaluation_time = time.time() - evaluation_start

    # Update function times
    function_times = state.get("function_times", {}).copy()
    if func_name not in function_times:
        function_times[func_name] = {}
    function_times[func_name]["evaluation"] = evaluation_time
    
    # Update refinement attempts if needed
    if needs_improvement:
        if current_attempts < max_refinements - 1:  # Allow one more attempt
            state_refinement_attempts[func_name] = current_attempts + 1
            logger.info(f"Incrementing refinement attempts for {func_name} to {state_refinement_attempts[func_name]} of {max_refinements}")
            return {
                "messages": [AIMessage(content=f"Evaluated harness for {func_name}. Needs improvement (attempt {current_attempts + 1} of {max_refinements}).")],
                "refinement_attempts": state_refinement_attempts,
                "processed_functions": state_processed_functions,
                "improvement_recommendation": improvement_recommendation,
                "function_times": function_times,
                "loop_counter": loop_counter,
                "next": "generator"
            }
        else:
            # Last attempt reached, mark as processed and move on
            if func_name not in state_processed_functions:
                state_processed_functions.append(func_name)
            state_refinement_attempts[func_name] = max_refinements  # Ensure we hit the max
            logger.info(f"Final attempt ({max_refinements} of {max_refinements}) for {func_name} completed, moving to next function")
            return {
                "messages": [AIMessage(content=f"Final refinement attempt for {func_name} completed. Moving to next function.")],
                "refinement_attempts": state_refinement_attempts,
                "processed_functions": state_processed_functions,
                "loop_counter": loop_counter,
                "next": "junction"
            }
    else:
        # No improvement needed, mark as processed
        if func_name not in state_processed_functions:
            state_processed_functions.append(func_name)
        logger.info(f"No improvements needed for {func_name}, marking as processed")
        return {
            "messages": [AIMessage(content=f"Evaluation successful for {func_name}. No improvements needed.")],
            "refinement_attempts": state_refinement_attempts,
            "processed_functions": state_processed_functions,
            "loop_counter": loop_counter,
            "next": "junction"
        }

def route_from_evaluator(state):
    """Routes from evaluator to either generator (for refinement) or junction (for next function)."""
    return state.get("next", "junction")