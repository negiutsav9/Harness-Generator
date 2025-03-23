"use client";

import { useState, useRef, useEffect } from "react";
import EditorLoader from "../components/EditorLoader";
import ResultsDisplay from "../components/ResultsDisplay";
import ChunkingSettingsPanel, {
  ChunkingSettings,
} from "../components/ChunkingSettingsPanel";
import LlmToggle from "../components/LlmToggle";
import {
  FileNode,
  updateFileContent,
  findFileByPath,
  combineSourceFiles,
} from "../utils/fileStore";

export default function Home() {
  const [code, setCode] = useState<string>("// Enter your C code here\n\n");
  const [isProcessing, setIsProcessing] = useState<boolean>(false);
  const [currentProcess, setCurrentProcess] = useState<string | null>(null);
  const [analysisComplete, setAnalysisComplete] = useState<boolean>(false);
  const [harnessComplete, setHarnessComplete] = useState<boolean>(false);
  const [analysisOutput, setAnalysisOutput] = useState<string>("");
  const [harnessOutput, setHarnessOutput] = useState<string>("");
  const [results, setResults] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);
  const [editorReady, setEditorReady] = useState<boolean>(false);
  const [fileStructure, setFileStructure] = useState<FileNode[]>([]);
  const [activeFile, setActiveFile] = useState<FileNode | null>(null);
  const [showFileExplorer, setShowFileExplorer] = useState<boolean>(false);
  const dirInputRef = useRef<HTMLInputElement>(null);
  const editorContainerRef = useRef<HTMLDivElement>(null);

  // LLM toggle state
  const [useLocalLlm, setUseLocalLlm] = useState<boolean>(false);

  // Chunking settings
  const [chunkingSettings, setChunkingSettings] = useState<ChunkingSettings>({
    useChunking: false,
    chunkSize: 40000,
    chunkThreshold: 100000,
  });

  // Track total code size for chunking decisions
  const [totalCodeSize, setTotalCodeSize] = useState<number>(0);

  // Update code size when fileStructure changes
  useEffect(() => {
    if (fileStructure.length > 0) {
      const combinedCode = combineSourceFiles(fileStructure);
      setTotalCodeSize(combinedCode.length);
    } else {
      setTotalCodeSize(code.length);
    }
  }, [fileStructure, code]);

  const handleCodeChange = (newCode: string) => {
    setCode(newCode);

    // Update the active file content in the file structure
    if (activeFile && !activeFile.isDirectory) {
      // Update the file content in our file structure
      const updatedFiles = updateFileContent(
        fileStructure,
        activeFile.path,
        newCode,
      );
      setFileStructure(updatedFiles);

      // Update the active file reference with the new content
      setActiveFile({
        ...activeFile,
        content: newCode,
      });
    }
  };

  const handleEditorReady = () => {
    setEditorReady(true);
  };

  const handleChunkingSettingsChange = (settings: ChunkingSettings) => {
    console.log("Chunking settings changed:", settings);
    setChunkingSettings(settings);
  };

  const handleLlmToggle = (useLocal: boolean) => {
    console.log(`Switching to ${useLocal ? "local" : "cloud"} LLM`);
    setUseLocalLlm(useLocal);
  };

  const handleDirectoryUpload = async (
    event: React.ChangeEvent<HTMLInputElement>,
  ) => {
    const files = event.target.files;
    if (!files || files.length === 0) return;

    // Array to store file contents
    const fileContents: { path: string; content: string }[] = [];

    // Process all files
    for (let i = 0; i < files.length; i++) {
      const file = files[i];
      const relativePath = file.webkitRelativePath || file.name;

      // Skip non-C/C++ files
      if (!/\.(c|cpp|h|hpp)$/i.test(file.name)) continue;

      // Read file content
      const content = await readFileAsText(file);
      fileContents.push({ path: relativePath, content });
    }

    if (fileContents.length === 0) {
      setError("No C/C++ files found in the selected directory");
      return;
    }

    // Build a file tree structure
    const rootNode: FileNode = {
      name: "root",
      path: "root",
      isDirectory: true,
      children: [],
    };

    // Organize files into a tree structure
    fileContents.forEach((file) => {
      const pathParts = file.path.split("/");
      let currentNode = rootNode;

      // Create directory structure
      for (let i = 0; i < pathParts.length - 1; i++) {
        const part = pathParts[i];
        let found = currentNode.children?.find((child) => child.name === part);

        if (!found) {
          const newDir: FileNode = {
            name: part,
            path: pathParts.slice(0, i + 1).join("/"),
            isDirectory: true,
            children: [],
          };
          currentNode.children = currentNode.children || [];
          currentNode.children.push(newDir);
          found = newDir;
        }

        currentNode = found;
      }

      // Add the file
      const fileName = pathParts[pathParts.length - 1];
      currentNode.children = currentNode.children || [];
      currentNode.children.push({
        name: fileName,
        path: file.path,
        isDirectory: false,
        content: file.content,
      });
    });

    // Remove the root node and use its children directly
    setFileStructure(rootNode.children || []);

    // Set the first file as active
    const firstFile = findFirstFile(rootNode);
    if (firstFile) {
      setActiveFile(firstFile);
      setCode(firstFile.content || "");
    } else {
      // No files found - unlikely at this point
      setError("No valid files found in directory");
    }

    setShowFileExplorer(true);

    // Reset process state when loading new files
    resetProcessState();

    // Calculate total code size
    const combinedCode = combineSourceFiles(rootNode.children || []);
    setTotalCodeSize(combinedCode.length);

    // Auto-enable chunking if code size is large
    if (combinedCode.length > chunkingSettings.chunkThreshold) {
      setChunkingSettings({
        ...chunkingSettings,
        useChunking: true,
      });
    }
  };

  // Helper function to find the first file in the tree
  const findFirstFile = (node: FileNode): FileNode | null => {
    if (!node.isDirectory) {
      return node;
    }

    if (node.children) {
      for (const child of node.children) {
        const found = findFirstFile(child);
        if (found) return found;
      }
    }

    return null;
  };

  // Helper function to read file contents
  const readFileAsText = (file: File): Promise<string> => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = (e) => resolve(e.target?.result as string);
      reader.onerror = reject;
      reader.readAsText(file);
    });
  };

  const triggerDirectoryUpload = () => {
    dirInputRef.current?.click();
  };

  const handleFileSelect = (file: FileNode) => {
    if (!file.isDirectory) {
      console.log("File selected:", file.path);

      // Make sure we have content
      if (file.content !== undefined) {
        // First set the code to trigger the editor update
        setCode(file.content || "");

        // Then update the active file - ensure file has a name property
        const selectedFile = {
          ...file,
          name: file.name || file.path.split("/").pop() || "Untitled",
        };

        // Force UI update for the title
        setActiveFile(null); // Clear first

        // Then set after a small delay
        setTimeout(() => {
          setActiveFile(selectedFile);

          // Force a re-render of the title
          document.title = `${selectedFile.name} - LLM-Based Harness Generator`;
        }, 10);
      } else {
        console.warn("Selected file has no content:", file.path);

        // Still set as active but with empty content
        setCode("");

        // Update active file with same technique
        setActiveFile(null);
        setTimeout(() => {
          setActiveFile({
            ...file,
            name: file.name || file.path.split("/").pop() || "Untitled",
          });
        }, 10);
      }
    } else {
      console.log("Directory selected, not changing editor content");
    }
  };

  const toggleFileExplorer = () => {
    setShowFileExplorer(!showFileExplorer);
  };

  const resetProcessState = () => {
    setAnalysisComplete(false);
    setHarnessComplete(false);
    setAnalysisOutput("");
    setHarnessOutput("");
    setCurrentProcess(null);
    setResults(null);
    setError(null);
  };

  const runAnalysis = async () => {
    // Reset previous output but keep completion states
    setAnalysisOutput("");
    setError(null);
    setCurrentProcess("analysis");
    setIsProcessing(true);

    // Determine what code to submit
    let codeToSubmit = code;

    // If we have multiple files, combine them for submission
    if (
      fileStructure.length > 1 ||
      (fileStructure.length === 1 && fileStructure[0].isDirectory)
    ) {
      codeToSubmit = combineSourceFiles(fileStructure);
    }

    try {
      // Update with processing message
      setAnalysisOutput("Starting code analysis...\n");
      await new Promise((resolve) => setTimeout(resolve, 500));

      // Append to the output as the process continues
      setAnalysisOutput(
        (prev) => prev + "Identifying memory-leak prone functions...\n",
      );

      // If chunking is enabled, add that to the output
      if (chunkingSettings.useChunking) {
        setAnalysisOutput(
          (prev) =>
            prev +
            `Code chunking enabled (${codeToSubmit.length.toLocaleString()} characters, chunk size: ${chunkingSettings.chunkSize.toLocaleString()})\n`,
        );
      }

      // Add LLM provider info to the output
      setAnalysisOutput(
        (prev) =>
          prev +
          `Using ${useLocalLlm ? "local Qwen2.5-Coder-32B" : "cloud-based Claude 3.7 Sonnet"} for analysis\n`,
      );

      // Step 1: Analyze code with chunking and LLM settings
      const analyzeResponse = await fetch("/api/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          code: codeToSubmit,
          language: "c",
          options: {
            ...chunkingSettings,
            excludeTests: true,
            useLocalLlm: useLocalLlm,
          },
        }),
      });

      if (!analyzeResponse.ok) {
        throw new Error("Failed to analyze code");
      }

      const analyzeData = await analyzeResponse.json();

      // Add chunking info to output if available
      if (analyzeData.chunking_info) {
        const chunkInfo = analyzeData.chunking_info;
        setAnalysisOutput(
          (prev) =>
            prev +
            `\nAnalysis method: ${chunkInfo.used_chunking ? "With chunking" : "Without chunking"}\n` +
            (chunkInfo.used_chunking
              ? `Code split into ${chunkInfo.chunks_count} chunks for analysis\n`
              : ""),
        );
      }

      // Update output with results summary
      setAnalysisOutput(
        (prev) =>
          prev +
          `Analysis complete. Identified ${analyzeData.target_functions.length} target functions.\n\n` +
          analyzeData.target_functions
            .map(
              (func: any, i: number) =>
                `${i + 1}. ${func.name} (Risk: ${func.risk_score.toFixed(2)})`,
            )
            .join("\n"),
      );

      // Store the results
      setResults((prev) => ({
        ...prev,
        target_functions: analyzeData.target_functions,
        function_summary: analyzeData.function_summary,
        chunking_info: analyzeData.chunking_info,
        llm_info: analyzeData.llm_info,
      }));

      setAnalysisComplete(true);
    } catch (err) {
      console.error("Error:", err);
      setError(
        err instanceof Error ? err.message : "An unknown error occurred",
      );
      setAnalysisOutput(
        (prev) =>
          prev +
          "\nError: Analysis failed. " +
          (err instanceof Error ? err.message : "Unknown error"),
      );
    } finally {
      setIsProcessing(false);
      setCurrentProcess(null);
    }
  };

  const runHarnessGeneration = async () => {
    // Check if analysis has been run
    if (!analysisComplete || !results || !results.target_functions) {
      setError("Please run code analysis first.");
      return;
    }

    // Reset previous output but keep completion states
    setHarnessOutput("");
    setError(null);
    setCurrentProcess("harness");
    setIsProcessing(true);

    // Determine what code to submit
    let codeToSubmit = code;

    // If we have multiple files, combine them for submission
    if (
      fileStructure.length > 1 ||
      (fileStructure.length === 1 && fileStructure[0].isDirectory)
    ) {
      codeToSubmit = combineSourceFiles(fileStructure);
    }

    try {
      // Update with processing message
      setHarnessOutput("Starting harness generation...\n");
      await new Promise((resolve) => setTimeout(resolve, 500));

      setHarnessOutput(
        (prev) =>
          prev + "Creating test harnesses for identified functions...\n",
      );

      // Add LLM provider info to the output
      setHarnessOutput(
        (prev) =>
          prev +
          `Using ${useLocalLlm ? "local Qwen2.5-Coder-32B" : "cloud-based Claude 3.7 Sonnet"} for generation\n`,
      );

      // Update harness generation with iterative approach info
      setHarnessOutput(
        (prev) =>
          prev +
          "Using iterative improvement process with CBMC verification\n" +
          "Each function will go through multiple improvement iterations\n",
      );

      // Step 2: Generate harnesses with LLM setting
      const generateResponse = await fetch("/api/generate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          code: codeToSubmit,
          target_functions: results.target_functions,
          useLocalLlm: useLocalLlm,
        }),
      });

      if (!generateResponse.ok) {
        throw new Error("Failed to generate harnesses");
      }

      const generateData = await generateResponse.json();

      // Update output with harness generation status
      setHarnessOutput(
        (prev) =>
          prev +
          `\nGenerated ${generateData.harnesses.length} test harnesses.\n\n`,
      );

      // Show iteration summary for each function
      generateData.harnesses.forEach((harness: any, i: number) => {
        const status = harness.improved ? "SUCCESS" : "PARTIAL";
        const iterations = harness.metadata?.iterations_performed || "unknown";

        setHarnessOutput(
          (prev) =>
            prev +
            `${i + 1}. ${harness.function_name}: ${status} (after ${iterations} iterations)\n`,
        );
      });

      // Store the results
      setResults((prev) => ({
        ...prev,
        harnesses: generateData.harnesses,
      }));

      setHarnessComplete(true);
    } catch (err) {
      console.error("Error:", err);
      setError(
        err instanceof Error ? err.message : "An unknown error occurred",
      );
      setHarnessOutput(
        (prev) =>
          prev +
          "\nError: Harness generation failed. " +
          (err instanceof Error ? err.message : "Unknown error"),
      );
    } finally {
      setIsProcessing(false);
      setCurrentProcess(null);
    }
  };

  return (
    <div className="app-container">
      {/* Centered title */}
      <div className="app-header">
        <h1 className="app-title">LLM-Based Harness Generation System</h1>
      </div>

      {/* Settings Panel Container */}
      <div className="settings-panel">
        {/* LLM Toggle */}
        <LlmToggle onToggle={handleLlmToggle} initialValue={useLocalLlm} />

        {/* Chunking Settings Panel */}
        <ChunkingSettingsPanel
          onSettingsChange={handleChunkingSettingsChange}
          initialSettings={chunkingSettings}
          codeSize={totalCodeSize}
        />
      </div>

      {/* Process buttons */}
      <div className="process-buttons">
        <button
          className={`process-button ${analysisComplete ? "complete" : ""} ${currentProcess === "analysis" ? "processing" : ""}`}
          onClick={runAnalysis}
          disabled={isProcessing}
        >
          {currentProcess === "analysis"
            ? "Analyzing..."
            : analysisComplete
              ? "Code Analysis ✓"
              : "Run Code Analysis"}
        </button>

        <button
          className={`process-button ${harnessComplete ? "complete" : ""} ${currentProcess === "harness" ? "processing" : ""}`}
          onClick={runHarnessGeneration}
          disabled={isProcessing || !analysisComplete}
        >
          {currentProcess === "harness"
            ? "Generating..."
            : harnessComplete
              ? "Harness Generation ✓"
              : "Generate Test Harnesses"}
        </button>
      </div>

      {/* Main content with code editor and output */}
      <div className="main-content">
        <div className="editor-section">
          <div className="editor-header">
            <div className="file-info">
              <button
                className={`file-explorer-toggle ${showFileExplorer ? "active" : ""}`}
                onClick={toggleFileExplorer}
                title="Toggle File Explorer"
              >
                <span className="icon">📁</span>
              </button>
              <span className="active-file">
                {activeFile ? activeFile.name : "No file loaded"}
              </span>
              {totalCodeSize > 0 && (
                <span className="code-size-indicator">
                  {totalCodeSize.toLocaleString()} chars
                  {chunkingSettings.useChunking && " (chunking enabled)"}
                </span>
              )}
            </div>
            <div className="editor-actions">
              <input
                type="file"
                ref={dirInputRef}
                onChange={handleDirectoryUpload}
                webkitdirectory=""
                directory=""
                multiple
                style={{ display: "none" }}
              />
              <button
                className="action-button"
                onClick={triggerDirectoryUpload}
                disabled={isProcessing}
              >
                Import Source Code
              </button>
            </div>
          </div>

          <div className="editor-content">
            {showFileExplorer && fileStructure.length > 0 && (
              <div className="file-explorer">
                <div className="file-explorer-header">
                  <h3>Project Files</h3>
                </div>
                <div className="file-explorer-content">
                  {renderFileTree(
                    fileStructure,
                    activeFile?.path || "",
                    handleFileSelect,
                  )}
                </div>
              </div>
            )}

            <div ref={editorContainerRef} className="editor-container">
              {!editorReady && (
                <div className="editor-placeholder">
                  <p>Loading code editor...</p>
                </div>
              )}
              <EditorLoader
                value={code}
                onChange={handleCodeChange}
                language="c"
                onReady={handleEditorReady}
              />
            </div>
          </div>
        </div>

        <div className="process-output">
          <div className="output-container">
            <h3 className="output-header">
              <span
                className={`status-indicator ${analysisComplete ? "success" : ""}`}
              ></span>
              Code Analysis Output
            </h3>
            <pre className="output-content">
              {analysisOutput || "Run Code Analysis to see output here."}
            </pre>
          </div>

          <div className="output-container">
            <h3 className="output-header">
              <span
                className={`status-indicator ${harnessComplete ? "success" : ""}`}
              ></span>
              Harness Generation Output
            </h3>
            <pre className="output-content">
              {harnessOutput || "Run Harness Generation to see output here."}
            </pre>
          </div>
        </div>
      </div>

      {/* Error message display */}
      {error && (
        <div className="error-message">
          <p>{error}</p>
        </div>
      )}

      <style jsx>{`
        .app-container {
          display: flex;
          flex-direction: column;
          min-height: 100vh;
          padding: 20px;
          max-width: 1200px;
          margin: 0 auto;
        }

        .app-header {
          text-align: center;
          margin-bottom: 20px;
        }

        .app-title {
          font-size: 24px;
          font-weight: bold;
          color: #333;
        }

        .settings-panel {
          display: flex;
          flex-direction: column;
          gap: 15px;
          margin-bottom: 20px;
        }

        .process-buttons {
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 20px;
          margin-bottom: 20px;
        }

        .process-button {
          padding: 12px;
          border: none;
          border-radius: 4px;
          font-size: 16px;
          font-weight: 500;
          cursor: pointer;
          transition: all 0.3s ease;
          background-color: #e0e0e0;
        }

        .process-button:hover:not(:disabled) {
          transform: translateY(-2px);
          box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .process-button:disabled {
          opacity: 0.6;
          cursor: not-allowed;
        }

        .process-button.processing {
          background-color: #4a90e2;
          color: white;
          animation: pulse 1.5s infinite;
        }

        .process-button.complete {
          background-color: #4caf50;
          color: white;
        }

        .main-content {
          display: flex;
          flex-direction: column;
          flex: 1;
          gap: 20px;
        }

        .editor-section {
          display: flex;
          flex-direction: column;
          border: 1px solid #ddd;
          border-radius: 4px;
          overflow: hidden;
        }

        .editor-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          padding: 10px 15px;
          background-color: #f5f5f5;
          border-bottom: 1px solid #ddd;
        }

        .file-info {
          display: flex;
          align-items: center;
          font-weight: 500;
        }

        .code-size-indicator {
          margin-left: 10px;
          font-size: 12px;
          background-color: #f0f7ff;
          padding: 2px 6px;
          border-radius: 4px;
          color: #0070f3;
        }

        .file-explorer-toggle {
          background: none;
          border: none;
          cursor: pointer;
          padding: 5px;
          margin-right: 10px;
          display: flex;
          align-items: center;
          justify-content: center;
          border-radius: 4px;
        }

        .file-explorer-toggle.active {
          background-color: #e0e0e0;
        }

        .active-file {
          font-weight: 500;
        }

        .action-button {
          padding: 6px 12px;
          background-color: #4a90e2;
          color: white;
          border: none;
          border-radius: 4px;
          cursor: pointer;
        }

        .editor-content {
          display: flex;
          height: 400px;
        }

        .file-explorer {
          width: 250px;
          border-right: 1px solid #ddd;
          display: flex;
          flex-direction: column;
          overflow: hidden;
        }

        .file-explorer-header {
          padding: 8px 10px;
          background-color: #f5f5f5;
          border-bottom: 1px solid #ddd;
        }

        .file-explorer-header h3 {
          margin: 0;
          font-size: 14px;
          font-weight: 500;
        }

        .file-explorer-content {
          flex: 1;
          overflow-y: auto;
          padding: 5px;
        }

        .file-node {
          padding: 4px 6px;
          cursor: pointer;
          display: flex;
          align-items: center;
          border-radius: 3px;
          margin-bottom: 2px;
        }

        .file-node:hover {
          background-color: #f0f7ff;
        }

        .file-node.active {
          background-color: #e3f2fd;
          font-weight: 500;
        }

        .file-icon {
          margin-right: 6px;
          font-size: 12px;
        }

        .file-name {
          font-size: 14px;
          white-space: nowrap;
          overflow: hidden;
          text-overflow: ellipsis;
        }

        .editor-container {
          flex: 1;
          position: relative;
        }

        .editor-placeholder {
          position: absolute;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
          display: flex;
          align-items: center;
          justify-content: center;
          background-color: #f9f9f9;
        }

        .process-output {
          display: flex;
          flex-direction: column;
          gap: 20px;
        }

        .output-container {
          border: 1px solid #ddd;
          border-radius: 4px;
          overflow: hidden;
        }

        .output-header {
          display: flex;
          align-items: center;
          padding: 10px 15px;
          margin: 0;
          background-color: #f5f5f5;
          border-bottom: 1px solid #ddd;
          font-size: 16px;
          font-weight: 500;
        }

        .status-indicator {
          display: inline-block;
          width: 10px;
          height: 10px;
          border-radius: 50%;
          margin-right: 10px;
          background-color: #ccc;
        }

        .status-indicator.success {
          background-color: #4caf50;
        }

        .output-content {
          padding: 15px;
          margin: 0;
          max-height: 300px;
          overflow-y: auto;
          background-color: #f9f9f9;
          font-family: monospace;
          font-size: 14px;
          white-space: pre-wrap;
          line-height: 1.5;
        }

        .error-message {
          margin-top: 20px;
          padding: 10px 15px;
          background-color: #ffebee;
          border-left: 4px solid #f44336;
          color: #d32f2f;
        }

        @keyframes pulse {
          0% {
            opacity: 1;
          }
          50% {
            opacity: 0.7;
          }
          100% {
            opacity: 1;
          }
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
          .process-buttons {
            grid-template-columns: 1fr !important;
          }

          .app-title {
            font-size: 20px !important;
          }

          .process-button {
            font-size: 14px !important;
            padding: 10px !important;
          }

          .editor-content {
            flex-direction: column;
            height: auto;
          }

          .file-explorer {
            width: 100%;
            height: 200px;
            border-right: none;
            border-bottom: 1px solid #ddd;
          }

          .editor-container {
            height: 300px;
          }

          .output-content {
            max-height: 200px;
          }
        }
      `}</style>
    </div>
  );
}

// Helper function to render file tree
function renderFileTree(
  files: FileNode[],
  activeFilePath: string,
  onFileSelect: (file: FileNode) => void,
  level = 0,
) {
  return (
    <div style={{ paddingLeft: level > 0 ? "15px" : "0" }}>
      {files.map((file) => (
        <div key={file.path}>
          <div
            className={`file-node ${file.path === activeFilePath ? "active" : ""}`}
            onClick={() => onFileSelect(file)}
          >
            <span className="file-icon">{file.isDirectory ? "📁" : "📄"}</span>
            <span className="file-name">{file.name}</span>
          </div>
          {file.isDirectory &&
            file.children &&
            file.children.length > 0 &&
            renderFileTree(
              file.children,
              activeFilePath,
              onFileSelect,
              level + 1,
            )}
        </div>
      ))}
    </div>
  );
}
