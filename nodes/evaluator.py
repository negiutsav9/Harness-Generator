"""
Harness evaluator node for CBMC harness generator workflow.
"""
import time
import re
import json
import logging
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from core.embedding_db import code_collection, query_pattern_db

# Set up logging - simplified
logger = logging.getLogger("evaluator")

def harness_evaluator_node(state):
    """Evaluates harnesses using LLM-powered analysis of CBMC output."""
    evaluation_start = time.time()
    
    loop_counter = state.get("loop_counter", 0)
    func_name = state.get("current_function", "")
    
    logger.info(f"Evaluating harness for {func_name}")
    
    harnesses = state.get("harnesses", {})
    cbmc_results = state.get("cbmc_results", {})

    # Initialization for function_times
    function_times = state.get("function_times", {}).copy()
    if func_name not in function_times:
        function_times[func_name] = {}
    
    # Get error tracking dictionaries
    cbmc_error_messages = state.get("cbmc_error_messages", {})
    harness_syntax_errors = state.get("harness_syntax_errors", {})
    parsing_issues = state.get("parsing_issues", {})
    verification_failures = state.get("verification_failures", {})
    
    # Get proof metrics to ensure we pass them through
    proof_metrics = state.get("proof_metrics", {}).copy()
    
    # Safety: Initialize refinement_attempts if not present
    state_refinement_attempts = state.get("refinement_attempts", {}).copy()
    if func_name not in state_refinement_attempts:
        state_refinement_attempts[func_name] = 0
    
    current_attempts = state_refinement_attempts.get(func_name, 0)
    max_refinements = 3
    
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
            "proof_metrics": proof_metrics,  # Ensure we pass the proof metrics forward
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
            "proof_metrics": proof_metrics,  # Pass proof metrics even on error
            "loop_counter": loop_counter,
            "next": "junction"
        }
    
    # Get function details
    function_result = code_collection.get(ids=[func_name], include=["documents", "metadatas"])
    if not function_result["ids"]:
        if func_name not in state_processed_functions:
            state_processed_functions.append(func_name)
            logger.info(f"Function {func_name} not found in database")
        
        return {
            "messages": [AIMessage(content=f"Error: Function {func_name} metadata not found. Marking as processed.")],
            "processed_functions": state_processed_functions,
            "proof_metrics": proof_metrics,  # Pass proof metrics even on error
            "loop_counter": loop_counter,
            "next": "junction"
        }
    
    func_code = function_result["documents"][0]
    func_metadata = function_result["metadatas"][0]
    
    # Get patterns for this function
    patterns_result = query_pattern_db(func_code)
    matching_patterns = patterns_result.get("matching_patterns", {})
    
    # Get CBMC output
    cbmc_stdout = cbmc_result.get("stdout", "")
    cbmc_stderr = cbmc_result.get("stderr", "")
    cbmc_status = cbmc_result.get("status", "UNKNOWN")
    verification_message = cbmc_result.get("message", "")
    suggestions = cbmc_result.get("suggestions", "")

    # Update this section in the evaluator node:
    if cbmc_status == "SUCCESS":
        # If verification was successful, skip further analysis and mark as processed
        if func_name not in state_processed_functions:
            state_processed_functions.append(func_name)
        logger.info(f"CBMC verification successful for {func_name}, marking as processed and moving to next function")
        
        # Log the proof metrics for successful verifications
        if func_name in proof_metrics:
            metrics = proof_metrics[func_name]
            logger.info(f"Proof metrics for {func_name}: reachable_lines={metrics.get('total_reachable_lines', 0)}, " 
                       f"coverage={metrics.get('total_coverage', 0):.2f}%, errors={metrics.get('reported_errors', 0)}")
        
        return {
            "messages": [AIMessage(content=f"CBMC verification successful for {func_name}. Moving to next function.")],
            "refinement_attempts": state_refinement_attempts,
            "processed_functions": state_processed_functions,
            "function_times": function_times,
            "proof_metrics": proof_metrics,  # Explicitly pass the proof metrics
            "loop_counter": loop_counter,
            "next": "junction"
        }
    
    # Extract actual failure messages
    failure_lines = []
    failure_details = {}
    
    # Scan for FAILURE lines in stdout
    for line in cbmc_stdout.split('\n'):
        if "FAILURE" in line:
            failure_lines.append(line.strip())
            # Extract failure category
            match = re.search(r'\[(.*?)\]', line)
            if match:
                category = match.group(1).split('.')[0]
                detail = line.split("FAILURE")[0] + "FAILURE"
                
                if category not in failure_details:
                    failure_details[category] = []
                failure_details[category].append(detail.strip())
    
    # Find declaration errors in stderr
    declaration_errors = []
    for line in cbmc_stderr.split('\n'):
        if "function" in line and ("not declared" in line or "implicit" in line):
            declaration_errors.append(line.strip())
    
    # Extract current code patterns
    includes = []
    nondet_declarations = []
    nondet_assignments = []
    existing_constraints = []
    buffer_allocations = []
    free_operations = []
    
    for line in harness_code.split('\n'):
        if line.strip().startswith("#include"):
            includes.append(line.strip())
        elif "nondet_" in line and "(" in line and ")" in line and "=" not in line:
            nondet_declarations.append(line.strip())
        elif re.search(r'nondet_\w+\(', line) and '=' in line:
            nondet_assignments.append(line.strip())
        elif "__CPROVER_assume" in line:
            existing_constraints.append(line.strip())
        elif "malloc" in line or "calloc" in line:
            buffer_allocations.append(line.strip())
        elif "free" in line:
            free_operations.append(line.strip())
    
    # Determine specific issues based on failures and errors
    specific_issues = []
    
    # Check for memory leaks
    if "__CPROVER__start.memory-leak" in "".join(failure_lines):
        specific_issues.append("Memory leak: Dynamically allocated memory not freed")
    
    # Check for no-body errors
    no_body_matches = [line for line in failure_lines if "no body for callee" in line]
    if no_body_matches:
        for line in no_body_matches:
            match = re.search(r'no body for callee ([^:]+)', line)
            if match:
                func = match.group(1)
                specific_issues.append(f"Missing implementation for function: {func}")
    
    # Check for assertion failures
    assertion_matches = [line for line in failure_lines if ".assertion." in line]
    if assertion_matches:
        for line in assertion_matches:
            match = re.search(r'line \d+ (.+?):', line)
            if match:
                assertion = match.group(1)
                specific_issues.append(f"Assertion failure: {assertion}")
    
    # Check for pointer issues
    pointer_matches = [line for line in failure_lines if any(x in line.lower() for x in ["pointer", "dereference", "null"])]
    if pointer_matches:
        specific_issues.append("Pointer dereference failure detected")
    
    # Check for arithmetic issues
    arithmetic_matches = [line for line in failure_lines if any(x in line.lower() for x in ["arithmetic", "overflow"])]
    if arithmetic_matches:
        specific_issues.append("Arithmetic overflow detected")
    
    # Check for declaration issues from stderr
    if declaration_errors:
        for error in declaration_errors[:3]:  # Limit to first 3 for readability
            match = re.search(r"function '([^']+)' is not declared", error)
            if match:
                func = match.group(1)
                specific_issues.append(f"Function not declared: {func}")
    
    # Determine specific fixes based on the issues
    specific_fixes = []
    
    # Check for missing header includes
    missing_headers = set()
    if any("malloc" in err for err in declaration_errors):
        missing_headers.add("<stdlib.h>")
    if any("nondet_bool" in err for err in declaration_errors):
        missing_headers.add("<stdbool.h>")
    if any("nondet_size_t" in err for err in declaration_errors):
        missing_headers.add("<stddef.h>")
    if any("INT_MAX" in line or "INT_MIN" in line for line in harness_code.split('\n')) and not any("<limits.h>" in inc for inc in includes):
        missing_headers.add("<limits.h>")
    
    # Add missing header recommendations
    for header in missing_headers:
        specific_fixes.append(f"Add #include {header}")
    
    # Check for missing nondet declarations
    missing_nondets = set()
    for error in declaration_errors:
        match = re.search(r"function '(nondet_[^']+)' is not declared", error)
        if match:
            nondet_func = match.group(1)
            
            if "nondet_bool" in nondet_func:
                missing_nondets.add("bool nondet_bool(void);")
            elif "nondet_size_t" in nondet_func:
                missing_nondets.add("size_t nondet_size_t(void);")
            elif "nondet_uint" in nondet_func:
                missing_nondets.add("unsigned int nondet_uint(void);")
            elif "nondet_int" in nondet_func:
                missing_nondets.add("int nondet_int(void);")
            elif "nondet_char" in nondet_func:
                missing_nondets.add("char nondet_char(void);")
            else:
                missing_nondets.add(f"/* Add declaration for {nondet_func} */")
    
    # Add missing nondet declarations recommendations
    for nondet in missing_nondets:
        specific_fixes.append(f"Add nondet function declaration: {nondet}")
    
    # Check for memory leaks
    if "__CPROVER__start.memory-leak" in "".join(failure_lines):
        # Find allocations without matching free
        allocated_vars = []
        for line in buffer_allocations:
            match = re.search(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(malloc|calloc)', line)
            if match:
                var = match.group(1)
                allocated_vars.append(var)
        
        freed_vars = []
        for line in free_operations:
            match = re.search(r'free\s*\(\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*\)', line)
            if match:
                var = match.group(1)
                freed_vars.append(var)
        
        for var in allocated_vars:
            if var not in freed_vars:
                specific_fixes.append(f"Add free operation for allocated variable: free({var});")
    
    # Check for no body errors
    if no_body_matches:
        specific_fixes.append("Add stubs or mock implementations for functions with missing bodies")
    
    # Check for assertion failures
    if assertion_matches:
        specific_fixes.append("Review and fix assertion conditions based on expected function behavior")
    
    # Check for pointer issues
    if pointer_matches:
        specific_fixes.append("Add NULL checks before dereferencing pointers")
        specific_fixes.append("Add constraints to ensure pointers are valid: __CPROVER_assume(ptr != NULL);")
    
    # Check for arithmetic issues
    if arithmetic_matches:
        specific_fixes.append("Add constraints to limit integer values: __CPROVER_assume(x >= 0 && x < INT_MAX/2);")
    
    # Check buffer allocations
    if buffer_allocations and any("malloc(1)" in alloc for alloc in buffer_allocations):
        specific_fixes.append("Use adequate buffer sizes instead of malloc(1)")
        specific_fixes.append("Add: size_t bufferSize = nondet_size_t(); __CPROVER_assume(bufferSize >= 50 && bufferSize <= 1024);")
    
    # Create a detailed improvement recommendation
    recommendation_prompt = f"""
    Analyze the following CBMC verification failures for function '{func_name}' and suggest specific code improvements:
    
    FUNCTION:
    ```c
    {func_code}
    ```
    
    CURRENT HARNESS:
    ```c
    {harness_code}
    ```
    
    CBMC VERIFICATION FAILURES:
    {chr(10).join(failure_lines[:30]) if failure_lines else "No specific failure lines found"}
    
    DECLARATION ERRORS:
    {chr(10).join(declaration_errors[:10]) if declaration_errors else "No declaration errors found"}
    
    IDENTIFIED ISSUES:
    {chr(10).join(specific_issues)}
    
    CURRENT INCLUDES:
    {chr(10).join(includes) if includes else "No includes found"}
    
    CURRENT NONDET DECLARATIONS:
    {chr(10).join(nondet_declarations) if nondet_declarations else "No nondet declarations found"}
    
    CURRENT CONSTRAINTS:
    {chr(10).join(existing_constraints) if existing_constraints else "No constraints found"}
    
    CURRENT MEMORY ALLOCATIONS:
    {chr(10).join(buffer_allocations) if buffer_allocations else "No memory allocations found"}
    
    CURRENT FREE OPERATIONS:
    {chr(10).join(free_operations) if free_operations else "No free operations found"}
    
    Please provide very specific, concrete code changes to fix these issues. Do NOT try to categorize them into types - focus on fixing the exact issues shown in the CBMC output.
    
    Respond with a JSON object containing:
    {{
        "needs_improvement": true or false,
        "explanation": "Brief explanation of the main issues",
        "specific_issues": ["issue1", "issue2", ...],
        "specific_fixes": ["fix1", "fix2", ...],
        "code_changes": {{
            "add_includes": ["<header1.h>", ...],
            "add_declarations": ["type func(args);", ...],
            "add_constraints": ["__CPROVER_assume(x > 0);", ...],
            "add_initializations": ["memset(&structure, 0, sizeof(structure));", ...],
            "replace_lines": [
                {{"old": "x = nondet_int();", "new": "x = nondet_int(); __CPROVER_assume(x != NULL);"}}
            ],
            "buffer_size_changes": [
                {{"old": "malloc(1)", "new": "size_t bufferSize = nondet_size_t();\\n__CPROVER_assume(bufferSize >= 50 && bufferSize <= 1024);\\nmalloc(bufferSize);"}}
            ],
            "free_operations": [
                "free(ptr);"
            ]
        }}
    }}
    """
    
    # Get LLM recommendations
    from utils.llm_utils import setup_llm
    llm = setup_llm()
    
    try:
        logger.info(f"Requesting specific issue fixes for {func_name}")
        
        # Check for the LLM model type to handle system prompt correctly
        model_name = str(llm).lower()
        
        # Setup messages for the LLM based on the model type
        if "gemini" in model_name:
            # For Gemini, we need to include the system prompt in the human message
            system_content = "You are a CBMC harness evaluator. Provide detailed analysis of verification issues in JSON format."
            recommendation_response = llm.invoke([
                HumanMessage(content=f"{system_content}\n\n{recommendation_prompt}")
            ])
        else:
            # For Claude and OpenAI models, use separate system and human messages
            recommendation_response = llm.invoke([
                SystemMessage(content="You are a CBMC harness evaluator. Provide detailed analysis of verification issues in JSON format."),
                HumanMessage(content=recommendation_prompt)
            ])
        
        # Parse LLM response
        json_match = re.search(r'```json\n(.*?)\n```', recommendation_response.content, re.DOTALL)
        if json_match:
            recommendations = json.loads(json_match.group(1))
        else:
            # Try to directly parse the content
            recommendations = json.loads(recommendation_response.content)
            
        needs_improvement = recommendations.get("needs_improvement", True)
        explanation = recommendations.get("explanation", "")
        specific_issues = recommendations.get("specific_issues", [])
        specific_fixes = recommendations.get("specific_fixes", [])
        code_changes = recommendations.get("code_changes", {})
        
        logger.info(f"Generated fixes for {func_name} - needs improvement: {needs_improvement}")
        
    except Exception as e:
        logger.warning(f"Failed to parse recommendations response: {e}")
        # Use our rule-based analysis as fallback
        needs_improvement = cbmc_status != "SUCCESS"
        explanation = "CBMC verification failed with specific issues detected in the output."
        specific_issues = specific_issues if specific_issues else ["CBMC verification failed"]
        specific_fixes = specific_fixes if specific_fixes else ["Review CBMC output and fix identified issues"]
        code_changes = {
            "add_includes": list(missing_headers),
            "add_declarations": list(missing_nondets),
            "add_constraints": [],
            "buffer_size_changes": [],
            "free_operations": []
        }
    
    # Construct improvement recommendation if needed
    if needs_improvement:
        # Format issues and fixes
        issues_text = "\n".join([f"- {issue}" for issue in specific_issues])
        fixes_text = "\n".join([f"- {fix}" for fix in specific_fixes])
        
        # Format proposed changes
        proposed_changes_text = ""
        if code_changes:
            proposed_changes_text = "\n\nProposed code changes:\n"
            
            # Add includes
            if "add_includes" in code_changes and code_changes["add_includes"]:
                proposed_changes_text += "\nAdd header files:\n"
                for header in code_changes["add_includes"]:
                    proposed_changes_text += f"- Add: #include {header}\n"
            
            # Add declarations
            if "add_declarations" in code_changes and code_changes["add_declarations"]:
                proposed_changes_text += "\nAdd declarations:\n"
                for decl in code_changes["add_declarations"]:
                    proposed_changes_text += f"- Add: {decl}\n"
            
            # Add constraints
            if "add_constraints" in code_changes and code_changes["add_constraints"]:
                proposed_changes_text += "\nAdd constraints:\n"
                for constraint in code_changes["add_constraints"]:
                    proposed_changes_text += f"- Add: {constraint}\n"
            
            # Add initializations
            if "add_initializations" in code_changes and code_changes["add_initializations"]:
                proposed_changes_text += "\nAdd initializations:\n"
                for init in code_changes["add_initializations"]:
                    proposed_changes_text += f"- Add: {init}\n"
            
            # Replace lines
            if "replace_lines" in code_changes and code_changes["replace_lines"]:
                proposed_changes_text += "\nReplace lines:\n"
                for replacement in code_changes["replace_lines"]:
                    proposed_changes_text += f"- Replace: {replacement.get('old', '')}\n  With: {replacement.get('new', '')}\n"
            
            # Buffer size changes
            if "buffer_size_changes" in code_changes and code_changes["buffer_size_changes"]:
                proposed_changes_text += "\nBuffer size changes:\n"
                for change in code_changes["buffer_size_changes"]:
                    proposed_changes_text += f"- Replace: {change.get('old', '')}\n  With: {change.get('new', '')}\n"
            
            # Free operations
            if "free_operations" in code_changes and code_changes["free_operations"]:
                proposed_changes_text += "\nAdd free operations:\n"
                for free_op in code_changes["free_operations"]:
                    proposed_changes_text += f"- Add: {free_op}\n"
        
        # Add raw failures for context
        raw_failures_text = "\n".join(failure_lines[:15]) if failure_lines else "No specific failure lines found"
        
        # Build the full improvement recommendation
        improvement_recommendation = f"""
        Previous harness for {func_name} needs improvement. Refinement attempt {current_attempts + 1} of {max_refinements}.
        
        CBMC verification status: {cbmc_status}
        
        EXPLANATION: {explanation}
        
        Specific issues detected:
        {issues_text}
        
        Recommended fixes:
        {fixes_text}
        {proposed_changes_text}
        
        Raw CBMC verification failures:
        {raw_failures_text}
        
        Current harness:
        ```c
        {harness_code}
        ```
        
        Original function:
        ```c
        {func_code}
        ```
        
        Please refine the harness to address these SPECIFIC issues. Focus on:
        1. Fixing the exact failures shown in the CBMC output
        2. Adding the recommended includes, declarations, and constraints
        3. Making the specific code changes suggested above
        
        Generate a complete, working harness that passes CBMC verification.
        """
        
        logger.info(f"Generated improvement recommendation for {func_name}")
    else:
        improvement_recommendation = ""
        logger.info(f"No improvements needed for {func_name}")
    
    # Calculate evaluation time
    evaluation_time = time.time() - evaluation_start
    
    # Update function times
    function_times[func_name]["evaluation"] = evaluation_time
    
    # Log proof metrics
    if func_name in proof_metrics:
        metrics = proof_metrics[func_name]
        logger.info(f"Current proof metrics for {func_name}: reachable_lines={metrics.get('total_reachable_lines', 0)}, " 
                   f"coverage={metrics.get('total_coverage', 0):.2f}%, errors={metrics.get('reported_errors', 0)}")
    
    # Update refinement attempts if needed - using refined logic
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
                "proof_metrics": proof_metrics,  # Explicitly pass the proof metrics
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
                "proof_metrics": proof_metrics,  # Explicitly pass the proof metrics
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
            "proof_metrics": proof_metrics,  # Explicitly pass the proof metrics
            "loop_counter": loop_counter,
            "next": "junction"
        }

def route_from_evaluator(state):
    """Routes from evaluator to either generator (for refinement) or junction (for next function)."""
    return state.get("next", "junction")