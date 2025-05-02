"""
Junction node for CBMC harness generator workflow.
"""
import logging
import time
from langchain_core.messages import AIMessage

# Set up logging
logger = logging.getLogger("junction")

def junction_node(state):
    """Processes vulnerable functions one at a time in sequential order."""
    # Start timing for this module
    module_start_time = time.time()
    
    # Get lists of functions
    vulnerable_functions = state.get("vulnerable_functions", [])
    processed_functions = state.get("processed_functions", [])
    
    # NEW: Add tracking for failed functions
    failed_functions = state.get("failed_functions", [])
    
    # Safety counter
    loop_counter = state.get("loop_counter", 0) + 1
    
    # Track progress
    total_functions = len(vulnerable_functions)
    completed_functions = len(processed_functions)
    
    logger.info(f"Junction node - processed {completed_functions}/{total_functions} functions")
    
    # Force termination if loop counter gets too high
    if loop_counter > 120:
        logger.warning(f"Loop counter exceeded maximum value. Forcing termination.")
        # Calculate module execution time
        module_time = time.time() - module_start_time
        
        # Update module timings
        module_timings = state.get("module_timings", {})
        if "junction" not in module_timings:
            module_timings["junction"] = 0
        module_timings["junction"] += module_time
        
        logger.info(f"Junction node completed in {module_time:.2f}s - Loop limit exceeded")
        
        return {
            "messages": [AIMessage(content=f"WARNING: Loop counter exceeded maximum value. Forcing termination to avoid recursion error.")],
            "loop_counter": 0,
            "module_timings": module_timings,
            "next": "output"
        }
    
    # Check if all functions processed
    if completed_functions >= total_functions:
        logger.info(f"All {total_functions} functions processed. Moving to output.")
        # Calculate module execution time
        module_time = time.time() - module_start_time
        
        # Update module timings
        module_timings = state.get("module_timings", {})
        if "junction" not in module_timings:
            module_timings["junction"] = 0
        module_timings["junction"] += module_time
        
        logger.info(f"Junction node completed in {module_time:.2f}s - All functions processed")
        
        return {
            "messages": [AIMessage(content=f"All {total_functions} functions have been processed. Moving to final output.")],
            "loop_counter": 0,
            "module_timings": module_timings,
            "next": "output"
        }
    
    # Get current function
    current_function = state.get("current_function", "")
    
    # If current function is in processed_functions or failed_functions, clear it
    if current_function and (current_function in processed_functions or current_function in failed_functions):
        current_function = ""
    
    # If valid current function, continue with it
    if current_function and current_function in vulnerable_functions and current_function not in processed_functions and current_function not in failed_functions:
        logger.info(f"Continuing with function: {current_function}")
        # Calculate module execution time
        module_time = time.time() - module_start_time
        
        # Update module timings
        module_timings = state.get("module_timings", {})
        if "junction" not in module_timings:
            module_timings["junction"] = 0
        module_timings["junction"] += module_time
        
        logger.info(f"Junction node completed in {module_time:.2f}s - Continuing with existing function")
        
        return {
            "messages": [AIMessage(content=f"Continuing processing of function: {current_function}")],
            "current_function": current_function,
            "loop_counter": loop_counter,
            "module_timings": module_timings,
            "next": "generator"
        }
    
    # Find next unprocessed and non-failed function
    for func in vulnerable_functions:
        # Skip pattern-based IDs to prevent processing them as functions
        if func.startswith("pattern:") or "pattern:" in func or ":if" in func or ":for" in func or ":while" in func:
            # If these are in the list but not yet marked as processed, add them to processed
            if func not in processed_functions:
                processed_functions.append(func)
                logger.info(f"Skipping pattern identifier: {func}")
            continue
            
        if func not in processed_functions and func not in failed_functions:
            logger.info(f"Selected next function: {func} ({completed_functions + 1}/{total_functions})")
            # Calculate module execution time
            module_time = time.time() - module_start_time
            
            # Update module timings
            module_timings = state.get("module_timings", {})
            if "junction" not in module_timings:
                module_timings["junction"] = 0
            module_timings["junction"] += module_time
            
            logger.info(f"Junction node completed in {module_time:.2f}s - Selected new function")
            
            return {
                "messages": [AIMessage(content=f"Processing function {completed_functions + 1} of {total_functions}: {func}")],
                "current_function": func,
                "loop_counter": loop_counter,
                "module_timings": module_timings,
                "next": "generator"
            }
    
    # If we get here, all remaining functions have failed
    if failed_functions:
        logger.warning(f"Skipping {len(failed_functions)} failed functions. Moving to output.")
        # Calculate module execution time
        module_time = time.time() - module_start_time
        
        # Update module timings
        module_timings = state.get("module_timings", {})
        if "junction" not in module_timings:
            module_timings["junction"] = 0
        module_timings["junction"] += module_time
        
        logger.info(f"Junction node completed in {module_time:.2f}s - Skipping failed functions")
        
        return {
            "messages": [AIMessage(content=f"Skipped {len(failed_functions)} functions due to errors. Moving to final output.")],
            "loop_counter": 0,
            "module_timings": module_timings,
            "next": "output"
        }
    
    # Fallback - should not reach here
    logger.warning("Junction fallback - all functions appear processed")
    # Calculate module execution time
    module_time = time.time() - module_start_time
    
    # Update module timings
    module_timings = state.get("module_timings", {})
    if "junction" not in module_timings:
        module_timings["junction"] = 0
    module_timings["junction"] += module_time
    
    logger.info(f"Junction node completed in {module_time:.2f}s - Fallback case")
    
    return {
        "messages": [AIMessage(content="All functions appear to be processed. Moving to output.")],
        "loop_counter": 0,
        "module_timings": module_timings,
        "next": "output"
    }

def route_from_junction(state):
    """Routes from junction to either generator or output."""
    return state.get("next", "generator")