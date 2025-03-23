"use client";

import React from "react";

interface ProgressSidebarProps {
  currentStep: number;
  iterationCount: number;
  isProcessing: boolean;
  onStepClick: (stepId: number) => void;
}

const ProgressSidebar: React.FC<ProgressSidebarProps> = ({
  currentStep,
  iterationCount,
  isProcessing,
  onStepClick,
}) => {
  const steps = [
    {
      id: 1,
      name: "Code Analysis",
      description: "Identifying memory-leak prone functions",
    },
    {
      id: 2,
      name: "Harness Generation",
      description: "Creating test harnesses",
    },
    { id: 3, name: "Verification", description: "Running CBMC verification" },
    {
      id: 4,
      name: "Review & Refine",
      description: "Evaluating and improving harnesses",
    },
  ];

  const getStepStatus = (stepId: number) => {
    if (currentStep === stepId) {
      return isProcessing ? "in-progress" : "pending";
    }
    if (currentStep > stepId) {
      return "success";
    }
    return "pending";
  };

  return (
    <div className="progress-sidebar">
      <h2>Progress</h2>
      <div className="iteration-info">
        <p>Iteration: {iterationCount || 0}</p>
      </div>

      <div className="steps-container">
        {steps.map((step) => (
          <div
            key={step.id}
            className={`step-item ${isProcessing ? "disabled" : "clickable"}`}
            onClick={() => !isProcessing && onStepClick(step.id)}
          >
            <div className="step-header">
              <span
                className={`status-indicator status-${getStepStatus(step.id)}`}
              ></span>
              <h3>{step.name}</h3>
            </div>
            <p className="step-description">{step.description}</p>
          </div>
        ))}
      </div>

      {isProcessing && (
        <div className="processing-indicator">
          <p>Processing... This may take a few minutes.</p>
        </div>
      )}

      <style jsx>{`
        .iteration-info {
          margin: 15px 0;
          padding: 8px;
          background-color: #f0f7ff;
          border-radius: 4px;
        }

        .steps-container {
          margin-top: 20px;
        }

        .step-item {
          margin-bottom: 15px;
          padding: 10px;
          border-radius: 4px;
          border-bottom: 1px solid #eee;
          transition: all 0.2s ease;
        }

        .step-item.clickable {
          cursor: pointer;
        }

        .step-item.clickable:hover {
          background-color: #f5f5f5;
          transform: translateY(-2px);
          box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        .step-item.disabled {
          opacity: 0.7;
          cursor: not-allowed;
        }

        .step-header {
          display: flex;
          align-items: center;
          margin-bottom: 5px;
        }

        .step-description {
          font-size: 14px;
          color: #666;
          margin-left: 18px;
        }

        .processing-indicator {
          margin-top: 20px;
          padding: 10px;
          background-color: #fff9c4;
          border-radius: 4px;
          font-size: 14px;
        }

        @keyframes pulse {
          0% {
            transform: scale(1);
          }
          50% {
            transform: scale(1.05);
          }
          100% {
            transform: scale(1);
          }
        }

        .clickable:active {
          animation: pulse 0.3s ease-in-out;
        }
      `}</style>
    </div>
  );
};

export default ProgressSidebar;
