"""
CBMC coverage calculation utilities for the harness generator.
"""
import json
import re
import logging
from typing import Dict, Any, Set, List

logger = logging.getLogger("coverage_parser")

def parse_line_ranges(line_ranges):
    """
    Parse a string of line ranges (e.g., '20-24,27') into a set of unique line numbers.
    :param line_ranges: A string representing line ranges.
    :return: A set of unique line numbers.
    """
    unique_lines = set()
    for line_range in line_ranges.split(','):
        if '-' in line_range:
            start, end = map(int, line_range.split('-'))
            unique_lines.update(range(start, end + 1))
        else:
            unique_lines.add(int(line_range))
    return unique_lines

def calculate_coverage(json_file_path, target_function_name):
    """
    Calculate total coverage and target function coverage.

    :param json_file_path: Path to the JSON file.
    :param target_function_name: Name of the target function.
    :return: A dictionary containing total coverage and target function coverage.
    """
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    # Ensure data is a list
    if not isinstance(data, list):
        raise ValueError("Expected JSON root structure to be a list.")
    
    # Find the dictionary containing 'goals'
    goals_dict = None
    for item in data:
        if isinstance(item, dict) and "goals" in item:
            goals_dict = item
            break
    
    if not goals_dict:
        raise ValueError("No dictionary with 'goals' key found in the JSON file.")

    # Extract goals
    goals = goals_dict.get("goals", [])
    
    # Initialize sets to track lines
    reachable_lines_main = set()
    total_lines_main = set()
    
    reachable_lines_target_function = set()
    total_lines_target_function = set()
    
    # Define harness file name pattern
    harness_file_name = f"{target_function_name}_harness.c"
    
    for goal in goals:  # Iterate over each goal in the 'goals' list
        basic_block_lines = goal.get("basicBlockLines", {})
        
        for file_path, function_lines in basic_block_lines.items():
            for function_name, line_ranges in function_lines.items():
                parsed_lines = parse_line_ranges(line_ranges)
                
                # Track lines for main function in harness file
                if function_name == "main" and harness_file_name in file_path:
                    total_lines_main.update(parsed_lines)
                    if goal.get("status") == "satisfied":
                        reachable_lines_main.update(parsed_lines)
                
                # Track lines for target function
                if function_name == target_function_name:
                    total_lines_target_function.update(parsed_lines)
                    if goal.get("status") == "satisfied":
                        reachable_lines_target_function.update(parsed_lines)
    
    # Calculate Total Coverage
    total_reachable_lines = len(reachable_lines_main.union(reachable_lines_target_function))
    total_possible_lines = len(total_lines_main.union(total_lines_target_function))
    
    total_coverage = total_reachable_lines / total_possible_lines if total_possible_lines > 0 else 0
    
    # Calculate Target Function Coverage
    target_function_coverage = len(reachable_lines_target_function) / len(total_lines_target_function) if len(total_lines_target_function) > 0 else 0
    
    # Calculate uncovered lines
    uncovered_lines_main = total_lines_main - reachable_lines_main
    uncovered_lines_target_function = total_lines_target_function - reachable_lines_target_function
    
    # Print debug information about lines
    print(f"Total Lines (Main Function): {len(total_lines_main)}")
    print(f"Reachable Lines (Main Function): {len(reachable_lines_main)}")
    print(f"Uncovered Lines (Main Function): {len(uncovered_lines_main)}")
    
    print(f"Total Lines (Target Function): {len(total_lines_target_function)}")
    print(f"Reachable Lines (Target Function): {len(reachable_lines_target_function)}")
    print(f"Uncovered Lines (Target Function): {len(uncovered_lines_target_function)}")
    
    print(f"Total Lines (Harness + Target Function): {total_possible_lines}")
    print(f"Reachable Lines (Harness + Target Function): {total_reachable_lines}")
    
    # Print detailed sets of covered and uncovered lines
    print(f"Covered Lines (Main Function): {sorted(reachable_lines_main)}")
    print(f"Uncovered Lines (Main Function): {sorted(uncovered_lines_main)}")
    
    print(f"Covered Lines (Target Function): {sorted(reachable_lines_target_function)}")
    print(f"Uncovered Lines (Target Function): {sorted(uncovered_lines_target_function)}")
    
    return {
        "Total Coverage": round(total_coverage * 100, 2),
        "Target Function Coverage": round(target_function_coverage * 100, 2),
        "Total Lines Main": len(total_lines_main),
        "Reachable Lines Main": len(reachable_lines_main),
        "Uncovered Lines Main": len(uncovered_lines_main),
        "Total Lines Target Function": len(total_lines_target_function),
        "Reachable Lines Target Function": len(reachable_lines_target_function),
        "Uncovered Lines Target Function": len(uncovered_lines_target_function),
        "Total Lines Combined": total_possible_lines,
        "Reachable Lines Combined": total_reachable_lines
    }

def extract_coverage_metrics_from_json(json_data, target_function_name):
    """
    Extract coverage metrics from CBMC JSON output.
    
    Args:
        json_data: The JSON data from CBMC output
        target_function_name: Name of the function being analyzed
        
    Returns:
        Dictionary with coverage metrics
    """
    # Initialize result structure
    result = {
        "total_reachable_lines": 0,
        "total_covered_lines": 0,
        "coverage_pct": 0.0,
        "func_reachable_lines": 0,
        "func_covered_lines": 0,
        "func_coverage_pct": 0.0,
        "errors": 0,
        "error_categories": [],
        "total_lines_main": 0,
        "reachable_lines_main": 0,
        "uncovered_lines_main": 0,
        "total_lines_target": 0,
        "reachable_lines_target": 0,
        "uncovered_lines_target": 0,
        "total_lines_combined": 0,
        "reachable_lines_combined": 0
    }
    
    try:
        # Extract function name without file prefix
        func_name = target_function_name
        if ":" in target_function_name:
            func_name = target_function_name.split(":")[-1]
        
        # Initialize tracking sets
        reachable_lines_main = set()
        total_lines_main = set()
        reachable_lines_target = set()
        total_lines_target = set()
        
        # Define harness file name pattern
        harness_file_name = f"{func_name}_harness.c"
        
        # Process goals
        if "goals" in json_data:
            goals = json_data["goals"]
            
            for goal in goals:
                basic_block_lines = goal.get("basicBlockLines", {})
                
                for file_path, function_lines in basic_block_lines.items():
                    for function_name, line_ranges in function_lines.items():
                        parsed_lines = parse_line_ranges(line_ranges)
                        
                        # Track main function lines
                        if function_name == "main" and harness_file_name in file_path:
                            total_lines_main.update(parsed_lines)
                            if goal.get("status") == "satisfied":
                                reachable_lines_main.update(parsed_lines)
                        
                        # Track target function lines
                        if function_name == func_name:
                            total_lines_target.update(parsed_lines)
                            if goal.get("status") == "satisfied":
                                reachable_lines_target.update(parsed_lines)
            
            # Calculate main function metrics
            result["total_lines_main"] = len(total_lines_main)
            result["reachable_lines_main"] = len(reachable_lines_main)
            result["uncovered_lines_main"] = len(total_lines_main) - len(reachable_lines_main)
            
            # Calculate target function metrics
            result["total_lines_target"] = len(total_lines_target)
            result["reachable_lines_target"] = len(reachable_lines_target)
            result["uncovered_lines_target"] = len(total_lines_target) - len(reachable_lines_target)
            
            # Calculate combined metrics
            total_combined = len(total_lines_main.union(total_lines_target))
            reachable_combined = len(reachable_lines_main.union(reachable_lines_target))
            
            result["total_lines_combined"] = total_combined
            result["reachable_lines_combined"] = reachable_combined
            
            # Calculate percentages
            result["total_reachable_lines"] = reachable_combined
            result["total_covered_lines"] = reachable_combined
            if total_combined > 0:
                result["coverage_pct"] = (reachable_combined / total_combined) * 100
            
            result["func_reachable_lines"] = len(reachable_lines_target)
            result["func_covered_lines"] = len(reachable_lines_target)
            if len(total_lines_target) > 0:
                result["func_coverage_pct"] = (len(reachable_lines_target) / len(total_lines_target)) * 100
        
        # Count errors and categorize
        error_count = 0
        error_categories = set()
        
        # Process failures
        if "verificationResults" in json_data:
            for res in json_data["verificationResults"]:
                if res.get("status") == "FAILURE":
                    error_count += 1
                    # Extract category from property
                    property_str = res.get("property", "")
                    if "memory" in property_str.lower():
                        error_categories.add("memory_leak")
                    elif "pointer" in property_str.lower():
                        error_categories.add("null_pointer")
                    elif "bound" in property_str.lower():
                        error_categories.add("array_bounds")
                    else:
                        error_categories.add("other")
        
        # Check for errors in messages (alternative method)
        if error_count == 0 and "messages" in json_data:
            for msg in json_data["messages"]:
                if msg.get("messageType") == "ERROR":
                    error_count += 1
                    # Extract category from message text
                    msg_text = msg.get("messageText", "").lower()
                    if "memory" in msg_text:
                        error_categories.add("memory_leak")
                    elif "null" in msg_text or "invalid pointer" in msg_text:
                        error_categories.add("null_pointer")
                    elif "bound" in msg_text or "index" in msg_text:
                        error_categories.add("array_bounds")
                    else:
                        error_categories.add("other")
        
        result["errors"] = error_count
        result["error_categories"] = list(error_categories)
        
    except Exception as e:
        logger.error(f"Error extracting coverage metrics: {str(e)}")
    
    return result

def generate_improved_report(coverage_data, target_function, version):
    """
    Generate a detailed coverage report for a specific version.
    
    Args:
        coverage_data: Coverage metrics data
        target_function: The target function name
        version: Version number
        
    Returns:
        Formatted report text
    """
    report = f"# Coverage Report for {target_function} (Version {version})\n\n"
    
    # Add a comprehensive coverage table
    report += "## Coverage Metrics\n\n"
    report += "| Category | Total Lines | Reachable Lines | Uncovered Lines | Coverage % |\n"
    report += "|----------|-------------|-----------------|-----------------|------------|\n"
    
    # Main function metrics
    main_coverage_pct = 0
    if coverage_data["total_lines_main"] > 0:
        main_coverage_pct = (coverage_data["reachable_lines_main"] / coverage_data["total_lines_main"]) * 100
    
    report += f"| Main Function | {coverage_data['total_lines_main']} | {coverage_data['reachable_lines_main']} | "
    report += f"{coverage_data['uncovered_lines_main']} | {main_coverage_pct:.2f}% |\n"
    
    # Target function metrics
    target_coverage_pct = 0
    if coverage_data["total_lines_target"] > 0:
        target_coverage_pct = (coverage_data["reachable_lines_target"] / coverage_data["total_lines_target"]) * 100
    
    report += f"| Target Function | {coverage_data['total_lines_target']} | {coverage_data['reachable_lines_target']} | "
    report += f"{coverage_data['uncovered_lines_target']} | {target_coverage_pct:.2f}% |\n"
    
    # Combined metrics
    combined_coverage_pct = 0
    if coverage_data["total_lines_combined"] > 0:
        combined_coverage_pct = (coverage_data["reachable_lines_combined"] / coverage_data["total_lines_combined"]) * 100
    
    report += f"| **Combined** | **{coverage_data['total_lines_combined']}** | **{coverage_data['reachable_lines_combined']}** | "
    report += f"**{coverage_data['total_lines_combined'] - coverage_data['reachable_lines_combined']}** | **{combined_coverage_pct:.2f}%** |\n\n"
    
    # Add error information
    report += "## Error Analysis\n\n"
    report += f"Total Errors: {coverage_data['errors']}\n\n"
    
    if coverage_data["error_categories"]:
        report += "Error Categories:\n"
        for category in coverage_data["error_categories"]:
            report += f"- {category}\n"
    else:
        report += "No errors detected.\n"
    
    return report

def extract_coverage_metrics(json_data, target_function_name):
    """
    Extract and calculate comprehensive coverage metrics from CBMC JSON data.
    
    Args:
        json_data: The JSON data from CBMC output
        target_function_name: Name of the target function
        
    Returns:
        Dictionary with detailed coverage metrics
    """
    # Get detailed metrics using the enhanced extraction function
    metrics = extract_coverage_metrics_from_json(json_data, target_function_name)
    
    # Create a standard format result dictionary for compatibility
    result = {
        "Total Coverage": round(metrics["coverage_pct"], 2),
        "Target Function Coverage": round(metrics["func_coverage_pct"], 2),
        "Total Lines Main": metrics["total_lines_main"],
        "Reachable Lines Main": metrics["reachable_lines_main"],
        "Uncovered Lines Main": metrics["uncovered_lines_main"],
        "Total Lines Target Function": metrics["total_lines_target"],
        "Reachable Lines Target Function": metrics["reachable_lines_target"],
        "Uncovered Lines Target Function": metrics["uncovered_lines_target"],
        "Total Lines Combined": metrics["total_lines_combined"],
        "Reachable Lines Combined": metrics["reachable_lines_combined"],
        "Errors": metrics["errors"],
        "Error Categories": metrics["error_categories"]
    }
    
    return result

# Example usage
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python coverage_parser.py <json_file_path> <target_function_name>")
        sys.exit(1)
    
    json_file_path = sys.argv[1]
    target_function_name = sys.argv[2]
    
    try:
        with open(json_file_path, 'r') as file:
            json_data = json.load(file)
        
        metrics = extract_coverage_metrics(json_data, target_function_name)
        
        print("\n=== Coverage Summary ===")
        print(f"Total Coverage: {metrics['Total Coverage']}%")
        print(f"Target Function Coverage: {metrics['Target Function Coverage']}%")
        print("\n=== Detailed Metrics ===")
        print(f"Main Function: {metrics['Reachable Lines Main']}/{metrics['Total Lines Main']} lines covered ({metrics['Uncovered Lines Main']} uncovered)")
        print(f"Target Function: {metrics['Reachable Lines Target Function']}/{metrics['Total Lines Target Function']} lines covered ({metrics['Uncovered Lines Target Function']} uncovered)")
        print(f"Combined: {metrics['Reachable Lines Combined']}/{metrics['Total Lines Combined']} lines covered")
        
        # Generate detailed report
        report = generate_improved_report(metrics, target_function_name, "latest")
        print("\n" + report)
        
    except ValueError as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print(f"Error: File '{json_file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{json_file_path}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")