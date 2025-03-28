"""
Code parsing utilities for the CBMC harness generator.
"""
import os
import re
from tqdm import tqdm
from core.embedding_db import code_collection
import logging

logger = logging.getLogger("code_parser")

def extract_header_information(content, file_path):
    """Extract includes, macros, and declarations from header files."""
    header_info = {
        "includes": [],
        "macros": [],
        "type_definitions": [],
        "function_declarations": [],
        "file_path": file_path
    }
    
    # Extract includes
    include_pattern = r'#include\s+[<"]([^>"]+)[>"]'
    header_info["includes"] = re.findall(include_pattern, content)
    
    # Extract macro definitions
    macro_pattern = r'#define\s+(\w+)(?:\(([^)]*)\))?\s+(.+)'
    macro_matches = re.finditer(macro_pattern, content, re.MULTILINE)
    for match in macro_matches:
        macro_name = match.group(1)
        macro_params = match.group(2)
        macro_value = match.group(3).strip()
        header_info["macros"].append({
            "name": macro_name,
            "params": macro_params,
            "value": macro_value
        })
    
    # Extract type definitions (structs, enums, typedefs)
    typedef_pattern = r'typedef\s+([^;]+);'
    struct_pattern = r'(?:typedef\s+)?struct\s+(\w+)\s*{([^}]+)}'
    enum_pattern = r'(?:typedef\s+)?enum\s+(\w+)\s*{([^}]+)}'
    
    for typedef in re.finditer(typedef_pattern, content, re.MULTILINE | re.DOTALL):
        header_info["type_definitions"].append({
            "type": "typedef",
            "definition": typedef.group(0)
        })
    
    for struct in re.finditer(struct_pattern, content, re.MULTILINE | re.DOTALL):
        header_info["type_definitions"].append({
            "type": "struct",
            "name": struct.group(1),
            "definition": struct.group(0)
        })
        
    for enum in re.finditer(enum_pattern, content, re.MULTILINE | re.DOTALL):
        header_info["type_definitions"].append({
            "type": "enum",
            "name": enum.group(1),
            "definition": enum.group(0)
        })
    
    # Extract function declarations (not definitions)
    func_decl_pattern = r'([\w\s\*]+)\s+(\w+)\s*\(([^)]*)\)\s*;'
    for match in re.finditer(func_decl_pattern, content, re.MULTILINE):
        return_type = match.group(1).strip()
        func_name = match.group(2)
        params = match.group(3).strip()
        
        # Skip if func_name is a keyword
        if func_name in ['if', 'for', 'while', 'switch', 'return', 'include']:
            continue
            
        header_info["function_declarations"].append({
            "name": func_name,
            "return_type": return_type,
            "params": params,
            "declaration": match.group(0)
        })
    
    return header_info

def embed_code(code: str, file_path: str = None) -> dict:
    """Embeds source code and stores it in the ChromaDB embedding database."""
    # Parse the code to extract functions
    functions = {}
    header_chunks = {}
    
    # Skip if code is empty
    if not code:
        logger.warning("Empty code provided for embedding")
        return {"functions": {}, "headers": {}, "message": "No code to embed"}
    
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
    
    # Special handling for header files
    is_header = file_path and file_path.endswith(('.h', '.hpp'))
    
    if is_header:
        # Process header file specially
        header_info = extract_header_information(code, file_path)
        
        # Store header file information with file path as key
        header_id = os.path.basename(file_path)
        header_chunks[header_id] = header_info
        
        # Add each function declaration to the function database
        for decl in header_info["function_declarations"]:
            func_id = f"{header_id}:{decl['name']}"
            functions[func_id] = {
                "return_type": decl["return_type"],
                "params": decl["params"],
                "body": "",  # No body for declarations
                "full_text": decl["declaration"],
                "file_path": file_path,
                "original_name": decl["name"],
                "is_declaration_only": True
            }
            
        # Add header information to the database
        try:
            header_document = (
                f"Header file: {header_id}\n"
                f"Includes: {', '.join(header_info['includes'])}\n"
                f"Function declarations: {len(header_info['function_declarations'])}\n"
                f"Type definitions: {len(header_info['type_definitions'])}\n"
                f"Macros: {len(header_info['macros'])}"
            )
            
            # Add header to collection
            code_collection.add(
                ids=[f"header:{header_id}"],
                documents=[header_document],
                metadatas=[{
                    "type": "header",
                    "file_path": file_path,
                    "includes": header_info["includes"],
                    "declaration_count": len(header_info["function_declarations"]),
                    "typedef_count": len(header_info["type_definitions"]),
                    "macro_count": len(header_info["macros"])
                }]
            )
            
            # Add function declarations to collection separately
            for decl in header_info["function_declarations"]:
                code_collection.add(
                    ids=[f"declaration:{header_id}:{decl['name']}"],
                    documents=[decl["declaration"]],
                    metadatas=[{
                        "type": "function_declaration",
                        "name": decl["name"],
                        "return_type": decl["return_type"],
                        "params": decl["params"],
                        "file_path": file_path,
                        "header": header_id
                    }]
                )
            
            logger.info(f"Processed header file {header_id} with {len(header_info['function_declarations'])} declarations")
        except Exception as e:
            logger.error(f"Error adding header information to database: {str(e)}")
        
        return {"functions": functions, "headers": header_chunks, "message": "Processed header file declarations"}
    
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
                
                # Extract function calls within this function
                function_calls = re.findall(r'\b(\w+)\s*\(', body)
                # Remove duplicates while preserving order
                function_calls = list(dict.fromkeys(function_calls))
                
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
                    "function_calls": function_calls,
                    "is_declaration_only": False
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
                    "function_calls": function_calls,
                    "is_implementation": True
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
        "headers": header_chunks,
        "message": f"Successfully embedded {len(functions)} functions from {file_path}"
    }