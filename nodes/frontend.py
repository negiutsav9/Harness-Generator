"""
Frontend node for CBMC harness generator workflow.
"""
import os
import re
import time
from langchain_core.messages import AIMessage, HumanMessage
from utils.file_utils import process_directory
from utils.syntax_checker import detect_syntax_errors
import logging

logger = logging.getLogger("frontend")

def frontend_node(state):
    """Extracts source code from user messages and initializes timing."""
    # Start timing for this module
    module_start_time = time.time()
    
    # Start timing the overall process if not already present
    if "main_start_time" not in state:
        state["main_start_time"] = time.time()

    logger.info("Processing incoming source code request")
    
    # Check if the user specified a directory path
    directory_path = None
    multiple_files = {}
    
    for message in reversed(state["messages"]):
        if isinstance(message, HumanMessage) and "directory:" in message.content.lower():
            # Extract directory path using regex
            dir_match = re.search(r'directory:\s*([^\s]+)', message.content, re.IGNORECASE)
            if dir_match:
                directory_path = dir_match.group(1)
                print(f"Directory path detected: {directory_path}")
                multiple_files = process_directory(directory_path)
                
                # Add CBMC test files to embedding
                cbmc_dirs = [
                    os.path.join(directory_path, "test", "cbmc", "include"),
                    os.path.join(directory_path, "test", "cbmc", "stubs"),
                    os.path.join(directory_path, "test", "cbmc", "sources")
                ]

                # Look one level up if not found
                if not any(os.path.exists(d) for d in cbmc_dirs):
                    cbmc_dirs = [
                        os.path.join(os.path.dirname(directory_path), "test", "cbmc", "include"),
                        os.path.join(os.path.dirname(directory_path), "test", "cbmc", "stubs"),
                        os.path.join(os.path.dirname(directory_path), "test", "cbmc", "sources")
                    ]

                # Process CBMC files
                for cbmc_dir in cbmc_dirs:
                    if os.path.exists(cbmc_dir):
                        print(f"Adding CBMC test files from {cbmc_dir}")
                        cbmc_files = process_directory(cbmc_dir)
                        # Add to our source files dictionary
                        multiple_files.update(cbmc_files)
                
                if multiple_files:
                    # Determine source subdirectory for reporting
                    source_subdir = os.path.join(directory_path, "source")
                    if not os.path.isdir(source_subdir):
                        source_subdir = directory_path
                    
                    # Initialize file_functions dictionary to track functions per file
                    file_functions = {}
                    
                    # Create a combined source for backward compatibility
                    combined_source = ""
                    for file_path, content in multiple_files.items():
                        combined_source += f"/* File: {file_path} */\n{content}\n\n"
                        file_functions[file_path] = []  # Initialize empty function list for each file
                    
                    logger.info(f"Found {len(multiple_files)} C source files in {directory_path}")
                    print(f"Combined source code length: {len(combined_source)} bytes")
                    
                    # Check for syntax errors in all source files
                    print("Performing syntax error detection using LLM...")
                    # Get LLM choice from state or use default
                    llm_choice = state.get("llm_choice", "claude")
                    syntax_errors = detect_syntax_errors(multiple_files, llm_choice)
                    
                    # If syntax errors are found, exit early with error message
                    if syntax_errors:
                        # Get file path and error details
                        file_path = list(syntax_errors.keys())[0]
                        error_details = syntax_errors[file_path]
                        
                        # Format the file path for better readability
                        rel_path = file_path
                        if directory_path in file_path:
                            rel_path = file_path[len(directory_path)+1:]
                        
                        # Create error message focusing on the line number
                        error_message = f"⚠️ SYNTAX ERROR DETECTED in {rel_path}:\n\n{error_details}"
                        ai_message = AIMessage(content=f"⚠️ ERROR: Processing halted. Please fix the syntax error before proceeding.\n\n{error_message}")
                        
                        logger.error(f"Syntax error found in {rel_path}. Exiting.")
                        print(f"SYNTAX ERROR: Found error in {rel_path}. Halting workflow.")
                        
                        # Return with syntax error flag for immediate exit
                        return {
                            "messages": [ai_message],
                            "syntax_error": True,
                            "exit_reason": "syntax_error",
                            "exit_message": error_message,
                            "next": "output"  # Force jump to output node
                        }
                    
                    # Continue normal flow if no errors found
                    return {
                        "messages": [AIMessage(content=f"Processing directory: {directory_path}. Found {len(multiple_files)} C source files in source code directory. No syntax errors detected.")],
                        "source_files": multiple_files,
                        "source_code": combined_source,  # For backward compatibility
                        "start_time": module_start_time,
                        "is_directory_mode": True,
                        "source_directory": source_subdir,
                        "file_functions": file_functions  # Initialize tracking of functions per file
                    }
                else:
                    logger.warning(f"No C source files found in {directory_path}")
                    return {
                        "messages": [AIMessage(content=f"No C source files found in source directory of: {directory_path}")],
                        "source_code": "",
                        "source_files": {},
                        "start_time": module_start_time,
                        "is_directory_mode": False,
                        "file_functions": {}
                    }
    
    # Handle source code already provided from command-line file argument or fall back to inline code
    if not state.get("source_code") or not state.get("source_files"):
        # Check if source files are already populated from main.py's file argument
        if state.get("source_code") and state.get("source_files"):
            # Source code already exists from command-line argument
            source_code = state.get("source_code")
            source_files = state.get("source_files")
            
            # Get the file name (should be just one file)
            file_name = list(source_files.keys())[0] if source_files else "command_line_file"
            
            # Log that we're using pre-checked source code
            logger.info(f"Using pre-checked source code from command line file: {file_name}")
            print(f"Using pre-checked source code from file: {file_name}")
            
            # Note: Syntax error checking for single file from command line is now done in main.py
            # This avoids double-checking and ensures a consistent approach
            syntax_errors = {}
            
            # If syntax errors are found, exit early with error message
            if syntax_errors:
                error_file = list(syntax_errors.keys())[0]
                error_details = syntax_errors[error_file]
                error_message = f"⚠️ SYNTAX ERROR DETECTED in {error_file}:\n\n{error_details}"
                ai_message = AIMessage(content=f"⚠️ ERROR: Processing halted. Please fix the syntax error before proceeding.\n\n{error_message}")
                
                logger.error(f"Syntax error found in {error_file}. Exiting.")
                print(f"SYNTAX ERROR: Found error in {error_file}. Halting workflow.")
                
                # Return with syntax error flag for immediate exit
                return {
                    "messages": [ai_message],
                    "syntax_error": True,
                    "exit_reason": "syntax_error",
                    "exit_message": error_message,
                    "next": "output"  # Force jump to output node
                }
                
            # Continue normal flow if no errors found
            return {
                "messages": [AIMessage(content=f"Processing file: {file_name} ({len(source_code)} characters). No syntax errors detected. Proceeding with code embedding.")],
                "source_code": source_code,
                "source_files": source_files,
                "start_time": module_start_time,
                "is_directory_mode": False,
                "file_functions": {file_name: []}  # Initialize tracking for single file
            }
        
        # Fall back to extracting code from message content if no file provided
        for message in reversed(state["messages"]):
            if isinstance(message, HumanMessage) and "```" in message.content:
                match = re.search(r'```(?:\w+)?\n(.+?)\n```', message.content, re.DOTALL)
                if match:
                    source_code = match.group(1)
                    
                    # Check for syntax errors in the inline code
                    print("Performing syntax error detection on inline code using LLM...")
                    llm_choice = state.get("llm_used", state.get("llm_choice", "claude"))
                    syntax_errors = detect_syntax_errors({"inline_code": source_code}, llm_choice)
                    
                    # If syntax errors are found, exit early with error message
                    if syntax_errors:
                        error_file = list(syntax_errors.keys())[0]
                        error_details = syntax_errors[error_file]
                        error_message = f"⚠️ SYNTAX ERROR DETECTED in inline code:\n\n{error_details}"
                        ai_message = AIMessage(content=f"⚠️ ERROR: Processing halted. Please fix the syntax error before proceeding.\n\n{error_message}")
                        
                        logger.error("Syntax error found in inline code. Exiting.")
                        print("SYNTAX ERROR: Found error in inline code. Halting workflow.")
                        
                        # Return with syntax error flag for immediate exit
                        return {
                            "messages": [ai_message],
                            "syntax_error": True,
                            "exit_reason": "syntax_error",
                            "exit_message": error_message,
                            "next": "output"  # Force jump to output node
                        }
                        
                    # Continue normal flow if no errors found
                    return {
                        "messages": [AIMessage(content=f"Received source code ({len(source_code)} characters). No syntax errors detected. Proceeding with code embedding.")],
                        "source_code": source_code,
                        "source_files": {"inline_code": source_code},  # Add to source_files for consistency
                        "start_time": module_start_time,
                        "is_directory_mode": False,
                        "file_functions": {"inline_code": []}  # Initialize tracking for single file
                    }
    
    # If no source code found or already exists
    # Calculate module execution time
    module_time = time.time() - module_start_time
    
    # Update module timings
    module_timings = state.get("module_timings", {})
    module_timings["frontend"] = module_time
    
    logger.info(f"Frontend node completed in {module_time:.2f}s")
    
    return {
        "messages": [AIMessage(content=f"Proceeding with code embedding.")],
        "source_code": state.get("source_code", ""),
        "source_files": state.get("source_files", {}),
        "start_time": state.get("main_start_time", time.time()),
        "is_directory_mode": state.get("is_directory_mode", False),
        "file_functions": state.get("file_functions", {}),
        "module_timings": module_timings
    }