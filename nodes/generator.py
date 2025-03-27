"""
Generator node for CBMC harness generator workflow.
"""
import time
import os
import re
import json
import logging
from langchain_core.messages import AIMessage, HumanMessage
from core import embedding_db
from utils.embedding_utils import get_existing_definitions, check_harness_conflicts

# Set up logging
logger = logging.getLogger("generator")

def find_cbmc_stubs(embedding_db):
    """
    Find all CBMC stub functions in the embedding database
    
    Args:
        embedding_db: The code embedding database
    
    Returns:
        Dictionary mapping function names to their stub implementations
    """
    try:
        # Query for all functions with file_type = cbmc_stub
        results = embedding_db.code_collection.get(
            where={"file_type": "cbmc_stub"},
            include=["metadatas", "documents"]
        )
        
        stubs = {}
        if results and results["ids"]:
            for i, metadata in enumerate(results["metadatas"]):
                func_name = metadata.get("name", "")
                if func_name:
                    stubs[func_name] = {
                        "code": results["documents"][i],
                        "file": metadata.get("file_path", "unknown"),
                        "is_stub": True
                    }
            
            logger.info(f"Found {len(stubs)} CBMC stub functions")
        else:
            logger.info("No CBMC stub functions found")
            
        return stubs
    except Exception as e:
        logger.error(f"Error finding CBMC stubs: {str(e)}")
        return {}

def find_existing_harnesses(embedding_db, func_name):
    """
    Find existing CBMC harnesses for the given function
    
    Args:
        embedding_db: The code embedding database
        func_name: Function name to look for harnesses
    
    Returns:
        List of existing harness implementation texts
    """
    try:
        # Extract base function name without file prefix
        base_func_name = func_name
        if ":" in func_name:
            _, base_func_name = func_name.split(":", 1)
            
        # Look for harness functions containing the function name
        harness_functions = []
        
        # Try to find direct match first (function_harness or harness_function)
        harness_patterns = [
            f"{base_func_name}_harness",
            f"harness_{base_func_name}"
        ]
        
        for pattern in harness_patterns:
            results = embedding_db.code_collection.get(
                where={"name": {"$eq": pattern}},
                include=["metadatas", "documents"]
            )
            
            if results and results["ids"]:
                for i, doc in enumerate(results["documents"]):
                    metadata = results["metadatas"][i]
                    file_path = metadata.get("file_path", "unknown")
                    harness_functions.append({
                        "name": pattern,
                        "code": doc,
                        "file": file_path
                    })
                    logger.info(f"Found existing harness: {pattern} in {file_path}")
        
        # If no direct match, try to find any harness containing the function call
        if not harness_functions:
            results = embedding_db.code_collection.get(
                where={"file_type": "cbmc_harness"},
                include=["metadatas", "documents"]
            )
            
            if results and results["ids"]:
                for i, doc in enumerate(results["documents"]):
                    # Check if this harness calls our target function
                    if f"{base_func_name}(" in doc:
                        metadata = results["metadatas"][i]
                        harness_name = metadata.get("name", "unknown")
                        file_path = metadata.get("file_path", "unknown")
                        harness_functions.append({
                            "name": harness_name,
                            "code": doc,
                            "file": file_path
                        })
                        logger.info(f"Found related harness: {harness_name} in {file_path}")
        
        return harness_functions
    except Exception as e:
        logger.error(f"Error finding existing harnesses: {str(e)}")
        return []

def get_function_dependencies(func_code, embeddings):
    """
    Extract function calls from the given function code and find their 
    implementations in the embeddings database.
    
    Args:
        func_code: The source code of the function
        embeddings: The embeddings dictionary from the state
        
    Returns:
        Dictionary of function_name -> function_code for dependencies
    """
    # Extract function calls using regex
    function_call_pattern = r'\b(\w+)\s*\('
    calls = re.findall(function_call_pattern, func_code)
    
    # Filter out standard library functions and duplicates
    standard_functions = ['printf', 'scanf', 'malloc', 'free', 'memcpy', 'strcpy', 
                         'strlen', 'strcmp', 'if', 'for', 'while', 'sizeof', 'return']
    unique_calls = set([call for call in calls if call not in standard_functions])
    
    # Get function codes from embeddings
    dependencies = {}
    
    for func_name in unique_calls:
        # Try to find the function in embeddings
        for key, data in embeddings.get('functions', {}).items():
            if ':' in key:
                file_name, function_name = key.split(':', 1)
            else:
                function_name = key
                
            if function_name == func_name:
                file_path = data.get('file_path', '')
                line_num = 0  # We don't have line numbers in our data structure
                full_text = data.get('full_text', '')
                
                if full_text:
                    dependencies[func_name] = {
                        'code': full_text,
                        'file': file_path,
                        'line': line_num
                    }
                    break
    
    return dependencies

def find_cbmc_test_headers(embedding_db):
    """
    Find CBMC test header files and their content
    
    Returns:
        Dictionary mapping header file names to their content
    """
    try:
        # Query for all CBMC test header files
        results = embedding_db.code_collection.get(
            where={"file_type": "cbmc_test_header"},
            include=["metadatas", "documents"]
        )
        
        headers = {}
        if results and results["ids"]:
            for i, metadata in enumerate(results["metadatas"]):
                file_path = metadata.get("file_path", "")
                if file_path:
                    file_name = os.path.basename(file_path)
                    headers[file_name] = {
                        "content": results["documents"][i],
                        "path": file_path
                    }
            
            logger.info(f"Found {len(headers)} CBMC test header files")
        else:
            logger.info("No CBMC test header files found")
            
        return headers
    except Exception as e:
        logger.error(f"Error finding CBMC test headers: {str(e)}")
        return {}

def generator_node(state):
    """Generates or refines CBMC-compatible harness for the current function."""
    # Get the global LLM instance
    from utils.llm_utils import setup_llm
    llm = setup_llm()

    # Start timing
    generation_start = time.time()
    
    func_name = state.get("current_function", "")
    logger.info(f"Generating harness for function: {func_name}")
    
    # Check if this is a refinement
    improvement_recommendation = state.get("improvement_recommendation", "")
    is_refinement = bool(improvement_recommendation)
    
    # Track harness history
    harness_history = state.get("harness_history", {})
    if func_name not in harness_history:
        harness_history[func_name] = []
    
    # Get previous harness if refining
    previous_harness = ""
    if is_refinement and func_name in state.get("harnesses", {}):
        previous_harness = state.get("harnesses", {})[func_name]
        # Add to history if not already there
        if previous_harness not in harness_history[func_name]:
            harness_history[func_name].append(previous_harness)
    
    # Get function code and dependencies if not refining
    if not is_refinement:
        function_result = embedding_db.code_collection.get(ids=[func_name], include=["documents", "metadatas"])
        
        if not function_result["ids"]:
            logger.error(f"Function {func_name} not found in database")
            return {
                "messages": [AIMessage(content=f"Error: Function {func_name} not found in database.")],
                "next": "junction"
            }
        
        func_code = function_result["documents"][0]
        func_metadata = function_result["metadatas"][0]
        
        # Extract base function name without file prefix
        base_func_name = func_name
        if ":" in func_name:
            _, base_func_name = func_name.split(":", 1)
        
        # Get embeddings to find function dependencies
        embeddings = state.get("embeddings", {})
        
        # Find dependencies of the function
        dependencies = get_function_dependencies(func_code, embeddings)
        
        # Find CBMC stubs
        cbmc_stubs = find_cbmc_stubs(embedding_db)
        
        # Find existing harnesses for this function
        existing_harnesses = find_existing_harnesses(embedding_db, func_name)
        
        # Find CBMC test headers
        cbmc_headers = find_cbmc_test_headers(embedding_db)
        
        # Get pattern information
        patterns_result = embedding_db.query_pattern_db(func_code)
        
        # Analyze function properties
        has_malloc = "malloc(" in func_code
        has_free = "free(" in func_code
        has_array_access = "[" in func_code and "]" in func_code
        has_pointer_arithmetic = "*" in func_code or "->" in func_code
        has_division = "/" in func_code or "%" in func_code
        has_type_conversion = "(" in func_code and ")" in func_code and any(type_name in func_code for type_name in ["int", "char", "float", "double", "size_t", "unsigned", "long"])
        
        # Produce targeted verification guide
        verification_checks = []
        if has_malloc or has_free:
            verification_checks.append("--memory-leak-check: Verify memory is properly allocated and freed")
        if has_array_access:
            verification_checks.append("--bounds-check: Verify array accesses are within bounds")
        if has_pointer_arithmetic:
            verification_checks.append("--pointer-overflow-check: Verify pointer arithmetic is safe")
        if has_division:
            verification_checks.append("--div-by-zero-check: Verify divisors are non-zero")
        if has_type_conversion:
            verification_checks.append("--conversion-check: Verify type conversions are safe")
        
        # Construct verification guide
        if verification_checks:
            verification_guide = "Relevant CBMC Verification Checks for this function:\n" + "\n".join(verification_checks)
        else:
            verification_guide = "This function doesn't appear to need special CBMC verification checks beyond basic assertions."
            
        # Format dependencies for inclusion in the prompt
        dependencies_section = ""
        if dependencies:
            dependencies_section = "## Function Dependencies:\n\n"
            for dep_name, dep_info in dependencies.items():
                dependencies_section += f"### Function: {dep_name}\n"
                dependencies_section += f"From file: {dep_info.get('file', 'unknown')}\n"
                dependencies_section += f"```c\n{dep_info.get('code', '/* Code not available */')}\n```\n\n"
        
        # Format CBMC stubs section
        cbmc_stubs_section = ""
        if cbmc_stubs:
            cbmc_stubs_section = "## Available CBMC Stubs:\n\n"
            for stub_name, stub_info in cbmc_stubs.items():
                cbmc_stubs_section += f"### Stub: {stub_name}\n"
                cbmc_stubs_section += f"From file: {stub_info.get('file', 'unknown')}\n"
                cbmc_stubs_section += f"```c\n{stub_info.get('code', '/* Stub code not available */')}\n```\n\n"
        
        # Format existing harnesses section
        existing_harnesses_section = ""
        if existing_harnesses:
            existing_harnesses_section = "## Existing CBMC Harnesses for Reference:\n\n"
            for harness in existing_harnesses:
                existing_harnesses_section += f"### Harness: {harness.get('name', 'unknown')}\n"
                existing_harnesses_section += f"From file: {harness.get('file', 'unknown')}\n"
                existing_harnesses_section += f"```c\n{harness.get('code', '/* Harness code not available */')}\n```\n\n"
        
        # Format header files section
        cbmc_headers_section = ""
        if cbmc_headers:
            cbmc_headers_section = "## Available CBMC Test Headers:\n\n"
            for header_name, header_info in list(cbmc_headers.items())[:3]:  # Limit to first 3 headers to avoid prompt size issues
                cbmc_headers_section += f"### Header: {header_name}\n"
                cbmc_headers_section += f"Path: {header_info.get('path', 'unknown')}\n"
                cbmc_headers_section += f"```c\n{header_info.get('content', '/* Header content not available */')}\n```\n\n"
        
        # Get existing definitions for conflict prevention
        existing_definitions = get_existing_definitions()
        
        # Determine domain for relevance filtering
        domain = None
        domains = {
            "HTTP": ["HTTP", "Http", "http"],
            "MQTT": ["MQTT", "Mqtt", "mqtt"],
            "TLS": ["TLS", "Tls", "tls"],
            "TCP": ["TCP", "Tcp", "tcp"],
            "JSON": ["JSON", "Json", "json"],
            "Socket": ["Socket", "socket"]
        }
        
        for d_name, keywords in domains.items():
            if any(kw in base_func_name for kw in keywords):
                domain = d_name
                break
        
        # Create a prompt section about existing definitions (limit to most relevant ones)
        existing_defs_section = ""
        if existing_definitions.get("macros") or existing_definitions.get("types") or existing_definitions.get("enums"):
            existing_defs_section = "\nEXISTING DEFINITIONS - DO NOT REDEFINE THESE:\n"
            
            # Add macros (limit to 10 most relevant)
            if existing_definitions.get("macros"):
                # Try to find the most relevant macros for this function
                relevant_macros = []
                for macro in existing_definitions["macros"]:
                    if macro in func_code or (domain and domain.lower() in macro.lower()):
                        relevant_macros.append(macro)
                
                # If we didn't find relevant macros, just use common ones
                if not relevant_macros and existing_definitions["macros"]:
                    common_macros = ["Log", "ASSERT", "CHECK", "CPROVER"]
                    relevant_macros = [m for m in existing_definitions["macros"] 
                                    if any(cm in m for cm in common_macros)][:10]
                    
                if relevant_macros:
                    existing_defs_section += "\nMacros:\n"
                    for macro in relevant_macros[:10]:  # Limit to 10
                        existing_defs_section += f"- {macro}\n"
            
            # Add types (limit to 10 most relevant)
            if existing_definitions.get("types"):
                # Try to find the most relevant types for this function
                relevant_types = []
                for type_name in existing_definitions["types"]:
                    if type_name in func_code or (domain and domain.lower() in type_name.lower()):
                        relevant_types.append(type_name)
                
                # If we didn't find relevant types, just use domain-specific ones
                if not relevant_types and domain and existing_definitions["types"]:
                    relevant_types = [t for t in existing_definitions["types"] 
                                    if domain.lower() in t.lower()][:10]
                    
                if relevant_types:
                    existing_defs_section += "\nTypes:\n"
                    for type_name in relevant_types[:10]:  # Limit to 10
                        existing_defs_section += f"- {type_name}\n"
            
            # Add enums (limit to 5 most relevant)
            if existing_definitions.get("enums"):
                # Try to find the most relevant enums for this function
                relevant_enums = []
                for enum_name in existing_definitions["enums"]:
                    if enum_name in func_code or (domain and domain.lower() in enum_name.lower()):
                        relevant_enums.append(enum_name)
                
                # If we didn't find relevant enums, just use domain-specific ones
                if not relevant_enums and domain and existing_definitions["enums"]:
                    relevant_enums = [e for e in existing_definitions["enums"] 
                                    if domain.lower() in e.lower()][:5]
                    
                if relevant_enums:
                    existing_defs_section += "\nEnums:\n"
                    for enum_name in relevant_enums[:5]:  # Limit to 5
                        existing_defs_section += f"- {enum_name}\n"
        
        # Clear guidance about avoiding unnecessary mocks and using existing resources
        cbmc_verification_info = f"""
        {verification_guide}
        
        {existing_defs_section}
        
        IMPORTANT GUIDELINES:
        
        1. INCLUDE THE ACTUAL FUNCTION IMPLEMENTATION in your harness - do NOT create mock implementations.
        2. Include the actual function implementation and any necessary dependencies DIRECTLY in the harness file.
        3. When including the function and its dependencies, add a comment with the original file name and approximate line number.
        4. USE THE PROVIDED CBMC STUBS when they are available instead of creating new ones.
        5. REFERENCE THE EXISTING HARNESSES as models for your implementation when appropriate.
        6. INCLUDE THE APPROPRIATE CBMC TEST HEADERS based on the function's needs.
        7. DO NOT REDEFINE macros, types, or enums that already exist in the test files.
        8. Focus on testing the actual function behavior, not on artificial scenarios.
        9. Only implement verification checks that are relevant to this specific function.
        
        The harness should:
        - Include the actual function implementation with comments about its source
        - Include necessary dependent functions with comments about their source
        - Use existing CBMC stubs when available
        - Follow the patterns in existing harnesses when available
        - Include appropriate CBMC test headers
        - AVOID REDEFINING any macros, types, or enums listed above
        - Use __CPROVER_assert() only for properties that could actually fail in this function
        - Use __CPROVER_assume() to specify realistic input constraints
        - Use nondet functions like nondet_int() for inputs that need to be nondeterministic
        """
        
        # Build generator prompt with focused verification
        generator_prompt = f"""
        You are a specialized harness generator for CBMC verification.
        Create a CBMC harness for the following function that INCLUDES THE ACTUAL FUNCTION IMPLEMENTATION:
        
        ```c
        {func_code}
        ```
        
        Function metadata:
        - Return type: {func_metadata.get("return_type", "void")}
        - Parameters: {func_metadata.get("params", "")}
        - Contains malloc: {has_malloc}
        - Contains free: {has_free}
        
        Matching vulnerability patterns:
        {json.dumps(patterns_result.get('matching_patterns', {}), indent=2)}
        
        {dependencies_section}
        
        {cbmc_stubs_section}
        
        {existing_harnesses_section}
        
        {cbmc_headers_section}
        
        {cbmc_verification_info}
        
        CRITICAL INSTRUCTIONS:
        1. INCLUDE the actual function implementation directly in the harness file
        2. Include necessary dependent functions that aren't standard library functions
        3. USE EXISTING CBMC STUBS instead of creating new ones whenever possible
        4. REFERENCE PATTERNS FROM EXISTING HARNESSES if available
        5. INCLUDE APPROPRIATE CBMC TEST HEADERS
        6. DO NOT REDEFINE ANY OF THE LISTED MACROS, TYPES, OR ENUMS
        7. Include a function named 'harness()' (not main()) that tests the implementation properly
        8. Only verify properties that are relevant to this specific function
        9. Include all necessary header files and declarations
        
        Format for including the original function:
        ```c
        // From: [original_file_name], Line: [approximate_line_number]
        [original_function_code]
        ```
        
        IMPORTANT: The verification harness MUST BE implemented as a 'void harness(void)' function rather than 'main()'.
        
        Provide the complete harness code without explanation.
        """
    else:
        # For refinement, use a more targeted improvement guidance
        generator_prompt = f"""
        You are a specialized harness generator for CBMC verification.
        You need to REFINE an existing harness based on SPECIFIC CBMC verification failures.
        
        {improvement_recommendation}
        
        Previous harness code that you should improve:
        ```c
        {previous_harness}
        ```
        
        CRITICAL INSTRUCTIONS:
        1. MAINTAIN all actual function implementations in the harness - do NOT remove or replace with mocks
        2. ADDRESS EACH SPECIFIC ISSUE mentioned in the evaluation feedback
        3. ADD all missing header files, function declarations, and constraints
        4. IMPLEMENT all suggested code changes precisely
        5. ENSURE proper memory management (allocation and freeing)
        6. FIX all pointer dereference issues with proper initialization and checks
        7. RESOLVE declaration errors by adding the necessary declarations
        8. If any actual function implementations were missing previously, add them now
        9. DO NOT REDEFINE macros, types or enums that are already defined in test headers
        
        Make sure your harness is complete, properly formatted, addresses ALL specific issues in the feedback, 
        and continues to include the actual function implementations with their source comments.
        
        IMPORTANT: The verification harness MUST BE implemented as a 'void harness(void)' function rather than 'main()'.
        
        Provide only the improved harness code without explanation.
        """
    
    # Generate the harness
    try:
        logger.info(f"Sending API request to generate harness for {func_name}")
        # Setup messages for the LLM
        response = llm.invoke([
            HumanMessage(content=generator_prompt)
        ])
        logger.info(f"Received API response for {func_name}")
        
        # Extract the harness code
        harness_code = response.content
        match = re.search(r'```(?:c)?\n(.+?)\n```', harness_code, re.DOTALL)
        if match:
            harness_code = match.group(1)
        
        # Check for conflicts with existing definitions
        existing_definitions = get_existing_definitions()
        modified_harness, conflicts_found = check_harness_conflicts(harness_code, existing_definitions)
        
        if conflicts_found:
            logger.info("Modified harness to avoid conflicts with existing definitions")
            harness_code = modified_harness
        
        # Check if the harness is already inside a harness function
        if "void harness()" not in harness_code and "int harness()" not in harness_code:
            logger.info(f"Wrapping harness for {func_name} in a harness() function")
            
            # Check if there's already a main function
            has_main = "void main(" in harness_code or "int main(" in harness_code
            
            if has_main:
                # Extract the main function content
                main_pattern = r"(void|int)\s+main\s*\(\s*(?:void|)\s*\)\s*\{([\s\S]*?)\}"
                main_match = re.search(main_pattern, harness_code, re.DOTALL)
                
                if main_match:
                    main_body = main_match.group(2)
                    
                    # Replace main with harness
                    harness_code = re.sub(
                        main_pattern,
                        "void harness(void) {\\2}",
                        harness_code,
                        count=1,
                        flags=re.DOTALL
                    )
                    
                    logger.info("Converted main() function to harness() function")
                else:
                    # If we couldn't extract main properly, just wrap everything
                    harness_code = f"""
// Function implementations and includes preserved
{harness_code}

// Added harness function wrapper
void harness(void) {{
    // Auto-generated harness function
    main();
}}
"""
                    logger.info("Added harness() function that calls main()")
            else:
                # No main function, wrap everything in a harness function
                # But preserve any includes and function implementations
                
                # Extract all includes and function implementations
                include_pattern = r"#include\s+[<\"][^>\"]+[>\"]"
                includes = re.findall(include_pattern, harness_code)
                
                # Remove includes from the code for wrapping
                for include in includes:
                    harness_code = harness_code.replace(include, "")
                
                # Find function implementations
                func_pattern = r"(\w+)\s+(\w+)\s*\(([^)]*)\)\s*\{([\s\S]*?)\}"
                functions = re.findall(func_pattern, harness_code, re.DOTALL)
                
                # Reconstruct the code with includes, functions, and harness
                new_code = ""
                
                # Add includes
                for include in includes:
                    new_code += include + "\n"
                
                # Add function implementations
                for func in functions:
                    return_type, func_name, params, body = func
                    new_code += f"{return_type} {func_name}({params}) {{{body}}}\n\n"
                
                # Add harness function
                new_code += """
void harness(void) {
    // Auto-generated harness function
    // Add test code here
}
"""
                harness_code = new_code
                logger.info("Created harness() function from scratch")
        
        # Validate harness completeness
        has_harness = "void harness(" in harness_code or "int harness(" in harness_code
        balanced_braces = harness_code.count("{") <= harness_code.count("}")
        
        # Verify that the actual function implementation is included
        original_func_name = func_name
        if ":" in func_name:
            _, original_func_name = func_name.split(":", 1)
            
        has_original_function = f"{original_func_name}(" in harness_code and "// From:" in harness_code
        
        if not has_original_function and not is_refinement:
            logger.warning(f"Harness for {func_name} does not include the original function implementation, attempting to fix")
            
            # Get function code again to ensure we have it
            function_result = embedding_db.code_collection.get(ids=[func_name], include=["documents", "metadatas"])
            
            if function_result["ids"]:
                func_code = function_result["documents"][0]
                file_name = "unknown"
                
                # Extract file name from func_id if possible
                if ":" in func_name:
                    file_name, _ = func_name.split(":", 1)
                
                # Add original function with source comment
                func_comment = f"\n// From: {file_name}, Line: approximate\n"
                
                # Find where to insert the function
                harness_func_idx = harness_code.find("void harness(")
                if harness_func_idx > 0:
                    # Insert before the harness function
                    harness_code = harness_code[:harness_func_idx] + func_comment + func_code + "\n\n" + harness_code[harness_func_idx:]
                else:
                    # Just add at the beginning
                    harness_code = func_comment + func_code + "\n\n" + harness_code
                
                logger.info(f"Added original function implementation to harness for {func_name}")
        
        if not has_harness or not balanced_braces:
            logger.warning(f"Incomplete harness for {func_name}, attempting to fix")
            
            # Fix incomplete harnesses
            if not balanced_braces:
                missing_braces = harness_code.count("{") - harness_code.count("}")
                if missing_braces > 0:
                    harness_code += "\n" + ("}" * missing_braces)
            
            # Make sure there's a harness function
            if not has_harness:
                if "int harness" not in harness_code and "void harness" not in harness_code:
                    harness_code += "\n\nvoid harness(void) {\n    // Auto-generated harness function\n}"
        
        # Save the new harness to history
        if harness_code not in harness_history[func_name]:
            harness_history[func_name].append(harness_code)
        
        # Update the harnesses dictionary
        harnesses = state.get("harnesses", {}).copy()
        harnesses[func_name] = harness_code
        
        # Determine version number for filename
        refinement_num = state.get("refinement_attempts", {}).get(func_name, 0)
        version_num = refinement_num + 1
        
        # Create harness directory
        harness_base_dir = "harnesses"
        os.makedirs(harness_base_dir, exist_ok=True)
        
        func_harness_dir = os.path.join(harness_base_dir, func_name)
        os.makedirs(func_harness_dir, exist_ok=True)
        
        # Save harness to file
        filename = os.path.join(func_harness_dir, f"v{version_num}.c")
        with open(filename, "w") as f:
            f.write(harness_code)
            f.flush()
            os.fsync(f.fileno())  # Force flush to disk
        
        # Calculate time
        generation_time = time.time() - generation_start
        
        # Update function times
        function_times = state.get("function_times", {}).copy()
        if func_name not in function_times:
            function_times[func_name] = {}
        function_times[func_name]["generation"] = generation_time
        
        logger.info(f"Successfully {'refined' if is_refinement else 'generated'} harness for {func_name} in {generation_time:.2f}s")
        return {
            "messages": [AIMessage(content=f"{'Refined' if is_refinement else 'Generated'} harness for function {func_name} in {generation_time:.2f}s including the actual function implementation with CBMC test resources")],
            "harnesses": harnesses,
            "harness_history": harness_history,
            "improvement_recommendation": "",
            "function_times": function_times,
            "next": "cbmc"  # Proceed to CBMC verification
        }
        
    except Exception as e:
        # Handle API errors
        error_msg = str(e)
        logger.error(f"Error generating harness for {func_name}: {error_msg}")
        print(f"\nERROR: API call failed when processing function {func_name}")
        print(f"Error message: {error_msg}")
        
        # Return to junction to try next function
        return {
            "messages": [AIMessage(content=f"Error generating harness for {func_name}: {error_msg}. Skipping to next function.")],
            "next": "junction"
        }

def route_from_generator(state):
    """Routes from generator to either cbmc or junction."""
    return state.get("next", "cbmc")