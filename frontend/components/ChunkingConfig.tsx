import React, { useState } from "react";

interface ChunkingConfigProps {
  enabled: boolean;
  chunkSize: number;
  chunkThreshold: number;
  onConfigChange: (config: {
    enabled: boolean;
    chunkSize: number;
    chunkThreshold: number;
  }) => void;
}

const ChunkingConfig: React.FC<ChunkingConfigProps> = ({
  enabled,
  chunkSize,
  chunkThreshold,
  onConfigChange,
}) => {
  const [isExpanded, setIsExpanded] = useState(false);

  const handleToggleEnabled = (e: React.ChangeEvent<HTMLInputElement>) => {
    onConfigChange({
      enabled: e.target.checked,
      chunkSize,
      chunkThreshold,
    });
  };

  const handleChunkSizeChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = parseInt(e.target.value, 10);
    if (!isNaN(value) && value > 0) {
      onConfigChange({
        enabled,
        chunkSize: value,
        chunkThreshold,
      });
    }
  };

  const handleThresholdChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = parseInt(e.target.value, 10);
    if (!isNaN(value) && value > 0) {
      onConfigChange({
        enabled,
        chunkSize,
        chunkThreshold: value,
      });
    }
  };

  return (
    <div className="chunking-config">
      <div className="config-header" onClick={() => setIsExpanded(!isExpanded)}>
        <div className="header-content">
          <span className="config-title">Advanced Analysis Options</span>
          <span className={`expand-icon ${isExpanded ? "expanded" : ""}`}>
            {isExpanded ? "▼" : "▶"}
          </span>
        </div>
      </div>

      {isExpanded && (
        <div className="config-content">
          <div className="config-item">
            <label className="switch">
              <input
                type="checkbox"
                checked={enabled}
                onChange={handleToggleEnabled}
              />
              <span className="slider round"></span>
            </label>
            <span className="option-label">
              Enable Code Chunking
              <span
                className="help-tooltip"
                title="Breaks large codebases into manageable pieces for analysis"
              >
                ?
              </span>
            </span>
          </div>

          <div className={`config-item ${!enabled ? "disabled" : ""}`}>
            <label htmlFor="chunk-size">Chunk Size (chars):</label>
            <input
              id="chunk-size"
              type="number"
              min="10000"
              max="100000"
              step="5000"
              value={chunkSize}
              onChange={handleChunkSizeChange}
              disabled={!enabled}
            />
          </div>

          <div className={`config-item ${!enabled ? "disabled" : ""}`}>
            <label htmlFor="chunk-threshold">Auto-Chunking Threshold:</label>
            <input
              id="chunk-threshold"
              type="number"
              min="5000"
              max="100000"
              step="5000"
              value={chunkThreshold}
              onChange={handleThresholdChange}
              disabled={!enabled}
            />
          </div>

          <div className="config-description">
            {enabled ? (
              <p>
                Chunking divides large codebases into smaller pieces for
                analysis. This improves reliability for larger projects but may
                take longer. Current settings will chunk files over{" "}
                {chunkThreshold.toLocaleString()} characters into chunks of{" "}
                {chunkSize.toLocaleString()} characters.
              </p>
            ) : (
              <p>
                Code chunking is disabled. Enable it for more reliable analysis
                of large codebases.
              </p>
            )}
          </div>
        </div>
      )}

      <style jsx>{`
        .chunking-config {
          margin-top: 10px;
          border: 1px solid #ddd;
          border-radius: 4px;
          overflow: hidden;
        }

        .config-header {
          background-color: #f5f5f5;
          padding: 10px 15px;
          cursor: pointer;
          user-select: none;
        }

        .header-content {
          display: flex;
          justify-content: space-between;
          align-items: center;
        }

        .config-title {
          font-weight: 500;
        }

        .expand-icon {
          font-size: 12px;
          transition: transform 0.2s;
        }

        .config-content {
          padding: 15px;
          border-top: 1px solid #ddd;
          background-color: #f9f9f9;
        }

        .config-item {
          margin-bottom: 15px;
          display: flex;
          align-items: center;
        }

        .config-item.disabled {
          opacity: 0.5;
        }

        .config-item label {
          margin-right: 10px;
          min-width: 180px;
        }

        .config-item input[type="number"] {
          width: 100px;
          padding: 5px;
          border: 1px solid #ddd;
          border-radius: 4px;
        }

        .config-description {
          margin-top: 10px;
          font-size: 14px;
          color: #666;
        }

        /* Switch styling */
        .switch {
          position: relative;
          display: inline-block;
          width: 50px;
          height: 24px;
          margin-right: 10px;
        }

        .switch input {
          opacity: 0;
          width: 0;
          height: 0;
        }

        .slider {
          position: absolute;
          cursor: pointer;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background-color: #ccc;
          transition: 0.4s;
        }

        .slider:before {
          position: absolute;
          content: "";
          height: 16px;
          width: 16px;
          left: 4px;
          bottom: 4px;
          background-color: white;
          transition: 0.4s;
        }

        input:checked + .slider {
          background-color: #4a90e2;
        }

        input:focus + .slider {
          box-shadow: 0 0 1px #4a90e2;
        }

        input:checked + .slider:before {
          transform: translateX(26px);
        }

        .slider.round {
          border-radius: 24px;
        }

        .slider.round:before {
          border-radius: 50%;
        }

        .option-label {
          display: flex;
          align-items: center;
        }

        .help-tooltip {
          display: inline-flex;
          align-items: center;
          justify-content: center;
          width: 16px;
          height: 16px;
          border-radius: 50%;
          background-color: #4a90e2;
          color: white;
          font-size: 12px;
          margin-left: 5px;
          cursor: help;
        }
      `}</style>
    </div>
  );
};

export default ChunkingConfig;
