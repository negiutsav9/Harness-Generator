"""
Output node for CBMC harness generator workflow.
"""
import os
import time
from langchain_core.messages import AIMessage
import logging

logger = logging.getLogger("output")

def output_node(state):
    """Provides final summary of all processed functions with performance metrics and generates an index report."""
    total_time = time.time() - state.get("start_time", time.time())

    logger.info("Generating final report and output summaries")
    
    # Get result directories from state
    result_directories = state.get("result_directories", {})
    reports_dir = result_directories.get("reports_dir", "reports")
    harnesses_dir = result_directories.get("harnesses_dir", "harnesses")
    verification_dir = result_directories.get("verification_dir", "verification")
    result_base_dir = result_directories.get("result_base_dir", "results")
    
    # Get LLM model info
    llm_used = state.get("llm_used", "claude")
    
    # Determine if we're in directory mode
    is_directory_mode = state.get("is_directory_mode", False)
    
    # Calculate summary statistics
    function_times = state.get("function_times", {})
    total_refinements = sum(state.get("refinement_attempts", {}).values())
    
    # Get the proof metrics
    proof_metrics = state.get("proof_metrics", {})
    
    # Calculate aggregate proof metrics
    aggregate_metrics = {
        "total_reachable_lines": 0,
        "total_covered_lines": 0,
        "func_reachable_lines": 0,
        "func_covered_lines": 0,
        "total_reported_errors": 0,
        "functions_with_full_coverage": 0,
        "functions_without_errors": 0
    }
    
    # Compute the aggregated proof metrics with improved error handling
    for func_name, metrics in proof_metrics.items():
        if "timeout" not in metrics and "system_error" not in metrics:  # Skip timeouts and errors
            # Add better error handling for metrics extraction
            total_reachable = metrics.get("total_reachable_lines", 0)
            if not isinstance(total_reachable, int):
                try:
                    total_reachable = int(total_reachable)
                except (ValueError, TypeError):
                    total_reachable = 0
                    
            aggregate_metrics["total_reachable_lines"] += total_reachable
            
            # Calculate covered lines from total_reachable_lines and total_coverage
            total_coverage_pct = metrics.get("total_coverage", 0)
            if isinstance(total_coverage_pct, str):
                try:
                    total_coverage_pct = float(total_coverage_pct.strip('%'))
                except (ValueError, TypeError):
                    total_coverage_pct = 0
            
            covered_lines = int(total_reachable * total_coverage_pct / 100) if total_reachable > 0 else 0
            aggregate_metrics["total_covered_lines"] += covered_lines
            
            # Handle function-specific metrics
            func_reachable = metrics.get("func_reachable_lines", 0)
            if not isinstance(func_reachable, int):
                try:
                    func_reachable = int(func_reachable)
                except (ValueError, TypeError):
                    func_reachable = 0
                    
            aggregate_metrics["func_reachable_lines"] += func_reachable
            
            # Calculate function covered lines
            func_coverage_pct = metrics.get("func_coverage", 0)
            if isinstance(func_coverage_pct, str):
                try:
                    func_coverage_pct = float(func_coverage_pct.strip('%'))
                except (ValueError, TypeError):
                    func_coverage_pct = 0
                    
            func_covered_lines = int(func_reachable * func_coverage_pct / 100) if func_reachable > 0 else 0
            aggregate_metrics["func_covered_lines"] += func_covered_lines
            
            # Add error counts
            reported_errors = metrics.get("reported_errors", 0)
            if not isinstance(reported_errors, int):
                try:
                    reported_errors = int(reported_errors)
                except (ValueError, TypeError):
                    reported_errors = 0
                    
            aggregate_metrics["total_reported_errors"] += reported_errors
            
            # Count functions with full coverage (100%)
            if func_coverage_pct == 100.0:
                aggregate_metrics["functions_with_full_coverage"] += 1
                
            # Count functions without errors
            if reported_errors == 0:
                aggregate_metrics["functions_without_errors"] += 1
    
    # Calculate overall coverage percentages with safeguards against division by zero
    overall_total_coverage = 0
    if aggregate_metrics["total_reachable_lines"] > 0:
        overall_total_coverage = (aggregate_metrics["total_covered_lines"] / aggregate_metrics["total_reachable_lines"]) * 100
        
    overall_func_coverage = 0
    if aggregate_metrics["func_reachable_lines"] > 0:
        overall_func_coverage = (aggregate_metrics["func_covered_lines"] / aggregate_metrics["func_reachable_lines"]) * 100
    
    # Create performance metrics
    if function_times:
        avg_generation_time = sum(times.get("generation", 0) for times in function_times.values()) / len(function_times)
        avg_verification_time = sum(times.get("verification", 0) for times in function_times.values()) / len(function_times)
        avg_evaluation_time = sum(times.get("evaluation", 0) for times in function_times.values()) / len(function_times)
        avg_refinements = total_refinements / len(state.get("refinement_attempts", {})) if state.get("refinement_attempts", {}) else 0
    else:
        avg_generation_time = avg_verification_time = avg_evaluation_time = avg_refinements = 0
    
    # Create a header based on mode
    if is_directory_mode:
        source_files = state.get("source_files", {})
        header = [
            f"# CBMC Harness Generation Complete - Directory Mode - {llm_used.capitalize()}",
            "",
            f"Total processing time: {total_time:.2f} seconds",
            f"Processed {len(source_files)} source files.",
            f"Analyzed {len(state.get('embeddings', {}).get('functions', {}))} functions.",
            f"Identified {len(state.get('vulnerable_functions', []))} functions with memory or arithmetic operations.",
            f"Generated {len(state.get('harnesses', {}))} verification harnesses.",
            f"Performed {total_refinements} harness refinements (average {avg_refinements:.2f} per function).",
        ]
        
        # Add file statistics
        header.extend([
            "",
            "## File Analysis",
        ])
        
        # Group functions by file
        files_functions = {}
        for func_id in state.get('vulnerable_functions', []):
            file_name = "unknown"
            if ":" in func_id:
                file_name, _ = func_id.split(":", 1)
            
            if file_name not in files_functions:
                files_functions[file_name] = []
            files_functions[file_name].append(func_id)
        
        # Add file details
        for file_name, funcs in files_functions.items():
            header.append(f"\n### {file_name}")
            header.append(f"Functions analyzed: {len(funcs)}")
            verified_funcs = [f for f in funcs if f in state.get('cbmc_results', {})]
            header.append(f"Functions verified: {len(verified_funcs)}")
            
            if verified_funcs:
                successful = sum(1 for f in verified_funcs if state.get('cbmc_results', {}).get(f, {}).get('status') == 'SUCCESS')
                header.append(f"Successful verifications: {successful}")
                header.append(f"Failed verifications: {len(verified_funcs) - successful}")
    else:
        # Single file mode header
        header = [
            f"# CBMC Harness Generation Complete - {llm_used.capitalize()}",
            "",
            f"Total processing time: {total_time:.2f} seconds",
            f"Analyzed {len(state.get('embeddings', {}).get('functions', {}))} functions.",
            f"Identified {len(state.get('vulnerable_functions', []))} functions with memory or arithmetic operations.",
            f"Generated {len(state.get('harnesses', {}))} verification harnesses.",
            f"Performed {total_refinements} harness refinements (average {avg_refinements:.2f} per function).",
        ]
    
    # Add unit proof metrics summary
    header.extend([
        "",
        "## Unit Proof Metrics Summary",
        f"Total reachable lines: {aggregate_metrics['total_reachable_lines']}",
        f"Total coverage: {overall_total_coverage:.2f}%",
        f"Total reachable lines for harnessed functions only: {aggregate_metrics['func_reachable_lines']}",
        f"Coverage of harnessed functions only: {overall_func_coverage:.2f}%",
        f"Number of reported errors: {aggregate_metrics['total_reported_errors']}",
        f"Functions with full coverage: {aggregate_metrics['functions_with_full_coverage']} of {len(proof_metrics)}",
        f"Functions without errors: {aggregate_metrics['functions_without_errors']} of {len(proof_metrics)}",
        "",
        "### Note on Error Reporting:",
        "- Errors are grouped by line number (one error per line)",
        "- Errors about missing function bodies are excluded",
        "- Loop unwinding assertions are excluded from error count",
    ])
    
    # Add performance metrics
    header.extend([
        "",
        "## Performance Metrics",
        f"Average harness generation time: {avg_generation_time:.2f} seconds",
        f"Average verification time: {avg_verification_time:.2f} seconds",
        f"Average evaluation time: {avg_evaluation_time:.2f} seconds",
        "",
        "## Summary of Results"
    ])
    
    # Add results for each function
    for func_name in state.get("vulnerable_functions", []):
        if func_name in state.get("cbmc_results", {}):
            result = state.get("cbmc_results", {})[func_name]
            refinements = state.get("refinement_attempts", {}).get(func_name, 0)
            
            # Extract original function name and file if in directory mode
            display_name = func_name
            file_info = ""
            if ":" in func_name and is_directory_mode:
                file_name, orig_name = func_name.split(":", 1)
                display_name = orig_name
                file_info = f" (File: {file_name})"
            
            header.append(f"\n### Function: {display_name}{file_info}")
            header.append(f"Status: {result['status']}")
            header.append(f"Refinements: {refinements}")
            header.append(f"Message: {result['message']}")
            if result.get("suggestions"):
                header.append(f"Suggestions: {result['suggestions']}")
            
            # Add proof metrics for this function
            if func_name in proof_metrics:
                metrics = proof_metrics[func_name]
                header.append(f"\n#### Unit Proof Metrics")
                
                if "timeout" in metrics or "system_error" in metrics:
                    status = "timeout" if "timeout" in metrics else "system error"
                    header.append(f"- Total reachable lines: N/A ({status})")
                    header.append(f"- Total coverage: N/A ({status})")
                    header.append(f"- Function reachable lines: N/A ({status})")
                    header.append(f"- Function coverage: N/A ({status})")
                    header.append(f"- Reported errors: N/A ({status})")
                else:
                    header.append(f"- Total reachable lines: {metrics.get('total_reachable_lines', 'N/A')}")
                    header.append(f"- Total coverage: {metrics.get('total_coverage', 0):.2f}%")
                    header.append(f"- Function reachable lines: {metrics.get('func_reachable_lines', 'N/A')}")
                    header.append(f"- Function coverage: {metrics.get('func_coverage', 0):.2f}%")
                    header.append(f"- Reported errors: {metrics.get('reported_errors', 0)}")
                
                # Add error details if any
                if metrics.get('reported_errors', 0) > 0 and metrics.get('error_lines'):
                    header.append(f"\n#### Error Details")
                    for file_name, line_nums in metrics.get('error_lines', {}).items():
                        header.append(f"- File: {file_name}")
                        header.append(f"  - Error lines: {', '.join(map(str, sorted(line_nums)))}")
            
            # Add harness evolution information
            harness_history = state.get("harness_history", {}).get(func_name, [])
            if harness_history:
                header.append(f"\n#### Harness Evolution:")
                for i, _ in enumerate(harness_history):
                    header.append(f"  - Version {i+1}: {os.path.join(harnesses_dir, func_name, f'v{i+1}.c')}")
                
                # Add improvement metrics if there were multiple versions
                if len(harness_history) > 1:
                    # Compare first and last version
                    first_version = harness_history[0]
                    last_version = harness_history[-1]
                    
                    # Basic line count comparison
                    first_lines = len(first_version.split('\n'))
                    last_lines = len(last_version.split('\n'))
                    line_diff = last_lines - first_lines
                    
                    header.append(f"  - Size evolution: Initial {first_lines} lines → Final {last_lines} lines ({'+' if line_diff > 0 else ''}{line_diff} lines)")
                    
                    # Check if final version addressed verification issues
                    if result['status'] == 'SUCCESS':
                        header.append(f"  - Refinement result: Successfully addressed all verification issues")
                    else:
                        header.append(f"  - Refinement result: Some issues remain after {refinements} refinements")
            
            # List all verification reports with updated paths
            header.append(f"\n#### Verification Reports: ")
            for i in range(1, refinements + 2):  # +2 because initial version is 1, and we need to go one past the refinement count
                header.append(f"  - {os.path.join(verification_dir, func_name, f'v{i}_results.txt')}")
                header.append(f"  - {os.path.join(verification_dir, func_name, f'v{i}_report.md')}")
    
    final_summary = "\n".join(header)
    
    # Create the report file
    os.makedirs(reports_dir, exist_ok=True)
    
    # Save final report
    final_report_path = os.path.join(reports_dir, "final_report.md")
    with open(final_report_path, "w") as f:
        f.write(final_summary)
        f.flush()
        os.fsync(f.fileno())
    
    # Generate an HTML version of the report
    try:
        # Try to generate HTML report if markdown is available
        import markdown
        html_report_path = os.path.join(reports_dir, "final_report.html")
        with open(html_report_path, "w") as f:
            f.write("<html><head><title>CBMC Verification Report</title>")
            f.write("<style>body{font-family:Arial,sans-serif;line-height:1.6;max-width:900px;margin:0 auto;padding:20px}h1{color:#2c3e50}h2{color:#3498db}h3{color:#2980b9}pre{background:#f8f8f8;border:1px solid #ddd;padding:10px;overflow:auto;border-radius:3px}table{border-collapse:collapse;width:100%}table,th,td{border:1px solid #ddd;padding:8px}th{background-color:#f2f2f2}tr:nth-child(even){background-color:#f9f9f9}</style>")
            f.write("</head><body>")
            f.write(markdown.markdown(final_summary))
            f.write("</body></html>")
    except ImportError:
        # If markdown is not available, create a simple HTML version
        html_report_path = os.path.join(reports_dir, "final_report.html")
        with open(html_report_path, "w") as f:
            f.write("<html><head><title>CBMC Verification Report</title></head><body>")
            f.write("<pre>" + final_summary + "</pre>")
            f.write("</body></html>")
    
    # Generate index.html that links to all reports
    index_path = os.path.join(reports_dir, "index.html")
    with open(index_path, "w") as f:
        f.write("<html><head><title>CBMC Verification Index</title>")
        f.write("<style>body{font-family:Arial,sans-serif;line-height:1.6;max-width:900px;margin:0 auto;padding:20px}h1{color:#2c3e50}h2{color:#3498db}h3{color:#2980b9}table{border-collapse:collapse;width:100%}table,th,td{border:1px solid #ddd;padding:8px}th{background-color:#f2f2f2}tr:nth-child(even){background-color:#f9f9f9}a{color:#3498db;text-decoration:none}a:hover{text-decoration:underline}</style>")
        f.write("</head><body>")
        f.write("<h1>CBMC Verification Reports</h1>")
        f.write("<p>This index provides links to all verification reports generated.</p>")
        f.write(f"<p><strong>LLM Model Used:</strong> {llm_used.capitalize()}</p>")
        
        # Link to final report
        f.write("<h2>Final Summary Report</h2>")
        f.write(f"<p><a href='final_report.html'>View Complete Summary Report</a></p>")
        
        # Add proof metrics summary table
        f.write("<h2>Unit Proof Metrics Summary</h2>")
        f.write("<table>")
        f.write("<tr><th>Metric</th><th>Value</th></tr>")
        f.write(f"<tr><td>Total reachable lines</td><td>{aggregate_metrics['total_reachable_lines']}</td></tr>")
        f.write(f"<tr><td>Total coverage</td><td>{overall_total_coverage:.2f}%</td></tr>")
        f.write(f"<tr><td>Harnessed functions reachable lines</td><td>{aggregate_metrics['func_reachable_lines']}</td></tr>")
        f.write(f"<tr><td>Harnessed functions coverage</td><td>{overall_func_coverage:.2f}%</td></tr>")
        f.write(f"<tr><td>Total reported errors</td><td>{aggregate_metrics['total_reported_errors']}</td></tr>")
        f.write(f"<tr><td>Functions with full coverage</td><td>{aggregate_metrics['functions_with_full_coverage']} of {len(proof_metrics)}</td></tr>")
        f.write(f"<tr><td>Functions without errors</td><td>{aggregate_metrics['functions_without_errors']} of {len(proof_metrics)}</td></tr>")
        f.write("</table>")
        
        # Table of function reports
        f.write("<h2>Function Reports</h2>")
        f.write("<table>")
        f.write("<tr><th>Function</th><th>File</th><th>Status</th><th>Coverage</th><th>Errors</th><th>Versions</th><th>Reports</th></tr>")
        
        for func_name in state.get("vulnerable_functions", []):
            if func_name in state.get("cbmc_results", {}):
                result = state.get("cbmc_results", {})[func_name]
                refinements = state.get("refinement_attempts", {}).get(func_name, 0)
                
                # Extract original function name and file if in directory mode
                display_name = func_name
                file_name = ""
                if ":" in func_name:
                    file_name, display_name = func_name.split(":", 1)
                
                # Determine status color
                status_style = ""
                if result['status'] == "SUCCESS":
                    status_style = "style='color:green;font-weight:bold'"
                elif result['status'] == "FAILED":
                    status_style = "style='color:red;font-weight:bold'"
                elif result['status'] == "TIMEOUT":
                    status_style = "style='color:orange;font-weight:bold'"
                else:
                    status_style = "style='color:gray;font-weight:bold'"
                
                # Get version count
                version_count = len(state.get("harness_history", {}).get(func_name, [])) or refinements + 1
                
                # Get function metrics
                metrics = proof_metrics.get(func_name, {})
                func_coverage = metrics.get("func_coverage", 0)
                reported_errors = metrics.get("reported_errors", 0)
                
                # Determine coverage color
                coverage_style = ""
                if func_coverage >= 90:
                    coverage_style = "style='color:green;font-weight:bold'"
                elif func_coverage >= 70:
                    coverage_style = "style='color:orange;font-weight:bold'"
                elif func_coverage > 0:
                    coverage_style = "style='color:red;font-weight:bold'"
                else:
                    coverage_style = "style='color:gray;font-weight:bold'"
                
                # Determine error color
                error_style = ""
                if reported_errors == 0:
                    error_style = "style='color:green;font-weight:bold'"
                else:
                    error_style = "style='color:red;font-weight:bold'"
                
                # Get coverage and error display values
                coverage_display = f"{func_coverage:.2f}%" if "timeout" not in metrics and "system_error" not in metrics else "N/A"
                errors_display = str(reported_errors) if "timeout" not in metrics and "system_error" not in metrics else "N/A"
                
                f.write(f"<tr><td>{display_name}</td><td>{file_name}</td><td {status_style}>{result['status']}</td>")
                f.write(f"<td {coverage_style}>{coverage_display}</td>")
                f.write(f"<td {error_style}>{errors_display}</td>")
                
                # Add links to all harness versions
                f.write("<td>")
                for i in range(1, version_count + 1):
                    harness_path = os.path.join(harnesses_dir, func_name, f"v{i}.c")
                    relative_path = os.path.relpath(harness_path, reports_dir)
                    f.write(f"<a href='../{relative_path}'>v{i}</a> ")
                f.write("</td>")
                
                # Add links to all version reports
                f.write("<td>")
                for i in range(1, refinements + 2):
                    report_path = os.path.join(verification_dir, func_name, f"v{i}_report.md")
                    relative_path = os.path.relpath(report_path, reports_dir)
                    f.write(f"<a href='../{relative_path}'>v{i}</a> ")
                f.write("</td></tr>")
        
        f.write("</table>")
        
        # Add evolution section if any functions have multiple versions
        evolution_data = [func for func in state.get("vulnerable_functions", []) 
                         if len(state.get("harness_history", {}).get(func, [])) > 1]
        
        if evolution_data:
            f.write("<h2>Harness Evolution</h2>")
            f.write("<p>The following functions underwent multiple iterations of refinement:</p>")
            
            f.write("<table>")
            f.write("<tr><th>Function</th><th>Versions</th><th>Final Status</th><th>Line Count Evolution</th><th>Coverage Evolution</th></tr>")
            
            for func_name in evolution_data:
                history = state.get("harness_history", {}).get(func_name, [])
                versions = len(history)
                status = state.get("cbmc_results", {}).get(func_name, {}).get("status", "UNKNOWN")
                
                # Calculate line count evolution
                if len(history) > 1:
                    first_lines = len(history[0].split('\n'))
                    last_lines = len(history[-1].split('\n'))
                    line_diff = last_lines - first_lines
                    line_evolution = f"{first_lines} → {last_lines} ({'+' if line_diff > 0 else ''}{line_diff})"
                else:
                    line_evolution = "N/A"
                
                # Determine status color
                status_style = ""
                if status == "SUCCESS":
                    status_style = "style='color:green;font-weight:bold'"
                elif status == "FAILED":
                    status_style = "style='color:red;font-weight:bold'"
                elif status == "TIMEOUT":
                    status_style = "style='color:orange;font-weight:bold'"
                else:
                    status_style = "style='color:gray;font-weight:bold'"
                
                # Extract display name
                display_name = func_name
                if ":" in func_name:
                    _, display_name = func_name.split(":", 1)
                
                # Coverage evolution - only available if we have it
                coverage_evolution = "N/A"
                metrics = proof_metrics.get(func_name, {})
                if "timeout" not in metrics and "system_error" not in metrics and metrics.get("func_coverage") is not None:
                    coverage_evolution = f"{metrics.get('func_coverage', 0):.2f}%"
                
                f.write(f"<tr><td>{display_name}</td><td>{versions}</td>")
                f.write(f"<td {status_style}>{status}</td><td>{line_evolution}</td><td>{coverage_evolution}</td></tr>")
            
            f.write("</table>")
        
        f.write("</body></html>")
    
    # Calculate relative path for displaying in message
    result_path = os.path.relpath(result_base_dir)
    
    return {
        "messages": [AIMessage(content=f"Analysis complete! Reports generated in '{result_path}'. Main index at {os.path.join(result_path, 'reports', 'index.html')}")]
    }