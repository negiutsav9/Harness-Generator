import json

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
        "Target Function Coverage": round(target_function_coverage * 100, 2)
    }

# Example usage
if __name__ == "__main__":
    json_file_path = "results/openai/20250414_081615/verification/core_http_client.c:HTTPClient_AddHeader/v3_coverage.json"  # Replace with actual path to JSON file
    target_function_name = "HTTPClient_AddHeader"  # Replace with actual target function name
    
    try:
        results = calculate_coverage(json_file_path, target_function_name)
        print(f"Total Coverage: {results['Total Coverage']}%")
        print(f"Target Function Coverage: {results['Target Function Coverage']}%")
    except ValueError as e:
        print(f"Error: {e}")
