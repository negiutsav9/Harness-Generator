"""
Output node for CBMC harness generator workflow with unified RAG database integration.
"""
import os
import time
import subprocess
import json
import glob
import re
from langchain_core.messages import AIMessage
import logging
import polars as pl
from typing import Dict, List, Any, Optional
from utils.rag import get_unified_db

logger = logging.getLogger("output")

def extract_coverage_metrics_from_json(json_data: Dict, func_name: str) -> Dict[str, Any]:
    """
    Extract coverage metrics from CBMC JSON output using the enhanced JSON structure.
    
    Args:
        json_data: The JSON data from CBMC output
        func_name: Name of the function being analyzed
        
    Returns:
        Dictionary with coverage metrics
    """
    # Initialize metrics
    metrics = {
        "total_reachable_lines": 0,
        "total_covered_lines": 0,
        "total_coverage_pct": 0.0,
        "func_reachable_lines": 0,
        "func_covered_lines": 0,
        "func_coverage_pct": 0.0,
        "reported_errors": 0,
        "failure_count": 0,
        "error_count": 0,
        "error_categories": []
    }
    
    # Extract target function name without file prefix
    target_function = func_name
    if ":" in func_name:
        target_function = func_name.split(":")[-1]
    
    try:
        # First try to parse the structured coverage goals
        if "goals" in json_data and isinstance(json_data["goals"], list):
            total_goals = 0
            satisfied_goals = 0
            func_goals = 0
            func_satisfied = 0
            
            for goal in json_data["goals"]:
                # Check if this is a coverage goal (might be in "goal" or "description" field)
                is_coverage_goal = False
                if "goal" in goal and isinstance(goal["goal"], str):
                    is_coverage_goal = "coverage" in goal["goal"]
                elif "description" in goal and isinstance(goal["description"], str):
                    is_coverage_goal = "coverage" in goal["description"] or "block" in goal["description"]
                
                if not is_coverage_goal:
                    continue
                
                # Count as a total goal
                total_goals += 1
                
                # Check if satisfied
                is_satisfied = False
                if "status" in goal:
                    is_satisfied = goal["status"] == "satisfied"
                
                if is_satisfied:
                    satisfied_goals += 1
                
                # Check if related to target function
                is_target = False
                
                # Method 1: Check sourceLocation
                if "sourceLocation" in goal and isinstance(goal["sourceLocation"], dict):
                    if "function" in goal["sourceLocation"]:
                        is_target = goal["sourceLocation"]["function"] == target_function
                
                # Method 2: Check description
                if not is_target and "description" in goal and isinstance(goal["description"], str):
                    is_target = target_function in goal["description"]
                    
                # Method 3: Check basicBlockLines
                if not is_target and "basicBlockLines" in goal and isinstance(goal["basicBlockLines"], dict):
                    for file, functions in goal["basicBlockLines"].items():
                        if target_function in functions:
                            is_target = True
                            break
                
                if is_target:
                    func_goals += 1
                    if is_satisfied:
                        func_satisfied += 1
            
            # Update metrics with the counts we found
            metrics["total_reachable_lines"] = total_goals
            metrics["total_covered_lines"] = satisfied_goals
            
            # Calculate percentages
            if total_goals > 0:
                metrics["total_coverage_pct"] = (satisfied_goals / total_goals) * 100
                
            if func_goals > 0:
                metrics["func_reachable_lines"] = func_goals
                metrics["func_covered_lines"] = func_satisfied
                metrics["func_coverage_pct"] = (func_satisfied / func_goals) * 100
            
        # If we didn't find any goals, try a simplified approach that looks at the raw JSON
        elif len(json_data) > 0:
            # Count blocks based on the presence of patterns in the string representation
            json_str = json.dumps(json_data)
            
            # Count total blocks
            total_blocks = json_str.count('"block"') + json_str.count('"coverage"')
            satisfied_blocks = json_str.count('"status":"satisfied"') + json_str.count('status="satisfied"')
            
            # Count function-specific blocks
            target_pattern = f'"{target_function}"'
            func_blocks = json_str.count(target_pattern)
            func_satisfied = 0
            
            # Estimate satisfaction rate for function blocks based on overall rate
            if total_blocks > 0 and func_blocks > 0:
                func_satisfied = int(func_blocks * (satisfied_blocks / total_blocks))
            
            metrics["total_reachable_lines"] = max(total_blocks, 1)  # Avoid division by zero
            metrics["total_covered_lines"] = satisfied_blocks
            metrics["func_reachable_lines"] = max(func_blocks, 1)  # Avoid division by zero
            metrics["func_covered_lines"] = func_satisfied
            
            # Calculate percentages
            metrics["total_coverage_pct"] = (satisfied_blocks / metrics["total_reachable_lines"]) * 100
            metrics["func_coverage_pct"] = (func_satisfied / metrics["func_reachable_lines"]) * 100
        
        # Extract error information
        errors = 0
        error_categories = []
        
        # Look for errors in messages
        if "messages" in json_data and isinstance(json_data["messages"], list):
            for message in json_data["messages"]:
                if isinstance(message, dict) and "messageType" in message:
                    if message["messageType"] == "ERROR":
                        errors += 1
                        # Try to categorize the error
                        if "messageText" in message:
                            error_text = message["messageText"].lower()
                            if "memory" in error_text and "memory_leak" not in error_categories:
                                error_categories.append("memory_leak")
                            elif "pointer" in error_text and "null_pointer" not in error_categories:
                                error_categories.append("null_pointer")
                            elif ("bounds" in error_text or "array" in error_text) and "array_bounds" not in error_categories:
                                error_categories.append("array_bounds")
                            elif ("division" in error_text or "zero" in error_text) and "division_by_zero" not in error_categories:
                                error_categories.append("division_by_zero")
                            elif "overflow" in error_text and "arithmetic_overflow" not in error_categories:
                                error_categories.append("arithmetic_overflow")
                            elif "generic_error" not in error_categories:
                                error_categories.append("generic_error")
        
        # Alternative way to find errors - look for failed verification
        if "verification-results" in json_data:
            for result in json_data["verification-results"]:
                if result.get("status") == "FAILURE":
                    errors += 1
                    if "property" in result:
                        prop = result["property"].lower()
                        if "memory" in prop and "memory_leak" not in error_categories:
                            error_categories.append("memory_leak")
                        elif "pointer" in prop and "null_pointer" not in error_categories:
                            error_categories.append("null_pointer")
                        elif "bound" in prop and "array_bounds" not in error_categories:
                            error_categories.append("array_bounds")
                        elif "division" in prop and "division_by_zero" not in error_categories:
                            error_categories.append("division_by_zero")
                        elif "overflow" in prop and "arithmetic_overflow" not in error_categories:
                            error_categories.append("arithmetic_overflow")
                        elif "generic_error" not in error_categories:
                            error_categories.append("generic_error")
        
        # Check for errors in the raw JSON string regardless of other detection methods
        json_str = json.dumps(json_data)
        failure_count = json_str.count('"FAILURE"') + json_str.count('"status":"failed"')
        error_count = json_str.count('"ERROR"') + json_str.count('"messageType":"ERROR"')
        
        # Look for stderr-based errors as well
        stderr_error_count = 0
        if "stderr" in json_data and isinstance(json_data["stderr"], str):
            stderr_error_count = json_data["stderr"].lower().count("error:")
            
        # If we have any kind of error, make sure it's captured
        if failure_count > 0 or error_count > 0 or stderr_error_count > 0:
            # Use the highest count as the reported error value
            errors = max(failure_count, error_count, stderr_error_count, errors)
            
            # Make sure we have at least one error category
            if not error_categories:
                error_categories.append("generic_error")
                
            logger.info(f"Error detection: failures={failure_count}, errors={error_count}, stderr_errors={stderr_error_count}")
        
        # Set all error metrics
        metrics["reported_errors"] = errors
        metrics["failure_count"] = failure_count
        metrics["error_count"] = error_count
        metrics["error_categories"] = error_categories  # Already a list from our previous fix
        
        # Add logging for traceability
        logger.info(f"Coverage metrics extraction - Coverage: {metrics.get('func_coverage_pct', 0.0):.2f}%, "
                   f"Error counts: reported={errors}, failures={failure_count}, total={error_count}")
        logger.info(f"Error categories: {error_categories}")
    
    except Exception as e:
        logger.error(f"Error extracting coverage metrics from JSON: {str(e)}")
    
    # If we got 0% coverage but didn't encounter errors in parsing,
    # set a reasonable minimum value to indicate some coverage
    if metrics["total_coverage_pct"] == 0.0 and metrics["reported_errors"] == 0:
        # First check if there's any evidence of coverage in the JSON
        json_str = json.dumps(json_data)
        if "coverage" in json_str or "block" in json_str:
            # Estimate minimum coverage
            metrics["total_reachable_lines"] = "NA"
            metrics["total_covered_lines"] = "NA"
            metrics["total_coverage_pct"] = "NA"
            metrics["func_reachable_lines"] = "NA"
            metrics["func_covered_lines"] = "NA"
            metrics["func_coverage_pct"] = "NA"
    
    return metrics

def run_cbmc_coverage_combined(
    function_names: List[str],
    harness_files: List[str],
    version_num: int,
    verification_dir: str,
    coverage_dir: str
) -> Dict[str, Dict[str, Any]]:
    """
    Run CBMC with coverage analysis for a specific version across all functions.
    
    Args:
        function_names: List of function names
        harness_files: List of harness files
        version_num: Version number
        verification_dir: Directory for verification files
        coverage_dir: Directory for coverage output
        
    Returns:
        Dictionary mapping function names to their coverage metrics
    """
    # Create version-specific directory
    version_coverage_dir = os.path.join(coverage_dir, f"version_{version_num}")
    os.makedirs(version_coverage_dir, exist_ok=True)
    
    # Find include directory
    verification_include_dir = os.path.join(verification_dir, "includes")
    
    # Create CBMC command with coverage options
    cbmc_cmd = [
        "cbmc",
        "--function", "main",  # Use main as entry point
        "--object-bits", "8",
        "--cover", "location",  # Generate location coverage
        "--json-ui"            # Use JSON output format
    ]
    
    # Add all harness files
    cbmc_cmd.extend(harness_files)
    
    # Add all C files from verification/includes directory
    c_files_in_includes = glob.glob(os.path.join(verification_include_dir, "*.c"))
    cbmc_cmd.extend(c_files_in_includes)
    
    # Add necessary include paths
    include_paths = [verification_include_dir]
    for path in include_paths:
        if os.path.exists(path):
            cbmc_cmd.extend(["-I", path])
    
    # Output files
    coverage_json_file = os.path.join(version_coverage_dir, f"v{version_num}_coverage.json")
    cmd_file = os.path.join(version_coverage_dir, f"v{version_num}_cmd.txt")
    
    # Save command for debugging
    with open(cmd_file, "w") as f:
        f.write(" ".join(cbmc_cmd))
    
    try:
        # Run CBMC with coverage analysis
        logger.info(f"Running CBMC coverage analysis for version {version_num} with {len(harness_files)} harness files")
        process = subprocess.run(
            cbmc_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=120,  # Longer timeout for combined analysis
            check=False
        )
        
        # Save stdout to JSON file
        with open(coverage_json_file, "w") as f:
            f.write(process.stdout)
        
        # Check if we got valid JSON
        try:
            json_data = json.loads(process.stdout)
            
            # Extract metrics for each function
            results = {}
            for func_name in function_names:
                # Extract function-specific metrics
                func_metrics = extract_coverage_metrics_from_json(json_data, func_name)
                results[func_name] = func_metrics
            
            return results
            
        except json.JSONDecodeError:
            logger.error(f"Failed to parse JSON output for version {version_num}")
            # Save stderr for debugging
            with open(os.path.join(version_coverage_dir, f"v{version_num}_error.txt"), "w") as f:
                f.write(process.stderr)
            return None
            
    except subprocess.TimeoutExpired:
        logger.warning(f"CBMC coverage analysis timed out for version {version_num}")
        return None
    except Exception as e:
        logger.error(f"Error running CBMC coverage analysis: {str(e)}")
        return None

def analyze_coverage_by_version(
    results_dir: str, 
    harnesses_dir: str, 
    verification_dir: str
) -> pl.DataFrame:
    """
    Run coverage analysis on all functions with harnesses, grouping by version.
    
    Args:
        results_dir: Base results directory
        harnesses_dir: Harnesses directory
        verification_dir: Verification directory
        
    Returns:
        Polars DataFrame with coverage metrics
    """
    # Check if the harnesses directory exists and has content
    if not os.path.exists(harnesses_dir):
        logger.error(f"Harnesses directory {harnesses_dir} does not exist")
        return pl.DataFrame()
    
    # Create output directory for coverage data
    coverage_dir = os.path.join(results_dir, "coverage")
    os.makedirs(coverage_dir, exist_ok=True)
    
    # Find all functions with harnesses
    function_dirs = glob.glob(os.path.join(harnesses_dir, "*"))
    
    if not function_dirs:
        logger.error("No harness functions found. Cannot run coverage analysis.")
        return pl.DataFrame()
    
    # Determine all available versions
    all_versions = set()
    
    for func_dir in function_dirs:
        harness_files = glob.glob(os.path.join(func_dir, "v*.c"))
        for harness_file in harness_files:
            version_match = re.search(r'v(\d+)\.c$', harness_file)
            if version_match:
                all_versions.add(int(version_match.group(1)))
    
    if not all_versions:
        logger.error("No harness versions found")
        return pl.DataFrame()
    
    # Sort versions
    all_versions = sorted(all_versions)
    logger.info(f"Found {len(all_versions)} harness versions: {all_versions}")
    
    # Prepare data for DataFrame
    coverage_data = []
    
    # Process each version with all harnesses of that version
    for version_num in all_versions:
        logger.info(f"Processing harness version {version_num}")
        
        # Collect all harness files for this version
        version_harness_files = []
        function_names = []
        
        for func_dir in function_dirs:
            func_name = os.path.basename(func_dir)
            harness_file = os.path.join(func_dir, f"v{version_num}.c")
            
            # If this version doesn't exist, use the latest available version for this function
            if not os.path.exists(harness_file):
                available_versions = sorted([
                    int(re.search(r'v(\d+)\.c$', f).group(1)) 
                    for f in glob.glob(os.path.join(func_dir, "v*.c"))
                ])
                
                if available_versions:
                    # Find the closest lower version
                    closest_version = None
                    for v in available_versions:
                        if v <= version_num:
                            closest_version = v
                            
                    if closest_version is not None:
                        harness_file = os.path.join(func_dir, f"v{closest_version}.c")
                        logger.info(f"Using v{closest_version} for {func_name} (requested v{version_num})")
                    else:
                        # If no lower version, use the lowest available
                        lowest_version = available_versions[0]
                        harness_file = os.path.join(func_dir, f"v{lowest_version}.c")
                        logger.info(f"Using v{lowest_version} for {func_name} (requested v{version_num})")
                else:
                    logger.warning(f"No harness versions found for {func_name}")
                    continue
            
            if os.path.exists(harness_file):
                version_harness_files.append(harness_file)
                function_names.append(func_name)
        
        if not version_harness_files:
            logger.warning(f"No harness files found for version {version_num}")
            continue
        
        # Run the coverage analysis for this version
        version_coverage_metrics = run_cbmc_coverage_combined(
            function_names,
            version_harness_files,
            version_num,
            verification_dir,
            coverage_dir
        )
        
        # Process results for each function
        for func_name in function_names:
            if version_coverage_metrics and func_name in version_coverage_metrics:
                metrics = version_coverage_metrics[func_name]
                
                coverage_data.append({
                    "function": func_name,
                    "version": version_num,
                    "total_reachable_lines": metrics["total_reachable_lines"],
                    "total_covered_lines": metrics["total_covered_lines"],
                    "total_coverage_pct": metrics["total_coverage_pct"],
                    "func_reachable_lines": metrics["func_reachable_lines"],
                    "func_covered_lines": metrics["func_covered_lines"],
                    "func_coverage_pct": metrics["func_coverage_pct"],
                    "reported_errors": metrics["reported_errors"],
                    "failure_count": metrics["failure_count"],
                    "error_count": metrics["error_count"],
                    "error_categories": str(metrics["error_categories"])
                })
    
    # Create Polars DataFrame
    if coverage_data:
        df = pl.DataFrame(coverage_data)
        
        # Sort by function and version
        df = df.sort(["function", "version"])
        
        # Create coverage directory for storing the JSON data
        data_dir = os.path.join(coverage_dir, "data")
        os.makedirs(data_dir, exist_ok=True)
        
        # Save individual JSON files for each function/version combination
        for i, row in enumerate(df.iter_rows(named=True)):
            func_name = row["function"]
            version = row["version"]
            
            # Create a flattened data structure for JSON
            json_data = {
                "function": func_name,
                "version": version,
                "total_coverage_pct": row["total_coverage_pct"],
                "func_coverage_pct": row["func_coverage_pct"],
                "total_reachable_lines": row["total_reachable_lines"],
                "total_covered_lines": row["total_covered_lines"],
                "func_reachable_lines": row["func_reachable_lines"],
                "func_covered_lines": row["func_covered_lines"],
                "reported_errors": row["reported_errors"],
                "failure_count": row["failure_count"],
                "error_count": row["error_count"]
            }
            
            # Save as JSON
            json_file = os.path.join(data_dir, f"{func_name}_v{version}.json")
            with open(json_file, "w") as f:
                json.dump(json_data, f, indent=2)
        
        return df
    else:
        logger.warning("No coverage data collected")
        return pl.DataFrame()

def generate_coverage_report(coverage_df: pl.DataFrame, coverage_dir: str):
    """
    Generate a simplified coverage report with table derived from JSON data only.
    
    Args:
        coverage_df: Coverage DataFrame
        coverage_dir: Directory to save the report
    """
    # Create output directory if it doesn't exist
    os.makedirs(coverage_dir, exist_ok=True)
    
    # Initialize variables for the case when no JSON files are found
    all_json_functions = []
    all_json_versions = []
    # Generate HTML report
    try:
        html_report = f"""
        <html>
        <head>
            <title>CBMC Coverage Analysis Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1, h2 {{ color: #2c3e50; }}
                table {{ border-collapse: collapse; width: 100%; margin-bottom: 20px; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: center; }}
                th {{ background-color: #f2f2f2; }}
                tr:nth-child(even) {{ background-color: #f9f9f9; }}
                .function-name {{ text-align: left; font-weight: bold; }}
                .good {{ color: green; }}
                .medium {{ color: orange; }}
                .poor {{ color: red; }}
                .version-header {{ 
                    background-color: #d5d5d5; 
                    font-weight: bold; 
                    text-align: center;
                }}
                .subheader {{
                    background-color: #e8e8e8;
                    font-weight: normal;
                }}
            </style>
        </head>
        <body>
            <h1>CBMC Coverage Analysis Report</h1>
        """
            
        # Only add function coverage matrix from JSON files in the data directory
        data_dir = os.path.join(coverage_dir, "data")
        if os.path.exists(data_dir):
            json_files = glob.glob(os.path.join(data_dir, "*.json"))
            if json_files:
                logger.info(f"Adding coverage matrix from {len(json_files)} JSON files in data directory")
                
                # Create a mapping of function and version to metrics
                json_coverage_data = {}
                
                for json_file in json_files:
                    try:
                        with open(json_file, 'r') as f:
                            data = json.load(f)
                            function = data.get("function")
                            version = data.get("version")
                            
                            if function and version is not None:
                                if function not in json_coverage_data:
                                    json_coverage_data[function] = {}
                                json_coverage_data[function][version] = data
                    except Exception as e:
                        logger.error(f"Error reading JSON file {json_file}: {str(e)}")
                
                if json_coverage_data:
                    # Add a section for the matrix from JSON data only
                    all_json_functions = sorted(json_coverage_data.keys())
                    all_json_versions = sorted(set(v for func_data in json_coverage_data.values() for v in func_data.keys()))
                    
                    # Count functions with errors for better tracking
                    funcs_with_errors = 0
                    for func_name, versions in json_coverage_data.items():
                        latest_version = max(versions.keys())
                        error_val = 0
                        if "reported_errors" in versions[latest_version]:
                            try:
                                if isinstance(versions[latest_version]["reported_errors"], (int, float)):
                                    error_val = int(versions[latest_version]["reported_errors"])
                                elif isinstance(versions[latest_version]["reported_errors"], str) and versions[latest_version]["reported_errors"] != "NA":
                                    error_val = int(float(versions[latest_version]["reported_errors"]))
                            except (ValueError, TypeError):
                                pass
                        
                        if error_val > 0:
                            funcs_with_errors += 1
                    
                    # Add a summary line for total functions with enhanced error tracking
                    html_report += f"""
                        <p>Total Functions Analyzed: {len(all_json_functions)}</p>
                        <p>Total Versions: {len(all_json_versions)}</p>
                        <p>Functions with Errors: {funcs_with_errors} ({(funcs_with_errors/len(all_json_functions)*100 if all_json_functions else 0):.1f}%)</p>
                    """
                    
                    html_report += """
                        <h2>Coverage Matrix from JSON Data</h2>
                        <p>This table shows coverage metrics extracted directly from JSON data files:</p>
                        <table>
                            <tr>
                                <th rowspan="2">Function</th>
                    """
                    
                    # Add version column headers
                    for version in all_json_versions:
                        html_report += f'<th colspan="3" class="version-header">Version {version}</th>'
                    
                    # Add sub-headers for total and func coverage
                    html_report += "</tr><tr>"
                    for _ in all_json_versions:
                        html_report += '<th class="subheader">Total %</th>'
                        html_report += '<th class="subheader">Func %</th>'
                        html_report += '<th class="subheader">Errors</th>'
                    html_report += "</tr>"
                    
                    # Add data rows
                    for func_name in all_json_functions:
                        html_report += f'<tr><td class="function-name">{func_name}</td>'
                        
                        for version in all_json_versions:
                            data = json_coverage_data.get(func_name, {}).get(version)
                            
                            if data:
                                # Ensure values are numeric
                                try:
                                    total_cov_val = data.get("total_coverage_pct", 0)
                                    func_cov_val = data.get("func_coverage_pct", 0)
                                    
                                    # Get error counts from different possible fields
                                    reported_errors = data.get("reported_errors", 0)
                                    failure_count = data.get("failure_count", 0)
                                    error_count = data.get("error_count", 0)
                                    
                                    # Handle string values for all error counts
                                    if isinstance(reported_errors, str) and reported_errors != "NA":
                                        try:
                                            reported_errors = int(float(reported_errors))
                                        except (ValueError, TypeError):
                                            reported_errors = 0
                                            
                                    if isinstance(failure_count, str) and failure_count != "NA":
                                        try:
                                            failure_count = int(float(failure_count))
                                        except (ValueError, TypeError):
                                            failure_count = 0
                                            
                                    if isinstance(error_count, str) and error_count != "NA":
                                        try:
                                            error_count = int(float(error_count))
                                        except (ValueError, TypeError):
                                            error_count = 0
                                    
                                    # Use the highest non-zero value for display
                                    error_value = max(reported_errors, failure_count, error_count)
                                    
                                    # Check if values are "NA" or strings
                                    if total_cov_val == "NA" or not isinstance(total_cov_val, (int, float)):
                                        total_cov = 0
                                        html_report += f'<td>N/A</td>'
                                    else:
                                        total_cov = float(total_cov_val)
                                        # Determine color class
                                        total_class = "good" if total_cov >= 80 else "medium" if total_cov >= 50 else "poor"
                                        html_report += f'<td class="{total_class}">{total_cov:.2f}%</td>'
                                        
                                    if func_cov_val == "NA" or not isinstance(func_cov_val, (int, float)):
                                        func_cov = 0
                                        html_report += f'<td>N/A</td>'
                                    else:
                                        func_cov = float(func_cov_val)
                                        # Determine color class
                                        func_class = "good" if func_cov >= 80 else "medium" if func_cov >= 50 else "poor"
                                        html_report += f'<td class="{func_class}">{func_cov:.2f}%</td>'
                                    
                                    # Check if there are any error categories to display alongside the count
                                    error_cats = []
                                    if "error_categories" in data and data["error_categories"]:
                                        try:
                                            # Handle both string and list representations
                                            if isinstance(data["error_categories"], str):
                                                if data["error_categories"].startswith("[") and data["error_categories"].endswith("]"):
                                                    # Try to parse as list-like string
                                                    error_cats = data["error_categories"].strip("[]").replace("'", "").split(", ")
                                                else:
                                                    error_cats = [data["error_categories"]]
                                            elif isinstance(data["error_categories"], list):
                                                error_cats = data["error_categories"]
                                        except Exception:
                                            pass
                                    
                                    # Force error value to at least 1 if we have error categories
                                    if error_cats and error_value == 0:
                                        error_value = 1
                                        logger.info(f"Force-updated error count for {func_name} v{version} - has error categories but zero count")
                                    
                                    # Display error count with color coding and tooltip showing error types
                                    error_class = "good" if error_value == 0 else "poor"
                                    error_tooltip = ' title="Errors: ' + ', '.join(error_cats) + '"' if error_cats else ''
                                    html_report += f'<td class="{error_class}"{error_tooltip}>{error_value}</td>'
                                except (ValueError, TypeError):
                                    # Handle non-numeric values
                                    html_report += f'<td>N/A</td><td>N/A</td><td>N/A</td>'
                            else:
                                html_report += '<td>-</td><td>-</td><td>-</td>'
                        
                        html_report += '</tr>'
                    
                    html_report += """
                        </table>
                    """
        
        html_report += """
        </body>
        </html>
        """
        
        # Save HTML report
        with open(os.path.join(coverage_dir, "coverage_report.html"), "w") as f:
            f.write(html_report)
            
    except Exception as e:
        logger.error(f"Error generating HTML report: {str(e)}")


def output_node(state):
    """Provides final summary and generates reports with unified RAG database integration."""
    total_time = time.time() - state.get("start_time", time.time())

    logger.info("Generating final report and output summaries")
    
    # Get result directories from state
    result_directories = state.get("result_directories", {})
    reports_dir = result_directories.get("reports_dir", "reports")
    harnesses_dir = result_directories.get("harnesses_dir", "harnesses")
    verification_dir = result_directories.get("verification_dir", "verification")
    result_base_dir = result_directories.get("result_base_dir", "results")
    
    # Get the unified RAG database
    rag_db = get_unified_db(os.path.join(result_base_dir, "rag_data"))
    
    # Get LLM model info
    llm_used = state.get("llm_used", "claude")
    
    # Determine if we're in directory mode
    is_directory_mode = state.get("is_directory_mode", False)
    
    # Get all vulnerable functions and harnesses
    vulnerable_functions = state.get("vulnerable_functions", [])
    harnesses = state.get("harnesses", {})
    cbmc_results = state.get("cbmc_results", {})
    
    # Check if all harnesses have been generated and verified
    all_harnesses_complete = True
    for func_name in vulnerable_functions:
        if func_name not in harnesses or func_name not in cbmc_results:
            all_harnesses_complete = False
            logger.warning(f"Function {func_name} does not have complete harness or verification results")
    
    # Calculate summary statistics
    function_times = state.get("function_times", {})
    total_refinements = sum(state.get("refinement_attempts", {}).values())
    
    # Instead of running coverage analysis, directly load the existing CSV file 
    # Construct the path using the LLM model and result directories
    coverage_dir = os.path.join(result_base_dir, "coverage", "data")
    coverage_file_path = os.path.join(coverage_dir, "coverage_metrics.csv")
    coverage_df = pl.DataFrame()
    
    if os.path.exists(coverage_file_path):
        logger.info(f"Loading coverage metrics from {coverage_file_path}")
        try:
            coverage_df = pl.read_csv(coverage_file_path)
            logger.info(f"Loaded coverage data with {len(coverage_df)} rows")
        except Exception as e:
            logger.error(f"Error reading coverage CSV: {str(e)}")
    else:
        logger.warning(f"Coverage metrics file not found at {coverage_file_path}")
    
    # Calculate aggregate metrics from the coverage data if loaded
    aggregate_metrics = {
        "total_reachable_lines": 0,
        "total_covered_lines": 0,
        "func_reachable_lines": 0,
        "func_covered_lines": 0,
        "total_reported_errors": 0,
        "functions_with_full_coverage": 0,
        "functions_without_errors": 0
    }
    
    if not coverage_df.is_empty():
        # Get latest version for each function
        try:
            latest_versions = coverage_df.group_by("function").agg(pl.max("version").alias("max_version"))
            latest_metrics = []
            
            for func_name, max_version in zip(latest_versions["function"], latest_versions["max_version"]):
                # Get metrics for this function and version
                metrics = coverage_df.filter(
                    (pl.col("function") == func_name) & (pl.col("version") == max_version)
                ).row(0, named=True)
                
                latest_metrics.append(metrics)
                
                # Add to aggregate totals - ensure we're handling numeric values only
                for metric_key in ["total_reachable_lines", "total_covered_lines", "func_reachable_lines", "func_covered_lines"]:
                    if metric_key in metrics:
                        metric_val = metrics[metric_key]
                        if isinstance(metric_val, (int, float)) and metric_val != "NA":
                            aggregate_metrics[metric_key] += int(metric_val)
                
                # Get all error metrics and add the highest one to the total
                reported_error_val = 0
                failure_count_val = 0
                error_count_val = 0
                
                # Process reported_errors
                if "reported_errors" in metrics:
                    error_val = metrics["reported_errors"]
                    # Try to convert string to int if needed
                    if isinstance(error_val, str) and error_val != "NA":
                        try:
                            reported_error_val = int(float(error_val))
                        except (ValueError, TypeError):
                            pass
                    elif isinstance(error_val, (int, float)) and error_val != "NA":
                        reported_error_val = int(error_val)
                
                # Process failure_count
                if "failure_count" in metrics:
                    failure_val = metrics["failure_count"]
                    if isinstance(failure_val, str) and failure_val != "NA":
                        try:
                            failure_count_val = int(float(failure_val))
                        except (ValueError, TypeError):
                            pass
                    elif isinstance(failure_val, (int, float)) and failure_val != "NA":
                        failure_count_val = int(failure_val)
                
                # Process error_count
                if "error_count" in metrics:
                    error_count = metrics["error_count"]
                    if isinstance(error_count, str) and error_count != "NA":
                        try:
                            error_count_val = int(float(error_count))
                        except (ValueError, TypeError):
                            pass
                    elif isinstance(error_count, (int, float)) and error_count != "NA":
                        error_count_val = int(error_count)
                
                # Add the highest non-zero error value to the total
                max_error_value = max(reported_error_val, failure_count_val, error_count_val)
                aggregate_metrics["total_reported_errors"] += max_error_value
                
                # Count functions with full coverage
                if "func_coverage_pct" in metrics:
                    coverage_val = metrics["func_coverage_pct"]
                    if isinstance(coverage_val, (int, float)) and coverage_val != "NA" and float(coverage_val) >= 95.0:
                        aggregate_metrics["functions_with_full_coverage"] += 1
                
                # Count functions without errors by checking all error metrics
                # Convert the values we already calculated above for reported_error_val, failure_count_val, and error_count_val
                # If all error values are 0, increment functions without errors
                if max(reported_error_val, failure_count_val, error_count_val) == 0:
                    aggregate_metrics["functions_without_errors"] += 1
        except Exception as e:
            logger.error(f"Error processing coverage data: {str(e)}")
    
    # Calculate overall coverage percentages with safety checks
    overall_total_coverage = 0.0
    if aggregate_metrics["total_reachable_lines"] > 0 and aggregate_metrics["total_covered_lines"] > 0:
        overall_total_coverage = (aggregate_metrics["total_covered_lines"] / aggregate_metrics["total_reachable_lines"]) * 100
        
    overall_func_coverage = 0.0
    if aggregate_metrics["func_reachable_lines"] > 0 and aggregate_metrics["func_covered_lines"] > 0:
        overall_func_coverage = (aggregate_metrics["func_covered_lines"] / aggregate_metrics["func_reachable_lines"]) * 100
    
    # Create performance metrics
    if function_times:
        avg_generation_time = sum(times.get("generation", 0) for times in function_times.values()) / len(function_times)
        avg_verification_time = sum(times.get("verification", 0) for times in function_times.values()) / len(function_times)
        avg_evaluation_time = sum(times.get("evaluation", 0) for times in function_times.values()) / len(function_times)
        avg_refinements = total_refinements / len(state.get("refinement_attempts", {})) if state.get("refinement_attempts", {}) else 0
    else:
        avg_generation_time = avg_verification_time = avg_evaluation_time = avg_refinements = 0
    
    # Get RAG database statistics
    try:
        rag_stats = {
            "code_functions": rag_db.code_collection.count(),
            "patterns": rag_db.pattern_collection.count(),
            "errors": rag_db.error_collection.count(),
            "solutions": rag_db.solution_collection.count()
        }
        logger.info(f"RAG database statistics: {rag_stats}")
    except Exception as e:
        logger.error(f"Error getting RAG statistics: {str(e)}")
        rag_stats = {
            "code_functions": 0,
            "patterns": 0,
            "errors": 0,
            "solutions": 0
        }
    
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
    
    # Add RAG database statistics section
    header.extend([
        "",
        "## RAG Knowledge Base Statistics",
        f"Code functions stored: {rag_stats['code_functions']}",
        f"Pattern templates: {rag_stats['patterns']}",
        f"Error patterns stored: {rag_stats['errors']}",
        f"Successful solutions: {rag_stats['solutions']}",
        "",
        "The RAG (Retrieval-Augmented Generation) knowledge base stores code functions, patterns, errors, and solutions to improve harness generation over time. Each run contributes to this knowledge base, helping future runs generate better harnesses with fewer iterations.",
    ])
    
    # Add unit proof metrics summary
    header.extend([
        "",
        "## Unit Proof Metrics Summary",
        f"Total reachable lines: {aggregate_metrics['total_reachable_lines']}",
        f"Total coverage: {overall_total_coverage:.2f}%",
        f"Total reachable lines for harnessed functions only: {aggregate_metrics['func_reachable_lines']}",
        f"Coverage of harnessed functions only: {overall_func_coverage:.2f}%",
        f"Number of reported errors: {aggregate_metrics['total_reported_errors']}",
        f"Functions with full coverage: {aggregate_metrics['functions_with_full_coverage']} of {len(state.get('cbmc_results', {}))}",
        f"Functions without errors: {aggregate_metrics['functions_without_errors']} of {len(state.get('cbmc_results', {}))}",
        "",
        "### Note on Error Reporting:",
        "- Errors are grouped by line number (one error per line)",
        "- Errors about missing function bodies are excluded",
        "- Loop unwinding assertions are excluded from error count",
    ])
    
    # Generate the enhanced coverage matrix table with more detailed metrics
    if not coverage_df.is_empty():
        # Extract functions and versions from the dataframe
        functions = sorted(list(set(coverage_df["function"].to_list())))
        versions = sorted(list(set(coverage_df["version"].to_list())))
        
        # Add table title
        header.extend([
            "",
            "## Detailed Coverage Matrix by Function and Version",
            "",
            "The table below shows detailed metrics for each function across different versions of the generated harnesses:",
            ""
        ])
        
        # Create markdown table with functions as rows and versions as columns
        # For each version, we have three sub-columns: Total Coverage, Functional Coverage, and Errors
        
        # Table header row with version columns
        # Table header row with version columns
        header_row = "| Function "
        for version in versions:
            header_row += f"| Version {version} "
        header_row += "|"
        header.append(header_row)

        # Sub-header row with Total, Func, and Errors columns for each version
        subheader_row = "| --- "
        for _ in versions:
            subheader_row += "| Total % | Func % | Errors "
        subheader_row += "|"
        header.append(subheader_row)

        # Data rows
        for function in functions:
            func_row = f"| {function} "
            for version in versions:
                # Find the record for this function and version
                try:
                    func_data = coverage_df.filter(
                        (pl.col("function") == function) & (pl.col("version") == version)
                    )
                    
                    if not func_data.is_empty():
                        record = func_data.row(0, named=True)
                        
                        # Handle both numeric and string values safely
                        total_cov_val = record.get("total_coverage_pct", "N/A")
                        func_cov_val = record.get("func_coverage_pct", "N/A")
                        errors_val = record.get("reported_errors", "N/A")
                        
                        # Also check for failure_count which might be present instead of reported_errors
                        if errors_val == "N/A" and "failure_count" in record:
                            errors_val = record.get("failure_count", "N/A")
                        # Also check for error_count which might be present instead
                        if errors_val == "N/A" and "error_count" in record:
                            errors_val = record.get("error_count", "N/A")
                        
                        # Ensure errors_val is properly converted to integer if it's a string
                        if isinstance(errors_val, str) and errors_val != "N/A":
                            try:
                                errors_val = int(float(errors_val))
                            except (ValueError, TypeError):
                                errors_val = 0
                        
                        # Format values properly
                        if isinstance(total_cov_val, (int, float)):
                            total_cov = f"{total_cov_val:.2f}%"
                        else:
                            total_cov = "N/A"
                            
                        if isinstance(func_cov_val, (int, float)):
                            func_cov = f"{func_cov_val:.2f}%"
                        else:
                            func_cov = "N/A"
                            
                        if isinstance(errors_val, (int, float)):
                            errors = str(errors_val)
                        else:
                            errors = "0"  # Default to 0 instead of N/A for errors
                            
                        func_row += f"| {total_cov} | {func_cov} | {errors} "
                    else:
                        func_row += "| - | - | - "
                except Exception as e:
                    logger.error(f"Error formatting coverage data: {str(e)}")
                    func_row += "| - | - | - "
            
            func_row += "|"
            header.append(func_row)
        
        # Add a note about the metrics
        header.extend([
            "",
            "**Metrics Legend:**",
            "- **Total %**: Percentage of all reachable lines that were covered during verification.",
            "- **Func %**: Percentage of target function lines that were covered.",
            "- **Errors**: Number of verification errors or failures detected."
        ])
    
    # Add performance metrics
    header.extend([
        "",
        "## Performance Metrics",
        f"Average harness generation time: {avg_generation_time:.2f} seconds",
        f"Average verification time: {avg_verification_time:.2f} seconds",
        f"Average evaluation time: {avg_evaluation_time:.2f} seconds",
        "",
        "## Coverage Analysis",
        f"Coverage report available at: {os.path.join('coverage', 'coverage_report.html')}",
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
            
            # Add coverage metrics for this function if available
            if not coverage_df.is_empty():
                # Find latest version metrics for this function
                func_data = coverage_df.filter(pl.col("function") == func_name)
                if not func_data.is_empty():
                    max_version = func_data["version"].max()
                    func_metrics = func_data.filter(pl.col("version") == max_version).row(0, named=True)
                    
                    header.append(f"\n#### Coverage Metrics")
                    
                    # Handle different metric names and potential string values
                    for metric_name, display_name in [
                        ("total_reachable_lines", "Total reachable lines"),
                        ("total_covered_lines", "Total coverage"),
                        ("func_reachable_lines", "Function reachable lines"),
                        ("func_coverage_pct", "Function coverage"),
                        ("reported_errors", "Reported errors")
                    ]:
                        if metric_name in func_metrics:
                            metric_value = func_metrics[metric_name]
                            
                            # For reported_errors, also try alternative fields if this is zero or N/A
                            if metric_name == "reported_errors" and (metric_value == 0 or metric_value == "N/A"):
                                # Try failure_count
                                if "failure_count" in func_metrics:
                                    failure_val = func_metrics["failure_count"]
                                    if failure_val != 0 and failure_val != "N/A":
                                        metric_value = failure_val
                                
                                # Try error_count
                                if metric_value == 0 or metric_value == "N/A":
                                    if "error_count" in func_metrics:
                                        error_val = func_metrics["error_count"]
                                        if error_val != 0 and error_val != "N/A":
                                            metric_value = error_val
                            
                            # Format percentage values appropriately
                            if metric_name.endswith("_pct") and isinstance(metric_value, (int, float)):
                                header.append(f"- {display_name}: {metric_value:.2f}%")
                            else:
                                header.append(f"- {display_name}: {metric_value}")
                    
                    # Add evolution metrics if function has multiple versions
                    versions = func_data["version"].unique()
                    if len(versions) > 1:
                        first_version = versions.min()
                        first_metrics = func_data.filter(pl.col("version") == first_version).row(0, named=True)
                        
                        # Handle potential string values for coverage metrics
                        try:
                            initial_cov = float(first_metrics.get('func_coverage_pct', 0))
                            final_cov = float(func_metrics.get('func_coverage_pct', 0))
                            cov_improvement = final_cov - initial_cov
                            
                            # Get error values with fallbacks to alternative fields
                            initial_errors = 0
                            for field in ['reported_errors', 'failure_count', 'error_count']:
                                if field in first_metrics and first_metrics[field] != "N/A":
                                    try:
                                        if isinstance(first_metrics[field], str):
                                            initial_errors = int(float(first_metrics[field]))
                                        else:
                                            initial_errors = int(first_metrics[field])
                                        if initial_errors > 0:
                                            break
                                    except (ValueError, TypeError):
                                        pass
                            
                            final_errors = 0
                            for field in ['reported_errors', 'failure_count', 'error_count']:
                                if field in func_metrics and func_metrics[field] != "N/A":
                                    try:
                                        if isinstance(func_metrics[field], str):
                                            final_errors = int(float(func_metrics[field]))
                                        else:
                                            final_errors = int(func_metrics[field])
                                        if final_errors > 0:
                                            break
                                    except (ValueError, TypeError):
                                        pass
                            
                            error_reduction = initial_errors - final_errors
                            
                            header.append(f"\n#### Coverage Evolution")
                            header.append(f"- Initial coverage (v{first_version}): {initial_cov:.2f}%")
                            header.append(f"- Final coverage (v{max_version}): {final_cov:.2f}%")
                            header.append(f"- Coverage improvement: {cov_improvement:.2f}%")
                            header.append(f"- Error reduction: {error_reduction}")
                        except (ValueError, TypeError) as e:
                            logger.error(f"Error calculating coverage evolution: {str(e)}")
            
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
    index_path = os.path.join(reports_dir, "coverage_report.html")
    with open(index_path, "w") as f:
        f.write("<html><head><title>CBMC Coverage Table </title>")
        f.write("<style>body{font-family:Arial,sans-serif;line-height:1.6;max-width:900px;margin:0 auto;padding:20px}h1{color:#2c3e50}h2{color:#3498db}h3{color:#2980b9}table{border-collapse:collapse;width:100%}table,th,td{border:1px solid #ddd;padding:8px}th{background-color:#f2f2f2}tr:nth-child(even){background-color:#f9f9f9}a{color:#3498db;text-decoration:none}a:hover{text-decoration:underline}</style>")
        f.write("</head><body>")
        
        
        # Table of function reports with enhanced metrics
        f.write("<h2>Function Reports</h2>")
        f.write("<table>")
        f.write("<tr><th rowspan='2'>Function</th><th rowspan='2'>File</th><th rowspan='2'>Status</th>")
        
        # Add version column headers
        if not coverage_df.is_empty():
            versions = sorted(list(set(coverage_df["version"].to_list())))
            for version in versions:
                f.write(f"<th colspan='3'>Version {version}</th>")
            f.write("</tr><tr>")
            
            # Add subheaders for each version
            for _ in versions:
                f.write("<th>Total %</th><th>Func %</th><th>Errors</th>")
        
        f.write("</tr>")
        
        # Function to get color based on class name
        def get_color_for_class(class_name):
            """Return a color hex code based on the class name."""
            if class_name == "good":
                return "#00691c"  # Dark green
            elif class_name == "medium":
                return "#FFA500"  # Orange
            elif class_name == "poor":
                return "#d32f2f"  # Red
            else:
                return "#000000"  # Black
        
        # Process each function
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
                
                # Start the row
                f.write(f"<tr><td>{display_name}</td><td>{file_name}</td><td {status_style}>{result['status']}</td>")
                
                # Add coverage metrics for each version
                if not coverage_df.is_empty():
                    for version in versions:
                        # Get data for this function and version
                        try:
                            func_data = coverage_df.filter(
                                (pl.col("function") == func_name) & (pl.col("version") == version)
                            )
                            
                            if not func_data.is_empty():
                                metrics = func_data.row(0, named=True)
                                
                                # Process total coverage
                                total_cov_val = metrics.get("total_coverage_pct", "N/A")
                                if isinstance(total_cov_val, (int, float)):
                                    total_class = "good" if total_cov_val >= 80 else "medium" if total_cov_val >= 50 else "poor"
                                    f.write(f"<td style='color:{get_color_for_class(total_class)}'>{total_cov_val:.2f}%</td>")
                                else:
                                    f.write("<td>N/A</td>")
                                
                                # Process func coverage
                                func_cov_val = metrics.get("func_coverage_pct", "N/A")
                                if isinstance(func_cov_val, (int, float)):
                                    func_class = "good" if func_cov_val >= 80 else "medium" if func_cov_val >= 50 else "poor"
                                    f.write(f"<td style='color:{get_color_for_class(func_class)}'>{func_cov_val:.2f}%</td>")
                                else:
                                    f.write("<td>N/A</td>")
                                
                                # Process errors/failures - Get all error metrics
                                reported_errors = 0
                                failure_count = 0
                                error_count = 0
                                
                                # Get the reported errors value
                                if "reported_errors" in metrics and metrics["reported_errors"] != "N/A":
                                    try:
                                        if isinstance(metrics["reported_errors"], str):
                                            reported_errors = int(float(metrics["reported_errors"]))
                                        else:
                                            reported_errors = int(metrics["reported_errors"])
                                    except (ValueError, TypeError):
                                        pass
                                
                                # Get the failure count value
                                if "failure_count" in metrics and metrics["failure_count"] != "N/A":
                                    try:
                                        if isinstance(metrics["failure_count"], str):
                                            failure_count = int(float(metrics["failure_count"]))
                                        else:
                                            failure_count = int(metrics["failure_count"])
                                    except (ValueError, TypeError):
                                        pass
                                
                                # Get the error count value
                                if "error_count" in metrics and metrics["error_count"] != "N/A":
                                    try:
                                        if isinstance(metrics["error_count"], str):
                                            error_count = int(float(metrics["error_count"]))
                                        else:
                                            error_count = int(metrics["error_count"])
                                    except (ValueError, TypeError):
                                        pass
                                
                                # Use the highest non-zero value for display
                                error_val = max(reported_errors, failure_count, error_count)
                                
                                # Color code the errors - green for 0, red for any errors
                                error_class = "good" if error_val == 0 else "poor"
                                f.write(f"<td style='color:{get_color_for_class(error_class)}'>{error_val}</td>")
                            else:
                                f.write("<td>-</td><td>-</td><td>-</td>")
                        except Exception as e:
                            logger.error(f"Error formatting HTML metrics for {func_name}, version {version}: {str(e)}")
                            f.write("<td>-</td><td>-</td><td>-</td>")
                
                f.write("</tr>")
        
        f.write("</table>")
        f.write("</body></html>")
    
    # Calculate relative path for displaying in message
    result_path = os.path.relpath(result_base_dir)
    coverage_path = os.path.join(result_path, "coverage", "coverage_report.html")
    
    return {
        "messages": [AIMessage(content=f"Analysis complete! Reports generated in '{result_path}'. Main index at {os.path.join(result_path, 'reports', 'index.html')}. Coverage report at {coverage_path}")]
    }