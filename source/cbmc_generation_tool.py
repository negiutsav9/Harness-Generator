import os
import re
import glob
import argparse
import json
import tempfile
import subprocess
from typing import Dict, List, Any, Literal
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from langgraph.graph import MessagesState, StateGraph, START, END
from langchain_anthropic import ChatAnthropic
import chromadb
from chromadb.utils import embedding_functions

os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Set up ChromaDB
chroma_client = chromadb.Client()
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# Create collections
try:
    code_collection = chroma_client.get_collection("code_embeddings")
except:
    code_collection = chroma_client.create_collection(
        name="code_embeddings",
        embedding_function=sentence_transformer_ef,
        metadata={"hnsw:space": "cosine"}
    )

try:
    pattern_collection = chroma_client.get_collection("pattern_embeddings")
except:
    pattern_collection = chroma_client.create_collection(
        name="pattern_embeddings",
        embedding_function=sentence_transformer_ef,
        metadata={"hnsw:space": "cosine"}
    )
    
    # Initialize pattern collection with memory and arithmetic patterns
    pattern_collection.add(
        ids=[
            # Memory patterns
            "pattern1", "pattern2", "pattern3", "pattern4", "pattern5",
            # Arithmetic patterns
            "pattern6", "pattern7", "pattern8", "pattern9", "pattern10",
            # CBMC verification knowledge
            "cbmc1", "cbmc2", "cbmc3", "cbmc4", "cbmc5", "cbmc6"
        ],
        documents=[
            # Memory patterns
            "Allocation without corresponding deallocation (malloc without free)",
            "Nested malloc calls with potential for partial free",
            "Conditional free that might not execute in all paths",
            "Memory leak through improper return path",
            "Double free or invalid free operations",
            
            # Arithmetic patterns
            "Integer overflow in arithmetic operations",
            "Division by zero risk",
            "Buffer overflow through array indexing",
            "Pointer arithmetic exceeding bounds",
            "Type conversion issues leading to data loss",
            
            # CBMC verification knowledge
            "CBMC memory-leak-check verification for allocated but not freed memory",
            "CBMC memory-cleanup-check verification for proper memory cleanup before exit",
            "CBMC bounds-check verification for array access within bounds",
            "CBMC pointer-overflow-check verification for pointer arithmetic operations",
            "CBMC conversion-check verification for problematic type conversions",
            "CBMC div-by-zero-check verification for division by zero risks"
        ],
        metadatas=[
            # Memory patterns metadata
            {
                "name": "malloc_without_free",
                "category": "memory",
                "description": "Allocation without corresponding deallocation",
                "severity": "high",
                "verification_strategy": "Check all execution paths for memory deallocation",
                "cbmc_flags": "--memory-leak-check",
                "assertion_template": "__CPROVER_assert(ptr == NULL, \"Memory leak detected\");"
            },
            {
                "name": "nested_malloc",
                "category": "memory",
                "description": "Nested malloc calls with potential for partial free",
                "severity": "medium",
                "verification_strategy": "Ensure all allocations are freed in all execution paths",
                "cbmc_flags": "--memory-leak-check",
                "assertion_template": "__CPROVER_assert(ptr1 == NULL && ptr2 == NULL, \"Nested memory leak detected\");"
            },
            {
                "name": "conditional_free",
                "category": "memory",
                "description": "Conditional free that might not execute",
                "severity": "medium",
                "verification_strategy": "Verify all conditions that lead to memory release",
                "cbmc_flags": "--memory-leak-check",
                "assertion_template": "__CPROVER_assert(condition || ptr == NULL, \"Conditional path may leak memory\");"
            },
            {
                "name": "return_leak",
                "category": "memory",
                "description": "Memory leak through improper return path",
                "severity": "medium",
                "verification_strategy": "Check all return paths for proper memory cleanup",
                "cbmc_flags": "--memory-leak-check --memory-cleanup-check",
                "assertion_template": "__CPROVER_assert(returned_ptr == NULL, \"Function may leak memory through return\");"
            },
            {
                "name": "double_free",
                "category": "memory",
                "description": "Double free or invalid free operations",
                "severity": "high",
                "verification_strategy": "Ensure each pointer is freed exactly once",
                "cbmc_flags": "--memory-leak-check",
                "assertion_template": "__CPROVER_assert(!freed[ptr_index], \"Potential double free\");"
            },
            
            # Arithmetic patterns metadata
            {
                "name": "integer_overflow",
                "category": "arithmetic",
                "description": "Integer overflow in arithmetic operations",
                "severity": "medium",
                "verification_strategy": "Check bounds of integer arithmetic",
                "cbmc_flags": "--conversion-check",
                "assertion_template": "__CPROVER_assert(result >= INT_MIN && result <= INT_MAX, \"Integer overflow detected\");"
            },
            {
                "name": "division_by_zero",
                "category": "arithmetic",
                "description": "Division by zero risk",
                "severity": "high",
                "verification_strategy": "Verify divisors are non-zero",
                "cbmc_flags": "--div-by-zero-check",
                "assertion_template": "__CPROVER_assume(divisor != 0);"
            },
            {
                "name": "buffer_overflow",
                "category": "arithmetic",
                "description": "Buffer overflow through array indexing",
                "severity": "high",
                "verification_strategy": "Ensure array indices are within bounds",
                "cbmc_flags": "--bounds-check",
                "assertion_template": "__CPROVER_assert(index >= 0 && index < array_size, \"Buffer overflow detected\");"
            },
            {
                "name": "pointer_arithmetic",
                "category": "arithmetic",
                "description": "Pointer arithmetic exceeding bounds",
                "severity": "high",
                "verification_strategy": "Verify pointer arithmetic stays within allocated bounds",
                "cbmc_flags": "--pointer-overflow-check",
                "assertion_template": "__CPROVER_assert(ptr >= base && ptr < base + size, \"Pointer arithmetic out of bounds\");"
            },
            {
                "name": "type_conversion",
                "category": "arithmetic",
                "description": "Type conversion issues leading to data loss",
                "severity": "low",
                "verification_strategy": "Check for potential data loss in type conversions",
                "cbmc_flags": "--conversion-check",
                "assertion_template": "__CPROVER_assert(orig_value == (OrigType)((DestType)orig_value), \"Data loss in type conversion\");"
            },
            
            # CBMC verification knowledge metadata
            {
                "name": "cbmc_memory_leak_check",
                "category": "cbmc_verification",
                "description": "Checks for memory that is allocated but not freed",
                "verification_details": "Detects allocated memory that is never freed, memory that becomes unreachable, and double free operations",
                "harness_usage": "Create appropriate memory allocations and verify they are properly freed",
                "flag": "--memory-leak-check"
            },
            {
                "name": "cbmc_memory_cleanup_check",
                "category": "cbmc_verification",
                "description": "Verifies all allocated memory is properly freed before program exit",
                "verification_details": "More stringent than memory-leak-check, requires explicit cleanup of all allocations",
                "harness_usage": "Ensure all memory allocations have corresponding free operations",
                "flag": "--memory-cleanup-check"
            },
            {
                "name": "cbmc_bounds_check",
                "category": "cbmc_verification",
                "description": "Verifies array accesses are within bounds",
                "verification_details": "Detects buffer overflows and underflows for both static and dynamic arrays",
                "harness_usage": "Test array accesses with both valid and invalid indices",
                "flag": "--bounds-check"
            },
            {
                "name": "cbmc_pointer_overflow_check",
                "category": "cbmc_verification",
                "description": "Detects pointer arithmetic that results in overflow",
                "verification_details": "Checks pointer arithmetic operations to prevent undefined behavior",
                "harness_usage": "Test pointer arithmetic operations with boundary values",
                "flag": "--pointer-overflow-check"
            },
            {
                "name": "cbmc_conversion_check",
                "category": "cbmc_verification",
                "description": "Detects problematic type conversions",
                "verification_details": "Identifies loss of information in numeric conversions and sign conversion issues",
                "harness_usage": "Test type conversions with values that may cause information loss",
                "flag": "--conversion-check"
            },
            {
                "name": "cbmc_div_by_zero_check",
                "category": "cbmc_verification",
                "description": "Checks for division by zero errors",
                "verification_details": "Verifies both integer and floating-point divisions and modulo operations with zero divisor",
                "harness_usage": "Test division operations with zero and near-zero divisors",
                "flag": "--div-by-zero-check"
            }
        ]
    )

def setup_llm():
    """Set up the LLM with optimized parameters for harness generation."""
    
    # Check if ANTHROPIC_API_KEY is set in environment variables
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    
    # Configure system prompt to encourage complete, non-truncated code generation
    system_prompt = """
    You are an expert at generating complete, correct CBMC verification harnesses for C functions.
    
    When generating code:
    - Always provide complete, syntactically valid code
    - Never truncate code with comments like "//..." or "/* ... */"
    - Always include a complete main() function
    - Always ensure balanced braces and complete control structures
    - Keep harnesses simple, focused, and minimal while still testing the function thoroughly
    - Complete all control structures and function bodies
    
    Your code must compile and run correctly with CBMC verification.
    """
    
    # Create the LLM instance with optimized parameters
    llm = ChatAnthropic(
        model="claude-3-7-sonnet-latest",
        anthropic_api_key=api_key,
        temperature=0.2,  # Lower temperature for more deterministic code generation
        max_tokens=4000,  # Ensure we have enough tokens for complete responses
        model_kwargs={"system": system_prompt},  # Use model_kwargs for the system prompt
    )
    
    return llm

llm = setup_llm()

# Define the state class
class HarnessGenerationState(MessagesState):
    # Original fields
    source_code: str = ""  # For single file compatibility
    embeddings: Dict = {}
    vulnerable_functions: List[str] = []
    harnesses: Dict[str, str] = {}
    cbmc_results: Dict[str, Any] = {}
    refinement_attempts: Dict[str, int] = {}
    current_function: str = ""  # Track the function currently being processed
    processed_functions: List[str] = []  # Track functions that have been processed
    improvement_recommendation: str = ""  # Store recommendations for harness improvement
    loop_counter: int = 0  # Counter to detect and prevent infinite loops
    
    # New field to track harness version history
    harness_history: Dict[str, List[str]] = {}
    
    # Progress tracking
    total_functions: int = 0  # Total number of functions to process
    current_function_index: int = 0  # Index of current function being processed
    
    # Timing information
    start_time: float = 0.0  # Timestamp when process started
    function_times: Dict[str, Dict[str, float]] = {}  # Timing for each function phase
    
    # New fields for multi-file support
    source_files: Dict[str, str] = {}  # Map of file paths to content
    is_directory_mode: bool = False  # Flag to indicate if processing directory
    source_directory: str = ""  # Path to the source directory
    file_functions: Dict[str, List[str]] = {}  # Map of file paths to function names
    
    # Enhanced tracking for CBMC errors and harness issues
    cbmc_error_messages: Dict[str, str] = {}  # Track specific CBMC error messages by function
    harness_syntax_errors: Dict[str, str] = {}  # Track syntax errors in harnesses
    parsing_issues: Dict[str, bool] = {}  # Track which functions had parsing issues
    verification_failures: Dict[str, List[str]] = {}  # Track verification failure types by function

def process_directory(directory_path: str) -> Dict[str, str]:
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
        print(f"Error: Directory '{directory_path}' does not exist")
        return source_files
    
    # Look for source/source_code subdirectory
    source_subdir = os.path.join(directory_path, "source")
    if not os.path.isdir(source_subdir):
        print(f"Warning: '{source_subdir}' directory not found. Using top directory.")
        source_subdir = directory_path
    
    print(f"Looking for source files in: {source_subdir}")
    
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
    
    return source_files

# Define tools
def embed_code(code: str, file_path: str = None) -> Dict[str, Any]:
    """Embeds source code and stores it in the ChromaDB embedding database."""
    # Import tqdm for progress tracking
    from tqdm import tqdm
    
    # Parse the code to extract functions
    functions = {}
    
    # Skip if code is empty
    if not code:
        return {"functions": {}, "message": "No code to embed"}
    
    # Clear existing collection first - only do this once at the start, not for each file
    if file_path and "core_http_client.c" in file_path:  # Only clear on first file
        try:
            existing_ids = code_collection.get()["ids"]
            if existing_ids:
                code_collection.delete(ids=existing_ids)
        except Exception as e:
            pass
    
    # Show file info
    file_name = os.path.basename(file_path) if file_path else "inline"
    
    try:
        # Use a simpler function pattern that's more reliable
        c_func_pattern = r"([\w\s\*]+)\s+(\w+)\s*\(([^)]*)\)\s*\{"
        
        # Use direct search instead of splitting first
        matches = list(re.finditer(c_func_pattern, code, re.MULTILINE))
        
        # Process each potential function with progress bar
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
            return {"functions": functions, "message": "Processed header file declarations"}
        
        # Use tqdm for progress tracking
        with tqdm(total=len(matches), desc=f"Analyzing {file_name}", unit="funcs") as pbar:
            for match in matches:
                try:
                    return_type = match.group(1).strip()
                    func_name = match.group(2).strip()
                    params = match.group(3).strip()
                    
                    # Update progress bar
                    pbar.set_description(f"Analyzing {func_name}")
                    
                    # Skip if func_name is a keyword
                    if func_name in ['if', 'for', 'while', 'switch', 'return', 'include']:
                        pbar.update(1)
                        continue
                    
                    # Skip if we've already seen this function
                    if func_name in seen_functions:
                        pbar.update(1)
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
                        pbar.update(1)
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
                    
                    # Update progress bar with function count
                    pbar.set_postfix(functions=len(functions))
                except Exception:
                    pass
                
                pbar.update(1)
        
        # Add to ChromaDB
        if function_ids:
            code_collection.add(
                ids=function_ids,
                documents=function_texts,
                metadatas=function_metadatas
            )
    
    except Exception:
        pass
    
    return {
        "functions": functions,
        "message": f"Successfully embedded {len(functions)} functions from {file_path}"
    }


def query_pattern_db(query: str) -> Dict[str, Any]:
    """Queries the ChromaDB pattern database for known memory leak patterns."""
    # Query the pattern collection to find relevant patterns
    results = pattern_collection.query(
        query_texts=[query],
        n_results=3  # Get the top 3 matching patterns
    )
    
    # Also check via metadata if the function contains known indicators
    if "malloc(" in query and "free(" not in query:
        # Direct metadata match for malloc without free
        direct_match = "malloc_without_free"
    elif "if" in query and "free(" in query:
        # Potential conditional free
        direct_match = "conditional_free"
    elif query.count("malloc(") > 1:
        # Multiple malloc calls
        direct_match = "nested_malloc"
    else:
        direct_match = None
    
    # Process results
    matching_patterns = {}
    
    # Add patterns from semantic search
    if len(results['ids']) > 0:
        for i, (pattern_id, metadata, distance) in enumerate(zip(
            results['ids'][0],
            results['metadatas'][0],
            results['distances'][0]
        )):
            # Only include if reasonably close in embedding space
            if distance < 0.3:
                matching_patterns[metadata['name']] = {
                    "description": metadata["description"],
                    "severity": metadata["severity"],
                    "verification_strategy": metadata["verification_strategy"],
                    "similarity_score": 1.0 - distance  # Convert to similarity
                }
    
    # Add direct match if found and not already included
    if direct_match and direct_match not in matching_patterns:
        # Find the metadata for this pattern
        pattern_match_idx = ['malloc_without_free', 'nested_malloc', 'conditional_free'].index(direct_match) + 1
        pattern_id = f"pattern{pattern_match_idx}"
        metadata_results = pattern_collection.get(ids=[pattern_id])
        if metadata_results['ids']:
            for metadata in metadata_results['metadatas']:
                if metadata['name'] == direct_match:
                    matching_patterns[direct_match] = {
                        "description": metadata["description"],
                        "severity": metadata["severity"],
                        "verification_strategy": metadata["verification_strategy"],
                        "similarity_score": 1.0  # Direct match gets perfect score
                    }
                    break
    
    return {
        "matching_patterns": matching_patterns,
        "message": f"Found {len(matching_patterns)} potential matching patterns via ChromaDB"
    }

# Node 1: Frontend - Initial processing of source code
def frontend_node(state):
    """Extracts source code from user messages and initializes timing."""
    # Start timing the overall process
    import time
    start_time = time.time()
    
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
                    
                    print(f"Combined source code length: {len(combined_source)} bytes")
                    
                    return {
                        "messages": [AIMessage(content=f"Processing directory: {directory_path}. Found {len(multiple_files)} C source files in source code directory.")],
                        "source_files": multiple_files,
                        "source_code": combined_source,  # For backward compatibility
                        "start_time": start_time,
                        "is_directory_mode": True,
                        "source_directory": source_subdir,
                        "file_functions": file_functions  # Initialize tracking of functions per file
                    }
                else:
                    return {
                        "messages": [AIMessage(content=f"No C source files found in source directory of: {directory_path}")],
                        "source_code": "",
                        "source_files": {},
                        "start_time": start_time,
                        "is_directory_mode": False,
                        "file_functions": {}
                    }
    
    # Fall back to the original single file processing if no directory is specified
    if not state.get("source_code"):
        for message in reversed(state["messages"]):
            if isinstance(message, HumanMessage) and "```" in message.content:
                match = re.search(r'```(?:\w+)?\n(.+?)\n```', message.content, re.DOTALL)
                if match:
                    source_code = match.group(1)
                    return {
                        "messages": [AIMessage(content=f"Received source code ({len(source_code)} characters). Proceeding with code embedding.")],
                        "source_code": source_code,
                        "source_files": {"inline_code": source_code},  # Add to source_files for consistency
                        "start_time": start_time,
                        "is_directory_mode": False,
                        "file_functions": {"inline_code": []}  # Initialize tracking for single file
                    }
    
    # If no source code found or already exists
    return {
        "messages": [AIMessage(content=f"Proceeding with code embedding.")],
        "source_code": state.get("source_code", ""),
        "source_files": state.get("source_files", {}),
        "start_time": start_time,
        "is_directory_mode": state.get("is_directory_mode", False),
        "file_functions": state.get("file_functions", {})
    }

# Node 2: Code Embedding System - Stores code in database
def code_embedding_node(state):
    """Embeds and stores code in the database."""
    
    # Check if we're in directory mode
    if state.get("is_directory_mode", False):
        source_files = state.get("source_files", {})
        
        # Process each file separately and combine the results
        all_embeddings = {"functions": {}}
        file_counts = {}
        
        # Process C source files first, then headers
        c_files = {}
        h_files = {}
        
        for file_path, file_content in source_files.items():
            if file_path.endswith(('.c', '.cpp')):
                c_files[file_path] = file_content
            else:
                h_files[file_path] = file_content
        
        # Process C files first (implementations)
        print(f"Processing {len(c_files)} C source files...")
        for file_path, file_content in c_files.items():
            print(f"Embedding file: {os.path.basename(file_path)}")
            file_result = embed_code(file_content, file_path)
            all_embeddings["functions"].update(file_result.get("functions", {}))
            file_counts[file_path] = len(file_result.get("functions", {}))
            print(f"Found {file_counts[file_path]} functions in {os.path.basename(file_path)}")
        
        # Process header files 
        print(f"Processing {len(h_files)} header files...")
        for file_path, file_content in h_files.items():
            print(f"Embedding file: {os.path.basename(file_path)}")
            file_result = embed_code(file_content, file_path)
            # Only add functions that haven't been found in C files
            new_funcs = 0
            for func_id, func_data in file_result.get("functions", {}).items():
                if func_id not in all_embeddings["functions"]:
                    all_embeddings["functions"][func_id] = func_data
                    new_funcs += 1
            file_counts[file_path] = new_funcs
            print(f"Found {new_funcs} new functions in {os.path.basename(file_path)}")
        
        # Create a summary of files processed
        file_summary = "\n".join([f"- {path}: {count} functions" for path, count in file_counts.items() if count > 0])
        
        return {
            "messages": [AIMessage(content=f"Source code embedded successfully across multiple files.\n\nSummary:\n{file_summary}\n\nTotal functions found: {len(all_embeddings['functions'])}")],
            "embeddings": all_embeddings
        }
    else:
        # Original single file processing
        result = embed_code(state.get("source_code", ""))
        
        return {
            "messages": [AIMessage(content=f"Source code embedded successfully. Found {len(result['functions'])} functions.")],
            "embeddings": result
        }

# Node 3: Analyzer - Identifies functions with memory or arithmetic operations and initializes sequence
def analyzer_node(state):
    """Analyzes code from CodeDB to identify functions with memory operations or arithmetic."""
    # Start timing for analysis phase
    import time
    analysis_start = time.time()
    
    # Get all functions from the code database
    all_functions = code_collection.get()
    target_functions = []
    
    # Get source directory path
    source_dir = state.get("source_directory", "")
    
    # Process functions to find those with memory operations or arithmetic
    # Only include functions from files directly in the source directory (not subdirectories)
    for i, metadata in enumerate(all_functions["metadatas"]):
        func_id = all_functions["ids"][i]
        func_code = all_functions["documents"][i]
        file_path = metadata.get("file_path", "")
        
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
    
    # Calculate time taken for analysis
    analysis_time = time.time() - analysis_start
    
    return {
        "messages": [AIMessage(content=f"Analysis complete in {analysis_time:.2f}s. Identified {len(target_functions)} functions with memory or arithmetic operations. Breakdown: {category_count['memory']} with memory operations, {category_count['arithmetic']} with arithmetic operations.")],
        "vulnerable_functions": target_functions,
        "total_functions": len(target_functions),
        "current_function_index": 0  # Initialize the index counter
    }

# Node 4: Junction - Processes one function at a time in sequential order
def junction_node(state):
    """Processes vulnerable functions one at a time in sequential order."""
    # Get the list of vulnerable functions and processed functions
    vulnerable_functions = state.get("vulnerable_functions", [])
    processed_functions = state.get("processed_functions", [])
    
    # Safety counter to prevent infinite recursion
    loop_counter = state.get("loop_counter", 0) + 1
    
    # Force termination if loop counter gets too high
    if loop_counter > 50:
        return {
            "messages": [AIMessage(content=f"WARNING: Loop counter exceeded maximum value. Forcing termination to avoid recursion error.")],
            "loop_counter": 0,  # Reset counter
            "next": "output"
        }
    
    # Track the progress
    total_functions = len(vulnerable_functions)
    completed_functions = len(processed_functions)
    
    # Check if we've processed all functions
    if completed_functions >= total_functions:
        return {
            "messages": [AIMessage(content=f"All {total_functions} functions have been processed. Moving to final output.")],
            "loop_counter": 0,  # Reset counter
            "next": "output"
        }
    
    # Get current function being processed
    current_function = state.get("current_function", "")
    
    # Important fix: If current function is in processed_functions, clear it
    if current_function and current_function in processed_functions:
        # This should never happen, but if it does, reset the current function
        current_function = ""
    
    # If we have a valid current function that's not processed, continue with it
    if current_function and current_function in vulnerable_functions and current_function not in processed_functions:
        return {
            "messages": [AIMessage(content=f"Continuing processing of function: {current_function}")],
            "current_function": current_function,
            "loop_counter": loop_counter,
            "next": "generator"
        }
    
    # Find the next unprocessed function
    for func in vulnerable_functions:
        if func not in processed_functions:
            # Select this function as the next to process
            return {
                "messages": [AIMessage(content=f"Processing function {completed_functions + 1} of {total_functions}: {func}")],
                "current_function": func,
                "loop_counter": loop_counter,
                "next": "generator"
            }
    
    # Fallback (should not reach here if logic is correct)
    return {
        "messages": [AIMessage(content="All functions appear to be processed. Moving to output.")],
        "loop_counter": 0,  # Reset counter
        "next": "output"
    }

# Node 5: Generator - Creates or refines harness for current function
def generator_node(state):
    """Generates or refines CBMC-compatible harness for the current function with timing."""
    import time
    import os
    generation_start = time.time()
    
    func_name = state.get("current_function", "")
    
    # Check if this is a refinement call
    improvement_recommendation = state.get("improvement_recommendation", "")
    is_refinement = bool(improvement_recommendation)
    
    # Track harness history in the state if not already present
    harness_history = state.get("harness_history", {})
    if func_name not in harness_history:
        harness_history[func_name] = []
    
    # Get the previous harness if this is a refinement
    previous_harness = ""
    if is_refinement and func_name in state.get("harnesses", {}):
        previous_harness = state.get("harnesses", {})[func_name]
        # Add to history if not already there
        if previous_harness not in harness_history[func_name]:
            harness_history[func_name].append(previous_harness)
    
    # Get function code from CodeDB if not refining
    if not is_refinement:
        function_result = code_collection.get(ids=[func_name], include=["documents", "metadatas"])
        
        if not function_result["ids"]:
            return {
                "messages": [AIMessage(content=f"Error: Function {func_name} not found in database.")],
                "next": "junction"  # Return to junction to process next function
            }
        
        func_code = function_result["documents"][0]
        func_metadata = function_result["metadatas"][0]
        
        # Get pattern information from PatternDB
        patterns_result = query_pattern_db(func_code)
        
        # Analyze function to determine which checks are actually needed
        has_malloc = "malloc(" in func_code
        has_free = "free(" in func_code
        has_array_access = "[" in func_code and "]" in func_code
        has_pointer_arithmetic = "*" in func_code or "->" in func_code
        has_division = "/" in func_code or "%" in func_code
        has_type_conversion = "(" in func_code and ")" in func_code and any(type_name in func_code for type_name in ["int", "char", "float", "double", "size_t", "unsigned", "long"])
        
        # Produce targeted verification guide based on actual function contents
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
        
        # Construct the verification guide
        if verification_checks:
            verification_guide = "Relevant CBMC Verification Checks for this function:\n" + "\n".join(verification_checks)
        else:
            verification_guide = "This function doesn't appear to need special CBMC verification checks beyond basic assertions."
        
        # Clear guidance about avoiding unnecessary mocks
        cbmc_verification_info = f"""
        {verification_guide}
        
        IMPORTANT GUIDELINES:
        
        1. Do NOT create mock implementations that aren't necessary for verification.
        2. Focus ONLY on testing the actual function behavior, not on artificial scenarios.
        3. Only implement verification checks that are relevant to this specific function.
        4. Avoid creating test cases for verification types that don't apply to this function.
        5. Keep the harness minimal and focused on real potential issues.
        
        The harness should:
        - Use __CPROVER_assert() only for properties that could actually fail in this function
        - Use __CPROVER_assume() to specify realistic input constraints
        - Use nondet functions like nondet_int() for inputs that need to be nondeterministic
        """
        
        # Build generator prompt with focused verification
        generator_prompt = f"""
        You are a specialized harness generator for CBMC verification.
        Create a MINIMAL, FOCUSED harness for the following function WITHOUT unnecessary mocks:
        
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
        
        {cbmc_verification_info}
        
        CRITICAL INSTRUCTIONS:
        1. DO NOT create mock implementations of functions that aren't directly related to verification
        2. DO NOT implement stubs or test code just to satisfy CBMC checklist items
        3. ONLY verify properties that are relevant to this specific function
        4. DO NOT add checks for issues that cannot occur in this function
        5. Keep the harness SMALL and FOCUSED - don't add anything that isn't necessary
        6. If function dependencies are unavailable, minimize assumptions rather than creating elaborate mocks
        7. Follow CBMC's harness structure with a void main() function
        
        Provide only the minimal, focused harness code without explanation.
        """
    else:
        # For refinement, use targeted improvement guidance
        generator_prompt = f"""
        You are a specialized harness generator for CBMC verification.
        You need to REFINE an existing harness based on evaluation feedback, focusing on ELIMINATING UNNECESSARY MOCKS.
        
        {improvement_recommendation}
        
        Previous harness code that you should improve:
        ```c
        {previous_harness}
        ```
        
        Create an improved version of the harness that addresses the identified issues while REMOVING UNNECESSARY CODE.
        
        CRITICAL INSTRUCTIONS:
        1. REMOVE any mock implementations that aren't directly necessary for verification
        2. ELIMINATE any test code that's just there to satisfy CBMC checklist items
        3. FOCUS only on testing real properties of the function that matter
        4. SIMPLIFY the harness - remove anything that isn't directly testing the function
        5. KEEP only the minimal verification needed to properly test the function
        6. AVOID adding checks for issues that cannot occur in this function
        
        The harness must use CBMC's special functions:
        - __CPROVER_assert() for verification of properties that actually matter
        - __CPROVER_assume() for realistic constraints
        - nondet functions for inputs
        
        Make sure your harness is complete and properly formatted.
        
        Provide only the improved, minimal harness code without explanation.
        """
    
    # Generate the harness
    try:
        # Setup messages for the LLM
        response = llm.invoke([
            HumanMessage(content=generator_prompt)
        ])
        
        # Extract the harness code
        harness_code = response.content
        match = re.search(r'```(?:c)?\n(.+?)\n```', harness_code, re.DOTALL)
        if match:
            harness_code = match.group(1)
        
        # Validate harness completeness
        has_main = "void main(" in harness_code or "int main(" in harness_code
        balanced_braces = harness_code.count("{") <= harness_code.count("}")
        
        if not has_main or not balanced_braces:
            print(f"Warning: Harness for {func_name} may be incomplete. Adding necessary closing elements.")
            
            # Try to fix incomplete harnesses
            if not balanced_braces:
                missing_braces = harness_code.count("{") - harness_code.count("}")
                if missing_braces > 0:
                    harness_code += "\n" + ("}" * missing_braces)
            
            # Make sure there's a main function
            if not has_main:
                if "int main" not in harness_code and "void main" not in harness_code:
                    harness_code += "\n\nvoid main() {\n    // Auto-generated main function\n}"
        
        # Save the new harness to history
        if harness_code not in harness_history[func_name]:
            harness_history[func_name].append(harness_code)
        
        # Update the harnesses dictionary
        harnesses = state.get("harnesses", {}).copy()
        harnesses[func_name] = harness_code
        
        # Determine iteration number for filename
        refinement_num = state.get("refinement_attempts", {}).get(func_name, 0)
        version_num = refinement_num + 1
        
        # Create organized directory structure for harnesses
        harness_base_dir = "harnesses"
        os.makedirs(harness_base_dir, exist_ok=True)
        
        # Create function-specific directory
        func_harness_dir = os.path.join(harness_base_dir, func_name)
        os.makedirs(func_harness_dir, exist_ok=True)
        
        # Save harness file
        filename = os.path.join(func_harness_dir, f"v{version_num}.c")
        
        # Save harness to file with explicit buffer flushing
        with open(filename, "w") as f:
            f.write(harness_code)
            f.flush()
            os.fsync(f.fileno())  # Force flush to disk
        
        # Calculate time spent on generation
        generation_time = time.time() - generation_start
        
        # Update function times dictionary
        function_times = state.get("function_times", {}).copy()
        if func_name not in function_times:
            function_times[func_name] = {}
        function_times[func_name]["generation"] = generation_time
        
        # Clear improvement recommendation after processing
        return {
            "messages": [AIMessage(content=f"{'Refined' if is_refinement else 'Generated'} minimal, focused harness for function {func_name} in {generation_time:.2f}s (without unnecessary mocks)")],
            "harnesses": harnesses,
            "harness_history": harness_history,
            "improvement_recommendation": "",
            "function_times": function_times,
            "next": "cbmc"  # Proceed to CBMC verification
        }
        
    except Exception as e:
        # Handle API errors
        error_msg = str(e)
        
        # Calculate time even for errors
        generation_time = time.time() - generation_start
        
        # Update function times dictionary
        function_times = state.get("function_times", {}).copy()
        if func_name not in function_times:
            function_times[func_name] = {}
        function_times[func_name]["generation_error"] = generation_time
        
        return {
            "messages": [AIMessage(content=f"Error {'refining' if is_refinement else 'generating'} harness for function {func_name} in {generation_time:.2f}s: {error_msg}")],
            "improvement_recommendation": "",
            "function_times": function_times,
            "next": "junction"  # Return to junction to process next function
        }

# Node 6: CBMC - Executes CBMC tool for current function (avoiding process forking)
def cbmc_node(state):
    """Executes CBMC verification on the current function's harness using sources from verification/sources directory."""
    import time
    import os
    import re
    import shutil
    verification_start = time.time()
    
    func_name = state.get("current_function", "")
    harnesses = state.get("harnesses", {})
    harness_code = harnesses.get(func_name, "")
    
    if not harness_code:
        return {
            "messages": [AIMessage(content=f"Error: No harness available for function {func_name}.")],
            "next": "junction"  # Return to junction to process next function
        }
    
    # Extract file path from function name if it includes file info
    file_basename = None
    original_func_name = func_name
    
    if ":" in func_name:
        file_basename, original_func_name = func_name.split(":", 1)
    
    # Create organized directory structure for verification
    verification_base_dir = "verification"
    os.makedirs(verification_base_dir, exist_ok=True)
    
    # Create function-specific directory
    func_verification_dir = os.path.join(verification_base_dir, func_name)
    os.makedirs(func_verification_dir, exist_ok=True)
    
    # Create proper directory structure for verification
    verification_src_dir = os.path.join(verification_base_dir, "src")
    os.makedirs(verification_src_dir, exist_ok=True)
    
    # Create include directory for headers
    verification_include_dir = os.path.join(verification_base_dir, "include")
    os.makedirs(verification_include_dir, exist_ok=True)
    
    # Create stubs directory for stubs
    verification_stubs_dir = os.path.join(verification_base_dir, "stubs")
    os.makedirs(verification_stubs_dir, exist_ok=True)
    
    # Create sources directory for CBMC sources
    verification_sources_dir = os.path.join(verification_base_dir, "sources")
    os.makedirs(verification_sources_dir, exist_ok=True)
    
    # Determine version number from refinement attempts
    refinement_num = state.get("refinement_attempts", {}).get(func_name, 0)
    version_num = refinement_num + 1
    
    # Define CBMC_MAX_OBJECT_SIZE
    cbmc_max_object_size = 1024 * 1024  # 1MB is a typical reasonable size
    
    # Create a header file with the CBMC_MAX_OBJECT_SIZE definition
    cbmc_defs_header = os.path.join(verification_include_dir, "cbmc_defs.h")
    with open(cbmc_defs_header, "w") as f:
        f.write("""/*
 * Auto-generated CBMC definitions header
 * This file provides definitions needed for CBMC verification
 */

#ifndef CBMC_DEFS_H
#define CBMC_DEFS_H

#include <stddef.h>
#include <limits.h>

/* CBMC object size constraints */
#ifndef CBMC_OBJECT_BITS
#define CBMC_OBJECT_BITS 8
#endif

#ifndef CBMC_MAX_OBJECT_SIZE
#define CBMC_MAX_OBJECT_SIZE (SIZE_MAX>>(CBMC_OBJECT_BITS+1))
#endif

#endif /* CBMC_DEFS_H */
""")
    
    # For directory mode, handle project file copying
    if state.get("is_directory_mode", False):
        # Get original source directory from state
        original_source_dir = state.get("source_directory", "")
        
        if original_source_dir and os.path.exists(original_source_dir):
            # First, copy only the necessary source files to avoid duplication
            for root, dirs, files in os.walk(original_source_dir):
                for file in files:
                    # Only copy .c and .h files to corresponding directories
                    if file.endswith(('.c', '.cpp')):
                        src_file = os.path.join(root, file)
                        dest_file = os.path.join(verification_src_dir, file)
                        shutil.copy2(src_file, dest_file)
                    elif file.endswith(('.h', '.hpp')):
                        src_file = os.path.join(root, file)
                        dest_file = os.path.join(verification_include_dir, file)
                        shutil.copy2(src_file, dest_file)
        
        # Get specific source file for this function from embeddings if available
        file_path = None
        embeddings = state.get("embeddings", {})
        functions = embeddings.get("functions", {})
        
        if func_name in functions and "file_path" in functions[func_name]:
            file_path = functions[func_name]["file_path"]
            if file_path and os.path.exists(file_path):
                source_file = os.path.join(verification_src_dir, os.path.basename(file_path))
    else:
        # Original single-file mode - write source to a flat file
        source_file = os.path.join(verification_src_dir, "source.c")
        with open(source_file, "w") as f:
            f.write(state.get("source_code", ""))
    
    # Find source files - MODIFIED to prioritize verification/sources directory
    source_files = []
    
    # First, look for files in the sources directory
    sources_dir_files = [f for f in os.listdir(verification_sources_dir) if f.endswith(('.c', '.cpp'))]
    if sources_dir_files:
        # Use all files from the sources directory
        for file in sources_dir_files:
            source_files.append(os.path.join(verification_sources_dir, file))
    else:
        # Fall back to src directory if no files in sources directory
        src_dir_files = [f for f in os.listdir(verification_src_dir) if f.endswith(('.c', '.cpp'))]
        if src_dir_files:
            for file in src_dir_files:
                source_files.append(os.path.join(verification_src_dir, file))
        else:
            # Create a fallback source file if no source files were found
            fallback_source = os.path.join(verification_src_dir, "source.c")
            with open(fallback_source, "w") as f:
                f.write("// Fallback source file\n")
            source_files.append(fallback_source)
            
    # Write harness to file - use original function name in the filename
    harness_filename = original_func_name if ":" not in func_name else original_func_name
    harness_file = os.path.join(verification_src_dir, f"{harness_filename}_harness.c")
    with open(harness_file, "w") as f:
        # Add include for the CBMC definitions header
        f.write("#include \"cbmc_defs.h\"\n\n")
        f.write(harness_code)

    # Copy necessary CBMC include files for verification
    # Look for test/cbmc directory relative to the project source
    project_dir = os.path.dirname(state.get("source_directory", ""))
    cbmc_include_dir = os.path.join(project_dir, "test", "cbmc", "include")
    
    # If not found, try looking one level up
    if not os.path.exists(cbmc_include_dir):
        cbmc_include_dir = os.path.join(os.path.dirname(project_dir), "test", "cbmc", "include")
    
    # If still not found, try looking in the current directory structure
    if not os.path.exists(cbmc_include_dir):
        cbmc_include_dir = "test/cbmc/include"
    
    if os.path.exists(cbmc_include_dir):
        # Copy all CBMC include files
        for file in os.listdir(cbmc_include_dir):
            src_file = os.path.join(cbmc_include_dir, file)
            dest_file = os.path.join(verification_include_dir, file)
            if os.path.isfile(src_file):
                shutil.copy2(src_file, dest_file)
                print(f"Copied CBMC include file: {file}")
                
    # Also check for stubs directory
    cbmc_stubs_dir = os.path.join(project_dir, "test", "cbmc", "stubs")
    
    # If not found, try looking one level up
    if not os.path.exists(cbmc_stubs_dir):
        cbmc_stubs_dir = os.path.join(os.path.dirname(project_dir), "test", "cbmc", "stubs")
    
    # If still not found, try looking in the current directory structure
    if not os.path.exists(cbmc_stubs_dir):
        cbmc_stubs_dir = "test/cbmc/stubs"
    
    if os.path.exists(cbmc_stubs_dir):
        # Copy all CBMC stub files
        for file in os.listdir(cbmc_stubs_dir):
            src_file = os.path.join(cbmc_stubs_dir, file)
            dest_file = os.path.join(verification_stubs_dir, file)
            if os.path.isfile(src_file):
                shutil.copy2(src_file, dest_file)
                print(f"Copied CBMC stub file: {file}")
                
    # Check for sources directory
    cbmc_sources_dir = os.path.join(project_dir, "test", "cbmc", "sources")
    
    # If not found, try looking one level up
    if not os.path.exists(cbmc_sources_dir):
        cbmc_sources_dir = os.path.join(os.path.dirname(project_dir), "test", "cbmc", "sources")
    
    # If still not found, try looking in the current directory structure
    if not os.path.exists(cbmc_sources_dir):
        cbmc_sources_dir = "test/cbmc/sources"
    
    if os.path.exists(cbmc_sources_dir):
        # Copy all CBMC source files
        for file in os.listdir(cbmc_sources_dir):
            src_file = os.path.join(cbmc_sources_dir, file)
            dest_file = os.path.join(verification_sources_dir, file)
            if os.path.isfile(src_file):
                shutil.copy2(src_file, dest_file)
                print(f"Copied CBMC source file: {file}")
    
    # Build list of CBMC command parameters - MODIFIED to use sources from verification/sources
    cbmc_cmd = [
        "cbmc",
    ]
    
    # Add source files from verification/sources first
    for file in os.listdir(verification_sources_dir):
        if file.endswith(('.c', '.cpp')):
            source_file_path = os.path.join(verification_sources_dir, file)
            cbmc_cmd.append(source_file_path)
    
    # Add the harness file
    cbmc_cmd.append(harness_file)
    
    # Add main CBMC options
    cbmc_cmd.extend([
        "--function", "main",
        "--memory-leak-check",
        "--memory-cleanup-check",
        "--bounds-check",
        "--pointer-overflow-check",
        "--div-by-zero-check",
        f"--object-bits", "8",  # Default for CBMC_OBJECT_BITS
    ])
    
    # Add CBMC object size constraint definition
    cbmc_cmd.extend([
        "-DCBMC_MAX_OBJECT_SIZE=" + str(cbmc_max_object_size)
    ])
    
    # Add stub files as needed
    for file in os.listdir(verification_stubs_dir):
        if file.endswith(('.c', '.cpp')):
            stub_file_path = os.path.join(verification_stubs_dir, file)
            cbmc_cmd.append(stub_file_path)
    
    # Add necessary include paths in the correct order
    cbmc_cmd.extend([
        "-I", verification_include_dir,
        "-I", verification_src_dir,
        "-I", verification_stubs_dir,
        "-I", verification_sources_dir
    ])
    
    # Save the command for debugging
    cmd_file = os.path.join(func_verification_dir, f"v{version_num}_command.txt")
    with open(cmd_file, 'w') as f:
        f.write(" ".join(cbmc_cmd))
    
    # Initialize dictionaries for tracking errors if they don't exist
    cbmc_error_messages = state.get("cbmc_error_messages", {}).copy()
    harness_syntax_errors = state.get("harness_syntax_errors", {}).copy()
    parsing_issues = state.get("parsing_issues", {}).copy()
    verification_failures = state.get("verification_failures", {}).copy()
    
    try:
        # Use subprocess.run for more reliable output capture
        process = subprocess.run(
            cbmc_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=60,
            check=False  # Don't raise exception on non-zero return
        )
        
        stdout = process.stdout
        stderr = process.stderr
        returncode = process.returncode
        
        # Combine stdout and stderr for more complete output
        full_output = stdout
        if stderr:
            full_output += "\n--- STDERR ---\n" + stderr
        
        # Process results
        status = "SUCCESS" if returncode == 0 else "FAILED"
        message = "VERIFICATION SUCCESSFUL: No issues detected."
        suggestions = ""
        
        # More detailed error analysis
        if returncode != 0:
            # Check for syntax errors or parsing issues first
            syntax_error_match = re.search(r'syntax error at line (\d+)', stderr)
            if syntax_error_match:
                line_number = syntax_error_match.group(1)
                harness_syntax_errors[func_name] = f"Syntax error at line {line_number}"
                message = f"HARNESS ERROR: Syntax error in harness at line {line_number}."
                suggestions = "Fix the syntax error in the harness."
            
            # Check for parsing issues
            if "PARSING ERROR" in stderr:
                parsing_issues[func_name] = True
                
                # Extract specific parsing error
                parsing_error_match = re.search(r'(.+?): fatal error: (.+)$', stderr, re.MULTILINE)
                if parsing_error_match:
                    error_location = parsing_error_match.group(1)
                    error_message = parsing_error_match.group(2)
                    message = f"PARSING ERROR: {error_message}"
                    suggestions = f"Fix the parsing error in {error_location}."
                else:
                    message = "PARSING ERROR: Could not parse the harness."
                    suggestions = "Check for missing include files or syntax errors."
            
            # Track the specific error message for this function
            cbmc_error_messages[func_name] = message
            
            # Check for common verification failures if no syntax/parsing issues
            if "VERIFICATION FAILED" in stdout and not parsing_issues.get(func_name, False):
                failure_types = []
                
                if "memory leak detected" in stdout.lower():
                    failure_types.append("memory_leak")
                    message = "VERIFICATION FAILED: Memory leak detected."
                    suggestions = "Ensure all allocated memory is freed in all execution paths."
                
                if "dereference failure" in stdout.lower() or "NULL pointer" in stdout.lower():
                    failure_types.append("null_pointer")
                    message = "VERIFICATION FAILED: Null pointer dereference detected."
                    suggestions = "Add null pointer checks before dereferencing."
                
                if "array bounds" in stdout.lower():
                    failure_types.append("array_bounds")
                    message = "VERIFICATION FAILED: Array bounds violation detected."
                    suggestions = "Add bounds checking for array accesses."
                
                if "division by zero" in stdout.lower():
                    failure_types.append("division_by_zero")
                    message = "VERIFICATION FAILED: Division by zero detected."
                    suggestions = "Add checks to ensure divisors are non-zero."
                
                if "pointer arithmetic" in stdout.lower() and "overflow" in stdout.lower():
                    failure_types.append("pointer_overflow")
                    message = "VERIFICATION FAILED: Pointer arithmetic overflow detected."
                    suggestions = "Ensure pointer arithmetic stays within allocated bounds."
                
                if "arithmetic overflow" in stdout.lower():
                    failure_types.append("arithmetic_overflow")
                    message = "VERIFICATION FAILED: Arithmetic overflow detected."
                    suggestions = "Add overflow checking for arithmetic operations."
                
                if "type" in stdout.lower() and "conversion" in stdout.lower():
                    failure_types.append("type_conversion")
                    message = "VERIFICATION FAILED: Problematic type conversion detected."
                    suggestions = "Verify type conversions do not result in information loss."
                
                if failure_types:
                    verification_failures[func_name] = failure_types
                else:
                    # Try to extract more details from the output
                    failure_lines = [line for line in stdout.split('\n') if "FAILED" in line]
                    if failure_lines:
                        message = f"VERIFICATION FAILED: {failure_lines[0]}"
                        verification_failures[func_name] = ["general_verification_failure"]
                    else:
                        message = "VERIFICATION FAILED: Unspecified verification error."
                        verification_failures[func_name] = ["unspecified_failure"]
                    
                    # Look for any assertion failures
                    assertion_lines = [line for line in stdout.split('\n') if "assertion" in line.lower() and "failed" in line.lower()]
                    if assertion_lines:
                        suggestions = f"Review assertion failure: {assertion_lines[0]}"
                    else:
                        suggestions = "Review the full verification output for details."
            else:
                # Handle errors that aren't explicit verification failures
                if "PARSING ERROR" not in stderr and "syntax error" not in stderr:
                    message = f"VERIFICATION FAILED: Command returned error code {returncode}."
                    if "file not found" in stderr:
                        missing_file_match = re.search(r"'([^']+)' file not found", stderr)
                        if missing_file_match:
                            missing_file = missing_file_match.group(1)
                            message += f" Missing header file: '{missing_file}'."
                            suggestions = f"Make sure '{missing_file}' is available in the include path."
                    elif stderr:
                        message += f" Error: {stderr[:200]}..."
                    suggestions = suggestions or "Check the CBMC command and harness for errors."
        
        # Update the results dictionary
        cbmc_results = state.get("cbmc_results", {}).copy()
        cbmc_results[func_name] = {
            "function": func_name,
            "status": status,
            "message": message,
            "suggestions": suggestions,
            "stdout": full_output,
            "returncode": returncode,
            "version": version_num,
            "has_syntax_error": func_name in harness_syntax_errors,
            "has_parsing_issue": func_name in parsing_issues,
            "verification_failure_types": verification_failures.get(func_name, [])
        }
        
        # Save verification results to file with version
        verification_file = os.path.join(func_verification_dir, f"v{version_num}_results.txt")
        with open(verification_file, "w") as f:
            f.write(f"Function: {func_name}\n")
            f.write(f"Version: {version_num}\n")
            f.write(f"Status: {status}\n")
            f.write(f"Message: {message}\n")
            if suggestions:
                f.write(f"Suggestions: {suggestions}\n")
            f.write("\nDetailed Output:\n")
            f.write(full_output)
        
        # Also save raw output for debugging
        raw_output_file = os.path.join(func_verification_dir, f"v{version_num}_raw_output.txt")
        with open(raw_output_file, "w") as f:
            f.write(full_output)
        
        # Generate a verification report for this version
        report_file = os.path.join(func_verification_dir, f"v{version_num}_report.md")
        with open(report_file, "w") as f:
            f.write(f"# CBMC Verification Report - {func_name} (Version {version_num})\n\n")
            f.write(f"## Summary\n\n")
            f.write(f"**Status:** {status}\n\n")
            f.write(f"**Message:** {message}\n\n")
            if suggestions:
                f.write(f"**Suggestions:** {suggestions}\n\n")
            
            f.write(f"## Harness Details\n\n")
            f.write(f"The harness file is located at: `harnesses/{func_name}/v{version_num}.c`\n\n")
            
            f.write(f"## Verification Command\n\n")
            f.write(f"```\n{' '.join(cbmc_cmd)}\n```\n\n")
            
            f.write(f"## Detailed Output\n\n")
            f.write("```\n")
            # Only include the first 20 lines and last 20 lines if output is very long
            if len(full_output.split('\n')) > 50:
                output_lines = full_output.split('\n')
                trimmed_output = '\n'.join(output_lines[:20] + ["\n... [output trimmed] ...\n"] + output_lines[-20:])
                f.write(trimmed_output)
                f.write("\n\nNote: Output has been trimmed. See full output in v{version_num}_raw_output.txt\n")
            else:
                f.write(full_output)
            f.write("\n```\n\n")
            
            if returncode != 0:
                f.write(f"## Analysis\n\n")
                f.write(f"The verification failed with return code {returncode}. ")
                if suggestions:
                    f.write(f"Based on the output, it is recommended to {suggestions.lower()}\n\n")
                
                f.write(f"## Next Steps\n\n")
                f.write(f"1. Review the harness implementation\n")
                f.write(f"2. Implement the suggested fixes\n")
                f.write(f"3. Run another verification iteration\n")
            else:
                f.write(f"## Analysis\n\n")
                f.write(f"The verification was successful. No issues were detected with the current harness implementation.\n\n")
        
    except subprocess.TimeoutExpired as e:
        # Handle timeout - make sure process exists before trying to kill it
        # The 'e' parameter will contain the process
        if hasattr(e, 'process'):
            e.process.kill()
            e.process.wait()
        
        # Handle timeout
        cbmc_results = state.get("cbmc_results", {}).copy()
        cbmc_results[func_name] = {
            "function": func_name,
            "status": "TIMEOUT",
            "message": "CBMC verification timed out after 60 seconds.",
            "suggestions": "The function may have complex paths requiring longer verification time. Consider simplifying.",
            "stdout": "TIMEOUT: Process exceeded 60 second time limit",
            "version": version_num,
            "has_syntax_error": False,
            "has_parsing_issue": False,
            "verification_failure_types": ["timeout"]
        }
        
        # Save timeout to file
        verification_file = os.path.join(func_verification_dir, f"v{version_num}_results.txt")
        with open(verification_file, "w") as f:
            f.write(f"Function: {func_name}\n")
            f.write(f"Version: {version_num}\n")
            f.write(f"Status: TIMEOUT\n")
            f.write(f"Error: CBMC verification timed out after 60 seconds\n")
            f.write(f"Suggestions: The function may have complex paths requiring longer verification time. Consider simplifying.\n")
            
        # Generate timeout report
        report_file = os.path.join(func_verification_dir, f"v{version_num}_report.md")
        with open(report_file, "w") as f:
            f.write(f"# CBMC Verification Report - {func_name} (Version {version_num})\n\n")
            f.write(f"## Summary\n\n")
            f.write(f"**Status:** TIMEOUT\n\n")
            f.write(f"**Message:** CBMC verification timed out after 60 seconds.\n\n")
            f.write(f"**Suggestions:** The function may have complex paths requiring longer verification time. Consider simplifying.\n\n")
            
            f.write(f"## Analysis\n\n")
            f.write(f"The verification process timed out, which typically happens when the function has many complex paths or loops that CBMC needs to analyze. You may need to simplify the harness or consider using loop unwinding bounds to limit the verification scope.\n\n")
            
            f.write(f"## Next Steps\n\n")
            f.write(f"1. Review the harness implementation and simplify if possible\n")
            f.write(f"2. Add loop unwinding bounds if there are loops in the function\n")
            f.write(f"3. Consider breaking the verification into smaller parts\n")
    
    except Exception as e:
        # Handle errors
        cbmc_results = state.get("cbmc_results", {}).copy()
        cbmc_results[func_name] = {
            "function": func_name,
            "status": "ERROR",
            "message": f"Error running CBMC: {str(e)}",
            "suggestions": "Check if CBMC is installed correctly.",
            "stdout": f"ERROR: {str(e)}",
            "version": version_num,
            "has_syntax_error": False,
            "has_parsing_issue": False,
            "verification_failure_types": ["system_error"]
        }
        
        # Save error to file
        verification_file = os.path.join(func_verification_dir, f"v{version_num}_results.txt")
        with open(verification_file, "w") as f:
            f.write(f"Function: {func_name}\n")
            f.write(f"Version: {version_num}\n")
            f.write(f"Status: ERROR\n")
            f.write(f"Error: {str(e)}\n")
            
        # Generate error report
        report_file = os.path.join(func_verification_dir, f"v{version_num}_report.md")
        with open(report_file, "w") as f:
            f.write(f"# CBMC Verification Report - {func_name} (Version {version_num})\n\n")
            f.write(f"## Summary\n\n")
            f.write(f"**Status:** ERROR\n\n")
            f.write(f"**Message:** Error running CBMC: {str(e)}\n\n")
            f.write(f"**Suggestions:** Check if CBMC is installed correctly.\n\n")
            
            f.write(f"## Analysis\n\n")
            f.write(f"The verification process encountered an error. This is typically due to issues with the CBMC installation or with the harness itself.\n\n")
            
            f.write(f"## Next Steps\n\n")
            f.write(f"1. Verify your CBMC installation is working correctly\n")
            f.write(f"2. Check the harness for syntax errors\n")
            f.write(f"3. Review the error message for specific issues to fix\n")
    
    # Calculate verification time
    verification_time = time.time() - verification_start
    
    # Update function times dictionary
    function_times = state.get("function_times", {}).copy()
    if func_name not in function_times:
        function_times[func_name] = {}
    function_times[func_name]["verification"] = verification_time
    
    return {
        "messages": [AIMessage(content=f"CBMC verification for function {func_name} v{version_num} complete in {verification_time:.2f}s. Status: {cbmc_results[func_name]['status']}. Results saved to {func_verification_dir}/v{version_num}_results.txt")],
        "cbmc_results": cbmc_results,
        "function_times": function_times,
        "cbmc_error_messages": cbmc_error_messages,
        "harness_syntax_errors": harness_syntax_errors,
        "parsing_issues": parsing_issues,
        "verification_failures": verification_failures,
        "next": "evaluator"  # Always proceed to evaluator
    }

# Node 6.5: Harness Evaluator - Evaluates harness quality and determines if refinement is needed
def harness_evaluator_node(state):
    """Evaluates the quality of generated harnesses based on CBMC output and suggests improvements."""
    import time
    evaluation_start = time.time()
    
    # SAFETY: Get and increment loop counter to prevent infinite recursion
    loop_counter = state.get("loop_counter", 0)
    print(f"DEBUG: Evaluator node - function: {state.get('current_function', '')}, loop: {loop_counter}")
    
    func_name = state.get("current_function", "")
    harnesses = state.get("harnesses", {})
    cbmc_results = state.get("cbmc_results", {})
    
    # Get error tracking dictionaries
    cbmc_error_messages = state.get("cbmc_error_messages", {})
    harness_syntax_errors = state.get("harness_syntax_errors", {})
    parsing_issues = state.get("parsing_issues", {})
    verification_failures = state.get("verification_failures", {})
    
    # SAFETY: Initialize refinement_attempts if not present for this function
    refinement_attempts = state.get("refinement_attempts", {}).copy()
    if func_name not in refinement_attempts:
        refinement_attempts[func_name] = 0
    
    # Get current attempts count
    current_attempts = refinement_attempts.get(func_name, 0)
    print(f"DEBUG: Current refinement attempts for {func_name}: {current_attempts}")
    
    # SAFETY: Force progression after max attempts regardless of other conditions
    max_refinements = 3
    if current_attempts >= max_refinements:
        processed_functions = state.get("processed_functions", []).copy()
        if func_name not in processed_functions:
            processed_functions.append(func_name)
            print(f"DEBUG: Max refinements reached, marking {func_name} as processed")
        
        return {
            "messages": [AIMessage(content=f"Maximum refinement attempts ({max_refinements}) reached for {func_name}. Moving to next function.")],
            "refinement_attempts": refinement_attempts,
            "processed_functions": processed_functions,
            "loop_counter": loop_counter,
            "next": "junction"
        }
    
    # SAFETY: Handle missing data
    harness_code = harnesses.get(func_name, "")
    cbmc_result = cbmc_results.get(func_name, {})
    
    if not harness_code or not cbmc_result:
        # Mark this function as processed even if there was an error
        processed_functions = state.get("processed_functions", []).copy()
        if func_name and func_name not in processed_functions:
            processed_functions.append(func_name)
            print(f"DEBUG: Missing harness/CBMC data, marking {func_name} as processed")
        
        return {
            "messages": [AIMessage(content=f"Error: Missing harness or CBMC result for function {func_name}. Marking as processed.")],
            "processed_functions": processed_functions,
            "loop_counter": loop_counter,
            "next": "junction"  # Move to next function
        }
    
    # Extract function details from code database
    function_result = code_collection.get(ids=[func_name], include=["documents", "metadatas"])
    if not function_result["ids"]:
        # Mark this function as processed even if there's an error
        processed_functions = state.get("processed_functions", []).copy()
        if func_name not in processed_functions:
            processed_functions.append(func_name)
            print(f"DEBUG: Function metadata not found, marking {func_name} as processed")
        
        return {
            "messages": [AIMessage(content=f"Error: Function {func_name} metadata not found. Marking as processed.")],
            "processed_functions": processed_functions,
            "loop_counter": loop_counter,
            "next": "junction"
        }
    
    func_code = function_result["documents"][0]
    func_metadata = function_result["metadatas"][0]
    
    # Get CBMC output
    cbmc_stdout = cbmc_result.get("stdout", "")
    cbmc_status = cbmc_result.get("status", "UNKNOWN")
    verification_message = cbmc_result.get("message", "")
    suggestions = cbmc_result.get("suggestions", "")
    
    # Check for syntax errors, parsing issues, and other error types from CBMC
    has_syntax_error = cbmc_result.get("has_syntax_error", False) or func_name in harness_syntax_errors
    has_parsing_issue = cbmc_result.get("has_parsing_issue", False) or func_name in parsing_issues
    verification_failure_types = cbmc_result.get("verification_failure_types", [])
    
    # Set evaluation criteria for harness quality
    evaluation_criteria = {
        "has_nondet_inputs": "__CPROVER_" in harness_code and "nondet" in harness_code,
        "has_assertions": "__CPROVER_assert" in harness_code,
        "has_assumptions": "__CPROVER_assume" in harness_code,
        "checks_memory_leaks": "memory leak" in harness_code.lower() or "free" in harness_code,
        "checks_bounds": "bounds" in harness_code.lower() or "index" in harness_code.lower(),
        "checks_arithmetic": any(op in harness_code for op in ["overflow", "division", "zero"]),
        "addresses_cbmc_errors": False,
        "verification_passed": cbmc_status == "SUCCESS",
        "syntactically_valid": not has_syntax_error and not has_parsing_issue
    }
    
    # Calculate overall quality score
    quality_score = sum(1 for criterion, value in evaluation_criteria.items() if value) / len(evaluation_criteria)
    quality_score = round(quality_score * 100)
    
    # Build the improvement recommendation based on CBMC results
    improvement_recommendation = ""
    needs_improvement = False
    
    # First handle syntax errors and parsing issues
    if has_syntax_error or has_parsing_issue:
        needs_improvement = True
        error_message = cbmc_error_messages.get(func_name, "Unknown error")
        syntax_error = harness_syntax_errors.get(func_name, "")
        
        improvement_recommendation = f"""
        Previous harness for {func_name} has syntax or parsing errors and needs to be fixed.
        
        CBMC error: {error_message}
        
        Syntax error details: {syntax_error}
        
        Current harness (with errors):
        ```c
        {harness_code}
        ```
        
        Original function:
        ```c
        {func_code}
        ```
        
        Please fix the syntax or parsing errors in the harness. Specifically:
        1. Make sure all variables are properly declared before use
        2. Check for balanced braces and proper function definitions
        3. Ensure all code is complete and not truncated
        4. Include all necessary header files
        
        Generate a complete, syntactically valid harness that can be properly compiled and analyzed by CBMC.
        """
    # Then handle verification failures
    elif cbmc_status != "SUCCESS" and verification_failure_types:
        needs_improvement = True
        
        # Analyze memory issues
        memory_issues = []
        if "memory_leak" in verification_failure_types:
            memory_issues.append("Memory leaks detected - ensure all allocated memory is freed")
        if "null_pointer" in verification_failure_types:
            memory_issues.append("Null pointer dereferences - add null pointer checks")
            
        # Analyze arithmetic issues
        arithmetic_issues = []
        if "division_by_zero" in verification_failure_types:
            arithmetic_issues.append("Division by zero - add checks to ensure divisors are non-zero")
        if "arithmetic_overflow" in verification_failure_types or "pointer_overflow" in verification_failure_types:
            arithmetic_issues.append("Arithmetic/pointer overflow - add bounds checking")
            
        # Analyze array bounds issues
        array_issues = []
        if "array_bounds" in verification_failure_types:
            array_issues.append("Array bounds violations - verify array indices are within bounds")
            
        # Analyze type conversion issues
        type_issues = []
        if "type_conversion" in verification_failure_types:
            type_issues.append("Type conversion problems - check for information loss in type conversions")
            
        improvement_recommendation = f"""
        Previous harness for {func_name} failed CBMC verification. Quality score: {quality_score}%.
        
        CBMC verification status: {cbmc_status}
        
        CBMC error message: {verification_message}
        
        Suggested fixes: {suggestions}
        
        CBMC output excerpt:
        {cbmc_stdout[:500] if len(cbmc_stdout) > 500 else cbmc_stdout}
        
        Current harness:
        ```c
        {harness_code}
        ```
        
        Original function:
        ```c
        {func_code}
        ```
        
        Please improve the harness to address the following issues:
        
        {', '.join(memory_issues) if memory_issues else ''}
        {', '.join(arithmetic_issues) if arithmetic_issues else ''}
        {', '.join(array_issues) if array_issues else ''}
        {', '.join(type_issues) if type_issues else ''}
        
        Generate a complete, working harness that properly tests the function and passes CBMC verification.
        
        Refinement attempt: {current_attempts + 1} of {max_refinements}
        """
    # Finally evaluate general harness quality
    else:
        # Determine if improvement is needed
        needs_improvement = (
            cbmc_status != "SUCCESS" or 
            quality_score < 70 or
            not evaluation_criteria["has_nondet_inputs"] or
            not evaluation_criteria["has_assertions"] or
            (func_metadata.get("has_malloc", False) and not evaluation_criteria["checks_memory_leaks"]) or
            not evaluation_criteria["syntactically_valid"]
        )
        
        if needs_improvement and not has_syntax_error and not has_parsing_issue:
            improvement_areas = []
            
            # Generate specific improvement suggestions
            if not evaluation_criteria["has_nondet_inputs"]:
                improvement_areas.append("Use CBMC's nondet functions for inputs")
            
            if not evaluation_criteria["has_assertions"]:
                improvement_areas.append("Add CPROVER assertions to verify behavior")
            
            if not evaluation_criteria["has_assumptions"]:
                improvement_areas.append("Use CPROVER assumptions to constrain input values")
            
            if func_metadata.get("has_malloc", False) and not evaluation_criteria["checks_memory_leaks"]:
                improvement_areas.append("Add memory leak verification")
            
            improvement_recommendation = f"""
            Previous harness for {func_name} needs improvement. Quality score: {quality_score}%.
            
            CBMC verification status: {cbmc_status}
            
            Current harness:
            ```c
            {harness_code}
            ```
            
            Original function:
            ```c
            {func_code}
            ```
            
            Identified issues:
            {', '.join(improvement_areas)}
            
            Please improve the harness to address these issues. Generate a complete, working harness that properly tests the function.
            
            Refinement attempt: {current_attempts + 1} of {max_refinements}
            """
    
    # Calculate evaluation time
    evaluation_time = time.time() - evaluation_start
    
    # Update function times dictionary
    function_times = state.get("function_times", {}).copy()
    if func_name not in function_times:
        function_times[func_name] = {}
    function_times[func_name]["evaluation"] = evaluation_time
    
    # CRITICAL: Update refinement attempts BEFORE returning
    # This ensures we don't get stuck in an infinite loop
    if needs_improvement:
        refinement_attempts[func_name] = current_attempts + 1
        print(f"DEBUG: Incremented refinement attempts for {func_name} to {refinement_attempts[func_name]}")
    
    # CRITICAL: Mark as processed if NOT going to refine
    # This ensures forward progress in the workflow
    processed_functions = state.get("processed_functions", []).copy()
    if not needs_improvement:
        if func_name not in processed_functions:
            processed_functions.append(func_name)
            print(f"DEBUG: No more improvements needed, marking {func_name} as processed")
    
    # CRITICAL: Return loop_counter to prevent recursive error
    return {
        "messages": [AIMessage(content=f"Evaluated harness for {func_name} in {evaluation_time:.2f}s. {cbmc_status}. {'Improvements needed.' if needs_improvement else 'No improvements needed.'}")],
        "refinement_attempts": refinement_attempts,
        "processed_functions": processed_functions,
        "improvement_recommendation": improvement_recommendation,
        "function_times": function_times,
        "loop_counter": loop_counter,  # Pass the loop counter to maintain recursion tracking
        "next": "generator" if needs_improvement else "junction"
    }

# Node 7: Output - Final summary with performance metrics
def output_node(state):
    """Provides final summary of all processed functions with performance metrics and generates an index report."""
    import time
    import os
    total_time = time.time() - state.get("start_time", time.time())
    
    # Determine if we're in directory mode
    is_directory_mode = state.get("is_directory_mode", False)
    
    # Calculate summary statistics
    function_times = state.get("function_times", {})
    total_refinements = sum(state.get("refinement_attempts", {}).values())
    
    # Create performance metrics
    if function_times:
        avg_generation_time = sum(times.get("generation", 0) for times in function_times.values()) / len(function_times)
        avg_verification_time = sum(times.get("verification", 0) for times in function_times.values()) / len(function_times)
        avg_evaluation_time = sum(times.get("evaluation", 0) for times in function_times.values()) / len(function_times)
        avg_refinements = total_refinements / len(state.get("refinement_attempts", {})) if state.get("refinement_attempts", {}) else 0
    else:
        avg_generation_time = avg_verification_time = avg_evaluation_time = avg_refinements = 0
    
    # Create a header based on mode
    if is_directory_mode:
        source_files = state.get("source_files", {})
        header = [
            "# CBMC Harness Generation Complete - Directory Mode",
            "",
            f"Total processing time: {total_time:.2f} seconds",
            f"Processed {len(source_files)} source files.",
            f"Analyzed {len(state.get('embeddings', {}).get('functions', {}))} functions.",
            f"Identified {len(state.get('vulnerable_functions', []))} functions with memory or arithmetic operations.",
            f"Generated {len(state.get('harnesses', {}))} verification harnesses.",
            f"Performed {total_refinements} harness refinements (average {avg_refinements:.2f} per function).",
        ]
        
        # Add file statistics
        header.extend([
            "",
            "## File Analysis",
        ])
        
        # Group functions by file
        files_functions = {}
        for func_id in state.get('vulnerable_functions', []):
            file_name = "unknown"
            if ":" in func_id:
                file_name, _ = func_id.split(":", 1)
            
            if file_name not in files_functions:
                files_functions[file_name] = []
            files_functions[file_name].append(func_id)
        
        # Add file details
        for file_name, funcs in files_functions.items():
            header.append(f"\n### {file_name}")
            header.append(f"Functions analyzed: {len(funcs)}")
            verified_funcs = [f for f in funcs if f in state.get('cbmc_results', {})]
            header.append(f"Functions verified: {len(verified_funcs)}")
            
            if verified_funcs:
                successful = sum(1 for f in verified_funcs if state.get('cbmc_results', {}).get(f, {}).get('status') == 'SUCCESS')
                header.append(f"Successful verifications: {successful}")
                header.append(f"Failed verifications: {len(verified_funcs) - successful}")
    else:
        # Single file mode header
        header = [
            "# CBMC Harness Generation Complete",
            "",
            f"Total processing time: {total_time:.2f} seconds",
            f"Analyzed {len(state.get('embeddings', {}).get('functions', {}))} functions.",
            f"Identified {len(state.get('vulnerable_functions', []))} functions with memory or arithmetic operations.",
            f"Generated {len(state.get('harnesses', {}))} verification harnesses.",
            f"Performed {total_refinements} harness refinements (average {avg_refinements:.2f} per function).",
        ]
    
    # Add performance metrics
    header.extend([
        "",
        "## Performance Metrics",
        f"Average harness generation time: {avg_generation_time:.2f} seconds",
        f"Average verification time: {avg_verification_time:.2f} seconds",
        f"Average evaluation time: {avg_evaluation_time:.2f} seconds",
        "",
        "## Summary of Results"
    ])
    
    # Add results for each function
    for func_name in state.get("vulnerable_functions", []):
        if func_name in state.get("cbmc_results", {}):
            result = state.get("cbmc_results", {})[func_name]
            refinements = state.get("refinement_attempts", {}).get(func_name, 0)
            
            # Extract original function name and file if in directory mode
            display_name = func_name
            file_info = ""
            if ":" in func_name and is_directory_mode:
                file_name, orig_name = func_name.split(":", 1)
                display_name = orig_name
                file_info = f" (File: {file_name})"
            
            header.append(f"\n### Function: {display_name}{file_info}")
            header.append(f"Status: {result['status']}")
            header.append(f"Refinements: {refinements}")
            header.append(f"Message: {result['message']}")
            if result.get("suggestions"):
                header.append(f"Suggestions: {result['suggestions']}")
            
            # Add harness evolution information
            harness_history = state.get("harness_history", {}).get(func_name, [])
            if harness_history:
                header.append(f"Harness Evolution:")
                for i, _ in enumerate(harness_history):
                    header.append(f"  - Version {i+1}: harnesses/{func_name}/v{i+1}.c")
                
                # Add improvement metrics if there were multiple versions
                if len(harness_history) > 1:
                    # Compare first and last version
                    first_version = harness_history[0]
                    last_version = harness_history[-1]
                    
                    # Basic line count comparison
                    first_lines = len(first_version.split('\n'))
                    last_lines = len(last_version.split('\n'))
                    line_diff = last_lines - first_lines
                    
                    header.append(f"  - Size evolution: Initial {first_lines} lines → Final {last_lines} lines ({'+' if line_diff > 0 else ''}{line_diff} lines)")
                    
                    # Check if final version addressed verification issues
                    if result['status'] == 'SUCCESS':
                        header.append(f"  - Refinement result: Successfully addressed all verification issues")
                    else:
                        header.append(f"  - Refinement result: Some issues remain after {refinements} refinements")
            
            # List all verification reports
            header.append(f"Verification Reports: ")
            for i in range(1, refinements + 2):  # +2 because initial version is 1, and we need to go one past the refinement count
                header.append(f"  - verification/{func_name}/v{i}_results.txt")
                header.append(f"  - verification/{func_name}/v{i}_report.md")
    
    final_summary = "\n".join(header)
    
    # Create a main index report file
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)
    
    # Save final report
    with open(f"{report_dir}/final_report.md", "w") as f:
        f.write(final_summary)
        f.flush()
        os.fsync(f.fileno())
    
    # Generate an HTML version of the report
    try:
        # Try to generate HTML report if markdown is available
        import markdown
        with open(f"{report_dir}/final_report.html", "w") as f:
            f.write("<html><head><title>CBMC Verification Report</title>")
            f.write("<style>body{font-family:Arial,sans-serif;line-height:1.6;max-width:900px;margin:0 auto;padding:20px}h1{color:#2c3e50}h2{color:#3498db}h3{color:#2980b9}pre{background:#f8f8f8;border:1px solid #ddd;padding:10px;overflow:auto;border-radius:3px}table{border-collapse:collapse;width:100%}table,th,td{border:1px solid #ddd;padding:8px}th{background-color:#f2f2f2}tr:nth-child(even){background-color:#f9f9f9}</style>")
            f.write("</head><body>")
            f.write(markdown.markdown(final_summary))
            f.write("</body></html>")
    except ImportError:
        # If markdown is not available, create a simple HTML version
        with open(f"{report_dir}/final_report.html", "w") as f:
            f.write("<html><head><title>CBMC Verification Report</title></head><body>")
            f.write("<pre>" + final_summary + "</pre>")
            f.write("</body></html>")
    
    # Generate index.html that links to all reports
    with open(f"{report_dir}/index.html", "w") as f:
        f.write("<html><head><title>CBMC Verification Index</title>")
        f.write("<style>body{font-family:Arial,sans-serif;line-height:1.6;max-width:900px;margin:0 auto;padding:20px}h1{color:#2c3e50}h2{color:#3498db}h3{color:#2980b9}table{border-collapse:collapse;width:100%}table,th,td{border:1px solid #ddd;padding:8px}th{background-color:#f2f2f2}tr:nth-child(even){background-color:#f9f9f9}a{color:#3498db;text-decoration:none}a:hover{text-decoration:underline}</style>")
        f.write("</head><body>")
        f.write("<h1>CBMC Verification Reports</h1>")
        f.write("<p>This index provides links to all verification reports generated.</p>")
        
        # Link to final report
        f.write("<h2>Final Summary Report</h2>")
        f.write("<p><a href='final_report.html'>View Complete Summary Report</a></p>")
        
        # Table of function reports
        f.write("<h2>Function Reports</h2>")
        f.write("<table>")
        f.write("<tr><th>Function</th><th>File</th><th>Status</th><th>Versions</th><th>Reports</th></tr>")
        
        for func_name in state.get("vulnerable_functions", []):
            if func_name in state.get("cbmc_results", {}):
                result = state.get("cbmc_results", {})[func_name]
                refinements = state.get("refinement_attempts", {}).get(func_name, 0)
                
                # Extract original function name and file if in directory mode
                display_name = func_name
                file_name = ""
                if ":" in func_name:
                    file_name, display_name = func_name.split(":", 1)
                
                # Determine status color
                status_style = ""
                if result['status'] == "SUCCESS":
                    status_style = "style='color:green;font-weight:bold'"
                elif result['status'] == "FAILED":
                    status_style = "style='color:red;font-weight:bold'"
                elif result['status'] == "TIMEOUT":
                    status_style = "style='color:orange;font-weight:bold'"
                else:
                    status_style = "style='color:gray;font-weight:bold'"
                
                # Get version count
                version_count = len(state.get("harness_history", {}).get(func_name, [])) or refinements + 1
                
                f.write(f"<tr><td>{display_name}</td><td>{file_name}</td><td {status_style}>{result['status']}</td>")
                
                # Add links to all harness versions 
                f.write("<td>")
                for i in range(1, version_count + 1):
                    f.write(f"<a href='../harnesses/{func_name}/v{i}.c'>v{i}</a> ")
                f.write("</td>")
                
                # Add links to all version reports
                f.write("<td>")
                for i in range(1, refinements + 2):
                    f.write(f"<a href='../verification/{func_name}/v{i}_report.md'>v{i}</a> ")
                f.write("</td></tr>")
        
        f.write("</table>")
        
        # Add evolution section if any functions have multiple versions
        evolution_data = [func for func in state.get("vulnerable_functions", []) 
                         if len(state.get("harness_history", {}).get(func, [])) > 1]
        
        if evolution_data:
            f.write("<h2>Harness Evolution</h2>")
            f.write("<p>The following functions underwent multiple iterations of refinement:</p>")
            
            f.write("<table>")
            f.write("<tr><th>Function</th><th>Versions</th><th>Final Status</th><th>Line Count Evolution</th></tr>")
            
            for func_name in evolution_data:
                history = state.get("harness_history", {}).get(func_name, [])
                versions = len(history)
                status = state.get("cbmc_results", {}).get(func_name, {}).get("status", "UNKNOWN")
                
                # Calculate line count evolution
                if len(history) > 1:
                    first_lines = len(history[0].split('\n'))
                    last_lines = len(history[-1].split('\n'))
                    line_diff = last_lines - first_lines
                    line_evolution = f"{first_lines} → {last_lines} ({'+' if line_diff > 0 else ''}{line_diff})"
                else:
                    line_evolution = "N/A"
                
                # Determine status color
                status_style = ""
                if status == "SUCCESS":
                    status_style = "style='color:green;font-weight:bold'"
                elif status == "FAILED":
                    status_style = "style='color:red;font-weight:bold'"
                elif status == "TIMEOUT":
                    status_style = "style='color:orange;font-weight:bold'"
                else:
                    status_style = "style='color:gray;font-weight:bold'"
                
                # Extract display name
                display_name = func_name
                if ":" in func_name:
                    _, display_name = func_name.split(":", 1)
                
                f.write(f"<tr><td>{display_name}</td><td>{versions}</td>")
                f.write(f"<td {status_style}>{status}</td><td>{line_evolution}</td></tr>")
            
            f.write("</table>")
        
        f.write("</body></html>")
    
    return {
        "messages": [AIMessage(content=f"Analysis complete! Reports generated in the 'reports' directory. View the main index at reports/index.html")]
    }

# Routing function for Junction node
def route_from_junction(state):
    """Routes from junction to either generator or output."""
    return state.get("next", "generator")

# Routing function for Generator node
def route_from_generator(state):
    """Routes from generator to either cbmc or junction."""
    return state.get("next", "cbmc")

# Routing function for CBMC node - Updated to point to Evaluator
def route_from_cbmc(state):
    """Routes from CBMC to harness evaluator."""
    return "evaluator"  # Always go to evaluator after CBMC

# Routing function for Evaluator node
def route_from_evaluator(state):
    """Routes from evaluator to either generator (for refinement) or junction (for next function)."""
    return state.get("next", "junction")

# Build the graph
workflow = StateGraph(HarnessGenerationState)

# Add nodes
workflow.add_node("frontend", frontend_node)
workflow.add_node("code_embedding", code_embedding_node)
workflow.add_node("analyzer", analyzer_node)
workflow.add_node("junction", junction_node)
workflow.add_node("generator", generator_node)
workflow.add_node("cbmc", cbmc_node)
workflow.add_node("evaluator", harness_evaluator_node)
workflow.add_node("output", output_node)

# Connect the nodes with the main flow
workflow.add_edge(START, "frontend")
workflow.add_edge("frontend", "code_embedding")
workflow.add_edge("code_embedding", "analyzer") 
workflow.add_edge("analyzer", "junction")

# Add conditional routing based on next state
workflow.add_conditional_edges(
    "junction",
    route_from_junction,
    {
        "generator": "generator",
        "output": "output"
    }
)

workflow.add_conditional_edges(
    "generator",
    route_from_generator,
    {
        "cbmc": "cbmc",
        "junction": "junction"
    }
)

# Route from CBMC to Evaluator
workflow.add_conditional_edges(
    "cbmc",
    route_from_cbmc,
    {
        "evaluator": "evaluator"
    }
)

# Route from Evaluator to either Generator (for refinement) or Junction (for next function)
workflow.add_conditional_edges(
    "evaluator",
    route_from_evaluator,
    {
        "generator": "generator",  # For harness refinement
        "junction": "junction"     # For next function
    }
)

workflow.add_edge("output", END)

# Compile the graph
app = workflow.compile()

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

# Update the main function to use the file-based estimation
def main():
    parser = argparse.ArgumentParser(description='CBMC Harness Generator')
    parser.add_argument('-d', '--directory', type=str, help='Directory containing C source files to analyze')
    parser.add_argument('-f', '--file', type=str, help='Single C source file to analyze')
    args = parser.parse_args()
    
    if args.directory:
        # Directory mode
        initial_message = HumanMessage(content=f"""
        I need to analyze all C source files in the directory: {args.directory}
        Please identify any potential memory leaks and generate CBMC harnesses for verification.
        """)
        
        # Count C source files in the directory for estimation
        source_files_count = 0
        source_subdir = os.path.join(args.directory, "source")
        if not os.path.isdir(source_subdir):
            source_subdir = args.directory
            
        for pattern in ['*.c', '*.cpp']:
            source_files_count += len(glob.glob(os.path.join(source_subdir, "**", pattern), recursive=True))
        
        # Calculate recursion limit based on file count
        recursion_limit = calculate_recursion_limit(source_files_count)
        
        # Run workflow with calculated limit
        result = app.invoke(
            {
                "messages": [initial_message],
                "source_code": "",
                "embeddings": {},
                "vulnerable_functions": [],
                "harnesses": {},
                "cbmc_results": {},
                "processed_functions": []
            },
            {"recursion_limit": recursion_limit}
        )
    elif args.file:
        # Single file mode - use a simpler estimation
        try:
            with open(args.file, 'r') as f:
                source_code = f.read()
                
            # For a single file, use a fixed recursion limit or estimate based on file size
            file_size = len(source_code)
            # Rough heuristic: 1 function per 100 lines, ~50 chars per line
            estimated_functions = max(5, file_size // 5000)
            recursion_limit = calculate_recursion_limit(estimated_functions // 8 + 1)  # Convert back to file count
                
            initial_message = HumanMessage(content=f"""
            I need to analyze the following C code for memory leaks and generate verification harnesses:

            ```c
            {source_code}
            ```

            Please identify any potential memory leaks and generate CBMC harnesses for verification.
            """)
            
            # Run workflow with calculated limit
            result = app.invoke(
                {
                    "messages": [initial_message],
                    "source_code": source_code,
                    "embeddings": {},
                    "vulnerable_functions": [],
                    "harnesses": {},
                    "cbmc_results": {},
                    "processed_functions": []
                },
                {"recursion_limit": recursion_limit}
            )
        except Exception as e:
            print(f"Error reading file {args.file}: {str(e)}")
            return
    else:
        print("Please provide either a directory (-d) or a file (-f) to analyze")
        return
    
    # Display the conversation
    print("=== Workflow Execution Results ===")
    for i, message in enumerate(result["messages"]):
        if isinstance(message, HumanMessage):
            print(f"\n===== Human Message {i+1} =====")
            print(message.content[:200] + "..." if len(message.content) > 200 else message.content)
        elif isinstance(message, AIMessage):
            print(f"\n===== AI Message {i+1} =====")
            print(message.content)

if __name__ == "__main__":
    main()