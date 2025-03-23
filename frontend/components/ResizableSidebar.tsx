"use client";

import React, { useState, useEffect, useRef } from "react";

interface ResizableSidebarProps {
  initialWidth?: number;
  minWidth?: number;
  maxWidth?: number;
  children: React.ReactNode;
}

const ResizableSidebar: React.FC<ResizableSidebarProps> = ({
  initialWidth = 250,
  minWidth = 150,
  maxWidth = 500,
  children,
}) => {
  const [width, setWidth] = useState(initialWidth);
  const [isResizing, setIsResizing] = useState(false);
  const sidebarRef = useRef<HTMLDivElement>(null);
  const resizerRef = useRef<HTMLDivElement>(null);

  // Initialize dragging
  const startResizing = (e: React.MouseEvent) => {
    e.preventDefault();
    setIsResizing(true);
  };

  // Handle resizing
  useEffect(() => {
    const handleResize = (e: MouseEvent) => {
      if (!isResizing) return;

      // Get the sidebar's bounding rectangle
      const rect = sidebarRef.current?.getBoundingClientRect();
      if (!rect) return;

      // Calculate new width
      const newWidth = e.clientX - rect.left;

      // Apply constraints
      if (newWidth >= minWidth && newWidth <= maxWidth) {
        setWidth(newWidth);
      }
    };

    const stopResizing = () => {
      setIsResizing(false);
    };

    if (isResizing) {
      document.addEventListener("mousemove", handleResize);
      document.addEventListener("mouseup", stopResizing);
    }

    return () => {
      document.removeEventListener("mousemove", handleResize);
      document.removeEventListener("mouseup", stopResizing);
    };
  }, [isResizing, minWidth, maxWidth]);

  return (
    <div
      ref={sidebarRef}
      className="resizable-sidebar"
      style={{ width: `${width}px` }}
    >
      <div className="sidebar-content">{children}</div>
      <div
        ref={resizerRef}
        className="sidebar-resizer"
        onMouseDown={startResizing}
      />

      <style jsx>{`
        .resizable-sidebar {
          position: relative;
          height: 100%;
          overflow: hidden;
          background-color: #f5f5f5;
          border-right: 1px solid #e0e0e0;
          transition: width 0.1s ease;
          transition-property: width;
          transition-duration: ${isResizing ? "0s" : "0.1s"};
        }

        .sidebar-content {
          width: 100%;
          height: 100%;
          overflow: auto;
        }

        .sidebar-resizer {
          position: absolute;
          top: 0;
          right: 0;
          width: 4px;
          height: 100%;
          background-color: transparent;
          cursor: col-resize;
          z-index: 10;
        }

        .sidebar-resizer:hover,
        .sidebar-resizer:active {
          background-color: #0070f3;
        }
      `}</style>
    </div>
  );
};

export default ResizableSidebar;
