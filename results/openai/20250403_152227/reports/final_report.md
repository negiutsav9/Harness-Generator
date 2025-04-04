# CBMC Harness Generation Complete - Directory Mode - Openai

Total processing time: 911.45 seconds
Processed 23 source files.
Analyzed 223 functions.
Identified 39 functions with memory or arithmetic operations.
Generated 3 verification harnesses.
Performed 7 harness refinements (average 2.33 per function).

## File Analysis

### core_http_client.c
Functions analyzed: 35
Functions verified: 3
Successful verifications: 2
Failed verifications: 1

### pattern
Functions analyzed: 4
Functions verified: 0

## RAG Knowledge Base Statistics
Code functions stored: 247
Pattern templates: 16
Error patterns stored: 0
Successful solutions: 0

The RAG (Retrieval-Augmented Generation) knowledge base stores code functions, patterns, errors, and solutions to improve harness generation over time. Each run contributes to this knowledge base, helping future runs generate better harnesses with fewer iterations.

## Unit Proof Metrics Summary
Total reachable lines: 0
Total coverage: 0.00%
Total reachable lines for harnessed functions only: 60
Coverage of harnessed functions only: 85.00%
Number of reported errors: 0
Functions with full coverage: 0 of 3
Functions without errors: 2 of 3

### Note on Error Reporting:
- Errors are grouped by line number (one error per line)
- Errors about missing function bodies are excluded
- Loop unwinding assertions are excluded from error count

## Performance Metrics
Average harness generation time: 11.49 seconds
Average verification time: 51.38 seconds
Average evaluation time: 0.00 seconds

## Summary of Results

### Function: HTTPClient_AddHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 4
Message: Verification successful

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 20
- Function coverage: 85.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250403_152227/harnesses/core_http_client.c:HTTPClient_AddHeader/v1.c
  - Version 2: results/openai/20250403_152227/harnesses/core_http_client.c:HTTPClient_AddHeader/v2.c
  - Version 3: results/openai/20250403_152227/harnesses/core_http_client.c:HTTPClient_AddHeader/v3.c
  - Version 4: results/openai/20250403_152227/harnesses/core_http_client.c:HTTPClient_AddHeader/v4.c
  - Size evolution: Initial 40 lines → Final 51 lines (+11 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250403_152227/verification/core_http_client.c:HTTPClient_AddHeader/v1_results.txt
  - results/openai/20250403_152227/verification/core_http_client.c:HTTPClient_AddHeader/v1_report.md
  - results/openai/20250403_152227/verification/core_http_client.c:HTTPClient_AddHeader/v2_results.txt
  - results/openai/20250403_152227/verification/core_http_client.c:HTTPClient_AddHeader/v2_report.md
  - results/openai/20250403_152227/verification/core_http_client.c:HTTPClient_AddHeader/v3_results.txt
  - results/openai/20250403_152227/verification/core_http_client.c:HTTPClient_AddHeader/v3_report.md
  - results/openai/20250403_152227/verification/core_http_client.c:HTTPClient_AddHeader/v4_results.txt
  - results/openai/20250403_152227/verification/core_http_client.c:HTTPClient_AddHeader/v4_report.md
  - results/openai/20250403_152227/verification/core_http_client.c:HTTPClient_AddHeader/v5_results.txt
  - results/openai/20250403_152227/verification/core_http_client.c:HTTPClient_AddHeader/v5_report.md

### Function: HTTPClient_AddRangeHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 20
- Function coverage: 85.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250403_152227/harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v1.c
  - Version 2: results/openai/20250403_152227/harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v2.c
  - Size evolution: Initial 32 lines → Final 35 lines (+3 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250403_152227/verification/core_http_client.c:HTTPClient_AddRangeHeader/v1_results.txt
  - results/openai/20250403_152227/verification/core_http_client.c:HTTPClient_AddRangeHeader/v1_report.md
  - results/openai/20250403_152227/verification/core_http_client.c:HTTPClient_AddRangeHeader/v2_results.txt
  - results/openai/20250403_152227/verification/core_http_client.c:HTTPClient_AddRangeHeader/v2_report.md

### Function: HTTPClient_InitializeRequestHeaders (File: core_http_client.c)
Status: FAILED
Refinements: 2
Message: VERIFICATION FAILED: Null pointer dereference detected
Suggestions: Add null pointer checks before dereferencing pointers

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 20
- Function coverage: 85.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250403_152227/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1.c
  - Version 2: results/openai/20250403_152227/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2.c
  - Size evolution: Initial 32 lines → Final 46 lines (+14 lines)
  - Refinement result: Some issues remain after 2 refinements

#### Verification Reports: 
  - results/openai/20250403_152227/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1_results.txt
  - results/openai/20250403_152227/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1_report.md
  - results/openai/20250403_152227/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2_results.txt
  - results/openai/20250403_152227/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2_report.md
  - results/openai/20250403_152227/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v3_results.txt
  - results/openai/20250403_152227/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v3_report.md