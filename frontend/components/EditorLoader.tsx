"use client";

import React, { useEffect, useState } from "react";
import dynamic from "next/dynamic";

// Dynamic import with a simple loading state
const CodeEditor = dynamic(() => import("./CodeEditor"), {
  ssr: false,
  loading: () => (
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        backgroundColor: "#f5f5f5",
      }}
    >
      Loading code editor...
    </div>
  ),
});

interface EditorLoaderProps {
  value: string;
  onChange: (value: string) => void;
  language: string;
  onReady?: () => void;
}

const EditorLoader: React.FC<EditorLoaderProps> = (props) => {
  const [isClient, setIsClient] = useState(false);

  // Force remounting when value changes significantly
  const [editorKey, setEditorKey] = useState("editor-1");

  // Force hydration to complete
  useEffect(() => {
    setIsClient(true);
  }, []);

  // Remount editor when value changes significantly
  useEffect(() => {
    if (props.value && props.value.length > 0) {
      // Generate a fingerprint based on content length and first few chars
      const contentFingerprint = `${props.value.length}-${props.value.substring(0, 10)}`;
      setEditorKey(`editor-${contentFingerprint}`);
    }
  }, [props.value]);

  // If we're not on the client yet, show a simple placeholder
  if (!isClient) {
    return (
      <div
        style={{
          width: "100%",
          height: "100%",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          backgroundColor: "#f5f5f5",
        }}
      >
        Initializing editor...
      </div>
    );
  }

  return (
    <div style={{ width: "100%", height: "100%", position: "relative" }}>
      <CodeEditor
        key={editorKey}
        value={props.value}
        onChange={props.onChange}
        language={props.language}
        onReady={props.onReady}
      />
    </div>
  );
};

export default EditorLoader;
