"use client";

import React, { useState } from "react";

interface FunctionCall {
  file: string;
  line_number: number;
  context: string;
}

interface FunctionDefinition {
  file: string;
  line_number: number;
}

interface FunctionSummary {
  function_name: string;
  risk_score: number;
  definition: FunctionDefinition;
  call_count: number;
  calls: FunctionCall[];
}

interface FunctionSummaryTableProps {
  summaryData: FunctionSummary[] | null;
  showRawOutput?: boolean;
  rawOutput?: string;
  onToggleView?: () => void;
}

const FunctionSummaryTable: React.FC<FunctionSummaryTableProps> = ({
  summaryData,
  showRawOutput = false,
  rawOutput = "",
  onToggleView,
}) => {
  // Handle invalid data format
  if (summaryData && !Array.isArray(summaryData) && !showRawOutput) {
    console.error(
      "Expected summaryData to be an array but got:",
      typeof summaryData,
    );
    return (
      <div className="error-data">
        <p>Error: Invalid data format for function summary.</p>
        <pre>{JSON.stringify(summaryData, null, 2)}</pre>
      </div>
    );
  }

  // Sort by risk score (highest first)
  const sortedData = summaryData
    ? [...summaryData].sort((a, b) => b.risk_score - a.risk_score)
    : [];

  const getRiskLevelClass = (score: number): string => {
    if (score >= 0.8) return "high-risk";
    if (score >= 0.5) return "medium-risk";
    return "low-risk";
  };

  return (
    <div className="function-summary-container">
      <div className="summary-header">
        <h2>Analysis Results</h2>
        {onToggleView && (
          <button className="view-toggle-button" onClick={onToggleView}>
            {showRawOutput ? "Show Summary Table" : "Show Raw Output"}
          </button>
        )}
      </div>

      {showRawOutput ? (
        <div className="raw-output">
          <pre>{rawOutput || "No analysis output available."}</pre>
        </div>
      ) : (
        <>
          {!summaryData || summaryData.length === 0 ? (
            <div className="no-data">No function summary data available</div>
          ) : (
            <table className="function-summary-table">
              <thead>
                <tr>
                  <th>Function</th>
                  <th>Risk Score</th>
                  <th>Definition</th>
                  <th>Call Count</th>
                  <th>Call Locations</th>
                </tr>
              </thead>
              <tbody>
                {sortedData.map((func, index) => (
                  <tr
                    key={index}
                    className={getRiskLevelClass(func.risk_score)}
                  >
                    <td className="function-name">{func.function_name}</td>
                    <td className="risk-score">
                      <div
                        className="risk-meter"
                        style={{
                          width: `${Math.min(func.risk_score * 100, 100)}%`,
                        }}
                      ></div>
                      <span>{func.risk_score.toFixed(2)}</span>
                    </td>
                    <td className="definition">
                      {func.definition.file}:{func.definition.line_number}
                    </td>
                    <td className="call-count">{func.call_count}</td>
                    <td className="call-locations">
                      {func.calls && func.calls.length > 0 ? (
                        <ul>
                          {func.calls.map((call, i) => (
                            <li key={i}>
                              <div className="call-location">
                                {call.file}:{call.line_number}
                              </div>
                              <div className="call-context">{call.context}</div>
                            </li>
                          ))}
                          {func.call_count > (func.calls?.length || 0) && (
                            <li className="more-calls">
                              ...and{" "}
                              {func.call_count - (func.calls?.length || 0)} more
                            </li>
                          )}
                        </ul>
                      ) : (
                        <span className="no-calls">No calls found</span>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </>
      )}

      <style jsx>{`
        .function-summary-container {
          margin-top: 20px;
          font-family: system-ui, sans-serif;
        }

        .summary-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: 15px;
        }

        .summary-header h2 {
          margin: 0;
          font-size: 18px;
          color: #333;
        }

        .view-toggle-button {
          background-color: #f0f0f0;
          border: 1px solid #ddd;
          border-radius: 4px;
          padding: 6px 12px;
          font-size: 14px;
          cursor: pointer;
          transition: all 0.2s ease;
        }

        .view-toggle-button:hover {
          background-color: #e0e0e0;
          border-color: #ccc;
        }

        .raw-output {
          background-color: #f8f8f8;
          border: 1px solid #e0e0e0;
          border-radius: 4px;
          padding: 15px;
          max-height: 500px;
          overflow-y: auto;
        }

        .raw-output pre {
          margin: 0;
          white-space: pre-wrap;
          font-family: monospace;
          font-size: 14px;
          line-height: 1.5;
        }

        .function-summary-table {
          width: 100%;
          border-collapse: collapse;
          font-size: 14px;
          background-color: white;
          box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }

        .function-summary-table th {
          padding: 10px;
          text-align: left;
          border-bottom: 2px solid #e0e0e0;
          background-color: #f5f5f5;
          font-weight: 600;
        }

        .function-summary-table td {
          padding: 10px;
          border-bottom: 1px solid #e0e0e0;
        }

        .high-risk {
          background-color: rgba(244, 67, 54, 0.05);
        }

        .medium-risk {
          background-color: rgba(255, 152, 0, 0.05);
        }

        .low-risk {
          background-color: rgba(76, 175, 80, 0.05);
        }

        .function-name {
          font-family: monospace;
          font-weight: 600;
        }

        .risk-score {
          position: relative;
          width: 100px;
        }

        .risk-meter {
          position: absolute;
          top: 0;
          left: 0;
          height: 100%;
          background-color: rgba(244, 67, 54, 0.2);
          z-index: 0;
        }

        .risk-score span {
          position: relative;
          z-index: 1;
          padding-left: 5px;
          font-weight: 600;
        }

        .definition {
          font-family: monospace;
        }

        .call-count {
          text-align: center;
        }

        .call-locations ul {
          list-style: none;
          margin: 0;
          padding: 0;
        }

        .call-locations li {
          margin-bottom: 5px;
          padding-bottom: 5px;
          border-bottom: 1px dotted #eee;
        }

        .call-locations li:last-child {
          margin-bottom: 0;
          padding-bottom: 0;
          border-bottom: none;
        }

        .call-location {
          font-family: monospace;
          font-size: 12px;
          color: #0070f3;
          margin-bottom: 2px;
        }

        .call-context {
          font-family: monospace;
          font-size: 12px;
          color: #666;
          white-space: nowrap;
          overflow: hidden;
          text-overflow: ellipsis;
          max-width: 300px;
        }

        .more-calls {
          font-style: italic;
          color: #777;
          font-size: 12px;
        }

        .no-calls {
          color: #999;
          font-style: italic;
        }

        .no-data {
          padding: 20px;
          text-align: center;
          color: #666;
          font-style: italic;
          background-color: #f9f9f9;
          border-radius: 4px;
        }

        .error-data {
          padding: 20px;
          color: #d32f2f;
          background-color: #ffebee;
          border-radius: 4px;
          margin-bottom: 20px;
        }

        .error-data pre {
          background-color: rgba(0, 0, 0, 0.05);
          padding: 10px;
          overflow: auto;
          max-height: 200px;
          margin-top: 10px;
          border-radius: 3px;
        }
      `}</style>
    </div>
  );
};

export default FunctionSummaryTable;
