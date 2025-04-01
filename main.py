#!/usr/bin/env python3
"""
Main entry point for the CBMC harness generator.
"""
import os
import glob
import argparse
import logging
import sys
from langchain_core.messages import HumanMessage
import polars as pl

from core.workflow import create_workflow
from utils.file_utils import process_directory, calculate_recursion_limit, setup_verification_directories
from utils.llm_utils import setup_llm
from utils.metrics_utils import initialize_metrics_tracker

# Improved logging setup:
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                   handlers=[logging.FileHandler("cbmc_main.log"), logging.StreamHandler()])
logger = logging.getLogger("main")

# Reduce verbosity of other loggers
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("chromadb").setLevel(logging.WARNING)

def main():
    """
    Main function for the CBMC harness generator.
    Parses command line arguments and runs the workflow.
    """
    # Set the TOKENIZERS_PARALLELISM environment variable
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    
    # Set up command line argument parser
    parser = argparse.ArgumentParser(description='CBMC Harness Generator')
    parser.add_argument('-d', '--directory', type=str, help='Directory containing C source files to analyze')
    parser.add_argument('-f', '--file', type=str, help='Single C source file to analyze')
    parser.add_argument('-l', '--llm', type=str, choices=['claude', 'openai', 'gemini'], default='claude',
                        help='LLM to use for code analysis and harness generation (default: claude)')
    parser.add_argument('-t', '--timeout', type=int, default=3600,
                        help='Timeout in seconds for the entire workflow (default: 3600)')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Enable verbose logging')
    parser.add_argument('-e', '--export', type=str, default='metrics.xlsx',
                        help='Export metrics to specified Excel file (default: metrics.xlsx)')
    args = parser.parse_args()
    
    # Set logging level based on verbose flag
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Verbose logging enabled")
    
    try:
        # Initialize the global LLM based on user choice
        logger.info(f"Initializing LLM: {args.llm}")
        setup_llm(model_choice=args.llm)
        
        # Set up workflow
        app = create_workflow()
        
        # Set up verification directories with LLM model name
        directories = setup_verification_directories(llm_used=args.llm)
        
        # Initialize metrics tracker with reports directory
        metrics_output_dir = directories["reports"]
        initialize_metrics_tracker(metrics_output_dir)
        
        # Add directories to state for access by nodes
        result_directories = {
            "harnesses_dir": directories["harnesses"],
            "verification_dir": directories["verification"],
            "reports_dir": directories["reports"],
            "result_base_dir": directories["result_base"]
        }
        
        if args.directory:
            # Directory mode
            logger.info(f"Processing directory: {args.directory}")
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
            
            logger.info(f"Found {source_files_count} source files in {source_subdir}")
            
            # Calculate recursion limit based on file count
            recursion_limit = calculate_recursion_limit(source_files_count)
            
            # Run workflow with calculated limit and timeout
            try:
                logger.info(f"Starting workflow with recursion limit {recursion_limit} and timeout {args.timeout}s")
                result = app.invoke(
                    {
                        "messages": [initial_message],
                        "source_code": "",
                        "embeddings": {},
                        "vulnerable_functions": [],
                        "harnesses": {},
                        "cbmc_results": {},
                        "processed_functions": [],
                        "result_directories": result_directories,
                        "llm_used": args.llm
                    },
                    {"recursion_limit": recursion_limit, "timeout": args.timeout}
                )
                logger.info("Workflow completed successfully")
            except TimeoutError:
                logger.error(f"Workflow timed out after {args.timeout} seconds")
                print(f"ERROR: Workflow timed out after {args.timeout} seconds. Try increasing the timeout with --timeout option.")
                return 1
            except Exception as e:
                logger.error(f"Error during workflow execution: {str(e)}", exc_info=True)
                print(f"ERROR: Workflow failed: {str(e)}")
                return 1
        elif args.file:
            # Single file mode
            logger.info(f"Processing single file: {args.file}")
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
                logger.info(f"Starting workflow with recursion limit {recursion_limit} and timeout {args.timeout}s")
                try:
                    result = app.invoke(
                        {
                            "messages": [initial_message],
                            "source_code": source_code,
                            "embeddings": {},
                            "vulnerable_functions": [],
                            "harnesses": {},
                            "cbmc_results": {},
                            "processed_functions": [],
                            "result_directories": result_directories,
                            "llm_used": args.llm
                        },
                        {"recursion_limit": recursion_limit, "timeout": args.timeout}
                    )
                    logger.info("Workflow completed successfully")
                except TimeoutError:
                    logger.error(f"Workflow timed out after {args.timeout} seconds")
                    print(f"ERROR: Workflow timed out after {args.timeout} seconds. Try increasing the timeout with --timeout option.")
                    return 1
                except Exception as e:
                    logger.error(f"Error during workflow execution: {str(e)}", exc_info=True)
                    print(f"ERROR: Workflow failed: {str(e)}")
                    return 1
            except Exception as e:
                logger.error(f"Error reading file {args.file}: {str(e)}")
                print(f"Error reading file {args.file}: {str(e)}")
                return 1
        else:
            logger.error("No input provided")
            print("Please provide either a directory (-d) or a file (-f) to analyze")
            return 1
        
        # Get metrics tracker and export data
        from utils.metrics_utils import get_metrics_tracker
        
        metrics_tracker = get_metrics_tracker()
        metrics_tracker.generate_summary()
        
        # Export metrics to CSV and Excel
        metrics_tracker.export_to_csv()
        if args.export:
            metrics_tracker.export_to_excel(args.export)
            print(f"Metrics exported to {os.path.join(metrics_tracker.output_dir, args.export)}")
        
        # Display the conversation
        print("=== Workflow Execution Results ===")
        for i, message in enumerate(result["messages"]):
            if isinstance(message, HumanMessage):
                print(f"\n===== Human Message {i+1} =====")
                print(message.content[:200] + "..." if len(message.content) > 200 else message.content)
            else:  # AIMessage
                print(f"\n===== AI Message {i+1} =====")
                print(message.content)
        
        logger.info("Workflow execution results displayed")
        print(f"\nResults are stored in: {directories['result_base']}")
        
    except Exception as e:
        logger.critical(f"Critical error: {str(e)}", exc_info=True)
        print(f"A critical error occurred: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())