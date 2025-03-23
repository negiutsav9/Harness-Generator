"use client";

import { useState, useEffect } from "react";

interface LlmToggleProps {
  onToggle: (useLocalLlm: boolean) => void;
  initialValue?: boolean;
}

export default function LlmToggle({
  onToggle,
  initialValue = false,
}: LlmToggleProps) {
  const [useLocalLlm, setUseLocalLlm] = useState<boolean>(initialValue);

  const handleToggle = () => {
    const newValue = !useLocalLlm;
    setUseLocalLlm(newValue);
    onToggle(newValue);
  };

  useEffect(() => {
    // Sync with parent component if initial value changes
    setUseLocalLlm(initialValue);
  }, [initialValue]);

  return (
    <div className="llm-toggle-container">
      <span className={`llm-toggle-label ${!useLocalLlm ? "active" : ""}`}>
        Claude 3.7 Sonnet
      </span>
      <label className="llm-toggle-switch">
        <input type="checkbox" checked={useLocalLlm} onChange={handleToggle} />
        <span className="llm-toggle-slider"></span>
      </label>
      <span className={`llm-toggle-label ${useLocalLlm ? "active" : ""}`}>
        Qwen2.5-Coder-32B
      </span>

      <style jsx>{`
        .llm-toggle-container {
          display: flex;
          align-items: center;
          gap: 8px;
          margin-bottom: 15px;
          background-color: #f5f5f5;
          padding: 10px 15px;
          border-radius: 4px;
          border: 1px solid #ddd;
        }

        .llm-toggle-label {
          font-size: 14px;
          color: #666;
        }

        .llm-toggle-label.active {
          color: #4a90e2;
          font-weight: 500;
        }

        .llm-toggle-switch {
          position: relative;
          display: inline-block;
          width: 50px;
          height: 24px;
        }

        .llm-toggle-switch input {
          opacity: 0;
          width: 0;
          height: 0;
        }

        .llm-toggle-slider {
          position: absolute;
          cursor: pointer;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background-color: #ccc;
          transition: 0.4s;
          border-radius: 24px;
        }

        .llm-toggle-slider:before {
          position: absolute;
          content: "";
          height: 16px;
          width: 16px;
          left: 4px;
          bottom: 4px;
          background-color: white;
          transition: 0.4s;
          border-radius: 50%;
        }

        input:checked + .llm-toggle-slider {
          background-color: #4caf50;
        }

        input:checked + .llm-toggle-slider:before {
          transform: translateX(26px);
        }
      `}</style>
    </div>
  );
}
