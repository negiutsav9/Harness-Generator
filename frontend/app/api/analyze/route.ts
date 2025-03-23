import { NextResponse } from "next/server";
import { spawn } from "child_process";
import path from "path";
import fs from "fs/promises";
import os from "os";

// Helper function to run the Python analyzer
async function runAnalyzer(code: string, options: any = {}): Promise<any> {
  try {
    // Create a temporary file to store the code
    const tempDir = await fs.mkdtemp(path.join(os.tmpdir(), "analyzer-"));
    const tempFile = path.join(tempDir, "code.c");
    await fs.writeFile(tempFile, code);

    // Calculate the project root directory
    const frontendDir = process.cwd();
    const projectRoot = path.resolve(frontendDir, "..");

    // Create Python script content - keep it simple and direct
    const scriptContent = `
import sys
import json
import os

# Add project root to Python path
sys.path.insert(0, "${projectRoot.replace(/\\/g, "\\\\")}")
print(f"Added project root to Python path: {sys.path}")

# Import the LLM provider
from llm.provider import get_llm_provider

# Read code from temp file
with open("${tempFile.replace(/\\/g, "\\\\")}", "r") as f:
    code = f.read()

# Parse options
use_local_llm = ${Boolean(options.useLocalLlm)}
use_chunking = ${Boolean(options.useChunking)}
chunk_size = ${options.chunkSize || 40000}
exclude_tests = ${Boolean(options.excludeTests)}

# Get the LLM provider (either Claude or Qwen based on toggle)
provider = get_llm_provider(use_local_llm)
provider_info = provider.get_info()
print(f"Using LLM provider: {provider_info['name']}")

# Create a prompt for code analysis
language = "c"
prompt = f"""
You are an expert in C memory management and leak detection. Analyze the following code to identify functions that might cause memory leaks.

```c
{code}
```

Please identify all functions that allocate memory (malloc, calloc, etc.) but might not properly free it in all code paths.
For each function, provide:
1. Function name
2. Function signature
3. Risk score (0.0-1.0) indicating likelihood of memory leaks
4. Brief explanation of the potential issue

Respond with a JSON array of objects with the following structure:
[
  {{
    "name": "function_name",
    "signature": "full_function_signature",
    "risk_score": 0.0_to_1.0,
    "explanation": "explanation_of_memory_leak_risk"
  }}
]

Only return the JSON array, no other text.
"""

# Get analysis from LLM provider
completion = provider.get_completion(prompt)

# Parse the result to extract JSON
import re
functions = []
try:
    # Try to find JSON array in the response
    json_match = re.search(r'\\[(.*?)\\]', completion, re.DOTALL)
    if json_match:
        json_str = f"[{json_match.group(1)}]"
        functions = json.loads(json_str)
except Exception as e:
    print(f"Error parsing response: {e}")

# Filter functions by risk threshold
risk_threshold = 0.5
high_risk_functions = [
    func for func in functions
    if func.get("risk_score", 0.0) >= risk_threshold
]

# Create result structure
result = {
    "target_functions": high_risk_functions,
    "llm_info": provider_info
}

# Print result as JSON for extraction
print("RESULT_JSON_START")
print(json.dumps(result))
print("RESULT_JSON_END")
`;

    const scriptFile = path.join(tempDir, "run_analyzer.py");
    await fs.writeFile(scriptFile, scriptContent);

    // Run the Python script
    return new Promise((resolve, reject) => {
      console.log("Executing Python script...");
      const process = spawn("python", [scriptFile]);
      let stdout = "";
      let stderr = "";

      process.stdout.on("data", (data) => {
        stdout += data.toString();
        console.log("Python stdout:", data.toString());
      });

      process.stderr.on("data", (data) => {
        stderr += data.toString();
        console.error("Python stderr:", data.toString());
      });

      process.on("close", (code) => {
        // Clean up temp files
        fs.rm(tempDir, { recursive: true, force: true }).catch(console.error);

        if (code !== 0) {
          return reject(new Error(`Analysis failed with code ${code}: ${stderr}`));
        }

        try {
          // Extract JSON from output
          const resultMatch = stdout.match(/RESULT_JSON_START\n([\s\S]*?)\nRESULT_JSON_END/);
          if (resultMatch && resultMatch[1]) {
            const result = JSON.parse(resultMatch[1]);
            resolve(result);
          } else {
            reject(new Error("Could not find result JSON in output"));
          }
        } catch (err) {
          console.error("Failed to parse output:", err);
          console.error("Raw stdout:", stdout);
          reject(new Error(`Failed to parse analysis results: ${err.message}`));
        }
      });
    });
  } catch (error) {
    console.error("Error running analyzer:", error);
    throw error;
  }
}

export async function POST(request: Request) {
  try {
    const { code, options = {} } = await request.json();

    if (!code) {
      return NextResponse.json(
        { error: "Code is required" },
        { status: 400 }
      );
    }

    console.log(`Analyzing code (${code.length} characters)`);
    console.log(`LLM toggle: ${options.useLocalLlm ? 'Qwen (local)' : 'Claude (cloud)'}`);

    // Run the analyzer
    const result = await runAnalyzer(code, options);
    return NextResponse.json(result);
  } catch (error) {
    console.error("Error in analyze API:", error);
    return NextResponse.json(
      {
        error: "Failed to analyze code: " +
          (error instanceof Error ? error.message : "Unknown error"),
        target_functions: []
      },
      { status: 500 }
    );
  }
}
