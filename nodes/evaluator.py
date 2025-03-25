"""
Harness evaluator node for CBMC harness generator workflow.
"""
import time
import re
import json
import logging
from langchain_core.messages import AIMessage, SystemMessage
from core.embedding_db import code_collection, query_pattern_db

# Set up logging - simplified
logger = logging.getLogger("evaluator")

def harness_evaluator_node(state):
    """Evaluates harnesses using LLM-powered analysis of CBMC output."""
    evaluation_start = time.time()
    
    loop_counter = state.get("loop_counter", 0)
    func_name = state.get("current_function", "")
    
    logger.info(f"Evaluating harness for {func_name} (attempt {loop_counter+1})")
    
    harnesses = state.get("harnesses", {})
    cbmc_results = state.get("cbmc_results", {})
    
    # Get error tracking dictionaries
    cbmc_error_messages = state.get("cbmc_error_messages", {})
    harness_syntax_errors = state.get("harness_syntax_errors", {})
    parsing_issues = state.get("parsing_issues", {})
    verification_failures = state.get("verification_failures", {})
    
    # Safety: Initialize refinement_attempts if not present
    refinement_attempts = state.get("refinement_attempts", {}).copy()
    if func_name not in refinement_attempts:
        refinement_attempts[func_name] = 0
    
    current_attempts = refinement_attempts.get(func_name, 0)
    max_refinements = 3
    
    # Force progression after max attempts
    if current_attempts >= max_refinements:
        processed_functions = state.get("processed_functions", []).copy()
        if func_name not in processed_functions:
            processed_functions.append(func_name)
            logger.info(f"Max refinements reached for {func_name}, proceeding to next function")
        
        return {
            "messages": [AIMessage(content=f"Maximum refinement attempts ({max_refinements}) reached for {func_name}. Moving to next function.")],
            "refinement_attempts": refinement_attempts,
            "processed_functions": processed_functions,
            "loop_counter": loop_counter,
            "next": "junction"
        }
    
    # Safety: Handle missing data
    harness_code = harnesses.get(func_name, "")
    cbmc_result = cbmc_results.get(func_name, {})
    
    if not harness_code or not cbmc_result:
        processed_functions = state.get("processed_functions", []).copy()
        if func_name and func_name not in processed_functions:
            processed_functions.append(func_name)
            logger.info(f"Missing data for {func_name}, proceeding to next function")
        
        return {
            "messages": [AIMessage(content=f"Error: Missing harness or CBMC result for function {func_name}. Marking as processed.")],
            "processed_functions": processed_functions,
            "loop_counter": loop_counter,
            "next": "junction"
        }
    
    # Get function details
    function_result = code_collection.get(ids=[func_name], include=["documents", "metadatas"])
    if not function_result["ids"]:
        processed_functions = state.get("processed_functions", []).copy()
        if func_name not in processed_functions:
            processed_functions.append(func_name)
            logger.info(f"Function {func_name} not found in database")
        
        return {
            "messages": [AIMessage(content=f"Error: Function {func_name} metadata not found. Marking as processed.")],
            "processed_functions": processed_functions,
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
    
    # Extract specific error types
    syntax_errors = re.findall(r"syntax error at line (\d+)", cbmc_stderr)
    include_errors = re.findall(r"function '([^']+)' is not declared", cbmc_stderr)
    nondet_errors = re.findall(r"function '(nondet_[^']+)' is not declared", cbmc_stderr)
    no_body_errors = re.findall(r"main symbol '([^']+)' has no body", cbmc_stderr)
    
    # Check for verification failures
    memory_issues = []
    if "memory leak detected" in cbmc_stdout.lower():
        memory_issues.append("Memory leak detected")
    if "dereference failure" in cbmc_stdout.lower() or "NULL pointer" in cbmc_stdout.lower():
        memory_issues.append("Null pointer dereference")
    if "array bounds" in cbmc_stdout.lower():
        memory_issues.append("Array bounds violation")
    if "division by zero" in cbmc_stdout.lower():
        memory_issues.append("Division by zero")
    
    logger.info(f"CBMC verification status: {cbmc_status}, Issues detected: {len(memory_issues)+len(syntax_errors)+len(include_errors)+len(nondet_errors)+len(no_body_errors)}")
    
    # Create prompt for LLM analysis
    prompt = f"""
    You are an expert in analyzing CBMC verification results and improving harnesses for memory safety verification.

    Analyze the following and determine what improvements are needed:

    FUNCTION:
    ```c
    {func_code}
    ```

    FUNCTION METADATA:
    - Return type: {func_metadata.get("return_type", "void")}
    - Parameters: {func_metadata.get("params", "")}
    - Contains malloc: {func_metadata.get("has_malloc", False)}
    - Contains free: {func_metadata.get("has_free", False)}

    MATCHING VULNERABILITY PATTERNS:
    {json.dumps(matching_patterns, indent=2)}

    CURRENT HARNESS (attempt {current_attempts + 1} of {max_refinements}):
    ```c
    {harness_code}
    ```

    CBMC VERIFICATION RESULTS:
    Status: {cbmc_status}
    Message: {verification_message}
    Suggestions: {suggestions}

    STDOUT EXCERPT:
    ```
    {cbmc_stdout[:1500] if len(cbmc_stdout) > 1500 else cbmc_stdout}
    ```

    STDERR EXCERPT:
    ```
    {cbmc_stderr[:1500] if len(cbmc_stderr) > 1500 else cbmc_stderr}
    ```

    SPECIFIC ISSUES DETECTED:
    - Syntax errors: {syntax_errors}
    - Include errors: {include_errors}
    - Nondet function errors: {nondet_errors}
    - No body errors: {no_body_errors}
    - Memory issues: {memory_issues}

    I need you to:
    1. Deeply analyze the CBMC output to understand verification failures
    2. Determine root causes of any issues
    3. Provide specific, actionable suggestions to improve the harness
    4. Consider the known vulnerability patterns in your analysis
    5. Recommend precise code changes to fix the issues

    Focus on addressing:
    - Syntax and declaration issues
    - Memory allocation and deallocation
    - Proper CBMC-specific functions (__CPROVER_assert, __CPROVER_assume)
    - Nondet function declarations and use
    - Complete coverage of execution paths

    Respond with a JSON object containing:
    {{
      "needs_improvement": true or false,
      "issues": ["issue1", "issue2", ...],
      "root_causes": ["cause1", "cause2", ...],
      "improvement_suggestions": ["suggestion1", "suggestion2", ...],
      "proposed_changes": {{
        "change1": "description1",
        "change2": "description2"
      }}
    }}
    """
    
    # Get LLM analysis
    from utils.llm_utils import setup_llm
    llm = setup_llm()
    logger.info(f"Requesting LLM analysis of CBMC results for {func_name}")
    response = llm.invoke([
        SystemMessage(content=prompt)
    ])
    
    # Parse LLM response
    try:
        # Find JSON content
        json_match = re.search(r'```json\n(.*?)\n```', response.content, re.DOTALL)
        if json_match:
            analysis = json.loads(json_match.group(1))
        else:
            # Try to directly parse the content
            analysis = json.loads(response.content)
        
        needs_improvement = analysis.get("needs_improvement", False)
        issues = analysis.get("issues", [])
        root_causes = analysis.get("root_causes", [])
        improvement_suggestions = analysis.get("improvement_suggestions", [])
        proposed_changes = analysis.get("proposed_changes", {})
        
        logger.info(f"LLM analysis complete - needs improvement: {needs_improvement}, issues found: {len(issues)}")
        
    except (json.JSONDecodeError, AttributeError) as e:
        logger.warning(f"Failed to parse LLM response as JSON: {e}")
        # Fallback analysis based on CBMC output patterns
        needs_improvement = cbmc_status != "SUCCESS"
        
        # Extract basic issues
        issues = []
        root_causes = []
        improvement_suggestions = []
        
        # Handle syntax and declaration errors
        if syntax_errors:
            issues.append(f"Syntax error at line(s) {', '.join(syntax_errors)}")
            root_causes.append("Syntax error in harness")
            improvement_suggestions.append("Fix syntax errors in the harness")
        
        if include_errors:
            issues.append(f"Missing declarations for: {', '.join(include_errors)}")
            root_causes.append("Missing include files or function declarations")
            
            missing_includes = {}
            for func in include_errors:
                if func == 'malloc' or func == 'free':
                    missing_includes['stdlib.h'] = True
                elif func == 'memcpy' or func == 'memmove' or func == 'strncpy':
                    missing_includes['string.h'] = True
            
            for header in missing_includes:
                improvement_suggestions.append(f"Add #include <{header}>")
        
        if nondet_errors:
            issues.append(f"Missing nondet function declarations: {', '.join(nondet_errors)}")
            root_causes.append("Missing CBMC nondet function declarations")
            improvement_suggestions.append("Add proper declarations for nondet functions")
        
        if memory_issues:
            issues.append('; '.join(memory_issues))
            
            if "Memory leak detected" in memory_issues:
                root_causes.append("Memory leak in function or harness")
                improvement_suggestions.append("Ensure all allocated memory is freed in all execution paths")
            
            if "Null pointer dereference" in memory_issues:
                root_causes.append("Missing null pointer check")
                improvement_suggestions.append("Add null pointer checks before dereferencing")
        
        # Use vulnerability patterns for context
        for pattern_name, pattern_info in matching_patterns.items():
            if pattern_name == "malloc_without_free":
                if "Memory leak" not in ' '.join(issues):
                    issues.append("Potential memory leak (malloc without free)")
                    root_causes.append("Allocation without corresponding deallocation")
                    improvement_suggestions.append(pattern_info.get("verification_strategy", "Check all execution paths for memory deallocation"))
            
            elif pattern_name == "conditional_free":
                if "Conditional path" not in ' '.join(issues):
                    issues.append("Conditional free path that might not execute")
                    root_causes.append("Conditional memory deallocation")
                    improvement_suggestions.append(pattern_info.get("verification_strategy", "Verify all conditions that lead to memory release"))
        
        proposed_changes = {}
        
        logger.info(f"Fallback analysis - issues identified: {len(issues)}")
    
    # Construct improvement recommendation if needed
    if needs_improvement:
        issues_text = "\n".join([f"- {issue}" for issue in issues])
        root_causes_text = "\n".join([f"- {cause}" for cause in root_causes])
        suggestions_text = "\n".join([f"- {suggestion}" for suggestion in improvement_suggestions])
        
        # Include proposed changes if available
        proposed_changes_text = ""
        if proposed_changes:
            proposed_changes_text = "\n\nProposed code changes:\n"
            for change_key, change_value in proposed_changes.items():
                proposed_changes_text += f"- {change_key}: {change_value}\n"
        
        improvement_recommendation = f"""
        Previous harness for {func_name} needs improvement. Refinement attempt {current_attempts + 1} of {max_refinements}.
        
        CBMC verification status: {cbmc_status}
        
        Issues detected:
        {issues_text}
        
        Root causes:
        {root_causes_text}
        
        Suggestions:
        {suggestions_text}
        {proposed_changes_text}
        
        Current harness:
        ```c
        {harness_code}
        ```
        
        Original function:
        ```c
        {func_code}
        ```
        
        Known vulnerability patterns for this function:
        {json.dumps(matching_patterns, indent=2)}
        
        Please refine the harness to address these issues. Focus on:
        1. Fixing the specific issues identified above
        2. Ensuring all execution paths are properly tested
        3. Adding appropriate CBMC assertions and assumptions
        4. Following proper CBMC verification practices
        
        Generate a complete, working harness that passes CBMC verification.
        """
        
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
        refinement_attempts[func_name] = current_attempts + 1
        logger.info(f"Incrementing refinement attempts for {func_name} to {refinement_attempts[func_name]}")
    
    # Mark as processed if not refining
    processed_functions = state.get("processed_functions", []).copy()
    if not needs_improvement:
        if func_name not in processed_functions:
            processed_functions.append(func_name)
            logger.info(f"Marking {func_name} as processed - no improvements needed")
    
    return {
        "messages": [AIMessage(content=f"Evaluated harness for {func_name} in {evaluation_time:.2f}s. {cbmc_status}. {'Improvements needed.' if needs_improvement else 'No improvements needed.'}")],
        "refinement_attempts": refinement_attempts,
        "processed_functions": processed_functions,
        "improvement_recommendation": improvement_recommendation,
        "function_times": function_times,
        "loop_counter": loop_counter,
        "next": "generator" if needs_improvement else "junction"
    }

def route_from_evaluator(state):
    """Routes from evaluator to either generator (for refinement) or junction (for next function)."""
    return state.get("next", "junction")