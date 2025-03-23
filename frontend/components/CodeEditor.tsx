"use client";

import { useEffect, useRef, useState } from "react";
import * as monaco from "monaco-editor";

interface CodeEditorProps {
  value: string;
  onChange: (value: string) => void;
  language: string;
  onReady?: () => void;
}

const CodeEditor: React.FC<CodeEditorProps> = ({
  value,
  onChange,
  language,
  onReady,
}) => {
  const editorRef = useRef<HTMLDivElement>(null);
  const [editor, setEditor] =
    useState<monaco.editor.IStandaloneCodeEditor | null>(null);
  const [isInitialized, setIsInitialized] = useState<boolean>(false);

  // Initialize Monaco editor
  useEffect(() => {
    // Clean up any existing editor instance first
    if (editor) {
      editor.dispose();
    }

    if (!editorRef.current) return;

    // Create a new editor instance
    try {
      console.log(
        "Creating Monaco editor with value length:",
        value?.length || 0,
      );

      // Ensure the container is visible and has dimensions
      if (
        editorRef.current.offsetWidth === 0 ||
        editorRef.current.offsetHeight === 0
      ) {
        console.warn(
          "Editor container has zero dimensions",
          editorRef.current.offsetWidth,
          editorRef.current.offsetHeight,
        );
      }

      const newEditor = monaco.editor.create(editorRef.current, {
        value: value || "// No content available",
        language: language || "plaintext",
        theme: "vs",
        automaticLayout: true,
        minimap: { enabled: true },
        scrollBeyondLastLine: false,
        fontSize: 14,
        lineNumbers: "on",
      });

      // Set up change handler
      newEditor.onDidChangeModelContent(() => {
        const newValue = newEditor.getValue();
        onChange(newValue);
      });

      // Force layout after creation
      setTimeout(() => {
        newEditor.layout();
        newEditor.focus();
      }, 100);

      setEditor(newEditor);
      setIsInitialized(true);

      if (onReady) {
        onReady();
      }

      console.log("Monaco editor initialized successfully");

      return () => {
        newEditor.dispose();
      };
    } catch (error) {
      console.error("Error initializing Monaco editor:", error);
    }
  }, [editorRef.current]); // Only recreate when the DOM element changes

  // Update value if changed externally
  useEffect(() => {
    if (editor) {
      const currentValue = editor.getValue();

      // Only update if values actually differ to prevent cursor jumps
      if (value !== currentValue) {
        console.log("Setting editor model value");
        editor.setValue(value || "");

        // Force a layout update
        setTimeout(() => {
          editor.layout();
        }, 50);
      }
    }
  }, [value, editor]);

  // Update language if changed
  useEffect(() => {
    if (editor) {
      const model = editor.getModel();
      if (model) {
        monaco.editor.setModelLanguage(model, language);
      }
    }
  }, [language, editor]);

  // Force layout on window resize
  useEffect(() => {
    const handleResize = () => {
      if (editor) {
        editor.layout();
      }
    };

    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, [editor]);

  return (
    <div
      style={{
        width: "100%",
        height: "100%",
        position: "relative",
        display: "flex",
        flexDirection: "column",
        border: "1px solid #ddd",
        overflow: "hidden",
      }}
    >
      <div
        ref={editorRef}
        style={{
          width: "100%",
          height: "100%",
          overflow: "hidden",
        }}
      ></div>

      {!isInitialized && (
        <div
          style={{
            position: "absolute",
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            backgroundColor: "rgba(245, 245, 245, 0.8)",
            zIndex: 100,
          }}
        >
          <p>Loading editor...</p>
        </div>
      )}
    </div>
  );
};

export default CodeEditor;
