"""
CBMC execution node for harness generator workflow.
"""
import os
import re
import time
import shutil
import subprocess
import glob
from langchain_core.messages import AIMessage
import logging

logger = logging.getLogger("cbmc")

def cbmc_node(state):
    """Executes CBMC verification on the current function's harness using sources from verification/sources directory."""
    verification_start = time.time()
    
    func_name = state.get("current_function", "")
    harnesses = state.get("harnesses", {})
    harness_code = harnesses.get(func_name, "")

    logger.info(f"Starting CBMC verification for function {func_name}")
    
    # Get result directories from state
    result_directories = state.get("result_directories", {})
    verification_base_dir = result_directories.get("verification_dir", "verification")
    harnesses_dir = result_directories.get("harnesses_dir", "harnesses")
    
    if not harness_code:
        logger.error(f"No harness available for function {func_name}")
        return {
            "messages": [AIMessage(content=f"Error: No harness available for function {func_name}.")],
            "next": "junction"  # Return to junction to process next function
        }
    
    # Extract file path from function name if it includes file info
    file_basename = None
    original_func_name = func_name
    
    if ":" in func_name:
        file_basename, original_func_name = func_name.split(":", 1)
    
    # Create function-specific directory
    func_verification_dir = os.path.join(verification_base_dir, func_name)
    os.makedirs(func_verification_dir, exist_ok=True)
    
    # Create proper directory structure for verification (with clearer names)
    verification_harness_dir = os.path.join(verification_base_dir, "harness_files")  # Renamed from "src"
    verification_include_dir = os.path.join(verification_base_dir, "includes")
    verification_stubs_dir = os.path.join(verification_base_dir, "stubs")
    verification_cbmc_utils_dir = os.path.join(verification_base_dir, "cbmc_utils")  # Renamed from "sources"
    os.makedirs(verification_harness_dir, exist_ok=True)
    os.makedirs(verification_include_dir, exist_ok=True)
    os.makedirs(verification_stubs_dir, exist_ok=True)
    os.makedirs(verification_cbmc_utils_dir, exist_ok=True)
    
    # Create a separate directory for project source files
    verification_project_src_dir = os.path.join(verification_base_dir, "project_src")
    os.makedirs(verification_project_src_dir, exist_ok=True)
    
    # Determine version number from refinement attempts
    refinement_num = state.get("refinement_attempts", {}).get(func_name, 0)
    version_num = refinement_num + 1
    
    # Define CBMC_MAX_OBJECT_SIZE
    cbmc_max_object_size = 1024 * 1024  # 1MB is a typical reasonable size
    
    # Create a header file with the CBMC_MAX_OBJECT_SIZE definition
    cbmc_defs_header = os.path.join(verification_include_dir, "cbmc_defs.h")
    with open(cbmc_defs_header, "w") as f:
        f.write("""/*
 * Auto-generated CBMC definitions header
 * This file provides definitions needed for CBMC verification
 */

#ifndef CBMC_DEFS_H
#define CBMC_DEFS_H

#include <stddef.h>
#include <limits.h>

/* CBMC object size constraints */
#ifndef CBMC_OBJECT_BITS
#define CBMC_OBJECT_BITS 8
#endif

#ifndef CBMC_MAX_OBJECT_SIZE
#define CBMC_MAX_OBJECT_SIZE (SIZE_MAX>>(CBMC_OBJECT_BITS+1))
#endif

#endif /* CBMC_DEFS_H */
""")
    
    # For directory mode, handle project file copying
    if state.get("is_directory_mode", False):
        # Get original source directory from state
        original_source_dir = state.get("source_directory", "")
        directory_path = os.path.dirname(original_source_dir) if original_source_dir else ""
        
        # Find the specific source file for this function from embeddings
        embeddings = state.get("embeddings", {})
        functions = embeddings.get("functions", {})
        
        if func_name in functions and "file_path" in functions[func_name]:
            file_path = functions[func_name]["file_path"]
            if file_path and os.path.exists(file_path):
                # Copy to the project source directory
                dest_file = os.path.join(verification_project_src_dir, os.path.basename(file_path))
                shutil.copy2(file_path, dest_file)
                print(f"Copied main source file: {file_path} → {dest_file}")
        
        # Copy necessary headers to include directory
        if original_source_dir and os.path.exists(original_source_dir):
            for root, dirs, files in os.walk(original_source_dir):
                for file in files:
                    # Copy headers to include directory
                    if file.endswith(('.h', '.hpp')):
                        src_file = os.path.join(root, file)
                        dest_file = os.path.join(verification_include_dir, file)
                        shutil.copy2(src_file, dest_file)
                        print(f"Copied header: {file}")
                    
                    # Copy implementation files 
                    elif file.endswith('.c') and file == "core_http_client.c":
                        src_file = os.path.join(root, file)
                        dest_file = os.path.join(verification_project_src_dir, file)
                        shutil.copy2(src_file, dest_file)
                        print(f"Copied implementation: {file}")
    else:
        # Original single-file mode - write source to a flat file
        source_file = os.path.join(verification_project_src_dir, "source.c")
        with open(source_file, "w") as f:
            f.write(state.get("source_code", ""))
    
    # Look for CBMC files from standard locations and copy them if they exist
    source_project_dir = os.path.dirname(state.get("source_directory", ""))
    
    # Copy CBMC include files
    for cbmc_dir_name in ["test/cbmc/include", "cbmc/include"]:
        cbmc_include_dir = os.path.join(source_project_dir, cbmc_dir_name)
        if os.path.exists(cbmc_include_dir):
            for file in os.listdir(cbmc_include_dir):
                if os.path.isfile(os.path.join(cbmc_include_dir, file)):
                    shutil.copy2(os.path.join(cbmc_include_dir, file), os.path.join(verification_include_dir, file))
                    print(f"Copied CBMC include file: {file}")
            break
    
    # Copy CBMC stub files
    for cbmc_dir_name in ["test/cbmc/stubs", "cbmc/stubs"]:
        cbmc_stubs_dir = os.path.join(source_project_dir, cbmc_dir_name)
        if os.path.exists(cbmc_stubs_dir):
            for file in os.listdir(cbmc_stubs_dir):
                if os.path.isfile(os.path.join(cbmc_stubs_dir, file)):
                    shutil.copy2(os.path.join(cbmc_stubs_dir, file), os.path.join(verification_stubs_dir, file))
                    print(f"Copied CBMC stub file: {file}")
            break
    
    # Copy CBMC utility source files
    for cbmc_dir_name in ["test/cbmc/sources", "cbmc/sources"]:
        cbmc_sources_dir = os.path.join(source_project_dir, cbmc_dir_name)
        if os.path.exists(cbmc_sources_dir):
            for file in os.listdir(cbmc_sources_dir):
                if os.path.isfile(os.path.join(cbmc_sources_dir, file)):
                    shutil.copy2(os.path.join(cbmc_sources_dir, file), os.path.join(verification_cbmc_utils_dir, file))
                    print(f"Copied CBMC utility file: {file}")
            break
            
    # Write harness to file
    harness_filename = original_func_name if ":" not in func_name else original_func_name
    harness_file = os.path.join(verification_harness_dir, f"{harness_filename}_harness.c")
    with open(harness_file, "w") as f:
        # Add include for the CBMC definitions header
        f.write("#include \"cbmc_defs.h\"\n\n")
        f.write(harness_code)
    
    # Build list of CBMC command parameters with clearer organization
    cbmc_cmd = [
        "cbmc",
        "--function", "main",  # Use main as the entry point in generated harnesses
        "--object-bits", "8",
        "-DCBMC_MAX_OBJECT_SIZE=" + str(cbmc_max_object_size)
    ]
    
    # Add source files in the correct order:
    # 1. First add harness file (most important)
    cbmc_cmd.append(harness_file)
    
    # 2. Add original project source files
    project_src_files = glob.glob(os.path.join(verification_project_src_dir, "*.c"))
    cbmc_cmd.extend(project_src_files)
    
    # 3. Add CBMC utility source files from the cbmc_utils directory
    cbmc_util_files = glob.glob(os.path.join(verification_cbmc_utils_dir, "*.c"))
    cbmc_cmd.extend(cbmc_util_files)
    
    # 4. Add stub files
    stub_files = glob.glob(os.path.join(verification_stubs_dir, "*.c"))
    cbmc_cmd.extend(stub_files)
    
    # Add verification flags
    cbmc_cmd.extend([
        "--memory-leak-check",
        "--memory-cleanup-check",
        "--bounds-check",
        "--pointer-overflow-check",
        "--div-by-zero-check",
        "--unwinding-assertions"
    ])
    
    # Add necessary include paths in the correct order
    cbmc_cmd.extend([
        "-I", verification_include_dir,
        "-I", verification_harness_dir,
        "-I", verification_stubs_dir,
        "-I", verification_cbmc_utils_dir,
        "-I", verification_project_src_dir
    ])
    
    # Add original project include paths if available
    source_project_dir = os.path.dirname(state.get("source_directory", ""))
    for include_path in ["source/include", "include", "source/interface"]:
        if os.path.exists(os.path.join(source_project_dir, include_path)):
            cbmc_cmd.extend(["-I", os.path.join(source_project_dir, include_path)])
    
    # Save the command for debugging
    cmd_file = os.path.join(func_verification_dir, f"v{version_num}_command.txt")
    with open(cmd_file, "w") as f:
        f.write(" ".join(cbmc_cmd))
    
    # Initialize dictionaries for tracking errors if they don't exist
    cbmc_error_messages = state.get("cbmc_error_messages", {}).copy()
    harness_syntax_errors = state.get("harness_syntax_errors", {}).copy()
    parsing_issues = state.get("parsing_issues", {}).copy()
    verification_failures = state.get("verification_failures", {}).copy()
    
    # Initialize proof metrics dictionary
    proof_metrics = state.get("proof_metrics", {}).copy()
    if func_name not in proof_metrics:
        proof_metrics[func_name] = {}
    
    # First, run property checking
    property_cmd = cbmc_cmd.copy()
    
    # Create a separate command for coverage with compatible flags
    coverage_cmd = cbmc_cmd.copy()
    coverage_cmd.extend([
        "--cover", "location",
        "--xml-ui",  # Using XML format for consistent parsing
        "--no-unwinding-assertions"
    ])

    try:
        # First run the property checking
        logger.info(f"Running property checking for {func_name}")
        property_process = subprocess.run(
            property_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=60,
            check=False
        )
        
        stdout = property_process.stdout
        stderr = property_process.stderr
        returncode = property_process.returncode
        
        # Then run the coverage checking separately
        logger.info(f"Running coverage checking for {func_name}")
        coverage_process = subprocess.run(
            coverage_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=60,
            check=False
        )
        
        coverage_stdout = coverage_process.stdout
        coverage_stderr = coverage_process.stderr
        
        # Extract coverage metrics
        logger.info(f"Extracting coverage metrics for {func_name}")
        
        # Initialize metrics
        total_blocks = 0
        covered_blocks = 0
        impl_blocks = 0
        impl_covered = 0
        
        # Parse coverage output - look for both XML and text formats
        if "<coverage" in coverage_stdout:
            # XML format parsing
            coverage_lines = coverage_stdout.split('\n')
            
            for line in coverage_lines:
                if '<coverage' in line and 'location' in line:
                    total_blocks += 1
                    if 'status="satisfied"' in line:
                        covered_blocks += 1
                        
                    # Check if this is an implementation block
                    if "_harness.c" not in line and ".c:" in line:
                        impl_blocks += 1
                        if 'status="satisfied"' in line:
                            impl_covered += 1
        else:
            # Text format parsing as backup
            coverage_lines = [line for line in coverage_stdout.split('\n') if "coverage" in line.lower()]
            
            # Count coverage blocks
            total_blocks = sum(1 for line in coverage_lines if "coverage." in line)
            covered_blocks = sum(1 for line in coverage_lines if "SATISFIED" in line)
            
            # Count implementation blocks
            impl_coverage_lines = [line for line in coverage_lines 
                                if "_harness.c" not in line and ".c:" in line]
            impl_blocks = len(impl_coverage_lines)
            impl_covered = sum(1 for line in impl_coverage_lines if "SATISFIED" in line)
        
        # Calculate coverage percentages
        if total_blocks > 0:
            total_coverage = (covered_blocks / total_blocks) * 100
        else:
            total_coverage = 0.0
            
        if impl_blocks > 0:
            func_coverage = (impl_covered / impl_blocks) * 100
        else:
            func_coverage = 0.0
        
        # Set the metrics values
        total_reachable_lines = total_blocks
        total_covered_lines = covered_blocks
        func_reachable_lines = impl_blocks
        func_covered_lines = impl_covered
        
        # Process results
        status = "SUCCESS" if returncode == 0 else "FAILED"
        message = "VERIFICATION SUCCESSFUL: No issues detected."
        suggestions = ""
        
        # More detailed error analysis
        if returncode != 0:
            # Check for syntax errors or parsing issues first
            syntax_error_match = re.search(r'syntax error at line (\d+)', stderr)
            if syntax_error_match:
                line_number = syntax_error_match.group(1)
                harness_syntax_errors[func_name] = f"Syntax error at line {line_number}"
                message = f"HARNESS ERROR: Syntax error in harness at line {line_number}."
                suggestions = "Fix the syntax error in the harness."
            
            # Check for parsing issues
            if "PARSING ERROR" in stderr:
                parsing_issues[func_name] = True
                
                # Extract specific parsing error
                parsing_error_match = re.search(r'(.+?): fatal error: (.+)$', stderr, re.MULTILINE)
                if parsing_error_match:
                    error_location = parsing_error_match.group(1)
                    error_message = parsing_error_match.group(2)
                    message = f"PARSING ERROR: {error_message}"
                    suggestions = f"Fix the parsing error in {error_location}."
                else:
                    message = "PARSING ERROR: Could not parse the harness."
                    suggestions = "Check for missing include files or syntax errors."
            
            # Track the specific error message for this function
            cbmc_error_messages[func_name] = message
            
            # Check for common verification failures if no syntax/parsing issues
            if "VERIFICATION FAILED" in stdout and not parsing_issues.get(func_name, False):
                failure_types = []
                
                if "memory leak detected" in stdout.lower():
                    failure_types.append("memory_leak")
                    message = "VERIFICATION FAILED: Memory leak detected."
                    suggestions = "Ensure all allocated memory is freed in all execution paths."
                
                elif "dereference failure" in stdout.lower() or "NULL pointer" in stdout.lower():
                    failure_types.append("null_pointer")
                    message = "VERIFICATION FAILED: Null pointer dereference detected."
                    suggestions = "Add null pointer checks before dereferencing."
                
                elif "array bounds" in stdout.lower():
                    failure_types.append("array_bounds")
                    message = "VERIFICATION FAILED: Array bounds violation detected."
                    suggestions = "Add bounds checking for array accesses."
                
                elif "division by zero" in stdout.lower():
                    failure_types.append("division_by_zero")
                    message = "VERIFICATION FAILED: Division by zero detected."
                    suggestions = "Add checks to ensure divisors are non-zero."
                
                elif "pointer arithmetic" in stdout.lower() and "overflow" in stdout.lower():
                    failure_types.append("pointer_overflow")
                    message = "VERIFICATION FAILED: Pointer arithmetic overflow detected."
                    suggestions = "Ensure pointer arithmetic stays within allocated bounds."
                
                elif "arithmetic overflow" in stdout.lower():
                    failure_types.append("arithmetic_overflow")
                    message = "VERIFICATION FAILED: Arithmetic overflow detected."
                    suggestions = "Add overflow checking for arithmetic operations."
                
                elif "type" in stdout.lower() and "conversion" in stdout.lower():
                    failure_types.append("type_conversion")
                    message = "VERIFICATION FAILED: Problematic type conversion detected."
                    suggestions = "Verify type conversions do not result in information loss."
                
                if failure_types:
                    verification_failures[func_name] = failure_types
                else:
                    # Try to extract more details from the output
                    failure_lines = [line for line in stdout.split('\n') if "FAILED" in line]
                    if failure_lines:
                        message = f"VERIFICATION FAILED: {failure_lines[0]}"
                        verification_failures[func_name] = ["general_verification_failure"]
                    else:
                        message = "VERIFICATION FAILED: Unspecified verification error."
                        verification_failures[func_name] = ["unspecified_failure"]
                    
                    # Look for any assertion failures
                    assertion_lines = [line for line in stdout.split('\n') if "assertion" in line.lower() and "failed" in line.lower()]
                    if assertion_lines:
                        suggestions = f"Review assertion failure: {assertion_lines[0]}"
                    else:
                        suggestions = "Review the full verification output for details."
            else:
                # Handle errors that aren't explicit verification failures
                if "PARSING ERROR" not in stderr and "syntax error" not in stderr:
                    message = f"VERIFICATION FAILED: Command returned error code {returncode}."
                    if "file not found" in stderr:
                        missing_file_match = re.search(r"'([^']+)' file not found", stderr)
                        if missing_file_match:
                            missing_file = missing_file_match.group(1)
                            message += f" Missing header file: '{missing_file}'."
                            suggestions = f"Make sure '{missing_file}' is available in the include path."
                    elif stderr:
                        message += f" Error: {stderr[:200]}..."
                    suggestions = suggestions or "Check the CBMC command and harness for errors."
        
        # Find all error lines, excluding unwinding assertions and missing function bodies
        error_lines = {}
        
        # Find all error lines that don't match the exclusion criteria
        for line in stdout.split('\n'):
            # First, collect line numbers with errors
            if "VERIFICATION FAILED" in line:
                # Exclude specific error types
                if "unwinding assertion" in line or "no body for function" in line:
                    continue
                
                # Extract location information
                loc_match = re.search(r'file ([^:]+):(\d+)', line)
                if loc_match:
                    file_name = loc_match.group(1)
                    line_num = int(loc_match.group(2))
                    if file_name not in error_lines:
                        error_lines[file_name] = set()
                    error_lines[file_name].add(line_num)
        
        # Count total unique line errors
        total_unique_errors = sum(len(lines) for lines in error_lines.values())
        
        # Store the proof metrics
        logger.info(f"Proof metrics for {func_name}:")
        logger.info(f"  Total reachable lines: {total_reachable_lines}")
        logger.info(f"  Total coverage: {total_coverage:.2f}%")
        logger.info(f"  Function reachable lines: {func_reachable_lines}")
        logger.info(f"  Function coverage: {func_coverage:.2f}%")
        logger.info(f"  Reported errors: {total_unique_errors}")
        
        proof_metrics[func_name] = {
            "total_reachable_lines": total_reachable_lines,
            "total_coverage": total_coverage,
            "func_reachable_lines": func_reachable_lines,
            "func_coverage": func_coverage,
            "reported_errors": total_unique_errors,
            "error_lines": error_lines  # Store the actual line numbers for reference
        }
        
        # Update the results dictionary
        cbmc_results = state.get("cbmc_results", {}).copy()
        cbmc_results[func_name] = {
            "function": func_name,
            "status": status,
            "message": message,
            "suggestions": suggestions,
            "stdout": stdout,
            "returncode": returncode,
            "version": version_num,
            "has_syntax_error": func_name in harness_syntax_errors,
            "has_parsing_issue": func_name in parsing_issues,
            "verification_failure_types": verification_failures.get(func_name, [])
        }
        
        # Save verification results to file with version
        verification_file = os.path.join(func_verification_dir, f"v{version_num}_results.txt")
        with open(verification_file, "w") as f:
            f.write(f"Function: {func_name}\n")
            f.write(f"Version: {version_num}\n")
            f.write(f"Status: {status}\n")
            f.write(f"Message: {message}\n")
            if suggestions:
                f.write(f"Suggestions: {suggestions}\n")
            f.write("\n=== PROOF METRICS ===\n")
            f.write(f"Total reachable lines: {total_reachable_lines}\n")
            f.write(f"Total coverage: {proof_metrics[func_name]['total_coverage']:.2f}%\n")
            f.write(f"Function reachable lines: {func_reachable_lines}\n")
            f.write(f"Function coverage: {func_coverage:.2f}%\n")
            f.write(f"Reported errors: {total_unique_errors}\n")
            f.write("\nDetailed Output:\n")
            f.write(stdout)
        
        # Also save raw output for debugging
        raw_output_file = os.path.join(func_verification_dir, f"v{version_num}_raw_output.txt")
        with open(raw_output_file, "w") as f:
            f.write(stdout)
        
        # Generate a verification report for this version
        report_file = os.path.join(func_verification_dir, f"v{version_num}_report.md")
        with open(report_file, "w") as f:
            f.write(f"# CBMC Verification Report - {func_name} (Version {version_num})\n\n")
            f.write(f"## Summary\n\n")
            f.write(f"**Status:** {status}\n\n")
            f.write(f"**Message:** {message}\n\n")
            if suggestions:
                f.write(f"**Suggestions:** {suggestions}\n\n")
            
            # Add Proof Metrics section
            f.write(f"## Proof Metrics\n\n")
            f.write(f"| Metric | Value |\n")
            f.write(f"|--------|-------|\n")
            f.write(f"| Total reachable lines | {total_reachable_lines} |\n")
            f.write(f"| Total coverage | {proof_metrics[func_name]['total_coverage']:.2f}% |\n")
            f.write(f"| Function reachable lines | {func_reachable_lines} |\n")
            f.write(f"| Function coverage | {func_coverage:.2f}% |\n")
            f.write(f"| Reported errors | {total_unique_errors} |\n\n")
            
            # Add error details if any
            if total_unique_errors > 0:
                f.write(f"### Error Details\n\n")
                for file_name, line_nums in error_lines.items():
                    f.write(f"**File:** {file_name}\n\n")
                    f.write(f"Error lines: {', '.join(map(str, sorted(line_nums)))}\n\n")
            
            # Update path to harness file to reflect new structure
            harness_path = os.path.join(harnesses_dir, func_name, f"v{version_num}.c")
            f.write(f"## Harness Details\n\n")
            f.write(f"The harness file is located at: `{harness_path}`\n\n")
            
            f.write(f"## Verification Command\n\n")
            f.write(f"```\n{' '.join(property_cmd)}\n```\n\n")
            
            f.write(f"## Detailed Output\n\n")
            f.write("```\n")
            # Only include the first 20 lines and last 20 lines if output is very long
            if len(stdout.split('\n')) > 50:
                output_lines = stdout.split('\n')
                trimmed_output = '\n'.join(output_lines[:20] + ["\n... [output trimmed] ...\n"] + output_lines[-20:])
                f.write(trimmed_output)
                f.write(f"\n\nNote: Output has been trimmed. See full output in v{version_num}_raw_output.txt\n")
            else:
                f.write(stdout)
            f.write("\n```\n\n")
            
            if returncode != 0:
                f.write(f"## Analysis\n\n")
                f.write(f"The verification failed with return code {returncode}. ")
                if suggestions:
                    f.write(f"Based on the output, it is recommended to {suggestions.lower()}\n\n")
                
                f.write(f"## Next Steps\n\n")
                f.write(f"1. Review the harness implementation\n")
                f.write(f"2. Implement the suggested fixes\n")
                f.write(f"3. Run another verification iteration\n")
            else:
                f.write(f"## Analysis\n\n")
                f.write(f"The verification was successful. No issues were detected with the current harness implementation.\n\n")
        
    except subprocess.TimeoutExpired as e:
        # Handle timeout
        if hasattr(e, 'process'):
            e.process.kill()
            e.process.wait()
        
        # Initialize metrics with default values for timeout
        proof_metrics[func_name] = {
            "total_reachable_lines": 0,
            "total_coverage": 0.0,
            "func_reachable_lines": 0,
            "func_coverage": 0.0,
            "reported_errors": 0,
            "error_lines": {},
            "timeout": True
        }
        
        # Handle timeout
        cbmc_results = state.get("cbmc_results", {}).copy()
        cbmc_results[func_name] = {
            "function": func_name,
            "status": "TIMEOUT",
            "message": "CBMC verification timed out after 60 seconds.",
            "suggestions": "The function may have complex paths requiring longer verification time. Consider simplifying.",
            "stdout": "TIMEOUT: Process exceeded 60 second time limit",
            "version": version_num,
            "has_syntax_error": False,
            "has_parsing_issue": False,
            "verification_failure_types": ["timeout"]
        }
        
        # Save timeout to file
        verification_file = os.path.join(func_verification_dir, f"v{version_num}_results.txt")
        with open(verification_file, "w") as f:
            f.write(f"Function: {func_name}\n")
            f.write(f"Version: {version_num}\n")
            f.write(f"Status: TIMEOUT\n")
            f.write(f"=== PROOF METRICS ===\n")
            f.write(f"Total reachable lines: N/A (timeout)\n")
            f.write(f"Total coverage: N/A (timeout)\n")
            f.write(f"Function reachable lines: N/A (timeout)\n")
            f.write(f"Function coverage: N/A (timeout)\n")
            f.write(f"Reported errors: N/A (timeout)\n")
            f.write(f"Error: CBMC verification timed out after 60 seconds\n")
            f.write(f"Suggestions: The function may have complex paths requiring longer verification time. Consider simplifying.\n")
            
        # Generate timeout report
        report_file = os.path.join(func_verification_dir, f"v{version_num}_report.md")
        with open(report_file, "w") as f:
            f.write(f"# CBMC Verification Report - {func_name} (Version {version_num})\n\n")
            f.write(f"## Summary\n\n")
            f.write(f"**Status:** TIMEOUT\n\n")
            f.write(f"**Message:** CBMC verification timed out after 60 seconds.\n\n")
            f.write(f"**Suggestions:** The function may have complex paths requiring longer verification time. Consider simplifying.\n\n")
            
            # Add empty proof metrics section
            f.write(f"## Proof Metrics\n\n")
            f.write(f"| Metric | Value |\n")
            f.write(f"|--------|-------|\n")
            f.write(f"| Total reachable lines | N/A (timeout) |\n")
            f.write(f"| Total coverage | N/A (timeout) |\n")
            f.write(f"| Function reachable lines | N/A (timeout) |\n")
            f.write(f"| Function coverage | N/A (timeout) |\n")
            f.write(f"| Reported errors | N/A (timeout) |\n\n")
            
            # Update path to harness file to reflect new structure
            harness_path = os.path.join(harnesses_dir, func_name, f"v{version_num}.c")
            f.write(f"## Harness Details\n\n")
            f.write(f"The harness file is located at: `{harness_path}`\n\n")
            
            f.write(f"## Analysis\n\n")
            f.write(f"The verification process timed out, which typically happens when the function has many complex paths or loops that CBMC needs to analyze. You may need to simplify the harness or consider using loop unwinding bounds to limit the verification scope.\n\n")
            
            f.write(f"## Next Steps\n\n")
            f.write(f"1. Review the harness implementation and simplify if possible\n")
            f.write(f"2. Add loop unwinding bounds if there are loops in the function\n")
            f.write(f"3. Consider breaking the verification into smaller parts\n")
    
    # Calculate verification time
    verification_time = time.time() - verification_start
    
    # Update function times dictionary
    function_times = state.get("function_times", {}).copy()
    if func_name not in function_times:
        function_times[func_name] = {}
    function_times[func_name]["verification"] = verification_time
    
    # Update result message with new paths
    result_base_dir = result_directories.get("result_base_dir", "results")
    result_message = f"CBMC verification for function {func_name} v{version_num} complete in {verification_time:.2f}s. Status: {cbmc_results[func_name]['status']}."
    result_message += f" Results saved to {func_verification_dir}/v{version_num}_results.txt"
    
    return {
        "messages": [AIMessage(content=result_message)],
        "cbmc_results": cbmc_results,
        "function_times": function_times,
        "cbmc_error_messages": cbmc_error_messages,
        "harness_syntax_errors": harness_syntax_errors,
        "parsing_issues": parsing_issues,
        "verification_failures": verification_failures,
        "proof_metrics": proof_metrics,  # Pass the proof metrics through the state
        "next": "evaluator"  # Always proceed to evaluator
    }

def route_from_cbmc(state):
    """Routes from CBMC to harness evaluator and passes proof metrics."""
    # Always route to evaluator
    return "evaluator"