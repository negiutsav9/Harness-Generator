"""
Harness evaluator node for CBMC harness generator workflow with unified RAG integration.
"""
import time
import logging
import os
from langchain_core.messages import AIMessage
from utils.cbmc_parser import generate_improvement_recommendation
from utils.rag import get_unified_db
from utils.metrics_utils import get_metrics_tracker

# Set up logging
logger = logging.getLogger("evaluator")

def harness_evaluator_node(state):
    """Evaluates harnesses using CBMC output and stores knowledge in unified RAG database."""
    evaluation_start = time.time()
    
    func_name = state.get("current_function", "")
    loop_counter = state.get("loop_counter", 0)
    
    logger.info(f"Evaluating harness for {func_name}")
    
    harnesses = state.get("harnesses", {})
    cbmc_results = state.get("cbmc_results", {})
    
    # Get result directories for RAG storage
    result_directories = state.get("result_directories", {})
    
    # Initialize unified RAG database
    rag_db = get_unified_db(os.path.join(result_directories.get("result_base_dir", "results"), "rag_data"))

    # Initialize function times tracking
    function_times = state.get("function_times", {}).copy()
    if func_name not in function_times:
        function_times[func_name] = {}
    
    # Initialize refinement attempts tracking
    state_refinement_attempts = state.get("refinement_attempts", {}).copy()
    if func_name not in state_refinement_attempts:
        state_refinement_attempts[func_name] = 0
    
    current_attempts = state_refinement_attempts.get(func_name, 0)
    max_refinements = 9  # Maximum number of refinement attempts
    
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
    
    # Get function code from RAG database first
    function_data = rag_db.get_code_function(func_name)
    func_code = ""
    
    if function_data:
        func_code = function_data["code"]
        logger.info(f"Retrieved function {func_name} from unified RAG database")
    else:
        # Fall back to code_collection if not in RAG database
        from core.embedding_db import code_collection
        function_result = code_collection.get(ids=[func_name], include=["documents", "metadatas"])
        
        if function_result["ids"]:
            func_code = function_result["documents"][0]
            
            # Store in unified database for future use
            rag_db.add_code_function(
                func_name, 
                func_code, 
                function_result["metadatas"][0]
            )
            logger.info(f"Retrieved function {func_name} from legacy code database")
        else:
            # Couldn't find function code
            if func_name not in state_processed_functions:
                state_processed_functions.append(func_name)
                logger.info(f"Function {func_name} not found in any database")
            
            return {
                "messages": [AIMessage(content=f"Error: Function {func_name} metadata not found. Marking as processed.")],
                "processed_functions": state_processed_functions,
                "loop_counter": loop_counter,
                "next": "junction"
            }
    
    # Check if verification was successful
    if cbmc_result.get("status") == "SUCCESS":
        # Store successful solution in the unified database
        logger.info(f"CBMC verification successful for {func_name}, storing solution in RAG database")
        
        solution_id = rag_db.store_solution(
            "",  # No error ID since there was no error
            func_name, 
            harness_code, 
            cbmc_result,
            current_attempts + 1
        )
        logger.info(f"Stored successful solution as {solution_id} in unified RAG database")
        
        # Mark function as processed
        if func_name not in state_processed_functions:
            state_processed_functions.append(func_name)
        
        # Get metrics tracker
        metrics_tracker = get_metrics_tracker()
        
        # Add success metric
        metrics = {
            "verification_status": "SUCCESS",
            "reachable_lines": cbmc_result.get("reachable_lines", 0),
            "covered_lines": cbmc_result.get("covered_lines", 0),
            "coverage_pct": cbmc_result.get("coverage_pct", 0.0),
            "errors": 0
        }
        
        evaluation_time_ms = int((time.time() - evaluation_start) * 1000)
        metrics_tracker.add_function_metrics(func_name, current_attempts + 1, metrics, evaluation_time_ms)
        
        return {
            "messages": [AIMessage(content=f"CBMC verification successful for {func_name}. Solution stored in knowledge base. Moving to next function.")],
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
        # Store the error in the unified database
        error_id = rag_db.store_error(
            func_name,
            harness_code,
            cbmc_result,
            current_attempts
        )
        logger.info(f"Stored error as {error_id} in unified RAG database")
        
        # Use our simplified recommendation generator
        improvement_recommendation = generate_improvement_recommendation(harness_code, func_code, cbmc_result)
        logger.info(f"Generated improvement recommendation for {func_name}")
        
        # Enhance the recommendation with RAG knowledge from similar issues
        rag_recommendations = rag_db.get_recommendations(
            func_name,
            func_code,
            cbmc_result,
            harness_code
        )
        
        if rag_recommendations and (rag_recommendations["has_similar_errors"] or rag_recommendations["has_matching_patterns"]):
            # Add RAG insights to the recommendation
            enhancement = "\n\nINSIGHTS FROM KNOWLEDGE BASE:\n"
            
            # Add similar errors info
            if rag_recommendations["has_similar_errors"]:
                similar_errors = rag_recommendations["similar_errors"]
                enhancement += f"\nFound {len(similar_errors)} similar errors in other functions:"
                for i, error in enumerate(similar_errors[:2]):  # Show top 2
                    enhancement += f"\n- Similar error in {error['func_name']}: {error['error_message']}"
            
            # Add matching patterns
            if rag_recommendations["has_matching_patterns"]:
                patterns = rag_recommendations["matching_patterns"]
                enhancement += f"\n\nMatching vulnerability patterns:"
                for name, pattern in patterns.items():
                    enhancement += f"\n- {pattern['description']} (Severity: {pattern['severity']})"
                    enhancement += f"\n  Strategy: {pattern['verification_strategy']}"
            
            # Add the enhancement to the recommendation
            improvement_recommendation += enhancement
            logger.info(f"Enhanced recommendation with insights from RAG database")
    else:
        improvement_recommendation = ""
        logger.info(f"No improvements needed for {func_name}")
    
    # Calculate evaluation time
    evaluation_time = time.time() - evaluation_start

    # Update function times
    function_times[func_name]["evaluation"] = evaluation_time
    
    # Update refinement attempts if needed
    if needs_improvement:
        if current_attempts < max_refinements - 1:  # Allow one more attempt
            state_refinement_attempts[func_name] = current_attempts + 1
            logger.info(f"Incrementing refinement attempts for {func_name} to {state_refinement_attempts[func_name]} of {max_refinements}")
            
            # Get metrics tracker
            metrics_tracker = get_metrics_tracker()
            
            # Add failure metric
            metrics = {
                "verification_status": cbmc_result.get("status", "FAILED"),
                "reachable_lines": cbmc_result.get("reachable_lines", 0),
                "covered_lines": cbmc_result.get("covered_lines", 0),
                "coverage_pct": cbmc_result.get("coverage_pct", 0.0),
                "errors": cbmc_result.get("errors", 0)
            }
            
            evaluation_time_ms = int(evaluation_time * 1000)
            metrics_tracker.add_function_metrics(func_name, current_attempts + 1, metrics, evaluation_time_ms)
            
            return {
                "messages": [AIMessage(content=f"Evaluated harness for {func_name}. Needs improvement (attempt {current_attempts + 1} of {max_refinements}). Using insights from unified knowledge base.")],
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
            
            # Get metrics tracker
            metrics_tracker = get_metrics_tracker()
            
            # Add final failure metric
            metrics = {
                "verification_status": cbmc_result.get("status", "FAILED"),
                "reachable_lines": cbmc_result.get("reachable_lines", 0),
                "covered_lines": cbmc_result.get("covered_lines", 0),
                "coverage_pct": cbmc_result.get("coverage_pct", 0.0),
                "errors": cbmc_result.get("errors", 0)
            }
            
            evaluation_time_ms = int(evaluation_time * 1000)
            metrics_tracker.add_function_metrics(func_name, current_attempts + 1, metrics, evaluation_time_ms)
            
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
        
        # Add success metric
        metrics_tracker = get_metrics_tracker()
        metrics = {
            "verification_status": "SUCCESS",
            "reachable_lines": cbmc_result.get("reachable_lines", 0),
            "covered_lines": cbmc_result.get("covered_lines", 0),
            "coverage_pct": cbmc_result.get("coverage_pct", 0.0),
            "errors": 0
        }
        
        evaluation_time_ms = int(evaluation_time * 1000)
        metrics_tracker.add_function_metrics(func_name, current_attempts + 1, metrics, evaluation_time_ms)
        
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