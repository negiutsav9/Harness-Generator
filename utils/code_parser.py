"""
Code parsing utilities for the CBMC harness generator.
"""
import os
import re
from tqdm import tqdm
from core.embedding_db import code_collection
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
                functions[func_id] = {
                    "return_type": match.group(1).strip(),
                    "params": match.group(3).strip(),
                    "body": "",  # No body for header declarations
                    "full_text": match.group(0),
                    "file_path": file_path,
                    "original_name": func_name
                }
            logger.info(f"Processed header file with {len(functions)} declarations")
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
                    "has_free": "free(" in body
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
                    "file_path": file_path if file_path else "inline"
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