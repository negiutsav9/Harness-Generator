"""
Code parsing utilities for the CBMC harness generator.
"""
import os
import re
from tqdm import tqdm
from core.embedding_db import code_collection, pattern_collection
import logging


logger = logging.getLogger("code_parser")


def embed_code(code: str, file_path: str = None) -> dict:
    """Embeds source code and stores it in the ChromaDB embedding database."""
    # Parse the code to extract functions
    functions = {}
    
    # Skip if code is empty
    if not code:
        logger.warning("Empty code provided for embedding")
        return {"functions": {}, "message": "No code to embed"}
    
    # Use a thread-safe flag to clear the collection only once per run
    # This static variable approach is better than using a global
    if not hasattr(embed_code, "_collection_cleared"):
        embed_code._collection_cleared = False
    
    # Clear existing collection only once at the start
    if not embed_code._collection_cleared:
        try:
            logger.info("First file being processed - clearing existing code collection")
            existing_ids = code_collection.get()["ids"]
            if existing_ids:
                logger.info(f"Deleting {len(existing_ids)} existing entries from code collection")
                code_collection.delete(ids=existing_ids)
            embed_code._collection_cleared = True
        except Exception as e:
            logger.error(f"Error clearing code collection: {str(e)}")
            embed_code._collection_cleared = True  # Mark as cleared even if it failed
    
    # Show file info
    file_name = os.path.basename(file_path) if file_path else "inline"
    logger.info(f"Processing file: {file_name}")
    
    try:
        # Use a simpler function pattern that's more reliable
        c_func_pattern = r"([\w\s\*]+)\s+(\w+)\s*\(([^)]*)\)\s*\{"
        
        # Use direct search instead of splitting first
        matches = list(re.finditer(c_func_pattern, code, re.MULTILINE))
        
        # Process each potential function without progress bar
        function_ids = []
        function_texts = []
        function_metadatas = []
        
        # Keep a set of function names to avoid duplicates
        seen_functions = set()
        
        # Check if this is a CBMC test file
        is_cbmc_test = False
        if file_path and ("test/cbmc" in file_path or "stubs" in file_path):
            is_cbmc_test = True
            logger.info(f"Identified CBMC test file: {file_path}")
        
        # Skip header files for faster processing
        if file_path and file_path.endswith(('.h', '.hpp')):
            # Handle header files with a different approach
            header_pattern = r"([\w\s\*]+)\s+(\w+)\s*\(([^)]*)\)\s*;"
            header_matches = re.finditer(header_pattern, code)
            for match in header_matches:
                func_name = match.group(2).strip()
                # Skip if func_name is a keyword
                if func_name in ['if', 'for', 'while', 'switch', 'return', 'include']:
                    continue
                # Create a function ID
                func_id = func_name
                if file_path:
                    file_basename = os.path.basename(file_path)
                    func_id = f"{file_basename}:{func_name}"
                
                # Mark CBMC test header files
                file_type = "cbmc_test_header" if is_cbmc_test else "header"
                
                functions[func_id] = {
                    "return_type": match.group(1).strip(),
                    "params": match.group(3).strip(),
                    "body": "",  # No body for header declarations
                    "full_text": match.group(0),
                    "file_path": file_path,
                    "original_name": func_name,
                    "file_type": file_type
                }
            logger.info(f"Processed header file with {len(functions)} declarations")
            
            # Add to ChromaDB
            if functions:
                logger.info(f"Adding {len(functions)} header declarations to ChromaDB")
                
                for func_id, func_data in functions.items():
                    function_ids.append(func_id)
                    function_texts.append(func_data["full_text"])
                    function_metadatas.append({
                        "name": func_data["original_name"],
                        "id": func_id,
                        "return_type": func_data["return_type"],
                        "params": func_data["params"],
                        "has_malloc": False,
                        "has_free": False,
                        "allocation_without_free": False,
                        "file_path": file_path if file_path else "inline",
                        "file_type": func_data["file_type"],
                        "is_cbmc_test": is_cbmc_test
                    })
                
                # Add to ChromaDB
                code_collection.add(
                    ids=function_ids,
                    documents=function_texts,
                    metadatas=function_metadatas
                )
            
            return {"functions": functions, "message": "Processed header file declarations"}
        
        # Process functions without tqdm progress bar
        logger.info(f"Analyzing {len(matches)} potential functions in {file_name}")
        processed_count = 0
        
        for match in matches:
            try:
                return_type = match.group(1).strip()
                func_name = match.group(2).strip()
                params = match.group(3).strip()
                
                # Skip if func_name is a keyword
                if func_name in ['if', 'for', 'while', 'switch', 'return', 'include']:
                    continue
                
                # Skip if we've already seen this function
                if func_name in seen_functions:
                    continue
                
                # Find function body
                start_pos = match.end()
                brace_count = 1
                end_pos = start_pos
                
                # Find the matching closing brace by counting
                try:
                    while brace_count > 0 and end_pos < len(code):
                        if code[end_pos] == '{':
                            brace_count += 1
                        elif code[end_pos] == '}':
                            brace_count -= 1
                        end_pos += 1
                except IndexError:
                    continue
                
                # If we couldn't find the end, set a max size
                if brace_count > 0:
                    end_pos = min(start_pos + 10000, len(code))
                
                # Extract body including braces
                body = code[start_pos-1:end_pos]
                
                # Create function ID with file info if provided
                func_id = func_name
                if file_path:
                    file_basename = os.path.basename(file_path)
                    func_id = f"{file_basename}:{func_name}"
                
                # Get full function text
                full_text = f"{return_type} {func_name}({params}) {body}"
                
                # Determine file type
                file_type = "source"
                if is_cbmc_test:
                    if "harness" in func_name.lower() or "harness" in file_path.lower():
                        file_type = "cbmc_harness"
                    elif "stub" in func_name.lower() or "stub" in file_path.lower() or "test/cbmc/stubs" in file_path:
                        file_type = "cbmc_stub"
                    else:
                        file_type = "cbmc_test"
                
                # Store in our result structures
                seen_functions.add(func_name)
                functions[func_id] = {
                    "return_type": return_type,
                    "params": params,
                    "body": body,
                    "full_text": full_text,
                    "file_path": file_path,
                    "original_name": func_name,
                    "has_malloc": "malloc(" in body,
                    "has_free": "free(" in body,
                    "file_type": file_type,
                    "is_cbmc_test": is_cbmc_test
                }
                
                # Add to arrays for ChromaDB
                function_ids.append(func_id)
                function_texts.append(full_text)
                function_metadatas.append({
                    "name": func_name,
                    "id": func_id,
                    "return_type": return_type,
                    "params": params,
                    "has_malloc": "malloc(" in body,
                    "has_free": "free(" in body,
                    "allocation_without_free": "malloc(" in body and "free(" not in body,
                    "file_path": file_path if file_path else "inline",
                    "file_type": file_type,
                    "is_cbmc_test": is_cbmc_test
                })
                
                processed_count += 1
                # Log progress periodically (every 10 functions)
                if processed_count % 10 == 0:
                    logger.debug(f"Processed {processed_count}/{len(matches)} functions")
                    
            except Exception as e:
                logger.debug(f"Error processing function: {e}")
        
        logger.info(f"Successfully processed {processed_count} functions from {file_name}")
        
        # Add to ChromaDB
        if function_ids:
            logger.info(f"Adding {len(function_ids)} functions to ChromaDB")
            code_collection.add(
                ids=function_ids,
                documents=function_texts,
                metadatas=function_metadatas
            )
    
    except Exception as e:
        logger.error(f"Error embedding code: {str(e)}")
    
    return {
        "functions": functions,
        "message": f"Successfully embedded {len(functions)} functions from {file_path}"
    }

def embed_cbmc_test_files(source_directory):
    """
    Find and embed all CBMC test files related to the source directory
    
    Args:
        source_directory: Base directory to look for CBMC test files
    
    Returns:
        Number of CBMC test files embedded
    """
    # Paths to look for CBMC test files
    cbmc_test_dirs = [
        os.path.join(source_directory, "test", "cbmc"),
        os.path.join(os.path.dirname(source_directory), "test", "cbmc"),
        "test/cbmc"
    ]
    
    cbmc_file_count = 0
    
    # Process each potential CBMC test directory
    for cbmc_dir in cbmc_test_dirs:
        if not os.path.exists(cbmc_dir):
            continue
            
        logger.info(f"Found CBMC test directory: {cbmc_dir}")
        
        # Process include directory
        include_dir = os.path.join(cbmc_dir, "include")
        if os.path.exists(include_dir):
            for root, _, files in os.walk(include_dir):
                for file in files:
                    if file.endswith(('.h', '.c', '.cpp', '.hpp')):
                        file_path = os.path.join(root, file)
                        try:
                            with open(file_path, 'r', encoding='utf-8') as f:
                                content = f.read()
                                if content:
                                    embed_code(content, file_path)
                                    cbmc_file_count += 1
                                    logger.info(f"Embedded CBMC include file: {file_path}")
                        except Exception as e:
                            logger.error(f"Error processing CBMC include file {file_path}: {str(e)}")
        
        # Process stubs directory
        stubs_dir = os.path.join(cbmc_dir, "stubs")
        if os.path.exists(stubs_dir):
            for root, _, files in os.walk(stubs_dir):
                for file in files:
                    if file.endswith(('.h', '.c', '.cpp', '.hpp')):
                        file_path = os.path.join(root, file)
                        try:
                            with open(file_path, 'r', encoding='utf-8') as f:
                                content = f.read()
                                if content:
                                    embed_code(content, file_path)
                                    cbmc_file_count += 1
                                    logger.info(f"Embedded CBMC stub file: {file_path}")
                        except Exception as e:
                            logger.error(f"Error processing CBMC stub file {file_path}: {str(e)}")
        
        # Process sources directory
        sources_dir = os.path.join(cbmc_dir, "sources")
        if os.path.exists(sources_dir):
            for root, _, files in os.walk(sources_dir):
                for file in files:
                    if file.endswith(('.h', '.c', '.cpp', '.hpp')):
                        file_path = os.path.join(root, file)
                        try:
                            with open(file_path, 'r', encoding='utf-8') as f:
                                content = f.read()
                                if content:
                                    embed_code(content, file_path)
                                    cbmc_file_count += 1
                                    logger.info(f"Embedded CBMC source file: {file_path}")
                        except Exception as e:
                            logger.error(f"Error processing CBMC source file {file_path}: {str(e)}")
                            
        # Process harness directory if it exists
        harness_dir = os.path.join(cbmc_dir, "harness")
        if os.path.exists(harness_dir):
            for root, _, files in os.walk(harness_dir):
                for file in files:
                    if file.endswith(('.h', '.c', '.cpp', '.hpp')):
                        file_path = os.path.join(root, file)
                        try:
                            with open(file_path, 'r', encoding='utf-8') as f:
                                content = f.read()
                                if content:
                                    embed_code(content, file_path)
                                    cbmc_file_count += 1
                                    logger.info(f"Embedded CBMC harness file: {file_path}")
                        except Exception as e:
                            logger.error(f"Error processing CBMC harness file {file_path}: {str(e)}")
                            
        # Found a valid CBMC test directory, so we can stop looking
        break
        
    # Log summary
    if cbmc_file_count > 0:
        logger.info(f"Successfully embedded {cbmc_file_count} CBMC test files")
    else:
        logger.warning("No CBMC test files found")
        
    return cbmc_file_count