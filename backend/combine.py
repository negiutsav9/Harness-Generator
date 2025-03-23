import json
import os

# Define paths for input and output files
part_files = [
    "part_1.ipynb",
    "part_2.ipynb",
    "part_3.ipynb",
    "part_4.ipynb",
    "part_5.ipynb"
]
output_file = "cbmc_harness_generator_combined.ipynb"

def combine_notebooks(input_files, output_file):
    """Combine multiple Jupyter notebooks into a single notebook"""
    
    # Initialize the combined notebook with the structure from the first notebook
    with open(input_files[0], 'r') as f:
        combined_notebook = json.load(f)
    
    # Clear the cells to start fresh
    combined_notebook['cells'] = []
    
    # Add a title cell
    title_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# CBMC-Compatible Harness Generation System\n",
            "\n",
            "This notebook implements the architecture outlined in the provided Mermaid diagram. The system uses LangGraph to orchestrate a workflow that analyzes source code for potential memory leaks and generates CBMC-compatible harnesses for verification."
        ]
    }
    combined_notebook['cells'].append(title_cell)
    
    # Process each input file
    for i, file_path in enumerate(input_files):
        try:
            with open(file_path, 'r') as f:
                notebook = json.load(f)
            
            # Add a section header if it's not the first file
            if i > 0:
                section_header = {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        f"## Part {i+1}: {notebook['cells'][0]['source'][0].strip('# ')}"
                    ]
                }
                combined_notebook['cells'].append(section_header)
            
            # Add all cells except the title (first markdown cell)
            skip_first = True
            for cell in notebook['cells']:
                if cell['cell_type'] == 'markdown' and skip_first:
                    skip_first = False
                    continue
                    
                # Add the cell to the combined notebook
                combined_notebook['cells'].append(cell)
                
            print(f"Added cells from {file_path}")
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    # Write the combined notebook to the output file
    with open(output_file, 'w') as f:
        json.dump(combined_notebook, f, indent=1)
    
    print(f"Combined notebook saved to {output_file}")


# Check if the files exist
for file_path in part_files:
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            print(f"Warning: {file_path} doesn't exist. Creating an empty file.")
            json.dump({"cells": [], "metadata": {}, "nbformat": 4, "nbformat_minor": 4}, f)

# Combine the notebooks
combine_notebooks(part_files, output_file)