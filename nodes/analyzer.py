"""
Analyzer node for CBMC harness generator workflow.
"""
import time
import os
import logging
import json
import re
from langchain_core.messages import AIMessage, SystemMessage
from core.embedding_db import code_collection, query_pattern_db

# Set up logging - simplified
logger = logging.getLogger("analyzer")

def analyzer_node(state):
    """Analyzes code from CodeDB to identify vulnerable functions using LLM reasoning."""
    analysis_start = time.time()
    
    logger.info(f"Starting LLM-enhanced code analysis")
    
    try:
        # Get all functions from the code database
        all_functions = code_collection.get()
        target_functions = []
        function_details = []
        
        logger.info(f"Retrieved {len(all_functions.get('ids', []))} functions for analysis")
        
        # Prepare function information for LLM analysis
        for i, func_id in enumerate(all_functions.get("ids", [])):
            metadata = all_functions["metadatas"][i]
            func_code = all_functions["documents"][i]
            file_path = metadata.get("file_path", "")
            
            # Match against known vulnerability patterns
            patterns_result = query_pattern_db(func_code)
            matching_patterns = patterns_result.get("matching_patterns", {})
            
            # Create rich context for LLM analysis
            function_details.append({
                "id": func_id,
                "code": func_code,
                "signature": f"{metadata.get('return_type', 'void')} {metadata.get('name', 'unknown')}({metadata.get('params', '')})",
                "has_malloc": metadata.get("has_malloc", False),
                "has_free": metadata.get("has_free", False),
                "file_path": file_path,
                "matching_patterns": matching_patterns
            })
            
            # Pre-filter based on memory/arithmetic operations
            has_memory_ops = any(op in func_code for op in [
                "malloc(", "calloc(", "realloc(", "free(", "alloca(", 
                "new ", "delete ", "memcpy(", "memmove(", "memset(",
                "&", "*", "->", "[]"
            ])
            
            has_arithmetic = any(op in func_code for op in [
                "+", "-", "*", "/", "%", "+=", "-=", "*=", "/=", "%=", "++", "--"
            ])
            
            # Add to target list if potentially vulnerable
            if has_memory_ops or has_arithmetic or matching_patterns:
                target_functions.append(func_id)
        
        logger.info(f"Pre-filtered to {len(target_functions)} potential targets based on operations and patterns")
        
        # Create prompt for LLM analysis
        prompt = f"""
        You are an expert in detecting memory safety issues in C code. Analyze these functions to identify those most likely to have memory issues.
        
        For each function, consider:
        1. Memory allocation without corresponding deallocation
        2. Conditional paths that might skip deallocation
        3. Error handling paths that might leak memory
        4. Buffer overflows and out-of-bounds access
        5. Use-after-free vulnerabilities
        6. Double-free issues
        7. Integer overflow leading to incorrect allocation
        
        I've already performed initial pattern matching against known vulnerability patterns in our database.
        
        Assign a risk score (1-10) to each function based on these factors. Prioritize functions that:
        - Have pattern matches from our database
        - Allocate memory but don't free it
        - Have complex control flow with memory operations
        - Mix pointer arithmetic with memory allocation
        
        Return a JSON object with:
        1. A sorted list of functions by risk score (highest first)
        2. A brief explanation for each function's risk assessment
        
        Here are the functions to analyze, with their pattern matching results:
        {json.dumps(function_details[:30], indent=2)}  # Limit for prompt size
        """
        
        # Get LLM analysis
        from utils.llm_utils import setup_llm
        llm = setup_llm()
        logger.info("Sending functions to LLM for vulnerability analysis")
        response = llm.invoke([
            SystemMessage(content=prompt)
        ])
        
        # Parse LLM response to extract vulnerable functions with risk assessment
        try:
            # Find JSON content
            json_match = re.search(r'```json\n(.*?)\n```', response.content, re.DOTALL)
            if json_match:
                analysis_json = json.loads(json_match.group(1))
            else:
                # Try to directly parse the content
                analysis_json = json.loads(response.content)
            
            # Extract functions with risk assessment
            risk_sorted_functions = analysis_json.get("functions", [])
            
            # Get function IDs
            vulnerable_functions = [func["id"] for func in risk_sorted_functions 
                                   if func.get("score", 0) >= 4]  # Filter medium and high risk
            
            # Create risk scores mapping
            risk_scores = {}
            for func in risk_sorted_functions:
                if "id" in func:
                    risk_scores[func["id"]] = {
                        "score": func.get("score", 0),
                        "reason": func.get("reason", ""),
                        "patterns": func.get("matching_patterns", [])
                    }
            
            logger.info(f"LLM analysis identified {len(vulnerable_functions)} vulnerable functions")
            
        except (json.JSONDecodeError, AttributeError) as e:
            logger.warning(f"Unable to parse LLM response as JSON, falling back to pattern-based filtering")
            # Fallback to pre-filtered target functions
            vulnerable_functions = target_functions
            
            # Create basic risk scores using pattern matching
            risk_scores = {}
            for i, func_info in enumerate(function_details):
                func_id = func_info.get("id")
                if func_id in vulnerable_functions:
                    patterns = func_info.get("matching_patterns", {})
                    score = min(4 + len(patterns) * 2, 10)  # Base score of 4, +2 for each pattern match
                    risk_scores[func_id] = {
                        "score": score,
                        "reason": f"Matched {len(patterns)} vulnerability patterns" if patterns else "Contains memory operations",
                        "patterns": list(patterns.keys())
                    }
        
        # Sort by risk score if available
        if risk_scores:
            vulnerable_functions.sort(key=lambda x: risk_scores.get(x, {}).get("score", 0), reverse=True)
        
        # Categorize identified issues
        category_count = {
            "memory_leak": sum(1 for _, info in risk_scores.items() if "leak" in info.get("reason", "").lower()),
            "null_pointer": sum(1 for _, info in risk_scores.items() if "null" in info.get("reason", "").lower()),
            "buffer_overflow": sum(1 for _, info in risk_scores.items() if "overflow" in info.get("reason", "").lower()),
            "use_after_free": sum(1 for _, info in risk_scores.items() if "after free" in info.get("reason", "").lower()),
        }
        
        # Calculate time taken
        analysis_time = time.time() - analysis_start
        logger.info(f"Analysis completed in {analysis_time:.2f}s - Found {len(vulnerable_functions)} vulnerable functions")
        
        return {
            "messages": [AIMessage(content=f"Analysis complete in {analysis_time:.2f}s. Identified {len(vulnerable_functions)} vulnerable functions, prioritized by risk. Main issues: {', '.join(f'{k}: {v}' for k, v in category_count.items() if v > 0)}.")],
            "vulnerable_functions": vulnerable_functions,
            "risk_scores": risk_scores,
            "total_functions": len(vulnerable_functions),
            "current_function_index": 0
        }
    except Exception as e:
        logger.error(f"Error during analysis: {str(e)}")
        # Return a minimal set to prevent complete failure
        return {
            "messages": [AIMessage(content=f"Error during analysis: {str(e)}. Proceeding with limited function set.")],
            "vulnerable_functions": target_functions[:10] if target_functions else [],
            "total_functions": len(target_functions[:10]) if target_functions else 0,
            "current_function_index": 0
        }