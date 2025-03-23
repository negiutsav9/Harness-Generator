"use client";

import React, { useState } from "react";

interface ResultsDisplayProps {
  results: any;
  error: string | null;
}

const ResultsDisplay: React.FC<ResultsDisplayProps> = ({ results, error }) => {
  const [activeTab, setActiveTab] = useState<string>("harnesses");

  if (error) {
    return (
      <div className="results-container error">
        <h2>Error</h2>
        <p className="error-message">{error}</p>
        <style jsx>{`
          .error {
            background-color: #ffebee;
          }
          .error-message {
            color: #d32f2f;
            margin-top: 10px;
          }
        `}</style>
      </div>
    );
  }

  if (!results) {
    return (
      <div className="results-container empty">
        <p>Submit your code to generate test harnesses</p>
        <style jsx>{`
          .empty {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100px;
            color: #757575;
          }
        `}</style>
      </div>
    );
  }

  return (
    <div className="results-container">
      <div className="results-tabs">
        <button
          className={`results-tab ${activeTab === "harnesses" ? "active" : ""}`}
          onClick={() => setActiveTab("harnesses")}
        >
          Generated Harnesses
        </button>
        <button
          className={`results-tab ${activeTab === "functions" ? "active" : ""}`}
          onClick={() => setActiveTab("functions")}
        >
          Identified Functions
        </button>
        <button
          className={`results-tab ${activeTab === "verification" ? "active" : ""}`}
          onClick={() => setActiveTab("verification")}
        >
          Verification Results
        </button>
      </div>

      <div className="results-content">
        {activeTab === "functions" && (
          <div className="functions-container">
            <h2>Identified Functions</h2>
            {results.target_functions && results.target_functions.length > 0 ? (
              <ul className="function-list">
                {results.target_functions.map((func: any, index: number) => (
                  <li key={index} className="function-item">
                    <div className="function-name">{func.name}</div>
                    <div className="function-signature">{func.signature}</div>
                    <div className="function-location">
                      File: {func.file}, Line: {func.line_number}
                    </div>
                    <div className="function-score">
                      Risk Score:{" "}
                      <span className="score">
                        {func.risk_score.toFixed(2)}
                      </span>
                    </div>
                  </li>
                ))}
              </ul>
            ) : (
              <p>No memory-leak prone functions identified.</p>
            )}
          </div>
        )}

        {activeTab === "harnesses" && (
          <div className="harnesses-container">
            <h2>Generated Harnesses</h2>
            {results.harnesses && results.harnesses.length > 0 ? (
              <div className="harness-list">
                {results.harnesses.map((harness: any, index: number) => (
                  <div key={index} className="harness-item">
                    <h3 className="harness-function">
                      Harness for: {harness.function_name}
                    </h3>
                    <pre className="harness-code">{harness.harness_code}</pre>
                  </div>
                ))}
              </div>
            ) : (
              <p>No harnesses have been generated yet.</p>
            )}
          </div>
        )}

        {activeTab === "verification" && (
          <div className="verification-container">
            <h2>Verification Results</h2>
            {results.verification && results.verification.length > 0 ? (
              <div className="verification-list">
                {results.verification.map((result: any, index: number) => (
                  <div
                    key={index}
                    className={`verification-item ${
                      result.status === "success" ? "success" : "error"
                    }`}
                  >
                    <h3 className="verification-function">
                      Function: {result.function_name}
                    </h3>
                    <div className="verification-status">
                      Status:{" "}
                      <span className={`status-${result.status}`}>
                        {result.status}
                      </span>
                    </div>
                    {result.errors && result.errors.length > 0 && (
                      <div className="verification-errors">
                        <h4>Errors:</h4>
                        <ul>
                          {result.errors.map((error: string, i: number) => (
                            <li key={i}>{error}</li>
                          ))}
                        </ul>
                      </div>
                    )}
                  </div>
                ))}
              </div>
            ) : (
              <p>No verification results available yet.</p>
            )}
          </div>
        )}
      </div>

      <style jsx>{`
        .functions-container,
        .harnesses-container,
        .verification-container {
          margin-top: 15px;
        }

        .function-list,
        .harness-list,
        .verification-list {
          margin-top: 15px;
        }

        .function-item,
        .harness-item,
        .verification-item {
          background-color: #f9f9f9;
          border: 1px solid #e0e0e0;
          border-radius: 4px;
          padding: 15px;
          margin-bottom: 15px;
        }

        .function-name,
        .harness-function,
        .verification-function {
          font-weight: bold;
          margin-bottom: 5px;
        }

        .function-signature {
          font-family: monospace;
          background-color: #f0f0f0;
          padding: 5px;
          border-radius: 3px;
          margin-bottom: 5px;
        }

        .function-location,
        .function-score {
          font-size: 14px;
          color: #666;
          margin-top: 5px;
        }

        .score {
          font-weight: bold;
          color: #d32f2f;
        }

        .harness-code {
          background-color: #f0f0f0;
          padding: 10px;
          border-radius: 3px;
          overflow-x: auto;
          font-family: monospace;
          font-size: 13px;
          line-height: 1.5;
          margin-top: 10px;
        }

        .verification-status {
          margin: 5px 0;
        }

        .status-success {
          color: #2e7d32;
        }

        .status-error,
        .status-failure {
          color: #d32f2f;
        }

        .verification-errors {
          margin-top: 10px;
        }

        .verification-errors h4 {
          margin-bottom: 5px;
        }

        .verification-errors ul {
          list-style-type: disc;
          padding-left: 20px;
        }

        .verification-errors li {
          margin-bottom: 3px;
        }

        .success {
          border-left: 4px solid #2e7d32;
        }

        .error {
          border-left: 4px solid #d32f2f;
        }
      `}</style>
    </div>
  );
};

export default ResultsDisplay;
