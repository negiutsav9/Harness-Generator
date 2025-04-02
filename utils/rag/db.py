"""
Unified embedding database for the CBMC harness generator.

This module provides a consolidated RAG (Retrieval-Augmented Generation) database
that combines code embeddings, pattern embeddings, harness error embeddings, and
solution embeddings in a single interface.

Usage:
    from utils.rag.db import get_unified_db
    
    # Get the global instance
    db = get_unified_db(persistence_dir="results/rag_data")
    
    # Store and retrieve code functions
    db.add_code_function(func_id, func_code, metadata)
    function = db.get_code_function(func_id)
    
    # Query for similar functions
    similar_functions = db.query_code_function(query_text)
    
    # Query for matching patterns
    pattern_results = db.query_pattern_db(func_code)
    
    # Store errors and solutions
    error_id = db.store_error(func_name, harness_code, cbmc_result, iteration)
    solution_id = db.store_solution(error_id, func_name, harness_code, cbmc_result, iteration)
    
    # Get recommendations for function with errors
    recommendations = db.get_recommendations(func_name, func_code, cbmc_result, harness_code)
"""
import os
import re
import json
import time
import logging
import chromadb
from chromadb.utils import embedding_functions
from typing import Dict, List, Any, Optional, Tuple, Set

# Set up logging
logger = logging.getLogger("rag.db")

class UnifiedEmbeddingDB:
    """
    Unified database for storing and retrieving embeddings for code, patterns, errors, and solutions.
    """
    
    def __init__(self, persistence_dir: str = "rag_data"):
        """
        Initialize the unified embedding database.
        
        Args:
            persistence_dir: Directory to store the persistent database
        """
        self.persistence_dir = persistence_dir
        os.makedirs(persistence_dir, exist_ok=True)
        
        # Set up ChromaDB with persistence
        self.chroma_client = chromadb.PersistentClient(path=persistence_dir)
        self.sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
        
        # Initialize all collections
        self._initialize_collections()
        
        logger.info(f"Initialized UnifiedEmbeddingDB with persistence at {persistence_dir}")
    
    def _initialize_collections(self):
        """Initialize all embedding collections."""
        # Create or get code collection
        try:
            self.code_collection = self.chroma_client.get_collection(
                name="code_embeddings",
                embedding_function=self.sentence_transformer_ef
            )
            logger.info(f"Retrieved existing code collection with {self.code_collection.count()} entries")
        except:
            self.code_collection = self.chroma_client.create_collection(
                name="code_embeddings",
                embedding_function=self.sentence_transformer_ef,
                metadata={"hnsw:space": "cosine"}
            )
            logger.info("Created new code collection")
        
        # Create or get pattern collection
        try:
            self.pattern_collection = self.chroma_client.get_collection(
                name="pattern_embeddings",
                embedding_function=self.sentence_transformer_ef
            )
            logger.info(f"Retrieved existing pattern collection with {self.pattern_collection.count()} entries")
        except:
            self.pattern_collection = self.chroma_client.create_collection(
                name="pattern_embeddings",
                embedding_function=self.sentence_transformer_ef,
                metadata={"hnsw:space": "cosine"}
            )
            self._initialize_pattern_collection()
            logger.info("Created new pattern collection with initial patterns")
        
        # Create or get error collection
        try:
            self.error_collection = self.chroma_client.get_collection(
                name="harness_errors",
                embedding_function=self.sentence_transformer_ef
            )
            logger.info(f"Retrieved existing error collection with {self.error_collection.count()} entries")
        except:
            self.error_collection = self.chroma_client.create_collection(
                name="harness_errors",
                embedding_function=self.sentence_transformer_ef,
                metadata={"hnsw:space": "cosine"}
            )
            logger.info("Created new error collection")
        
        # Create or get solution collection
        try:
            self.solution_collection = self.chroma_client.get_collection(
                name="harness_solutions",
                embedding_function=self.sentence_transformer_ef
            )
            logger.info(f"Retrieved existing solution collection with {self.solution_collection.count()} entries")
        except:
            self.solution_collection = self.chroma_client.create_collection(
                name="harness_solutions",
                embedding_function=self.sentence_transformer_ef,
                metadata={"hnsw:space": "cosine"}
            )
            logger.info("Created new solution collection")
    
    def _initialize_pattern_collection(self):
        """Initialize pattern collection with common memory and arithmetic patterns."""
        self.pattern_collection.add(
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
    
    # CODE EMBEDDING METHODS
    
    def add_code_function(self, func_id: str, func_code: str, metadata: Dict[str, Any]) -> bool:
        """
        Add a function to the code collection.
        
        Args:
            func_id: Unique ID for the function
            func_code: The function code
            metadata: Metadata about the function
            
        Returns:
            True if successful, False otherwise
        """
        try:
            self.code_collection.add(
                ids=[func_id],
                documents=[func_code],
                metadatas=[metadata]
            )
            logger.info(f"Added function {func_id} to code collection")
            return True
        except Exception as e:
            logger.error(f"Error adding function {func_id} to code collection: {str(e)}")
            return False
    
    def query_code_function(self, query: str, n_results: int = 5) -> List[Dict[str, Any]]:
        """
        Query the code collection for functions matching the query.
        
        Args:
            query: The search query
            n_results: Number of results to return
            
        Returns:
            List of matching functions with metadata
        """
        try:
            results = self.code_collection.query(
                query_texts=[query],
                n_results=n_results
            )
            
            functions = []
            if results["ids"] and results["ids"][0]:
                for i, func_id in enumerate(results["ids"][0]):
                    metadata = results["metadatas"][0][i]
                    distance = results["distances"][0][i] if "distances" in results else 1.0
                    
                    functions.append({
                        "func_id": func_id,
                        "code": results["documents"][0][i] if "documents" in results else "",
                        "metadata": metadata,
                        "similarity_score": 1.0 - distance
                    })
            
            return functions
        except Exception as e:
            logger.error(f"Error querying code collection: {str(e)}")
            return []
    
    def get_code_function(self, func_id: str) -> Optional[Dict[str, Any]]:
        """
        Get a specific function by ID.
        
        Args:
            func_id: ID of the function
            
        Returns:
            Function data or None if not found
        """
        try:
            result = self.code_collection.get(
                ids=[func_id],
                include=["documents", "metadatas"]
            )
            
            if result["ids"]:
                return {
                    "func_id": result["ids"][0],
                    "code": result["documents"][0],
                    "metadata": result["metadatas"][0]
                }
            return None
        except Exception as e:
            logger.error(f"Error getting function {func_id}: {str(e)}")
            return None
    
    # PATTERN METHODS
    
    def query_pattern_db(self, query: str) -> Dict[str, Any]:
        """
        Query the pattern collection for relevant patterns.
        
        Args:
            query: The search query
            
        Returns:
            Dictionary with matching patterns
        """
        # Query the pattern collection to find relevant patterns
        try:
            results = self.pattern_collection.query(
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
                metadata_results = self.pattern_collection.get(ids=[pattern_id])
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
                "message": f"Found {len(matching_patterns)} potential matching patterns"
            }
        except Exception as e:
            logger.error(f"Error querying pattern database: {str(e)}")
            return {
                "matching_patterns": {},
                "message": f"Error querying pattern database: {str(e)}"
            }
    
    # ERROR AND SOLUTION METHODS
    
    def store_error(self, 
                   func_name: str, 
                   harness_code: str, 
                   cbmc_result: Dict[str, Any], 
                   iteration: int) -> str:
        """
        Store an error pattern in the error collection.
        
        Args:
            func_name: Name of the function
            harness_code: The harness code that produced the error
            cbmc_result: The CBMC verification result
            iteration: The iteration number
            
        Returns:
            The ID of the stored error
        """
        # Generate a unique ID
        error_id = f"{func_name}_error_{iteration}_{int(time.time())}"
        
        # Extract key error information
        error_categories = cbmc_result.get("error_categories", [])
        error_message = cbmc_result.get("message", "Unknown error")
        
        # Create error description for embedding
        error_description = f"Function: {func_name}\nError: {error_message}\nCategories: {', '.join(error_categories)}"
        
        # Extract failing code patterns for better retrieval
        error_locations = cbmc_result.get("error_locations", {})
        error_lines = []
        
        # Find the harness lines corresponding to errors
        # Find the harness lines corresponding to errors
        for file_name, line_nums in error_locations.items():
            harness_lines = harness_code.split('\n')
            for line_num in line_nums:
                # Convert line_num to integer if it's a string
                if isinstance(line_num, str):
                    try:
                        line_num = int(line_num)
                    except ValueError:
                        # Skip this line number if it can't be converted
                        continue
                
                # Only add lines that exist in the harness (adjust for 0-indexing)
                if 0 <= line_num - 1 < len(harness_lines):
                    error_lines.append(harness_lines[line_num - 1].strip())
        
        # Add error line snippets to description if available
        if error_lines:
            error_description += f"\nError patterns:\n" + "\n".join(error_lines)
        
        # Store error in knowledge base
        try:
            self.error_collection.add(
                ids=[error_id],
                documents=[error_description],
                metadatas=[{
                    "func_name": func_name,
                    "iteration": iteration,
                    "error_categories": json.dumps(error_categories),
                    "error_message": error_message,
                    "has_memory_leak": "memory_leak" in error_categories,
                    "has_array_bounds": "array_bounds" in error_categories,
                    "has_null_pointer": "null_pointer" in error_categories,
                    "has_arithmetic_issue": any(cat in error_categories for cat in ["division_by_zero", "arithmetic_overflow"]),
                    "timestamp": time.time()
                }]
            )
            logger.info(f"Stored error pattern {error_id} for {func_name}")
            return error_id
        except Exception as e:
            logger.error(f"Error storing error pattern: {str(e)}")
            return ""
    
    def store_solution(self, 
                      error_id: str, 
                      func_name: str, 
                      harness_code: str, 
                      cbmc_result: Dict[str, Any],
                      iteration: int) -> str:
        """
        Store a successful solution in the solution collection.
        
        Args:
            error_id: ID of the corresponding error
            func_name: Name of the function
            harness_code: The successful harness code
            cbmc_result: The successful CBMC verification result
            iteration: The iteration number
            
        Returns:
            The ID of the stored solution
        """
        # Generate a unique ID
        solution_id = f"{func_name}_solution_{iteration}_{int(time.time())}"
        
        # Create solution description for embedding
        solution_description = f"Function: {func_name}\nSuccessful harness for iteration {iteration}"
        
        # Add coverage metrics
        if "coverage_pct" in cbmc_result:
            coverage = cbmc_result.get("coverage_pct", 0.0)
            solution_description += f"\nCoverage: {coverage:.2f}%"
        
        # Extract successful patterns - look for memory management and testing patterns
        patterns = []
        
        # Find malloc/free patterns
        malloc_free_pattern = self._extract_pattern(harness_code, r'(\w+\s*=\s*malloc\([^;]+;.*?free\(\s*\w+\s*\);)', 
                                                   "Memory allocation pattern")
        if malloc_free_pattern:
            patterns.append(malloc_free_pattern)
        
        # Find null checks
        null_check_pattern = self._extract_pattern(harness_code, r'(if\s*\(\s*\w+\s*==\s*NULL\s*\)[^}]+})', 
                                                  "Null check pattern")
        if null_check_pattern:
            patterns.append(null_check_pattern)
        
        # Find CPROVER assumes
        cprover_pattern = self._extract_pattern(harness_code, r'(__CPROVER_assume\([^;]+;)', 
                                               "CPROVER assumption pattern")
        if cprover_pattern:
            patterns.append(cprover_pattern)
        
        # Add patterns to description
        if patterns:
            solution_description += "\nSuccessful patterns:\n" + "\n".join(patterns)
        
        # Store solution in knowledge base
        try:
            self.solution_collection.add(
                ids=[solution_id],
                documents=[solution_description],
                metadatas=[{
                    "func_name": func_name,
                    "iteration": iteration,
                    "related_error_id": error_id,
                    "coverage": cbmc_result.get("coverage_pct", 0.0),
                    "patterns_found": len(patterns),
                    "has_malloc_free": bool(malloc_free_pattern),
                    "has_null_check": bool(null_check_pattern),
                    "has_cprover_assume": bool(cprover_pattern),
                    "timestamp": time.time(),
                    "harness_code": harness_code  # Store complete harness for reuse
                }]
            )
            logger.info(f"Stored solution {solution_id} for {func_name}")
            return solution_id
        except Exception as e:
            logger.error(f"Error storing solution: {str(e)}")
            return ""
    
    def _extract_pattern(self, code: str, pattern: str, label: str) -> str:
        """
        Extract reusable code patterns from harness code.
        
        Args:
            code: The harness code
            pattern: Regex pattern to extract
            label: Label for the pattern
            
        Returns:
            Extracted pattern with label or empty string if not found
        """
        matches = re.findall(pattern, code, re.DOTALL)
        if matches:
            # Return the first match with label
            return f"{label}:\n{matches[0].strip()}"
        return ""
    
    def query_similar_errors(self, 
                           func_name: str, 
                           func_code: str, 
                           error_description: str, 
                           top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Query the error collection for similar error patterns.
        
        Args:
            func_name: Name of the function
            func_code: The function code
            error_description: Description of the current error
            top_k: Number of results to return
            
        Returns:
            List of similar error patterns with metadata
        """
        # Create query combining function information with error description
        function_signature = self._extract_function_signature(func_code)
        query = f"Function: {func_name}\n{function_signature}\nError: {error_description}"
        
        # Check if there are any errors in the database
        if self.error_collection.count() == 0:
            logger.info("No errors in knowledge base yet")
            return []
        
        try:
            # Query for similar errors
            results = self.error_collection.query(
                query_texts=[query],
                n_results=top_k
            )
            
            # Process and return results
            similar_errors = []
            if results["ids"] and results["ids"][0]:
                for i, error_id in enumerate(results["ids"][0]):
                    # Skip if we have no metadatas
                    if not results["metadatas"] or not results["metadatas"][0]:
                        continue
                        
                    metadata = results["metadatas"][0][i]
                    distance = results["distances"][0][i] if "distances" in results else 1.0
                    
                    # Convert JSON strings back to Python objects
                    error_categories = json.loads(metadata.get("error_categories", "[]"))
                    
                    similar_errors.append({
                        "error_id": error_id,
                        "func_name": metadata.get("func_name", ""),
                        "error_categories": error_categories,
                        "error_message": metadata.get("error_message", ""),
                        "similarity_score": 1.0 - distance,  # Convert distance to similarity
                        "document": results["documents"][0][i] if "documents" in results else ""
                    })
            
            logger.info(f"Found {len(similar_errors)} similar errors for {func_name}")
            return similar_errors
        except Exception as e:
            logger.error(f"Error querying similar errors: {str(e)}")
            return []
    
    def query_solutions_for_error(self, 
                                error_id: str, 
                                func_name: str, 
                                top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Query the solution collection for solutions matching a specific error.
        
        Args:
            error_id: ID of the error to find solutions for
            func_name: Name of the function
            top_k: Number of results to return
            
        Returns:
            List of solutions with metadata
        """
        if not error_id:
            # Also try to search by function name
            solutions = self.solution_collection.get(
                where={"func_name": func_name},
                limit=top_k
            )
        else:
            # Try to find solutions related to the error ID
            solutions = self.solution_collection.get(
                where={"related_error_id": error_id},
                limit=top_k
            )
            
            # If no solutions found, try to find solutions for the function
            if not solutions["ids"]:
                solutions = self.solution_collection.get(
                    where={"func_name": func_name},
                    limit=top_k
                )
        
        if not solutions["ids"]:
            logger.info(f"No solutions found for error {error_id} or function {func_name}")
            return []
        
        # Process and return results
        solution_list = []
        for i, solution_id in enumerate(solutions["ids"]):
            metadata = solutions["metadatas"][i]
            solution_list.append({
                "solution_id": solution_id,
                "func_name": metadata.get("func_name", ""),
                "iteration": metadata.get("iteration", 0),
                "coverage": metadata.get("coverage", 0.0),
                "patterns_found": metadata.get("patterns_found", 0),
                "harness_code": metadata.get("harness_code", ""),
                "document": solutions["documents"][i] if "documents" in solutions else ""
            })
        
        logger.info(f"Found {len(solution_list)} solutions for error {error_id}")
        return solution_list
    
    def _extract_function_signature(self, func_code: str) -> str:
        """
        Extract the function signature from the function code.
        
        Args:
            func_code: The function code
            
        Returns:
            Function signature (return type, name, parameters)
        """
        signature_match = re.search(r'^([\w\s\*]+)\s+(\w+)\s*\(([^)]*)\)', func_code.strip(), re.MULTILINE)
        if signature_match:
            return_type = signature_match.group(1).strip()
            func_name = signature_match.group(2).strip()
            params = signature_match.group(3).strip()
            return f"{return_type} {func_name}({params})"
        return ""
    
    def get_recommendations(self, 
                          func_name: str, 
                          func_code: str, 
                          cbmc_result: Dict[str, Any],
                          previous_harness: str) -> Dict[str, Any]:
        """
        Get comprehensive recommendations for fixing a failing harness.
        
        Args:
            func_name: Name of the function
            func_code: The function code
            cbmc_result: The CBMC verification result
            previous_harness: The previous harness code that failed
            
        Returns:
            Dictionary with recommendations
        """
        # Extract error information
        error_categories = cbmc_result.get("error_categories", [])
        error_message = cbmc_result.get("message", "Unknown error")
        
        # Build error description
        error_description = f"{error_message}"
        if error_categories:
            error_description += f" Categories: {', '.join(error_categories)}"
        
        # Query for similar errors
        similar_errors = self.query_similar_errors(func_name, func_code, error_description)
        
        # Get solutions for similar errors
        solutions = []
        if similar_errors:
            # Get the most similar error
            most_similar = similar_errors[0]
            solutions = self.query_solutions_for_error(most_similar["error_id"], func_name)
        
        # Query for patterns that match this function's issues
        pattern_results = self.query_pattern_db(func_code)
        matching_patterns = pattern_results.get("matching_patterns", {})
        
        # Build recommendation
        recommendation = {
            "has_similar_errors": bool(similar_errors),
            "similar_errors": similar_errors,
            "has_solutions": bool(solutions),
            "solutions": solutions,
            "has_matching_patterns": bool(matching_patterns),
            "matching_patterns": matching_patterns,
            "error_categories": error_categories,
            "recommendations": []
        }
        
        # Add specific recommendations based on what we found
        if solutions and solutions[0].get("harness_code"):
            # Best case: we have a complete solution for a similar error
            best_solution = solutions[0]
            recommendation["recommendations"].append({
                "type": "complete_solution",
                "message": f"Found a complete solution for a similar error in function {best_solution['func_name']}",
                "harness_code": best_solution["harness_code"]
            })
        elif matching_patterns:
            # Second best: we have patterns that match the vulnerabilities in this function
            for pattern_name, pattern_info in matching_patterns.items():
                recommendation["recommendations"].append({
                    "type": "pattern",
                    "pattern_name": pattern_name,
                    "message": f"Found a matching pattern: {pattern_info['description']}",
                    "verification_strategy": pattern_info["verification_strategy"],
                    "severity": pattern_info["severity"]
                })
        
        # Add default recommendations based on error categories
        if "memory_leak" in error_categories:
            recommendation["recommendations"].append({
                "type": "default",
                "message": "Ensure proper memory cleanup after allocation",
                "suggestion": "Add corresponding free() calls for each malloc() and implement proper error handling"
            })
        
        if "null_pointer" in error_categories:
            recommendation["recommendations"].append({
                "type": "default",
                "message": "Add null pointer checks before dereferencing",
                "suggestion": "Add if (ptr != NULL) checks and CPROVER_assume(ptr != NULL) where appropriate"
            })
        
        return recommendation
    
# Global instance for convenience
_db_instance = None

def get_unified_db(persistence_dir: str = "rag_db") -> UnifiedEmbeddingDB:
    """
    Get the global unified database instance.
    
    Args:
        persistence_dir: Directory for persistence
        
    Returns:
        The global UnifiedEmbeddingDB instance
    """
    global _db_instance
    if _db_instance is None:
        _db_instance = UnifiedEmbeddingDB(persistence_dir)
    return _db_instance