"""
Syntax error detection utility using LLMs for the CBMC harness generator.
"""
import logging
from langchain_core.messages import HumanMessage
from utils.llm_utils import setup_llm

logger = logging.getLogger("syntax_checker")

def detect_syntax_errors(source_files, llm_choice='claude'):
    """
    Detect syntax errors in C source files using an LLM.
    Exits immediately on first error found to save resources.
    
    Args:
        source_files: Dictionary mapping file paths to their content
        llm_choice: LLM to use for syntax checking ('claude', 'openai', or 'gemini')
        
    Returns:
        Dictionary with at most one entry mapping file path to error description,
        or empty dictionary if no errors found
    """
    logger.info(f"Checking syntax errors in {len(source_files)} files using {llm_choice}")
    
    # Set up the LLM
    llm = setup_llm(llm_choice)
    
    # Dictionary to store detected errors (will contain at most one file)
    syntax_errors = {}
    
    # Process each file, stopping at the first error
    file_count = 0
    for file_path, content in source_files.items():
        file_count += 1
        logger.info(f"Checking file {file_count}/{len(source_files)}: {file_path}")
        
        # Skip empty files
        if not content.strip():
            logger.warning(f"Skipping empty file: {file_path}")
            continue
        
        # Determine if file is in main source directory
        import os
        parent_dir_name = os.path.basename(os.path.dirname(file_path))
        is_in_source_dir = parent_dir_name == "source"
        file_location = "main source directory" if is_in_source_dir else "subdirectory"
        
        # Construct prompt for syntax checking
        prompt = f"""
        You are an expert C/C++ compiler and static analyzer. Your task is to detect any syntax errors
        in the following C/C++ source code. Focus ONLY on syntax errors such as:
        
        - Missing semicolons
        - Unbalanced braces, parentheses, or brackets
        - Incorrect function declarations
        - Undefined variables or types
        - Invalid syntax or keywords
        - Missing include files that are commonly needed
        
        Only report issues that would prevent the code from compiling. Do not comment on:
        - Style issues
        - Performance optimizations
        - Logic errors
        - Semantic errors that wouldn't prevent compilation
        
        For each error you find, provide:
        1. The line number
        2. The error description
        3. A suggested fix
        
        If there are no syntax errors, respond with "No syntax errors detected."
        
        Here is the code to analyze from file {file_path}:
        
        ```c
        {content}
        ```
        """
        
        try:
            # Send the prompt to the LLM
            messages = [HumanMessage(content=prompt)]
            response = llm.invoke(messages)
            
            # Process the response
            error_report = response.content.strip()
            
            # Exit immediately if errors are found
            if "No syntax errors detected" not in error_report:
                logger.warning(f"STOPPING: Detected syntax errors in {file_path} ({file_location})")
                syntax_errors[file_path] = error_report
                # Return immediately with just this error
                return syntax_errors
            else:
                logger.info(f"No syntax errors detected in {file_path} ({file_location})")
        
        except Exception as e:
            logger.error(f"Error checking syntax in {file_path}: {str(e)}")
            syntax_errors[file_path] = f"Error during syntax check: {str(e)}"
            # Also return immediately on exceptions
            return syntax_errors
    
    # If we get here, no errors were found
    logger.info(f"Completed checking {file_count} files. No syntax errors detected.")
    return syntax_errors