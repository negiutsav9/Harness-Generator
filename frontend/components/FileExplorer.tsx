"use client";

import React, { useState } from "react";

interface FileNode {
  name: string;
  path: string;
  isDirectory: boolean;
  children?: FileNode[];
  content?: string;
}

interface FileExplorerProps {
  files: FileNode[];
  onFileSelect: (file: FileNode) => void;
  activeFilePath?: string;
}

const FileExplorer: React.FC<FileExplorerProps> = ({
  files,
  onFileSelect,
  activeFilePath,
}) => {
  const [expandedFolders, setExpandedFolders] = useState<Set<string>>(
    new Set(),
  );

  const toggleFolder = (path: string) => {
    const newExpandedFolders = new Set(expandedFolders);
    if (newExpandedFolders.has(path)) {
      newExpandedFolders.delete(path);
    } else {
      newExpandedFolders.add(path);
    }
    setExpandedFolders(newExpandedFolders);
  };

  const renderFileNode = (node: FileNode, depth = 0) => {
    const isExpanded = expandedFolders.has(node.path);
    const isActive = node.path === activeFilePath;

    // Don't render ">" if this is not a directory
    const showArrow = node.isDirectory;

    return (
      <div key={node.path} className="tree-item">
        <div
          className={`tree-node ${isActive ? "active" : ""}`}
          style={{ paddingLeft: `${depth * 16}px` }}
          data-path={node.path}
          onClick={() => {
            if (node.isDirectory) {
              toggleFolder(node.path);
            } else {
              onFileSelect({
                ...node,
                content: node.content || "",
              });
            }
          }}
        >
          {showArrow && (
            <span
              className="arrow"
              style={{
                transform: isExpanded ? "rotate(90deg)" : "rotate(0deg)",
                display: "inline-block",
              }}
            >
              &gt;
            </span>
          )}
          <span className="icon">{node.isDirectory ? "📁" : "📄"}</span>
          <span className="name">{node.name}</span>
        </div>

        {node.isDirectory && isExpanded && node.children && (
          <div className="children">
            {node.children
              .sort((a, b) => {
                // Directories first, then files
                if (a.isDirectory && !b.isDirectory) return -1;
                if (!a.isDirectory && b.isDirectory) return 1;
                // Then sort alphabetically
                return a.name.localeCompare(b.name);
              })
              .map((child) => renderFileNode(child, depth + 1))}
          </div>
        )}
      </div>
    );
  };

  return (
    <div className="file-explorer">
      <div className="file-explorer-header">
        <h3>Files</h3>
      </div>
      <div className="file-explorer-content">
        {files.length === 0 ? (
          <div className="no-files">
            <p>No files uploaded yet</p>
            <p>Use "Upload File" or "Import Directory" to add files</p>
          </div>
        ) : (
          files.map((file) => renderFileNode(file))
        )}
      </div>

      <style jsx>{`
        .file-explorer {
          height: 100%;
          display: flex;
          flex-direction: column;
          background-color: #f3f3f3;
          font-family:
            -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
            Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
        }

        .file-explorer-header {
          padding: 8px 12px;
          background-color: #f3f3f3;
          display: flex;
          justify-content: space-between;
          align-items: center;
          border-bottom: 1px solid #e0e0e0;
        }

        .file-explorer-header h3 {
          margin: 0;
          font-size: 12px;
          font-weight: normal;
          color: #444;
          text-transform: uppercase;
        }

        .file-explorer-content {
          flex: 1;
          overflow-y: auto;
          user-select: none;
        }

        .no-files {
          padding: 15px;
          color: #666;
          font-size: 13px;
          text-align: center;
        }

        .no-files p {
          margin: 5px 0;
        }

        .tree-item {
          margin: 0;
        }

        .tree-node {
          display: flex;
          align-items: center;
          padding: 1px 0;
          height: 22px;
          font-size: 13px;
          color: #333;
          cursor: pointer;
        }

        .tree-node:hover {
          background-color: #e8e8e8;
        }

        .tree-node.active {
          background-color: #dfdfdf;
        }

        .arrow {
          font-size: 10px;
          width: 14px;
          display: inline-block;
          text-align: center;
          color: #555;
          transform-origin: center;
          transition: transform 0.2s;
          visibility: visible;
        }

        ${Array.from(expandedFolders)
          .map(
            (path) => `
          [data-path="${path}"] .arrow {
            transform: rotate(90deg);
          }
        `,
          )
          .join("\n")}

        .icon {
          margin: 0 4px;
          font-size: 12px;
        }

        .name {
          white-space: nowrap;
          overflow: hidden;
          text-overflow: ellipsis;
        }

        .children {
          margin-left: 0;
        }
      `}</style>
    </div>
  );
};

export default FileExplorer;
