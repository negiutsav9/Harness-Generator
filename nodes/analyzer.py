"""
Analyzer node for CBMC harness generator workflow.
"""
import time
import os
import logging
from langchain_core.messages import AIMessage
from core.embedding_db import code_collection

# Set up logging
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                   handlers=[logging.FileHandler("cbmc_analyzer.log"), logging.StreamHandler()])
logger = logging.getLogger("analyzer")

def analyzer_node(state):

    """Analyzes code from CodeDB to identify functions with memory operations or arithmetic."""
    # Start timing for analysis phase
    analysis_start = time.time()
    
    logger.info("Starting analysis phase")
    
    try:
        # Get all functions from the code database
        all_functions = code_collection.get()
        target_functions = []
        
        logger.info(f"Retrieved {len(all_functions.get('ids', []))} functions from database")
        
        # Get source directory path
        source_dir = state.get("source_directory", "")
        
        # Set a timeout limit in seconds for analysis (5 minutes)
        timeout_limit = 300
        
        # Process functions to find those with memory operations or arithmetic
        # Only include functions from files directly in the source directory (not subdirectories)
        count = 0
        start_time = time.time()
        for i, metadata in enumerate(all_functions["metadatas"]):
            # Check for timeout
            if time.time() - start_time > timeout_limit:
                logger.warning(f"Analysis timeout after processing {count} functions. Proceeding with functions identified so far.")
                break
                
            func_id = all_functions["ids"][i]
            func_code = all_functions["documents"][i]
            file_path = metadata.get("file_path", "")
            
            # Log progress periodically
            count += 1
            if count % 20 == 0:
                logger.info(f"Processed {count}/{len(all_functions['ids'])} functions")
            
            try:
                # Skip functions from files in subdirectories like include, dependency, etc.
                if file_path:
                    # Check if this is a file directly in the source directory
                    if os.path.dirname(file_path) == source_dir:
                        # Only process files directly in source dir
                        # Check for memory operations
                        has_memory_ops = any(op in func_code for op in [
                            "malloc(", "calloc(", "realloc(", "free(", "alloca(", 
                            "new ", "delete ", "memcpy(", "memmove(", "memset(",
                            "&", "*", "->", "[]"  # Memory-related operators
                        ])
                        
                        # Check for arithmetic operations
                        has_arithmetic = any(op in func_code for op in [
                            "+", "-", "*", "/", "%",  # Basic arithmetic
                            "+=", "-=", "*=", "/=", "%=",  # Compound assignment
                            "++", "--",  # Increment/decrement
                            "==", "!=", "<", ">", "<=", ">=",  # Comparison operators
                            "<<", ">>", "&", "|", "^", "~",  # Bitwise operations
                            "fabs(", "sqrt(", "pow(", "sin(", "cos(",  # Math functions
                            "int ", "float ", "double ", "long "  # Numeric types
                        ])
                        
                        # Add this function if it deals with memory or arithmetic
                        if has_memory_ops or has_arithmetic:
                            target_functions.append(func_id)
                            logger.debug(f"Added function: {func_id}")
            except Exception as e:
                logger.error(f"Error processing function {func_id}: {str(e)}")
                continue
        
        # Remove duplicates if any
        target_functions = list(set(target_functions))
        
        # Sort functions alphabetically for consistent processing order
        target_functions.sort()
        
        # Count functions by category
        category_count = {
            "memory": sum(1 for i, metadata in enumerate(all_functions["metadatas"]) 
                      if any(op in all_functions["documents"][i] for op in 
                             ["malloc(", "calloc(", "realloc(", "free(", "memcpy("])),
            "arithmetic": sum(1 for i, metadata in enumerate(all_functions["metadatas"]) 
                         if any(op in all_functions["documents"][i] for op in 
                                ["+", "-", "*", "/", "%", "+=", "-=", "*=", "/="]))
        }
        
        # Log summary information
        logger.info(f"Analysis complete: identified {len(target_functions)} functions")
        logger.info(f"Functions by category: {category_count['memory']} memory, {category_count['arithmetic']} arithmetic")
        
        # Calculate time taken for analysis
        analysis_time = time.time() - analysis_start
        logger.info(f"Analysis completed in {analysis_time:.2f} seconds")
        
        return {
            "messages": [AIMessage(content=f"Analysis complete in {analysis_time:.2f}s. Identified {len(target_functions)} functions with memory or arithmetic operations. Breakdown: {category_count['memory']} with memory operations, {category_count['arithmetic']} with arithmetic operations.")],
            "vulnerable_functions": target_functions,
            "total_functions": len(target_functions),
            "current_function_index": 0  # Initialize the index counter
        }
    except Exception as e:
        logger.error(f"Error in analyzer node: {str(e)}", exc_info=True)
        # Return a minimal set to prevent complete failure
        return {
            "messages": [AIMessage(content=f"Error during analysis: {str(e)}. Proceeding with limited function set.")],
            "vulnerable_functions": target_functions[:10] if len(target_functions) > 10 else target_functions,
            "total_functions": len(target_functions[:10]) if len(target_functions) > 10 else len(target_functions),
            "current_function_index": 0
        }