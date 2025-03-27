"""
utils/embedding_utils.py - Module for handling embedding database access and analysis.
"""
import re
import logging
import os
import sys
from core import embedding_db

logger = logging.getLogger("embedding_utils")

def get_existing_definitions():
    """
    Extract existing macro definitions, types, and structures from the embedding database.
    
    Returns:
        Dictionary containing discovered definitions
    """
    definitions = {
        "macros": set(),
        "types": set(),
        "enums": set()
    }
    
    try:
        # Query all documents in the database
        results = embedding_db.code_collection.get(include=["documents"])
        
        if not results or not results["documents"]:
            logger.warning("No documents found in embedding database")
            return definitions
            
        logger.info(f"Scanning {len(results['documents'])} documents for definitions")
        
        # Process each document
        for doc in results["documents"]:
            # Find macro definitions
            macro_pattern = r"#define\s+(\w+)"
            for match in re.finditer(macro_pattern, doc):
                macro_name = match.group(1)
                definitions["macros"].add(macro_name)
            
            # Find typedef definitions
            typedef_pattern = r"typedef\s+.+\s+(\w+)\s*;"
            for match in re.finditer(typedef_pattern, doc):
                type_name = match.group(1)
                definitions["types"].add(type_name)
            
            # Find enum definitions
            enum_pattern = r"enum\s+(\w+)"
            for match in re.finditer(enum_pattern, doc):
                enum_name = match.group(1)
                definitions["enums"].add(enum_name)
                
        logger.info(f"Found {len(definitions['macros'])} macros, {len(definitions['types'])} types, "
                    f"and {len(definitions['enums'])} enums in database")
        
        return definitions
    
    except Exception as e:
        logger.error(f"Error extracting definitions: {str(e)}")
        return definitions

def check_harness_conflicts(harness_code, existing_definitions=None):
    """
    Check a generated harness for conflicts with existing definitions.
    
    Args:
        harness_code: The generated harness code
        existing_definitions: Dictionary of existing definitions (if None, will be fetched)
        
    Returns:
        Tuple of (modified_harness, conflicts_found)
    """
    if existing_definitions is None:
        existing_definitions = get_existing_definitions()
    
    conflicts_found = False
    modified_harness = harness_code
    
    # Check for macro redefinitions
    for macro in existing_definitions["macros"]:
        pattern = rf"#define\s+{re.escape(macro)}\b"
        if re.search(pattern, harness_code):
            # Add conditional guard around the macro
            modified_harness = re.sub(
                pattern,
                f"#ifndef {macro}\n#define {macro}",
                modified_harness
            )
            conflicts_found = True
            logger.info(f"Found conflicting macro definition: {macro}")
    
    # Check for type redefinitions
    for type_name in existing_definitions["types"]:
        pattern = rf"typedef\s+.+\s+{re.escape(type_name)}\s*;"
        if re.search(pattern, harness_code):
            # Comment out the conflicting type definition
            modified_harness = re.sub(
                pattern,
                f"/* Type already defined elsewhere: \\0 */",
                modified_harness
            )
            conflicts_found = True
            logger.info(f"Found conflicting type definition: {type_name}")
    
    # Check for enum redefinitions
    for enum_name in existing_definitions["enums"]:
        pattern = rf"enum\s+{re.escape(enum_name)}"
        if re.search(pattern, harness_code):
            # Comment out the conflicting enum definition
            modified_harness = re.sub(
                pattern,
                f"/* Enum already defined elsewhere: \\0 */",
                modified_harness
            )
            conflicts_found = True
            logger.info(f"Found conflicting enum definition: {enum_name}")
    
    return modified_harness, conflicts_found