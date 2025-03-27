"""
File handling utilities for the CBMC harness generator.
"""
import os
import glob
import shutil
import logging
from utils.code_parser import embed_code, embed_cbmc_test_files

logger = logging.getLogger("file_utils")

def process_directory(directory_path: str) -> dict:
    """
    Process all C source files in the source/source_code subdirectory of the given directory.
    
    Args:
        directory_path: Path to the directory containing C source files
        
    Returns:
        Dictionary mapping file paths to their content
    """
    source_files = {}
    
    # Check if the directory exists
    if not os.path.isdir(directory_path):
        logger.error(f"Directory '{directory_path}' does not exist")
        return source_files
    
    # Look for source/source_code subdirectory
    source_subdir = os.path.join(directory_path, "source")
    if not os.path.isdir(source_subdir):
        logger.warning(f"'{source_subdir}' directory not found. Using top directory.")
        source_subdir = directory_path
    
    logger.info(f"Looking for source files in: {source_subdir}")
    
    # Find all C source files in the source subdirectory
    c_file_patterns = ['*.c', '*.h', '*.cpp', '*.hpp']
    for pattern in c_file_patterns:
        file_paths = glob.glob(os.path.join(source_subdir, "**", pattern), recursive=True)
        for file_path in file_paths:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if not content:
                        print(f"Warning: Empty file: {file_path}")
                    source_files[file_path] = content
                    print(f"Processed file: {file_path} ({len(content)} bytes)")
            except UnicodeDecodeError:
                # Try with a different encoding if UTF-8 fails
                try:
                    with open(file_path, 'r', encoding='latin-1') as f:
                        content = f.read()
                        source_files[file_path] = content
                        print(f"Processed file with latin-1 encoding: {file_path} ({len(content)} bytes)")
                except Exception as e:
                    print(f"Error reading file {file_path}: {str(e)}")
            except Exception as e:
                print(f"Error reading file {file_path}: {str(e)}")
    
    # Also look for CBMC test files
    cbmc_test_files_count = embed_cbmc_test_files(directory_path)
    if cbmc_test_files_count > 0:
        logger.info(f"Embedded {cbmc_test_files_count} CBMC test files")
    
    return source_files

def calculate_recursion_limit(num_files):
    """Calculate a safe recursion limit based on estimated complexity."""
    # Estimate number of functions based on number of files
    # On average, a C file might have 5-10 functions
    estimated_functions_per_file = 10
    estimated_functions = num_files * estimated_functions_per_file
    
    # Default max refinements per function
    max_refinements = 3
    
    # Base recursion limit
    base_limit = 20
    
    # Calculate limit based on estimated functions and refinements
    # Formula: base + (estimated_functions * (refinements + 1) * nodes_per_function_cycle)
    nodes_per_function_cycle = 4  # junction, generator, cbmc, evaluator
    function_recursion = estimated_functions * (max_refinements + 1) * nodes_per_function_cycle
    
    # Add safety buffer - minimum 100, scales with function count
    safe_limit = max(100, base_limit + function_recursion)
    
    print(f"Set recursion limit to {safe_limit} (estimated {estimated_functions} functions from {num_files} files)")
    
    return safe_limit

def setup_verification_directories():
    """
    Set up the directory structure for verification.
    """
    # Create organized directory structure
    directories = [
        "harnesses",
        "verification",
        "verification/src",
        "verification/include",
        "verification/stubs",
        "verification/sources",
        "reports"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    return directories

def copy_cbmc_test_files(source_directory, dest_directory="verification"):
    """
    Find and copy all CBMC test files to the verification directory
    
    Args:
        source_directory: Base directory to look for CBMC test files
        dest_directory: Destination directory for CBMC test files
    
    Returns:
        Number of files copied
    """
    # Paths to look for CBMC test files
    cbmc_test_dirs = [
        os.path.join(source_directory, "test", "cbmc"),
        os.path.join(os.path.dirname(source_directory), "test", "cbmc"),
        "test/cbmc"
    ]
    
    file_count = 0
    
    # Process each potential CBMC test directory
    for cbmc_dir in cbmc_test_dirs:
        if not os.path.exists(cbmc_dir):
            continue
            
        logger.info(f"Found CBMC test directory: {cbmc_dir}")
        
        # Process include directory
        include_dir = os.path.join(cbmc_dir, "include")
        if os.path.exists(include_dir):
            dest_include_dir = os.path.join(dest_directory, "include")
            os.makedirs(dest_include_dir, exist_ok=True)
            
            for root, _, files in os.walk(include_dir):
                for file in files:
                    if file.endswith(('.h', '.c', '.cpp', '.hpp')):
                        src_file = os.path.join(root, file)
                        dest_file = os.path.join(dest_include_dir, file)
                        try:
                            shutil.copy2(src_file, dest_file)
                            file_count += 1
                            logger.info(f"Copied CBMC include file: {file} to {dest_file}")
                        except Exception as e:
                            logger.error(f"Error copying CBMC include file {src_file}: {str(e)}")
        
        # Process stubs directory
        stubs_dir = os.path.join(cbmc_dir, "stubs")
        if os.path.exists(stubs_dir):
            dest_stubs_dir = os.path.join(dest_directory, "stubs")
            os.makedirs(dest_stubs_dir, exist_ok=True)
            
            for root, _, files in os.walk(stubs_dir):
                for file in files:
                    if file.endswith(('.h', '.c', '.cpp', '.hpp')):
                        src_file = os.path.join(root, file)
                        dest_file = os.path.join(dest_stubs_dir, file)
                        try:
                            shutil.copy2(src_file, dest_file)
                            file_count += 1
                            logger.info(f"Copied CBMC stub file: {file} to {dest_file}")
                        except Exception as e:
                            logger.error(f"Error copying CBMC stub file {src_file}: {str(e)}")
        
        # Process sources directory
        sources_dir = os.path.join(cbmc_dir, "sources")
        if os.path.exists(sources_dir):
            dest_sources_dir = os.path.join(dest_directory, "sources")
            os.makedirs(dest_sources_dir, exist_ok=True)
            
            for root, _, files in os.walk(sources_dir):
                for file in files:
                    if file.endswith(('.h', '.c', '.cpp', '.hpp')):
                        src_file = os.path.join(root, file)
                        dest_file = os.path.join(dest_sources_dir, file)
                        try:
                            shutil.copy2(src_file, dest_file)
                            file_count += 1
                            logger.info(f"Copied CBMC source file: {file} to {dest_file}")
                        except Exception as e:
                            logger.error(f"Error copying CBMC source file {src_file}: {str(e)}")
        
        # Found a valid CBMC test directory, so we can stop looking
        break
        
    # Log summary
    if file_count > 0:
        logger.info(f"Successfully copied {file_count} CBMC test files to {dest_directory}")
    else:
        logger.warning("No CBMC test files found to copy")
        
    return file_count