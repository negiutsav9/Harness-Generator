# CBMC Harness Generation Complete - Directory Mode - Openai

Total processing time: 3077.29 seconds
Processed 23 source files.
Analyzed 223 functions.
Identified 39 functions with memory or arithmetic operations.
Generated 8 verification harnesses.
Performed 44 harness refinements (average 5.50 per function).

## File Analysis

### core_http_client.c
Functions analyzed: 35
Functions verified: 8
Successful verifications: 3
Failed verifications: 5

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
Total reachable lines for harnessed functions only: 120
Coverage of harnessed functions only: 85.00%
Number of reported errors: 0
Functions with full coverage: 0 of 8
Functions without errors: 3 of 8

### Note on Error Reporting:
- Errors are grouped by line number (one error per line)
- Errors about missing function bodies are excluded
- Loop unwinding assertions are excluded from error count

## Performance Metrics
Average harness generation time: 5.89 seconds
Average verification time: 55.24 seconds
Average evaluation time: 0.00 seconds

## Summary of Results

### Function: HTTPClient_AddHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 2
Message: Verification successful

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 20
- Function coverage: 85.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_AddHeader/v1.c
  - Version 2: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_AddHeader/v2.c
  - Version 3: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_AddHeader/v3.c
  - Size evolution: Initial 40 lines → Final 48 lines (+8 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_AddHeader/v1_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_AddHeader/v1_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_AddHeader/v2_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_AddHeader/v2_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_AddHeader/v3_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_AddHeader/v3_report.md

### Function: HTTPClient_AddRangeHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 2
Message: Verification successful

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 20
- Function coverage: 85.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v1.c
  - Version 2: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v2.c
  - Version 3: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v3.c
  - Size evolution: Initial 30 lines → Final 40 lines (+10 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_AddRangeHeader/v1_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_AddRangeHeader/v1_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_AddRangeHeader/v2_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_AddRangeHeader/v2_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_AddRangeHeader/v3_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_AddRangeHeader/v3_report.md

### Function: HTTPClient_InitializeRequestHeaders (File: core_http_client.c)
Status: FAILED
Refinements: 9
Message: VERIFICATION FAILED: Null pointer dereference detected
Suggestions: Add null pointer checks before dereferencing pointers

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 20
- Function coverage: 85.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1.c
  - Version 2: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2.c
  - Version 3: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v3.c
  - Version 4: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v4.c
  - Size evolution: Initial 29 lines → Final 60 lines (+31 lines)
  - Refinement result: Some issues remain after 9 refinements

#### Verification Reports: 
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v3_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v3_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v4_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v4_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v5_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v5_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v6_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v6_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v7_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v7_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v8_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v8_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v9_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v9_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v10_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v10_report.md

### Function: HTTPClient_ReadHeader (File: core_http_client.c)
Status: FAILED
Refinements: 9
Message: VERIFICATION FAILED: Memory leak detected
Suggestions: Ensure all allocated memory is freed in all execution paths

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 20
- Function coverage: 85.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_ReadHeader/v1.c
  - Version 2: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_ReadHeader/v2.c
  - Size evolution: Initial 40 lines → Final 40 lines (0 lines)
  - Refinement result: Some issues remain after 9 refinements

#### Verification Reports: 
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReadHeader/v1_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReadHeader/v1_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReadHeader/v2_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReadHeader/v2_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReadHeader/v3_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReadHeader/v3_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReadHeader/v4_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReadHeader/v4_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReadHeader/v5_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReadHeader/v5_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReadHeader/v6_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReadHeader/v6_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReadHeader/v7_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReadHeader/v7_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReadHeader/v8_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReadHeader/v8_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReadHeader/v9_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReadHeader/v9_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReadHeader/v10_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReadHeader/v10_report.md

### Function: HTTPClient_ReceiveAndParseHttpResponse (File: core_http_client.c)
Status: FAILED
Refinements: 9
Message: VERIFICATION FAILED: Null pointer dereference detected
Suggestions: Add null pointer checks before dereferencing pointers

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 20
- Function coverage: 85.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1.c
  - Version 2: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v2.c
  - Version 3: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v3.c
  - Version 4: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v4.c
  - Version 5: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v5.c
  - Version 6: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v6.c
  - Size evolution: Initial 36 lines → Final 56 lines (+20 lines)
  - Refinement result: Some issues remain after 9 refinements

#### Verification Reports: 
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v2_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v2_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v3_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v3_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v4_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v4_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v5_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v5_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v6_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v6_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v7_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v7_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v8_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v8_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v9_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v9_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v10_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v10_report.md

### Function: HTTPClient_Send (File: core_http_client.c)
Status: TIMEOUT
Refinements: 9
Message: CBMC verification timed out after 170 seconds.
Suggestions: The function may have complex paths requiring longer verification time. Consider using more selective file inclusion or increasing timeout.

#### Harness Evolution:
  - Version 1: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_Send/v1.c
  - Version 2: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_Send/v2.c
  - Version 3: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_Send/v3.c
  - Size evolution: Initial 44 lines → Final 61 lines (+17 lines)
  - Refinement result: Some issues remain after 9 refinements

#### Verification Reports: 
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_Send/v1_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_Send/v1_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_Send/v2_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_Send/v2_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_Send/v3_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_Send/v3_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_Send/v4_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_Send/v4_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_Send/v5_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_Send/v5_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_Send/v6_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_Send/v6_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_Send/v7_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_Send/v7_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_Send/v8_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_Send/v8_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_Send/v9_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_Send/v9_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_Send/v10_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_Send/v10_report.md

### Function: HTTPClient_SendHttpData (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: Verification successful

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 20
- Function coverage: 85.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_SendHttpData/v1.c

#### Verification Reports: 
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_SendHttpData/v1_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_SendHttpData/v1_report.md

### Function: HTTPClient_SendHttpHeaders (File: core_http_client.c)
Status: TIMEOUT
Refinements: 4
Message: CBMC verification timed out after 120 seconds.
Suggestions: The function may have complex paths requiring longer verification time. Consider using more selective file inclusion or increasing timeout.

#### Harness Evolution:
  - Version 1: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v1.c
  - Version 2: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v2.c
  - Version 3: results/openai/20250403_133836/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v3.c
  - Size evolution: Initial 39 lines → Final 51 lines (+12 lines)
  - Refinement result: Some issues remain after 4 refinements

#### Verification Reports: 
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v1_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v1_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v2_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v2_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v3_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v3_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v4_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v4_report.md
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v5_results.txt
  - results/openai/20250403_133836/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v5_report.md