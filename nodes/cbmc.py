"""
CBMC execution node for harness generator workflow.
"""
import os
import time
import shutil
import subprocess
import glob
from langchain_core.messages import AIMessage
import logging
from utils.cbmc_parser import process_cbmc_output
from utils.metrics_utils import get_metrics_tracker

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
    
    # Create proper directory structure for verification
    verification_harness_dir = os.path.join(verification_base_dir, "harness_files")
    verification_include_dir = os.path.join(verification_base_dir, "includes")
    verification_stubs_dir = os.path.join(verification_base_dir, "stubs")
    verification_cbmc_utils_dir = os.path.join(verification_base_dir, "cbmc_utils")
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
    else:
        # Original single-file mode - write source to a flat file
        source_file = os.path.join(verification_project_src_dir, "source.c")
        with open(source_file, "w") as f:
            f.write(state.get("source_code", ""))
    
    # Write harness to file
    harness_filename = original_func_name if ":" not in func_name else original_func_name
    harness_file = os.path.join(verification_harness_dir, f"{harness_filename}_harness.c")
    with open(harness_file, "w") as f:
        # Add include for the CBMC definitions header
        f.write("#include \"cbmc_defs.h\"\n\n")
        f.write(harness_code)
    
    # Build CBMC command parameters
    cbmc_cmd = [
        "cbmc",
        "--function", "main",  # Use main as the entry point in generated harnesses
        "--object-bits", "8",
        "-DCBMC_MAX_OBJECT_SIZE=" + str(cbmc_max_object_size)
    ]
    
    # Add source files in the correct order
    cbmc_cmd.append(harness_file)
    cbmc_cmd.extend(glob.glob(os.path.join(verification_project_src_dir, "*.c")))
    cbmc_cmd.extend(glob.glob(os.path.join(verification_cbmc_utils_dir, "*.c")))
    cbmc_cmd.extend(glob.glob(os.path.join(verification_stubs_dir, "*.c")))
    
    # Add verification flags
    cbmc_cmd.extend([
        "--memory-leak-check",
        "--memory-cleanup-check",
        "--bounds-check",
        "--pointer-overflow-check",
        "--div-by-zero-check",
    ])
    
    # Add necessary include paths
    cbmc_cmd.extend([
        "-I", verification_include_dir,
        "-I", verification_harness_dir,
        "-I", verification_stubs_dir,
        "-I", verification_cbmc_utils_dir,
        "-I", verification_project_src_dir
    ])
    
    # Save the command for debugging
    cmd_file = os.path.join(func_verification_dir, f"v{version_num}_command.txt")
    with open(cmd_file, "w") as f:
        f.write(" ".join(cbmc_cmd))
    
    # Create a separate command for coverage with compatible flags
    coverage_cmd = cbmc_cmd.copy()
    coverage_cmd.extend([
        "--cover", "location",
        "--xml-ui"  # Using XML format for consistent parsing
    ])
    
    # Initialize result variables
    cbmc_stdout = ""
    cbmc_stderr = ""
    cbmc_returncode = 0
    cbmc_results = state.get("cbmc_results", {}).copy()
    
    try:
        # Run the verification
        logger.info(f"Running CBMC verification for {func_name}")
        property_process = subprocess.run(
            cbmc_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=60,
            check=False
        )
        
        cbmc_stdout = property_process.stdout
        cbmc_stderr = property_process.stderr
        cbmc_returncode = property_process.returncode
        
        # Save raw output immediately
        raw_output_file = os.path.join(func_verification_dir, f"v{version_num}_raw_output.txt")
        with open(raw_output_file, "w") as f:
            f.write("=== STDOUT ===\n")
            f.write(cbmc_stdout)
            f.write("\n\n=== STDERR ===\n")
            f.write(cbmc_stderr)
        
        # Run coverage checking separately
        try:
            logger.info(f"Running coverage checking for {func_name}")
            coverage_process = subprocess.run(
                coverage_cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=30,  # Shorter timeout for coverage
                check=False
            )
            
            coverage_stdout = coverage_process.stdout
            
            # Save coverage output
            coverage_file = os.path.join(func_verification_dir, f"v{version_num}_coverage.txt")
            with open(coverage_file, "w") as f:
                f.write(coverage_stdout)
                
            # Process the combined stdout with coverage
            cbmc_stdout += "\n" + coverage_stdout
            
        except subprocess.TimeoutExpired:
            logger.warning(f"Coverage check timed out for {func_name}")
        except Exception as e:
            logger.error(f"Error running coverage check: {str(e)}")
        
        # Process CBMC output using our new parser
        cbmc_result = process_cbmc_output(cbmc_stdout, cbmc_stderr)
        
        # Update metrics
        metrics_tracker = get_metrics_tracker()
        
        # Get runtime in milliseconds
        verification_time_ms = int((time.time() - verification_start) * 1000)
        
        # Add metrics to tracker
        metrics_tracker.add_function_metrics(
            func_name, 
            version_num, 
            cbmc_result,
            verification_time_ms
        )
        
        # Create a structured result for the state
        cbmc_results[func_name] = {
            "function": func_name,
            "status": cbmc_result["verification_status"],
            "message": cbmc_result["message"],
            "suggestions": cbmc_result["suggestions"],
            "stdout": cbmc_stdout,
            "stderr": cbmc_stderr,
            "returncode": cbmc_returncode,
            "version": version_num,
            "error_categories": cbmc_result["error_categories"],
            "missing_functions": list(cbmc_result["missing_functions"]),
            "verification_failures": cbmc_result["verification_failures"],
            "error_locations": cbmc_result["error_locations"]
        }
        
        # Save verification results to a structured file
        verification_file = os.path.join(func_verification_dir, f"v{version_num}_results.txt")
        with open(verification_file, "w") as f:
            f.write(f"Function: {func_name}\n")
            f.write(f"Version: {version_num}\n")
            f.write(f"Status: {cbmc_result['verification_status']}\n")
            f.write(f"Message: {cbmc_result['message']}\n")
            if cbmc_result["suggestions"]:
                f.write(f"Suggestions: {cbmc_result['suggestions']}\n")
            
            f.write("\n=== PROOF METRICS ===\n")
            f.write(f"Reachable lines: {cbmc_result['reachable_lines']}\n")
            f.write(f"Covered lines: {cbmc_result['covered_lines']}\n")
            f.write(f"Coverage: {cbmc_result['coverage_pct']:.2f}%\n")
            f.write(f"Errors: {cbmc_result['errors']}\n")
            
            if cbmc_result["error_categories"]:
                f.write("\n=== ERROR CATEGORIES ===\n")
                for category in cbmc_result["error_categories"]:
                    f.write(f"- {category}\n")
            
            if cbmc_result["missing_functions"]:
                f.write("\n=== MISSING FUNCTIONS ===\n")
                for func in cbmc_result["missing_functions"]:
                    f.write(f"- {func}\n")
            
            f.write("\n=== STDOUT ===\n")
            f.write(cbmc_stdout)
            f.write("\n\n=== STDERR ===\n")
            f.write(cbmc_stderr)
        
        # Generate a more helpful report in markdown format
        report_file = os.path.join(func_verification_dir, f"v{version_num}_report.md")
        with open(report_file, "w") as f:
            f.write(f"# CBMC Verification Report - {func_name} (Version {version_num})\n\n")
            f.write(f"## Summary\n\n")
            f.write(f"**Status:** {cbmc_result['verification_status']}\n\n")
            f.write(f"**Message:** {cbmc_result['message']}\n\n")
            if cbmc_result["suggestions"]:
                f.write(f"**Suggestions:** {cbmc_result['suggestions']}\n\n")
            
            # Add Proof Metrics section
            f.write(f"## Proof Metrics\n\n")
            f.write(f"| Metric | Value |\n")
            f.write(f"|--------|-------|\n")
            f.write(f"| Reachable lines | {cbmc_result['reachable_lines']} |\n")
            f.write(f"| Covered lines | {cbmc_result['covered_lines']} |\n")
            f.write(f"| Coverage | {cbmc_result['coverage_pct']:.2f}% |\n")
            f.write(f"| Errors | {cbmc_result['errors']} |\n\n")
            
            # Add error details if any
            if cbmc_result["error_categories"]:
                f.write(f"## Error Categories\n\n")
                for category in cbmc_result["error_categories"]:
                    f.write(f"- {category}\n")
                f.write("\n")
            
            # Add error locations if any
            if cbmc_result["error_locations"]:
                f.write(f"## Error Locations\n\n")
                for file, lines in cbmc_result["error_locations"].items():
                    f.write(f"**File:** {file}\n\n")
                    f.write(f"Error lines: {', '.join(map(str, sorted(lines)))}\n\n")
            
            # Add missing functions if any
            if cbmc_result["missing_functions"]:
                f.write(f"## Missing Functions\n\n")
                for func in cbmc_result["missing_functions"]:
                    f.write(f"- {func}\n")
                f.write("\n")
            
            # Add harness details
            harness_path = os.path.join(harnesses_dir, func_name, f"v{version_num}.c")
            f.write(f"## Harness Details\n\n")
            f.write(f"The harness file is located at: `{harness_path}`\n\n")
            
            f.write(f"## Verification Command\n\n")
            f.write(f"```\n{' '.join(cbmc_cmd)}\n```\n\n")
            
            f.write(f"## Next Steps\n\n")
            if cbmc_result["verification_status"] == "SUCCESS":
                f.write(f"The verification was successful. No issues were detected.\n")
            else:
                f.write(f"Based on the verification results, the following steps are recommended:\n\n")
                if cbmc_result["missing_functions"]:
                    f.write(f"1. Implement the missing functions needed by the harness\n")
                elif "memory_leak" in cbmc_result["error_categories"]:
                    f.write(f"1. Fix memory leaks by ensuring all allocated memory is freed\n")
                elif "null_pointer" in cbmc_result["error_categories"]:
                    f.write(f"1. Add null pointer checks before dereferencing pointers\n")
                elif "array_bounds" in cbmc_result["error_categories"]:
                    f.write(f"1. Add bounds checking for array accesses\n")
                else:
                    f.write(f"1. Review the verification failures and implement fixes\n")
                f.write(f"2. Run the verification again to confirm the issues are resolved\n")
    
    except subprocess.TimeoutExpired as e:
        # Handle timeout case
        if hasattr(e, 'process'):
            e.process.kill()
            e.process.wait()
        
        logger.warning(f"CBMC verification timed out for {func_name}")
        
        # Create timeout result
        cbmc_result = {
            "verification_status": "TIMEOUT",
            "message": "CBMC verification timed out after 60 seconds",
            "suggestions": "The function may have complex paths requiring longer verification time. Consider simplifying.",
            "error_categories": ["timeout"],
            "missing_functions": set(),
            "verification_failures": ["timeout"],
            "error_locations": {},
            "reachable_lines": 0,
            "covered_lines": 0,
            "coverage_pct": 0.0,
            "errors": 0
        }
        
        # Update metrics tracker
        metrics_tracker = get_metrics_tracker()
        verification_time_ms = int((time.time() - verification_start) * 1000)
        metrics_tracker.add_function_metrics(func_name, version_num, cbmc_result, verification_time_ms)
        
        # Update cbmc_results
        cbmc_results[func_name] = {
            "function": func_name,
            "status": "TIMEOUT",
            "message": "CBMC verification timed out after 60 seconds.",
            "suggestions": "The function may have complex paths requiring longer verification time. Consider simplifying.",
            "stdout": "TIMEOUT: Process exceeded 60 second time limit",
            "stderr": "",
            "returncode": -1,
            "version": version_num,
            "error_categories": ["timeout"],
            "missing_functions": [],
            "verification_failures": ["timeout"],
            "error_locations": {}
        }
        
        # Save timeout information to files
        verification_file = os.path.join(func_verification_dir, f"v{version_num}_results.txt")
        with open(verification_file, "w") as f:
            f.write(f"Function: {func_name}\n")
            f.write(f"Version: {version_num}\n")
            f.write(f"Status: TIMEOUT\n")
            f.write(f"Message: CBMC verification timed out after 60 seconds\n")
            f.write(f"Suggestions: The function may have complex paths requiring longer verification time. Consider simplifying.\n")
            
        # Create a timeout report
        report_file = os.path.join(func_verification_dir, f"v{version_num}_report.md")
        with open(report_file, "w") as f:
            f.write(f"# CBMC Verification Report - {func_name} (Version {version_num})\n\n")
            f.write(f"## Summary\n\n")
            f.write(f"**Status:** TIMEOUT\n\n")
            f.write(f"**Message:** CBMC verification timed out after 60 seconds.\n\n")
            f.write(f"**Suggestions:** The function may have complex paths requiring longer verification time. Consider simplifying.\n\n")
            
            f.write(f"## Analysis\n\n")
            f.write(f"The verification process timed out, which typically happens when the function has many complex paths or loops that CBMC needs to analyze. You may need to simplify the harness or consider using loop unwinding bounds to limit the verification scope.\n\n")
            
            f.write(f"## Next Steps\n\n")
            f.write(f"1. Review the harness implementation and simplify if possible\n")
            f.write(f"2. Add loop unwinding bounds if there are loops in the function\n")
            f.write(f"3. Consider breaking the verification into smaller parts\n")
            
    except Exception as e:
        # Handle other exceptions
        logger.error(f"Error running CBMC verification: {str(e)}", exc_info=True)
        
        # Create error result
        cbmc_result = {
            "verification_status": "ERROR",
            "message": f"Error running CBMC verification: {str(e)}",
            "suggestions": "Fix the error and try again",
            "error_categories": ["system_error"],
            "missing_functions": set(),
            "verification_failures": ["system_error"],
            "error_locations": {},
            "reachable_lines": 0,
            "covered_lines": 0,
            "coverage_pct": 0.0,
            "errors": 1
        }
        
        # Update metrics tracker
        metrics_tracker = get_metrics_tracker()
        verification_time_ms = int((time.time() - verification_start) * 1000)
        metrics_tracker.add_function_metrics(func_name, version_num, cbmc_result, verification_time_ms)
        
        # Update cbmc_results
        cbmc_results[func_name] = {
            "function": func_name,
            "status": "ERROR",
            "message": f"Error running CBMC verification: {str(e)}",
            "suggestions": "Fix the error and try again",
            "stdout": "",
            "stderr": str(e),
            "returncode": -1,
            "version": version_num,
            "error_categories": ["system_error"],
            "missing_functions": [],
            "verification_failures": ["system_error"],
            "error_locations": {}
        }
        
        # Save error information to files
        verification_file = os.path.join(func_verification_dir, f"v{version_num}_results.txt")
        with open(verification_file, "w") as f:
            f.write(f"Function: {func_name}\n")
            f.write(f"Version: {version_num}\n")
            f.write(f"Status: ERROR\n")
            f.write(f"Message: Error running CBMC verification: {str(e)}\n")
            f.write(f"Suggestions: Fix the error and try again\n")
            
        # Create an error report
        report_file = os.path.join(func_verification_dir, f"v{version_num}_report.md")
        with open(report_file, "w") as f:
            f.write(f"# CBMC Verification Report - {func_name} (Version {version_num})\n\n")
            f.write(f"## Summary\n\n")
            f.write(f"**Status:** ERROR\n\n")
            f.write(f"**Message:** Error running CBMC verification: {str(e)}\n\n")
            f.write(f"**Suggestions:** Fix the error and try again\n\n")
            
            f.write(f"## Analysis\n\n")
            f.write(f"An error occurred during the verification process. This might be due to a system issue or a problem with the harness code.\n\n")
            
            f.write(f"## Error Details\n\n")
            f.write(f"```\n{str(e)}\n```\n\n")
            
            f.write(f"## Next Steps\n\n")
            f.write(f"1. Check if CBMC is installed and configured correctly\n")
            f.write(f"2. Review the harness code for syntax errors\n")
            f.write(f"3. Try running CBMC manually with the command above\n")
    
    # Calculate verification time
    verification_time = time.time() - verification_start
    
    # Update function times dictionary
    function_times = state.get("function_times", {}).copy()
    if func_name not in function_times:
        function_times[func_name] = {}
    function_times[func_name]["verification"] = verification_time
    
    # Update result message
    result_message = f"CBMC verification for function {func_name} v{version_num} complete in {verification_time:.2f}s. Status: {cbmc_results[func_name]['status']}."
    
    return {
        "messages": [AIMessage(content=result_message)],
        "cbmc_results": cbmc_results,
        "function_times": function_times,
        "next": "evaluator"  # Always proceed to evaluator
    }

def route_from_cbmc(state):
    """Routes from CBMC to harness evaluator."""
    # Always route to evaluator
    return "evaluator"