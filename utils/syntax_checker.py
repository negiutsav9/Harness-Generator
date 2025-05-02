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
        
        # Skip empty files and header (.h) files
        if not content.strip():
            logger.warning(f"Skipping empty file: {file_path}")
            continue
            
        # Skip header files
        if file_path.lower().endswith('.h'):
            logger.info(f"Skipping header file: {file_path}")
            continue
        
        # Determine if file is in main source directory
        import os
        parent_dir_name = os.path.basename(os.path.dirname(file_path))
        is_in_source_dir = parent_dir_name == "source"
        file_location = "main source directory" if is_in_source_dir else "subdirectory"
        
        # Get full absolute path if available
        full_path = file_path
        if not os.path.isabs(file_path) and ":" not in file_path:  # Not already an absolute path or containing a device separator
            # Try to reconstruct the full path using directory information if we have it
            # This is best-effort and won't always be correct
            try:
                if parent_dir_name == "source":
                    # Look for a parent directory that might contain this file
                    potential_dirs = [d for d in os.listdir() if os.path.isdir(d)]
                    for d in potential_dirs:
                        potential_path = os.path.join(d, "source", os.path.basename(file_path))
                        if os.path.exists(potential_path):
                            full_path = os.path.abspath(potential_path)
                            break
            except:
                # If any error occurs, just use the original path
                pass
        
        # Construct prompt for syntax checking
        prompt = f"""
        You are an expert C/C++ compiler and static analyzer. Your task is to detect any syntax errors
        in the following C/C++ source code. Focus ONLY on actual syntax errors such as:
        
        - Missing semicolons
        - Unbalanced braces, parentheses, or brackets
        - Incorrect function declarations
        - Undefined variables or types
        - Invalid syntax or keywords
        - Missing include files that are commonly needed
        
        IMPORTANT: DO NOT treat comments as syntax errors, even if they have unusual formatting.
        Comments in C/C++ (// line comments or /* block comments */) should be completely ignored
        in your syntax analysis as they are not part of the executable code.
        
        Only report issues that would prevent the code from compiling. Do not comment on:
        - Style issues
        - Performance optimizations
        - Logic errors
        - Semantic errors that wouldn't prevent compilation
        - Documentation or comment issues
        
        For each error you find, you MUST provide:
        1. The exact line number where the error occurs
        2. A clear and specific error description
        3. A suggested fix
        
        Your response MUST start with the line number of the error, clearly formatted like:
        "Line 42: [error description]"
        
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
                syntax_errors[full_path] = error_report
                # Return immediately with just this error
                return syntax_errors
            else:
                logger.info(f"No syntax errors detected in {file_path} ({file_location})")
        
        except Exception as e:
            logger.error(f"Error checking syntax in {file_path}: {str(e)}")
            syntax_errors[full_path] = f"Error during syntax check: {str(e)}"
            # Also return immediately on exceptions
            return syntax_errors
    
    # If we get here, no errors were found
    logger.info(f"Completed checking {file_count} files. No syntax errors detected.")
    return syntax_errors