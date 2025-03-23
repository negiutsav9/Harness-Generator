"use client";

import React, { useState, useEffect } from "react";

interface ChunkingSettingsProps {
  onSettingsChange: (settings: ChunkingSettings) => void;
  initialSettings?: ChunkingSettings;
  codeSize?: number;
}

export interface ChunkingSettings {
  useChunking: boolean;
  chunkSize: number;
  chunkThreshold: number;
}

const ChunkingSettingsPanel: React.FC<ChunkingSettingsProps> = ({
  onSettingsChange,
  initialSettings,
  codeSize = 0,
}) => {
  // Default values
  const defaultSettings: ChunkingSettings = {
    useChunking: false,
    chunkSize: 40000,
    chunkThreshold: 100000,
  };

  // Use provided initial settings or defaults
  const [settings, setSettings] = useState<ChunkingSettings>(
    initialSettings || defaultSettings,
  );

  // Panel expanded state
  const [isExpanded, setIsExpanded] = useState(false);

  // Auto-enable chunking if code size exceeds threshold
  useEffect(() => {
    if (codeSize > settings.chunkThreshold && !settings.useChunking) {
      const newSettings = {
        ...settings,
        useChunking: true,
      };
      setSettings(newSettings);
      onSettingsChange(newSettings);
    }
  }, [codeSize, settings.chunkThreshold]);

  // Handle changes to settings
  const handleSettingChange = (key: keyof ChunkingSettings, value: any) => {
    const newSettings = { ...settings, [key]: value };
    setSettings(newSettings);
    onSettingsChange(newSettings);
  };

  return (
    <div className="chunking-settings-panel">
      <div className="panel-header" onClick={() => setIsExpanded(!isExpanded)}>
        <span className="panel-title">
          {isExpanded ? "▼" : "▶"} Code Analysis Settings
        </span>
        {settings.useChunking && (
          <span className="chunking-badge">Chunking Enabled</span>
        )}
      </div>

      {isExpanded && (
        <div className="panel-content">
          <div className="setting-row">
            <label className="setting-label">
              <input
                type="checkbox"
                checked={settings.useChunking}
                onChange={(e) =>
                  handleSettingChange("useChunking", e.target.checked)
                }
              />
              <span>Enable Code Chunking</span>
            </label>
            <div className="setting-info">
              Splits large code into smaller pieces for more reliable analysis
            </div>
          </div>

          <div
            className={`setting-row ${!settings.useChunking ? "disabled" : ""}`}
          >
            <label className="setting-label">
              <span>Chunk Size (characters):</span>
              <input
                type="number"
                value={settings.chunkSize}
                min="10000"
                max="100000"
                step="10000"
                disabled={!settings.useChunking}
                onChange={(e) =>
                  handleSettingChange(
                    "chunkSize",
                    parseInt(e.target.value) || 40000,
                  )
                }
              />
            </label>
            <div className="setting-info">
              Maximum size of each code chunk (recommended: 40,000 - 50,000)
            </div>
          </div>

          <div
            className={`setting-row ${!settings.useChunking ? "disabled" : ""}`}
          >
            <label className="setting-label">
              <span>Auto-Chunking Threshold:</span>
              <input
                type="number"
                value={settings.chunkThreshold}
                min="50000"
                max="200000"
                step="10000"
                disabled={!settings.useChunking}
                onChange={(e) =>
                  handleSettingChange(
                    "chunkThreshold",
                    parseInt(e.target.value) || 100000,
                  )
                }
              />
            </label>
            <div className="setting-info">
              Code size at which chunking automatically activates
            </div>
          </div>

          <div className="code-size-info">
            Current code size: <strong>{codeSize.toLocaleString()}</strong>{" "}
            characters
            {codeSize > 0 && (
              <span>
                {codeSize > settings.chunkThreshold
                  ? " (chunking recommended)"
                  : " (chunking optional)"}
              </span>
            )}
          </div>
        </div>
      )}

      <style jsx>{`
        .chunking-settings-panel {
          margin-bottom: 20px;
          border: 1px solid #ddd;
          border-radius: 4px;
          overflow: hidden;
        }

        .panel-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          padding: 10px 15px;
          background-color: #f5f5f5;
          cursor: pointer;
          user-select: none;
        }

        .panel-title {
          font-weight: 500;
        }

        .chunking-badge {
          font-size: 12px;
          background-color: #4a90e2;
          color: white;
          padding: 3px 8px;
          border-radius: 12px;
        }

        .panel-content {
          padding: 15px;
          border-top: 1px solid #ddd;
        }

        .setting-row {
          margin-bottom: 15px;
        }

        .setting-row.disabled {
          opacity: 0.6;
        }

        .setting-label {
          display: flex;
          align-items: center;
          justify-content: space-between;
          margin-bottom: 5px;
        }

        .setting-label input[type="checkbox"] {
          margin-right: 8px;
        }

        .setting-label input[type="number"] {
          width: 100px;
          padding: 5px;
          margin-left: 10px;
          border: 1px solid #ddd;
          border-radius: 4px;
        }

        .setting-info {
          font-size: 12px;
          color: #666;
          margin-top: 2px;
        }

        .code-size-info {
          margin-top: 15px;
          padding: 10px;
          background-color: #f0f7ff;
          border-radius: 4px;
          font-size: 13px;
        }
      `}</style>
    </div>
  );
};

export default ChunkingSettingsPanel;
