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
    
    # Enhanced CBMC output parsing - More detailed and structured approach
    
    # 1. Extract all failure lines and categorize by type
    failure_lines = []
    failure_details = {}
    failure_locations = {}  # Track file:line info for each failure
    
    # Parse each line of stdout for detailed failure information
    for line in cbmc_stdout.split('\n'):
        if "FAILURE" in line or "FAILED" in line:
            # Skip unwinding assertions as they're often not relevant to core bugs
            if "unwinding assertion" in line:
                continue
                
            failure_lines.append(line.strip())
            
            # Parse and categorize failure type
            failure_category = "general"  # Default category
            
            if "[memory]" in line or "memory-leak" in line or "dynamic memory" in line:
                failure_category = "memory"
            elif "[pointer]" in line or "dereference failure" in line or "NULL pointer" in line:
                failure_category = "pointer"
            elif "[array]" in line or "array bounds" in line:
                failure_category = "array_bounds"
            elif "[arithmetic]" in line or "division by zero" in line or "overflow" in line:
                failure_category = "arithmetic"
            elif "[assertion]" in line or "__CPROVER_assert" in line:
                failure_category = "assertion"
            
            # Extract location information if available
            loc_match = re.search(r'file ([^:]+):(\d+)', line)
            if loc_match:
                file_name = loc_match.group(1)
                line_num = int(loc_match.group(2))
                location = f"{file_name}:{line_num}"
                
                # Add to location tracking
                if location not in failure_locations:
                    failure_locations[location] = []
                failure_locations[location].append(line.strip())
                
                # Add more detailed location to failure category
                failure_category = f"{failure_category}_{file_name}_{line_num}"
            
            # Add to categorized failure details
            if failure_category not in failure_details:
                failure_details[failure_category] = []
            failure_details[failure_category].append(line.strip())
    
    # 2. Enhanced error detection from stderr
    parsing_errors = []
    compilation_errors = []
    declaration_errors = []
    redeclaration_errors = []
    type_errors = []
    missing_files = []
    
    # More detailed error parsing from stderr
    for line in cbmc_stderr.split('\n'):
        line = line.strip()
        if not line:
            continue
            
        # Track parsing errors
        if "PARSING ERROR" in line or "syntax error" in line:
            parsing_errors.append(line)
            
        # Track compilation errors (often indicate code structure issues)
        elif "error:" in line or "CONVERSION ERROR" in line:
            compilation_errors.append(line)
            
        # Missing declarations
        if "function" in line and ("not declared" in line or "implicit" in line):
            declaration_errors.append(line)
            
        # Track redeclaration errors
        if "redeclaration" in line:
            redeclaration_errors.append(line)
            
            # Extract what's being redeclared
            match = re.search(r'redeclaration of \'([^\']+)\'', line)
            if match:
                redeclared_item = match.group(1)
                if redeclared_item not in redeclaration_errors:
                    redeclaration_errors.append(redeclared_item)
                    
        # Track type errors
        if "incompatible types" in line or "type mismatch" in line:
            type_errors.append(line)
            
        # Track missing files/headers
        if "No such file or directory" in line or "file not found" in line:
            missing_file_match = re.search(r"'([^']+)' file not found", line)
            if missing_file_match:
                missing_file = missing_file_match.group(1)
                missing_files.append(missing_file)

    # Enhanced detection and handling of "no body for callee" errors
    no_body_errors = []
    missing_functions = set()

    # Extract all missing function bodies
    for line in cbmc_stdout.split('\n'):
        if "no body for callee" in line:
            no_body_errors.append(line.strip())
            # Extract function name
            match = re.search(r'no body for callee (\w+)', line)
            if match:
                missing_functions.add(match.group(1))
    
    # Improved failure analysis - extract trace information if present
    trace_steps = []
    in_trace = False
    
    for line in cbmc_stdout.split('\n'):
        if "Trace for " in line:
            in_trace = True
            trace_steps.append(line.strip())
        elif in_trace and line.strip().startswith("State"):
            trace_steps.append(line.strip())
        elif in_trace and not line.strip():
            in_trace = False
    
    # 3. Extract current harness structural information for better analysis
    harness_structure = {
        "includes": [],
        "type_definitions": [],
        "nondet_declarations": [],
        "nondet_assignments": [],
        "constraints": [],
        "buffer_allocations": [],
        "free_operations": [],
        "memory_operations": [],
        "assertions": [],
        "function_calls": [],
        "has_stubs": False
    }
    
    # Parse harness code to identify key components with improved patterns
    current_section = None  # Track which section we're in
    for line in harness_code.split('\n'):
        line = line.strip()
        if not line or line.startswith("//"):
            continue
            
        # Track includes
        if line.startswith("#include"):
            harness_structure["includes"].append(line)
            
        # Track type definitions
        elif line.startswith("typedef") or line.startswith("struct") or line.startswith("enum") or line.startswith("union"):
            harness_structure["type_definitions"].append(line)
            current_section = "type_definition"
            
        # Track nondet declarations
        elif "nondet_" in line and "(" in line and ")" in line and "=" not in line:
            harness_structure["nondet_declarations"].append(line)
            
        # Track nondet assignments
        elif re.search(r'nondet_\w+\(', line) and '=' in line:
            harness_structure["nondet_assignments"].append(line)
            
        # Track constraints
        elif "__CPROVER_assume" in line:
            harness_structure["constraints"].append(line)
            
        # Track memory operations with more comprehensive patterns
        elif "malloc" in line or "calloc" in line or "realloc" in line:
            harness_structure["buffer_allocations"].append(line)
            harness_structure["memory_operations"].append(line)
            
        # Track free operations
        elif "free" in line and "(" in line:
            harness_structure["free_operations"].append(line)
            harness_structure["memory_operations"].append(line)
            
        # Track assertions
        elif "__CPROVER_assert" in line or "assert" in line:
            harness_structure["assertions"].append(line)
            
        # Track function calls - improved to catch more cases
        elif re.search(r'(\w+)\s*\([^;]*\)', line) and "=" not in line and not line.startswith("#"):
            # Extract function name
            func_match = re.search(r'(\w+)\s*\(', line)
            if func_match and func_match.group(1) not in ["if", "for", "while", "switch"]:
                harness_structure["function_calls"].append(line)
                
        # Check for stub implementations
        if ("// Stub implementation" in line or "/* Stub " in line or "/* Mock " in line 
                or "// Mock implementation" in line):
            harness_structure["has_stubs"] = True
    
    # 4. Perform detailed gap analysis between errors and harness structure
    gap_analysis = {
        "missing_includes": [],
        "missing_declarations": [],
        "missing_constraints": [],
        "missing_memory_operations": [],
        "missing_assertions": [],
        "invalid_stubs": harness_structure["has_stubs"],
        "memory_leaks": False,
        "pointer_issues": False,
        "array_bounds_issues": False,
        "arithmetic_issues": False,
        "type_mismatches": False,
        "missing_function_bodies": bool(missing_functions)
    }
    
    # Check for memory leaks
    if any("memory leak" in line.lower() or "memory-leak" in line.lower() for line in failure_lines):
        gap_analysis["memory_leaks"] = True
        
        # Find allocations without matching free
        allocated_vars = []
        for line in harness_structure["buffer_allocations"]:
            match = re.search(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(malloc|calloc)', line)
            if match:
                var = match.group(1)
                allocated_vars.append(var)
        
        freed_vars = []
        for line in harness_structure["free_operations"]:
            match = re.search(r'free\s*\(\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*\)', line)
            if match:
                var = match.group(1)
                freed_vars.append(var)
        
        # Find variables that are allocated but not freed
        for var in allocated_vars:
            if var not in freed_vars:
                gap_analysis["missing_memory_operations"].append(f"Missing free for: {var}")
    
    # Check for pointer issues
    if any("pointer" in line.lower() or "dereference" in line.lower() or "null" in line.lower() for line in failure_lines):
        gap_analysis["pointer_issues"] = True
        
        # Check for missing NULL pointer constraints
        for line in harness_structure["nondet_assignments"]:
            if "=" in line and "*" in line and not any(f"__CPROVER_assume({var} != NULL)" in harness_code for var in re.findall(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*=', line)):
                var_match = re.search(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*=', line)
                if var_match:
                    var = var_match.group(1)
                    gap_analysis["missing_constraints"].append(f"Missing NULL check for: {var}")
    
    # Check for array bounds issues
    if any("array bounds" in line.lower() or "buffer" in line.lower() for line in failure_lines):
        gap_analysis["array_bounds_issues"] = True
        
        # Check for missing size constraints on arrays or buffers
        for line in harness_structure["buffer_allocations"]:
            if "malloc" in line and "1)" in line:  # Suspicious single-byte allocation
                gap_analysis["missing_constraints"].append("Using malloc(1) is suspicious - consider appropriate buffer size")
    
    # Check for arithmetic issues
    if any("arithmetic" in line.lower() or "overflow" in line.lower() or "division" in line.lower() for line in failure_lines):
        gap_analysis["arithmetic_issues"] = True
        
        # Check for missing constraints on integer inputs
        for line in harness_structure["nondet_assignments"]:
            if "nondet_int" in line or "nondet_uint" in line:
                var_match = re.search(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*=', line)
                if var_match:
                    var = var_match.group(1)
                    if not any(f"__CPROVER_assume({var}" in constraint for constraint in harness_structure["constraints"]):
                        gap_analysis["missing_constraints"].append(f"Missing bounds constraint for: {var}")

    # Check for missing function body issues
    if missing_functions:
        gap_analysis["missing_function_bodies"] = True
        for func_name in missing_functions:
            gap_analysis["missing_declarations"].append(f"Missing implementation for function: {func_name}")
    
    # Check for declaration issues from stderr
    if declaration_errors:
        for error in declaration_errors:
            match = re.search(r"function '([^']+)' is not declared", error)
            if match:
                func = match.group(1)
                
                # Check for standard library functions that need specific includes
                if func in ["malloc", "free", "calloc", "realloc"]:
                    if not any("stdlib.h" in include for include in harness_structure["includes"]):
                        gap_analysis["missing_includes"].append("<stdlib.h>")
                elif func in ["memcpy", "memset", "strcpy", "strcmp"]:
                    if not any("string.h" in include for include in harness_structure["includes"]):
                        gap_analysis["missing_includes"].append("<string.h>")
                elif func in ["printf", "fprintf", "sprintf"]:
                    if not any("stdio.h" in include for include in harness_structure["includes"]):
                        gap_analysis["missing_includes"].append("<stdio.h>")
                elif func.startswith("nondet_"):
                    gap_analysis["missing_declarations"].append(f"Missing declaration for: {func}")
                else:
                    gap_analysis["missing_declarations"].append(f"Missing declaration for: {func}")
    
    # Missing header files
    if missing_files:
        for file in missing_files:
            gap_analysis["missing_includes"].append(file)
    
    # Compile specific issues into a detailed analysis
    analysis_details = {
        "has_compilation_errors": bool(compilation_errors),
        "has_parsing_errors": bool(parsing_errors),
        "has_redeclaration_errors": bool(redeclaration_errors),
        "has_declaration_errors": bool(declaration_errors),
        "has_type_errors": bool(type_errors),
        "has_failure_trace": bool(trace_steps),
        "has_missing_includes": bool(gap_analysis["missing_includes"]),
        "has_memory_leaks": gap_analysis["memory_leaks"],
        "has_pointer_issues": gap_analysis["pointer_issues"],
        "has_array_bounds_issues": gap_analysis["array_bounds_issues"],
        "has_arithmetic_issues": gap_analysis["arithmetic_issues"],
        "has_stubs": harness_structure["has_stubs"],
        "has_missing_function_bodies": bool(missing_functions),
        "raw_failure_count": len(failure_lines),
        "categories": list(failure_details.keys())
    }
    
    # Generate specific improvement recommendations based on the analysis
    specific_issues = []
    specific_fixes = []
    
    # Add common patterns for known issues
    common_patterns = []
    
    # Deal with critical errors first - redeclaration errors
    if analysis_details["has_redeclaration_errors"]:
        specific_issues.append("Critical: Redeclaration errors detected - duplicate type definitions")
        specific_fixes.append("Remove duplicate type definitions - ensure each type is defined only once")
        specific_fixes.append("Use header files instead of redefining types in the harness")
        
    # Deal with parsing errors
    if analysis_details["has_parsing_errors"]:
        specific_issues.append("Critical: Syntax or parsing errors in the harness code")
        for error in parsing_errors[:3]:  # First 3 for brevity
            specific_issues.append(f"Parse error: {error}")
        specific_fixes.append("Fix syntax errors in the harness code")
        
    # Deal with compilation errors
    if analysis_details["has_compilation_errors"]:
        specific_issues.append("Compilation errors in the harness code")
        for error in compilation_errors[:3]:  # First 3 for brevity
            specific_issues.append(f"Compile error: {error}")
        specific_fixes.append("Fix compilation errors in the harness code")
        
    # Deal with missing includes
    if analysis_details["has_missing_includes"]:
        specific_issues.append("Missing necessary header files")
        for include in gap_analysis["missing_includes"]:
            specific_fixes.append(f"Add missing include: {include}")
            
    # Deal with missing declarations
    if analysis_details["has_declaration_errors"]:
        specific_issues.append("Missing function declarations")
        for decl in gap_analysis["missing_declarations"]:
            specific_fixes.append(decl)
            
    # Deal with stubs (always remove if present)
    if analysis_details["has_stubs"]:
        specific_issues.append("Harness contains unnecessary mock/stub implementations")
        specific_fixes.append("Remove all mock and stub implementations from the harness")
        specific_fixes.append("Use only actual functions from the codebase")
        
    # Deal with memory leaks
    if analysis_details["has_memory_leaks"]:
        specific_issues.append("Memory leak detected: Allocated memory not properly freed")
        for fix in gap_analysis["missing_memory_operations"]:
            specific_fixes.append(fix)
        
        # Add example pattern for memory management
        common_patterns.append("""
        // Memory management pattern
        void* buffer = malloc(size);
        // ... use buffer ...
        free(buffer);  // Always free allocated memory
        """)
            
    # Deal with pointer issues
    if analysis_details["has_pointer_issues"]:
        specific_issues.append("Pointer dereference failure: Possible NULL pointer dereference")
        for fix in gap_analysis["missing_constraints"]:
            if "NULL check" in fix:
                specific_fixes.append(fix)
        specific_fixes.append("Add NULL pointer checks before dereferencing")
        
        # Add example pattern for NULL pointer checks
        common_patterns.append("""
        // Null pointer check pattern
        void* ptr = malloc(size);
        __CPROVER_assume(ptr != NULL);  // Ensure pointer is valid before use
        // ... use ptr ...
        """)
            
    # Deal with array bounds issues
    if analysis_details["has_array_bounds_issues"]:
        specific_issues.append("Array bounds violation: Buffer overflow risk")
        specific_fixes.append("Add constraints to ensure array indices are within bounds")
        specific_fixes.append("Use realistic buffer sizes instead of fixed small sizes")
        
        # Add example pattern for array bounds checking
        common_patterns.append("""
        // Array bounds pattern
        size_t index = nondet_size_t();
        size_t size = 10;
        __CPROVER_assume(index < size);  // Ensure index is within bounds
        array[index] = value;  // Safe array access
        """)
            
    # Deal with arithmetic issues
    if analysis_details["has_arithmetic_issues"]:
        specific_issues.append("Arithmetic error: Possible overflow or division by zero")
        for fix in gap_analysis["missing_constraints"]:
            if "bounds constraint" in fix:
                specific_fixes.append(fix)
        specific_fixes.append("Add constraints to limit integer values and prevent overflow")
        specific_fixes.append("Add checks to ensure divisors are non-zero")
        
        # Add example pattern for arithmetic safety
        common_patterns.append("""
        // Arithmetic safety pattern
        int value = nondet_int();
        __CPROVER_assume(value > 0 && value < INT_MAX/2);  // Prevent overflow
        // ... use value ...
        
        int divisor = nondet_int();
        __CPROVER_assume(divisor != 0);  // Prevent division by zero
        result = value / divisor;  // Safe division
        """)
    
    # Deal with missing function bodies - NEW SECTION
    if missing_functions:
        # This is a critical issue that needs special handling
        specific_issues.append(f"Critical: Missing function bodies for {len(missing_functions)} functions")
        for func in missing_functions:
            specific_issues.append(f"Missing implementation for: {func}")
        
        # Add specific recommendations
        specific_fixes.append("You must address all missing function bodies using one of these approaches:")
        specific_fixes.append("1. Find and include the complete function implementation from the codebase")
        specific_fixes.append("2. Create a minimal valid stub implementation that satisfies CBMC verification")
        specific_fixes.append("3. Modify the test strategy to avoid calling these functions directly")
        
        # Add example pattern for handling missing functions
        example_stub = f"""
        // Option 1: Minimal stub for missing function (adapt for each function)
        {list(missing_functions)[0] if missing_functions else 'missing_function'}(...) {{
            // Return a valid status without complex side effects
            return HTTPSuccess; // Or appropriate return value
        }}
        
        // Option 2: Avoid calling function and use constraints
        // Instead of: status = {list(missing_functions)[0] if missing_functions else 'missing_function'}(...);
        // Do: 
        HTTPStatus_t status = nondet_HTTPStatus_t();
        __CPROVER_assume(status == HTTPSuccess || status == HTTPInvalidParameter);
        """
        
        common_patterns.append(example_stub)
    
    # Ensure we have at least some generic recommendations if nothing specific was found
    if not specific_issues:
        if failure_lines:
            specific_issues.append("Verification failures detected but could not be specifically categorized")
            specific_fixes.append("Review CBMC output carefully for specific verification failures")
        else:
            specific_issues.append("CBMC failed but did not produce specific error messages")
            specific_fixes.append("Ensure the harness correctly tests the function with appropriate inputs")
    
    # Determine if the harness needs improvement
    needs_improvement = (
        analysis_details["has_redeclaration_errors"] or
        analysis_details["has_parsing_errors"] or
        analysis_details["has_compilation_errors"] or
        analysis_details["has_missing_includes"] or
        analysis_details["has_declaration_errors"] or
        analysis_details["has_stubs"] or
        analysis_details["has_memory_leaks"] or
        analysis_details["has_pointer_issues"] or
        analysis_details["has_array_bounds_issues"] or
        analysis_details["has_arithmetic_issues"] or
        analysis_details["has_missing_function_bodies"] or
        bool(failure_lines)
    )
    
    # Create detailed improvement recommendation
    if needs_improvement:
        # Format issues and fixes
        issues_text = "\n".join([f"- {issue}" for issue in specific_issues])
        fixes_text = "\n".join([f"- {fix}" for fix in specific_fixes])
        
        # Add patterns text if we have any
        patterns_text = ""
        if common_patterns:
            patterns_text = "\n\nRecommended patterns for CBMC verification:\n\n"
            for i, pattern in enumerate(common_patterns):
                patterns_text += f"Pattern {i+1}:\n```c\n{pattern.strip()}\n```\n\n"
                
        # Format verification failures
        failures_text = ""
        if failure_details:
            failures_text = "\n\nDetailed CBMC verification failures:\n\n"
            for category, failures in failure_details.items():
                failures_text += f"\n{category.capitalize()} failures ({len(failures)}):\n"
                for failure in failures[:3]:  # Show first 3 of each category
                    failures_text += f"- {failure}\n"
        
        # Format 'no body for callee' errors separately for emphasis
        no_body_text = ""
        if missing_functions:
            no_body_text = "\n\nMISSING FUNCTION BODIES DETECTED:\n\n"
            for func in missing_functions:
                no_body_text += f"- no body for callee: {func}\n"
            
            no_body_text += """
            You must implement or stub these functions. Options:
            1. Find and include the actual implementation
            2. Create minimal stubs that return appropriate values
            3. Avoid calling these functions and simulate their effects
            """
        
        # Format failure trace if available
        trace_text = ""
        if trace_steps:
            trace_text = "\n\nExecution trace from CBMC:\n\n"
            for step in trace_steps[:10]:  # Show first 10 steps
                trace_text += f"{step}\n"
            if len(trace_steps) > 10:
                trace_text += f"... and {len(trace_steps) - 10} more steps\n"
                
        # Format errors from stderr
        stderr_text = ""
        if cbmc_stderr:
            stderr_text = "\n\nCBMC stderr output:\n\n"
            stderr_lines = cbmc_stderr.split('\n')
            for line in stderr_lines[:15]:  # Show first 15 lines
                if line.strip():
                    stderr_text += f"{line}\n"
            if len(stderr_lines) > 15:
                stderr_text += f"... and {len(stderr_lines) - 15} more lines\n"
                
        # Summarize failure locations
        locations_text = ""
        if failure_locations:
            locations_text = "\n\nFailure locations:\n\n"
            for location, failures in failure_locations.items():
                locations_text += f"- {location}: {len(failures)} failures\n"
        
        # Build structured improvement recommendation
        improvement_recommendation = f"""
        Previous harness for {func_name} needs improvement. Refinement attempt {current_attempts + 1} of {max_refinements}.
        
        CBMC verification status: {cbmc_status}
        
        KEY ISSUES IDENTIFIED:
        {issues_text}
        
        RECOMMENDED FIXES:
        {fixes_text}
        {patterns_text}
        
        {no_body_text}
        {failures_text}
        {locations_text}
        {trace_text}
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
        1. DO NOT CREATE ANY MOCK OR STUB IMPLEMENTATIONS unless specifically required for missing functions
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

    # Update function times - FIXED VERSION with better initialization
    function_times = state.get("function_times", {}).copy()
    if func_name not in function_times:
        function_times[func_name] = {}
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