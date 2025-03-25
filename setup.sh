#!/bin/bash
# Setup script for CBMC Harness Generator

# Exit on any error
set -e

echo "Setting up CBMC Harness Generator..."

# Check if Python 3.8+ is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
if (( $(echo "$PYTHON_VERSION < 3.8" | bc -l) )); then
    echo "Error: Python version must be 3.8 or higher. Found version $PYTHON_VERSION"
    exit 1
fi

echo "Found Python $PYTHON_VERSION"

# Check if CBMC is installed
if ! command -v cbmc &> /dev/null; then
    echo "Warning: CBMC is not installed or not in PATH."
    
    # Suggest installation based on OS
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "For Ubuntu/Debian, install CBMC using: sudo apt-get install cbmc"
        echo "For other Linux distributions, see: https://github.com/diffblue/cbmc"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "For macOS, install CBMC using: brew install cbmc"
    elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        echo "For Windows, download CBMC from: https://github.com/diffblue/cbmc/releases"
    fi
    
    read -p "Do you want to continue without CBMC? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Setup aborted. Please install CBMC and run setup again."
        exit 1
    fi
else
    CBMC_VERSION=$(cbmc --version | head -n 1)
    echo "Found $CBMC_VERSION"
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo "Creating project directories..."
mkdir -p harnesses verification/src verification/include verification/stubs verification/sources reports

# Set up environment variable for API keys
echo "Setting up API keys for LLMs..."

# Anthropic API key setup
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "Anthropic API key is not set."
    read -p "Enter your Anthropic API key (or press Enter to skip): " api_key
    if [ ! -z "$api_key" ]; then
        export ANTHROPIC_API_KEY="$api_key"
        echo "export ANTHROPIC_API_KEY=\"$api_key\"" >> ~/.bashrc
        echo "Added Anthropic API key to ~/.bashrc. Run 'source ~/.bashrc' to apply in current session."
    else
        echo "Skipping Anthropic API key setup. You can set it later or use OpenAI instead with --llm openai."
    fi
else
    echo "Anthropic API key is already set."
fi

# OpenAI API key setup
if [ -z "$OPENAI_API_KEY" ]; then
    echo "OpenAI API key is not set."
    read -p "Enter your OpenAI API key (or press Enter to skip): " api_key
    if [ ! -z "$api_key" ]; then
        export OPENAI_API_KEY="$api_key"
        echo "export OPENAI_API_KEY=\"$api_key\"" >> ~/.bashrc
        echo "Added OpenAI API key to ~/.bashrc. Run 'source ~/.bashrc' to apply in current session."
    else
        echo "Skipping OpenAI API key setup. You can set it later or use Claude instead with --llm claude."
    fi
else
    echo "OpenAI API key is already set."
fi

echo
echo "Setup complete! You can now run the CBMC Harness Generator with:"
echo "    python main.py -f path/to/your/file.c                # Use Claude by default"
echo "    python main.py -f path/to/your/file.c --llm claude   # Explicitly use Claude"
echo "    python main.py -f path/to/your/file.c --llm openai   # Use OpenAI GPT models"
echo "    python main.py -d path/to/your/project               # Process an entire directory"
echo
echo "Make sure the appropriate API key is set for the LLM you want to use."