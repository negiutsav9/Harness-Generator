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
    max_refinements = 6
    
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
    
    # Check for redeclaration errors in stderr
    redeclaration_errors = []
    redeclared_items = set()
    for line in cbmc_stderr.split('\n'):
        if "redeclaration" in line:
            redeclaration_errors.append(line.strip())
            match = re.search(r'redeclaration of \'([^\']+)\'', line)
            if match:
                redeclared_items.add(match.group(1))
    
    # Check for conversion errors
    conversion_errors = []
    for line in cbmc_stderr.split('\n'):
        if "CONVERSION ERROR" in line:
            conversion_errors.append(line.strip())
    
    # Extract current code patterns
    includes = []
    nondet_declarations = []
    nondet_assignments = []
    existing_constraints = []
    buffer_allocations = []
    free_operations = []
    type_definitions = []
    
    for line in harness_code.split('\n'):
        line = line.strip()
        if line.startswith("#include"):
            includes.append(line)
        elif "nondet_" in line and "(" in line and ")" in line and "=" not in line:
            nondet_declarations.append(line)
        elif re.search(r'nondet_\w+\(', line) and '=' in line:
            nondet_assignments.append(line)
        elif "__CPROVER_assume" in line:
            existing_constraints.append(line)
        elif "malloc" in line or "calloc" in line:
            buffer_allocations.append(line)
        elif "free" in line:
            free_operations.append(line)
        elif line.startswith("typedef") or line.startswith("enum") or line.startswith("struct"):
            type_definitions.append(line)
    
    # Check for stub implementations
    stub_markers = ["// Stub implementation", "/* Stub ", "/* Mock ", "// Mock implementation"]
    contains_stubs = any(marker in harness_code for marker in stub_markers)
    
    # Look for function implementations
    func_impl_pattern = r"(\w+)\s+(\w+)\s*\([^)]*\)\s*\{[^}]+\}"
    potential_stubs = re.findall(func_impl_pattern, harness_code)
    # Filter out main function
    potential_stubs = [f for f in potential_stubs if f[1] != "main"]
    
    # Check for non-existent headers
    available_headers = state.get("embeddings", {}).get("available_headers", [])
    standard_headers = ["stdio.h", "stdlib.h", "string.h", "stddef.h", "stdint.h", 
                       "stdbool.h", "math.h", "ctype.h", "time.h", "limits.h",
                       "assert.h", "errno.h", "float.h", "signal.h"]
    
    non_existent_headers = []
    for line in harness_code.split('\n'):
        if line.strip().startswith("#include"):
            include_match = re.search(r'#include\s+[<"]([^>"]+)[>"]', line)
            if include_match:
                header_name = include_match.group(1)
                if (header_name not in available_headers and header_name not in standard_headers):
                    non_existent_headers.append(header_name)
    
    # Determine specific issues based on failures and errors
    specific_issues = []
    
    # First check for redeclaration errors as they're critical
    if redeclaration_errors:
        for item in redeclared_items:
            specific_issues.append(f"Redeclaration of '{item}' - type defined multiple times")
    
    # Add issues for conversion errors
    if conversion_errors:
        specific_issues.append("CONVERSION ERROR detected - check for type compatibility issues")
    
    # Add issues for non-existent headers if any
    if non_existent_headers:
        specific_issues.append(f"Harness includes non-existent header files: {', '.join(non_existent_headers)}")
    
    # Check if harness contains stubs/mocks that should be eliminated
    if contains_stubs or potential_stubs:
        specific_issues.append("Harness contains unnecessary mock/stub implementations")
    
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
    
    # First handle redeclaration errors as they're critical
    if redeclaration_errors:
        for item in redeclared_items:
            specific_fixes.append(f"Remove duplicate definitions of '{item}' - make sure it's only defined once")
        specific_fixes.append("Use header files instead of redefining types in the harness")
        specific_fixes.append("Make sure types are not defined both in included headers and in the harness itself")
    
    # Add fixes for conversion errors
    if conversion_errors:
        specific_fixes.append("Fix type conflicts and ensure proper type compatibility")
    
    # First recommend removing non-existent headers if any exist
    if non_existent_headers:
        specific_fixes.append("Remove non-existent header files or replace them with standard headers")
        for header in non_existent_headers:
            specific_fixes.append(f"Remove include: #include \"{header}\"")
    
    # Next recommend removing stubs if any exist
    if contains_stubs or potential_stubs:
        specific_fixes.append("Remove all mock and stub implementations from the harness")
        specific_fixes.append("Use only actual functions from the codebase")
    
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
        specific_fixes.append("Use only functions that exist in the codebase - do not call functions that aren't implemented")
    
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
    
    # Prepare special messages for critical errors
    critical_error_message = ""
    
    # Special handling for redeclaration errors
    if redeclaration_errors:
        redeclared_list = ", ".join([f"'{item}'" for item in redeclared_items])
        critical_error_message = f"""
        CRITICAL ERROR: The harness has duplicate declarations of {redeclared_list}. 
        This is preventing CBMC from running.
        
        You MUST fix this by:
        1. Remove ALL typedefs, enums, and struct definitions from the harness that are already defined in headers
        2. Include ONLY the necessary header files that contain these definitions
        3. If you need to define custom types, ensure they have unique names that don't conflict
        4. Ensure the original function implementation does not include duplicate type definitions
        
        This is the most critical issue to fix - your harness will not work until this is resolved.
        """
    
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
    
    {critical_error_message if critical_error_message else ""}
    
    CBMC VERIFICATION FAILURES:
    {chr(10).join(failure_lines[:30]) if failure_lines else "No specific failure lines found"}
    
    CBMC STDERR OUTPUT:
    {chr(10).join(cbmc_stderr.split('\n')[:20]) if cbmc_stderr else "No stderr output captured"}
    
    DECLARATION ERRORS:
    {chr(10).join(declaration_errors[:10]) if declaration_errors else "No declaration errors found"}
    
    REDECLARATION ERRORS:
    {chr(10).join(redeclaration_errors[:10]) if redeclaration_errors else "No redeclaration errors found"}
    
    IDENTIFIED ISSUES:
    {chr(10).join(specific_issues)}
    
    CURRENT INCLUDES:
    {chr(10).join(includes) if includes else "No includes found"}
    
    CURRENT TYPE DEFINITIONS:
    {chr(10).join(type_definitions) if type_definitions else "No type definitions found"}
    
    CURRENT NONDET DECLARATIONS:
    {chr(10).join(nondet_declarations) if nondet_declarations else "No nondet declarations found"}
    
    CURRENT CONSTRAINTS:
    {chr(10).join(existing_constraints) if existing_constraints else "No constraints found"}
    
    CURRENT MEMORY ALLOCATIONS:
    {chr(10).join(buffer_allocations) if buffer_allocations else "No memory allocations found"}
    
    CURRENT FREE OPERATIONS:
    {chr(10).join(free_operations) if free_operations else "No free operations found"}
    
    NON-EXISTENT HEADERS:
    {chr(10).join(non_existent_headers) if non_existent_headers else "No non-existent headers found"}
    
    THE MOST CRITICAL ISSUE: 
    {f"Redeclaration errors: {', '.join(redeclared_items)}" if redeclaration_errors else 
    "Check for and remove any mock implementations or stubs. Do not implement functions that should already exist in the codebase."}
    
    Please provide very specific, concrete code changes to fix these issues. Focus on {
    "removing duplicate type definitions and ensuring proper code structure" if redeclaration_errors else 
    "removing stubs/mocks and using actual functions from the codebase"}.
    
    Respond with a JSON object containing:
    {{
        "needs_improvement": true or false,
        "explanation": "Brief explanation of the main issues",
        "specific_issues": ["issue1", "issue2", ...],
        "specific_fixes": ["fix1", "fix2", ...],
        "has_stubs_or_mocks": true or false,
        "has_nonexistent_headers": true or false,
        "has_redeclaration_errors": true or false,
        "redeclared_items": ["item1", "item2", ...],
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
            ],
            "remove_headers": [
                "header_name.h"
            ],
            "remove_types": [
                {{"name": "HTTPSuccess", "reason": "Already defined in included header"}}
            ],
            "remove_stubs": [
                {{"start_line": "// Stub implementation for func1", "end_line": "}} // End of stub"}}
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
            system_content = "You are a CBMC harness evaluator. Focus on fixing critical errors like redeclarations before anything else. Provide detailed analysis of verification issues in JSON format."
            recommendation_response = llm.invoke([
                HumanMessage(content=f"{system_content}\n\n{recommendation_prompt}")
            ])
        else:
            # For Claude and OpenAI models, use separate system and human messages
            recommendation_response = llm.invoke([
                SystemMessage(content="You are a CBMC harness evaluator. Focus on fixing critical errors like redeclarations before anything else. Provide detailed analysis of verification issues in JSON format."),
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
        has_stubs_or_mocks = recommendations.get("has_stubs_or_mocks", False)
        has_nonexistent_headers = recommendations.get("has_nonexistent_headers", False)
        has_redeclaration_errors = recommendations.get("has_redeclaration_errors", False)
        redeclared_items = recommendations.get("redeclared_items", [])
        code_changes = recommendations.get("code_changes", {})
        
        # Prioritize stub/mock removal if detected
        if has_stubs_or_mocks:
            if "Harness contains unnecessary mock/stub implementations" not in specific_issues:
                specific_issues.insert(0, "Harness contains unnecessary mock/stub implementations")
            if "Remove all mock and stub implementations" not in specific_fixes:
                specific_fixes.insert(0, "Remove all mock and stub implementations from the harness")
                
        # Prioritize non-existent header removal if detected
        if has_nonexistent_headers:
            if not any("non-existent header" in issue for issue in specific_issues):
                specific_issues.insert(0, "Harness includes non-existent header files")
            if not any("non-existent header" in fix for fix in specific_fixes):
                specific_fixes.insert(0, "Remove non-existent header files and use only standard headers or headers from the codebase")
        
        # Prioritize redeclaration errors above all else
        if has_redeclaration_errors or redeclaration_errors:
            if not any("redeclaration" in issue.lower() for issue in specific_issues):
                specific_issues.insert(0, f"Redeclaration errors: Types defined multiple times")
            if not any("duplicate" in fix.lower() for fix in specific_fixes):
                specific_fixes.insert(0, "Remove duplicate type definitions and ensure each type is only defined once")
        
        logger.info(f"Generated fixes for {func_name} - needs improvement: {needs_improvement}")
        
    except Exception as e:
        logger.warning(f"Failed to parse recommendations response: {e}")
        # Use our rule-based analysis as fallback
        needs_improvement = cbmc_status != "SUCCESS"
        explanation = "CBMC verification failed with specific issues detected in the output."
        specific_issues = specific_issues if specific_issues else ["CBMC verification failed"]
        specific_fixes = specific_fixes if specific_fixes else ["Review CBMC output and fix identified issues"]
        has_stubs_or_mocks = contains_stubs or bool(potential_stubs)
        has_nonexistent_headers = bool(non_existent_headers)
        has_redeclaration_errors = bool(redeclaration_errors)
        code_changes = {
            "add_includes": list(missing_headers),
            "add_declarations": list(missing_nondets),
            "add_constraints": [],
            "buffer_size_changes": [],
            "free_operations": [],
            "remove_headers": non_existent_headers,
            "remove_types": [{"name": item, "reason": "Already defined in included header"} for item in redeclared_items]
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
            
            # Prioritize removing duplicate types if needed
            if "remove_types" in code_changes and code_changes["remove_types"]:
                proposed_changes_text += "\nRemove duplicate type definitions:\n"
                for type_info in code_changes["remove_types"]:
                    proposed_changes_text += f"- Remove: {type_info.get('name', '')} ({type_info.get('reason', '')})\n"
            
            # Add headers to remove
            if "remove_headers" in code_changes and code_changes["remove_headers"]:
                proposed_changes_text += "\nRemove non-existent headers:\n"
                for header in code_changes["remove_headers"]:
                    proposed_changes_text += f"- Remove: #include \"{header}\"\n"
            
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
            
            # Remove stubs
            if "remove_stubs" in code_changes and code_changes["remove_stubs"]:
                proposed_changes_text += "\nRemove stub implementations:\n"
                for stub in code_changes["remove_stubs"]:
                    proposed_changes_text += f"- Remove from: {stub.get('start_line', '')}\n  To: {stub.get('end_line', '')}\n"
        
        # Add raw failures for context
        raw_failures_text = "\n".join(failure_lines[:15]) if failure_lines else "No specific failure lines found"

        # Add raw failures for context
        if failure_lines:
            raw_failures_text = "\n".join(failure_lines[:20])  # Show more failure lines
            failure_summary = "\n\nFAILURE SUMMARY:\n"
            
            # Group failures by category
            for category, details in failure_details.items():
                failure_summary += f"\n{category} failures ({len(details)}):\n"
                for detail in details[:3]:  # Show first 3 of each category
                    failure_summary += f"- {detail}\n"
        else:
            raw_failures_text = "No specific failure lines found"
            failure_summary = ""
        
        # Add stderr if available (especially important for redeclaration errors)
        stderr_text = ""
        if cbmc_stderr:
            stderr_text = "\nCBMC STDERR OUTPUT:\n" + "\n".join(cbmc_stderr.split('\n')[:20])
        
        # Build the full improvement recommendation
        improvement_recommendation = f"""
        Previous harness for {func_name} needs improvement. Refinement attempt {current_attempts + 1} of {max_refinements}.
        
        CBMC verification status: {cbmc_status}
        
        EXPLANATION: {explanation}
        
        {critical_error_message if critical_error_message else ""}
        
        Specific issues detected:
        {issues_text}
        
        Recommended fixes:
        {fixes_text}
        {proposed_changes_text}

        {failure_summary}
        
        Raw CBMC verification failures:
        {raw_failures_text}
        
        {stderr_text}
        
        Current harness:
        ```c
        {harness_code}
        ```
        
        Original function:
        ```c
        {func_code}
        ```
        
        CRITICAL INSTRUCTIONS:
        1. DO NOT CREATE ANY MOCK OR STUB IMPLEMENTATIONS
        2. Use only functions that actually exist in the codebase
        3. Only include header files that actually exist in the codebase or standard libraries
        4. Focus on creating a minimal test harness with appropriate inputs
        5. Fix the exact failures shown in the CBMC output
        6. Add the recommended includes, declarations, and constraints
        7. If you need to call a function, assume it exists and just declare its prototype
        8. REMOVE any existing stubs or mocks from the previous harness
        9. Make the harness as minimal and focused as possible
        10. FOLLOW PROPER C CODE STRUCTURE:
           - Include directives first
           - Type definitions (typedef, enum, struct) next ONLY IF not already defined in headers
           - Function declarations next
           - Function implementations next
           - Main function last
        11. DO NOT duplicate type definitions from header files - if a type is already defined in a header, just include the header
        
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