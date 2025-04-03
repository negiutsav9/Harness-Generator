"""
Harness evaluator node for CBMC harness generator workflow with unified RAG integration.
"""
import time
import logging
import os
import re
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
        
        # Add success metric with enhanced metrics
        metrics = {
            "verification_status": "SUCCESS",
            "reachable_lines": cbmc_result.get("reachable_lines", 0),
            "covered_lines": cbmc_result.get("covered_lines", 0),
            "coverage_pct": cbmc_result.get("coverage_pct", 0.0),
            "errors": 0,
            # Add enhanced metrics
            "func_reachable_lines": cbmc_result.get("func_reachable_lines", 0),
            "func_covered_lines": cbmc_result.get("func_covered_lines", 0),
            "func_coverage_pct": cbmc_result.get("func_coverage_pct", 0.0),
            "error_categories": []
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
        
        # ENHANCEMENT 1: Detect dynamic memory leak issues and provide targeted solution
        if "memory_leak" in cbmc_result.get("error_categories", []) or "__CPROVER_memory_leak" in cbmc_stdout:
            # Extract malloc calls that may not be freed
            malloc_matches = re.findall(r'(\w+)\s*=\s*(?:malloc|calloc)\([^;]+\)', harness_code)
            
            # Check which of these variables don't have matching free() calls
            unfree_vars = []
            for var in malloc_matches:
                if f"free({var})" not in harness_code:
                    unfree_vars.append(var)
            
            # Add specific memory leak fix recommendation
            if unfree_vars:
                improvement_recommendation += "\n\n=========================================\n"
                improvement_recommendation += "MEMORY LEAK RESOLUTION\n"
                improvement_recommendation += "=========================================\n"
                improvement_recommendation += f"Found {len(unfree_vars)} allocated variables that are not being freed:\n"
                
                for var in unfree_vars:
                    improvement_recommendation += f"- {var}\n"
                
                improvement_recommendation += "\nAdd explicit free operations for these variables to fix memory leaks:\n\n"
                improvement_recommendation += "```c\n"
                for var in unfree_vars:
                    improvement_recommendation += f"// Free allocated memory for {var}\n"
                    improvement_recommendation += f"free({var});\n"
                improvement_recommendation += "```\n\n"
                improvement_recommendation += "Make sure to add these free operations before the function exits or returns.\n"
        
        # ENHANCEMENT 2: Check for UNKNOWN status that requires stubs,
        # but ONLY create stubs for MISSING functions, not existing dependencies
        if (current_attempts == 4 or current_attempts == 5) and "UNKNOWN" in cbmc_result.get("status", ""):
            # Get missing functions from CBMC result
            missing_functions = cbmc_result.get("missing_functions", [])
            
            # Extract all function calls from the harness
            function_calls = set(re.findall(r'\b(\w+)\s*\(', harness_code))
            
            # Remove standard library and CBMC-specific functions
            standard_funcs = {
                "malloc", "calloc", "realloc", "free", "memset", "memcpy", "memmove",
                "printf", "fprintf", "sprintf", "__CPROVER_assume", "__CPROVER_assert"
            }
            function_calls = function_calls - standard_funcs
            
            # Filter to only truly missing functions to avoid creating stubs for existing dependencies
            truly_missing = []
            
            for func in missing_functions:
                # Check if function exists in the database
                function_exists = False
                
                # Check in RAG database
                if rag_db.get_code_function(func):
                    function_exists = True
                
                # Check in code_collection if not found in RAG
                if not function_exists:
                    from core.embedding_db import code_collection
                    try:
                        func_result = code_collection.get(ids=[func], include=["documents"])
                        if func_result["ids"]:
                            function_exists = True
                    except:
                        pass
                
                # Only add truly missing functions
                if not function_exists:
                    truly_missing.append(func)
            
            # Now generate stubs only for truly missing functions
            if truly_missing:
                # Generate stub recommendations
                stub_recommendations = generate_stub_implementations(truly_missing, cbmc_stdout)
                
                # Add stub recommendations to improvement recommendation
                improvement_recommendation += "\n\n=========================================\n"
                improvement_recommendation += "MISSING FUNCTION STUB IMPLEMENTATION\n"
                improvement_recommendation += "=========================================\n"
                improvement_recommendation += f"After multiple refinement attempts, verification is still missing {len(truly_missing)} functions.\n"
                improvement_recommendation += "Implement the following stub functions:\n\n"
                improvement_recommendation += stub_recommendations
                
                logger.info(f"Added stub implementation recommendations for {len(truly_missing)} missing functions")
        
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
            
            # Add failure metric with enhanced metrics
            metrics = {
                "verification_status": cbmc_result.get("status", "FAILED"),
                "reachable_lines": cbmc_result.get("reachable_lines", 0),
                "covered_lines": cbmc_result.get("covered_lines", 0),
                "coverage_pct": cbmc_result.get("coverage_pct", 0.0),
                "errors": cbmc_result.get("errors", 0),
                # Add enhanced metrics
                "func_reachable_lines": cbmc_result.get("func_reachable_lines", 0),
                "func_covered_lines": cbmc_result.get("func_covered_lines", 0),
                "func_coverage_pct": cbmc_result.get("func_coverage_pct", 0.0),
                "error_categories": cbmc_result.get("error_categories", [])
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
            
            # Add final failure metric with enhanced metrics
            metrics = {
                "verification_status": cbmc_result.get("status", "FAILED"),
                "reachable_lines": cbmc_result.get("reachable_lines", 0),
                "covered_lines": cbmc_result.get("covered_lines", 0),
                "coverage_pct": cbmc_result.get("coverage_pct", 0.0),
                "errors": cbmc_result.get("errors", 0),
                # Add enhanced metrics
                "func_reachable_lines": cbmc_result.get("func_reachable_lines", 0),
                "func_covered_lines": cbmc_result.get("func_covered_lines", 0),
                "func_coverage_pct": cbmc_result.get("func_coverage_pct", 0.0),
                "error_categories": cbmc_result.get("error_categories", [])
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
        
        # Add success metric with enhanced metrics
        metrics_tracker = get_metrics_tracker()
        metrics = {
            "verification_status": "SUCCESS",
            "reachable_lines": cbmc_result.get("reachable_lines", 0),
            "covered_lines": cbmc_result.get("covered_lines", 0),
            "coverage_pct": cbmc_result.get("coverage_pct", 0.0),
            "errors": 0,
            # Add enhanced metrics
            "func_reachable_lines": cbmc_result.get("func_reachable_lines", 0),
            "func_covered_lines": cbmc_result.get("func_covered_lines", 0),
            "func_coverage_pct": cbmc_result.get("func_coverage_pct", 0.0),
            "error_categories": []
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

# Helper functions for handling UNKNOWN status

def extract_unknown_functions(cbmc_stdout):
    """
    Extract function names and issues with UNKNOWN status from CBMC output.
    
    Args:
        cbmc_stdout: CBMC standard output
        
    Returns:
        Dictionary mapping function names to issues
    """
    unknown_functions = {}
    
    # Extract function and file names from CBMC output
    function_pattern = r'(\w+\.c) function (\w+)'
    function_matches = re.finditer(function_pattern, cbmc_stdout)
    
    for match in function_matches:
        file_name = match.group(1)
        function_name = match.group(2)
        
        # Look for UNKNOWN issues in this function
        # Extract lines after this function declaration
        function_index = match.end()
        next_chunk = cbmc_stdout[function_index:function_index + 2000]  # Look at next 2000 chars
        
        # Extract issues with UNKNOWN status
        unknown_issues = []
        unknown_lines = re.finditer(r'\[(\w+\.\w+\.\d+)\].+: UNKNOWN', next_chunk)
        
        for issue in unknown_lines:
            issue_id = issue.group(1)
            issue_line = issue.group(0).strip()
            unknown_issues.append((issue_id, issue_line))
        
        if unknown_issues:
            unknown_functions[function_name] = {
                "file_name": file_name,
                "issues": unknown_issues
            }
    
    # If no functions found with the pattern, try a more general approach
    if not unknown_functions:
        # Try to find all lines with UNKNOWN status and extract function names
        unknown_lines = re.finditer(r'\[(\w+)\.(\w+)\.(\d+)\].+line (\d+).+: UNKNOWN', cbmc_stdout)
        
        for issue in unknown_lines:
            function_prefix = issue.group(1)
            issue_type = issue.group(2)
            line_num = issue.group(4)
            issue_line = issue.group(0).strip()
            
            # Use the function prefix as the function name
            if function_prefix not in unknown_functions:
                unknown_functions[function_prefix] = {
                    "file_name": "unknown.c",
                    "issues": []
                }
            
            unknown_functions[function_prefix]["issues"].append((f"{function_prefix}.{issue_type}", issue_line))
    
    return unknown_functions

def generate_stub_implementations(unknown_functions, cbmc_stdout):
    """
    Generate stub implementation recommendations for functions with UNKNOWN status.
    
    Args:
        unknown_functions: Dictionary of functions with UNKNOWN status or list of function names
        cbmc_stdout: CBMC standard output
        
    Returns:
        String with recommended stub implementations
    """
    stub_recommendations = ""
    
    # Handle both dictionary and list input formats
    if isinstance(unknown_functions, list):
        # Convert list to dictionary format expected by the rest of the function
        function_dict = {}
        for func_name in unknown_functions:
            function_dict[func_name] = {
                "file_name": "unknown.c",
                "issues": [("unknown", "Unknown issue")]
            }
        unknown_functions = function_dict
    
    for function_name, data in unknown_functions.items():
        file_name = data.get("file_name", "unknown.c")
        issues = data.get("issues", [])
        
        # Get unique issue types
        issue_types = set()
        for issue_id, issue_line in issues:
            # Extract issue type: pointer_arithmetic, pointer_dereference, etc.
            if "pointer_arithmetic" in issue_id:
                issue_types.add("pointer_arithmetic")
            elif "pointer_dereference" in issue_id:
                issue_types.add("pointer_dereference")
            elif "array_bounds" in issue_id:
                issue_types.add("array_bounds")
            elif "null_pointer" in issue_id:
                issue_types.add("null_pointer")
            elif "memory_leak" in issue_id:
                issue_types.add("memory_leak")
            else:
                issue_types.add("unknown_issue")
        
        # Get function signature if possible
        signature = extract_function_signature(cbmc_stdout, function_name)
        
        if not signature:
            # Create a generic signature
            signature = f"void {function_name}(...)"
        
        # Generate stub implementation based on issue types
        stub_recommendations += f"// Stub for function: {function_name} in {file_name}\n"
        stub_recommendations += f"// Issues: {', '.join(issue_types)}\n"
        
        # Generate stub code
        stub_recommendations += generate_stub_code(signature, issue_types) + "\n\n"
    
    return stub_recommendations

def extract_function_signature(cbmc_stdout, function_name):
    """
    Extract function signature from CBMC output if possible.
    
    Args:
        cbmc_stdout: CBMC standard output
        function_name: Name of the function
        
    Returns:
        Function signature or None if not found
    """
    # Look for function declaration in the output
    signature_pattern = fr'{function_name}\s*\(([^)]*)\)'
    signature_match = re.search(signature_pattern, cbmc_stdout)
    
    if signature_match:
        params = signature_match.group(1).strip()
        
        # Try to find return type
        return_type_pattern = fr'(\w+\s+)+{function_name}\s*\('
        return_type_match = re.search(return_type_pattern, cbmc_stdout)
        
        if return_type_match:
            return_type = return_type_match.group(0).replace(f"{function_name}(", "").strip()
        else:
            return_type = "void"  # Default return type
        
        return f"{return_type} {function_name}({params})"
    
    return None

def generate_stub_code(signature, issue_types):
    """
    Generate appropriate stub code based on function signature and issue types.
    
    Args:
        signature: Function signature
        issue_types: Set of issue types
        
    Returns:
        Stub implementation
    """
    # Extract function name and parameters
    signature_parts = signature.split("(", 1)
    func_header = signature_parts[0].strip()
    params_part = "(" + signature_parts[1]
    
    # Extract return type and function name
    header_parts = func_header.split()
    if len(header_parts) >= 2:
        return_type = " ".join(header_parts[:-1])
        func_name = header_parts[-1]
    else:
        return_type = "void"
        func_name = func_header
    
    # Generate parameter names for preconditions
    params_list = params_part.strip("()").split(",")
    param_names = []
    
    for i, param in enumerate(params_list):
        if param.strip() and param.strip() != "void":
            # Extract parameter name
            param_parts = param.strip().split()
            if len(param_parts) >= 2:
                param_name = param_parts[-1].strip("*")
            else:
                param_name = f"param{i+1}"
            
            # Add to parameter names list
            param_names.append((param, param_name))
    
    # Generate stub code
    stub_code = f"extern {signature} {{\n"
    
    # Add contract-style preconditions
    if "pointer_arithmetic" in issue_types or "pointer_dereference" in issue_types:
        stub_code += "    // PRECONDITIONS for pointer safety\n"
        
        for param, name in param_names:
            if "*" in param:
                stub_code += f"    __CPROVER_precondition({name} != NULL, \"{name} must not be NULL\");\n"
                
                # For array parameters, add size precondition
                if "[]" in param or ("pointer" in param.lower()):
                    stub_code += f"    size_t {name}_size = nondet_size_t();\n"
                    stub_code += f"    __CPROVER_assume({name}_size > 0 && {name}_size <= 100);\n"
    
    # Add additional preconditions based on issue types
    if "array_bounds" in issue_types:
        stub_code += "    // PRECONDITIONS for array bounds safety\n"
        for param, name in param_names:
            if "*" in param or "[]" in param:
                stub_code += f"    size_t {name}_index = nondet_size_t();\n"
                stub_code += f"    __CPROVER_assume({name}_index < {name}_size);\n"
    
    # Add non-deterministic return value for non-void functions
    if return_type != "void":
        stub_code += f"\n    // Return a non-deterministic value of appropriate type\n"
        
        if return_type in ["int", "unsigned int", "long", "unsigned long"]:
            stub_code += f"    {return_type} result = nondet_{return_type.replace(' ', '_')}();\n"
            stub_code += f"    return result;\n"
        elif return_type in ["char", "unsigned char"]:
            stub_code += f"    {return_type} result = nondet_{return_type.replace(' ', '_')}();\n"
            stub_code += f"    return result;\n"
        elif "*" in return_type:
            # Pointer return type
            stub_code += f"    {return_type} result = NULL;\n"
            stub_code += f"    return result;\n"
        else:
            # Generic return
            stub_code += f"    {return_type} result;\n"
            stub_code += f"    return result;\n"
    
    # Close function
    stub_code += "}"
    
    return stub_code

def route_from_evaluator(state):
    """Routes from evaluator to either generator (for refinement) or junction (for next function)."""
    return state.get("next", "junction")