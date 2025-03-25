"""
LLM setup and utilities for the CBMC harness generator.
"""
import os
import sys
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
import logging

# Global LLM instance
_global_llm = None

logger = logging.getLogger("llm_utils")

def setup_llm(model_choice='claude'):
    """Set up the LLM with optimized parameters for harness generation.
    
    Args:
        model_choice: 'claude' or 'openai' to select which LLM to use
    
    Returns:
        A configured LLM instance ready for use
    """
    global _global_llm
    
    # If already initialized, return the existing instance
    if _global_llm is not None:
        logger.debug("Using existing LLM instance")
        return _global_llm
    
    logger.info(f"Initializing new {model_choice} LLM instance")
    
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
    
    try:
        # Determine which model to use based on the choice
        if model_choice.lower() == 'claude':
            anthropic_api_key = os.environ.get("ANTHROPIC_API_KEY")
            if not anthropic_api_key:
                print("ERROR: ANTHROPIC_API_KEY not set. Set this environment variable or use --llm openai.")
                sys.exit(1)
            
            _global_llm = ChatAnthropic(
                model="claude-3-7-sonnet-latest",
                anthropic_api_key=anthropic_api_key,
                temperature=0.2,  # Lower temperature for more deterministic code generation
                max_tokens=4000,  # Ensure we have enough tokens for complete responses
                model_kwargs={"system": system_prompt},  # Use model_kwargs for the system prompt
            )
        
        elif model_choice.lower() == 'openai':
            openai_api_key = os.environ.get("OPENAI_API_KEY")
            if not openai_api_key:
                print("ERROR: OPENAI_API_KEY not set. Set this environment variable or use --llm claude.")
                sys.exit(1)
            
            _global_llm = ChatOpenAI(
                model="gpt-4o",  # Use GPT-4o for best code generation capabilities
                openai_api_key=openai_api_key,
                temperature=0.2,
                max_tokens=4000,
                model_kwargs={"response_format": {"type": "text"}},
            )
        
        else:
            raise ValueError(f"Unknown LLM choice: {model_choice}. Use 'claude' or 'openai'.")
        
        return _global_llm
        
    except Exception as e:
        print(f"ERROR: Failed to initialize LLM: {str(e)}")
        sys.exit(1)