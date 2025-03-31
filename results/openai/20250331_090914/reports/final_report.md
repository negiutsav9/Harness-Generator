# CBMC Harness Generation Complete - Directory Mode - Openai

Total processing time: 1132.62 seconds
Processed 23 source files.
Analyzed 223 functions.
Identified 39 functions with memory or arithmetic operations.
Generated 3 verification harnesses.
Performed 11 harness refinements (average 2.20 per function).

## File Analysis

### core_http_client.c
Functions analyzed: 35
Functions verified: 3
Successful verifications: 2
Failed verifications: 1

### pattern
Functions analyzed: 4
Functions verified: 0

## Unit Proof Metrics Summary
Total reachable lines: 383
Total coverage: 79.63%
Total reachable lines for harnessed functions only: 190
Coverage of harnessed functions only: 78.95%
Number of reported errors: 0
Functions with full coverage: 0 of 3
Functions without errors: 3 of 3

### Note on Error Reporting:
- Errors are grouped by line number (one error per line)
- Errors about missing function bodies are excluded
- Loop unwinding assertions are excluded from error count

## Performance Metrics
Average harness generation time: 4.47 seconds
Average verification time: 0.37 seconds
Average evaluation time: 0.02 seconds

## Summary of Results

### Function: HTTPClient_AddHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 113
- Total coverage: 79.65%
- Function reachable lines: 56
- Function coverage: 78.57%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_090914/harnesses/core_http_client.c:HTTPClient_AddHeader/v1.c
  - Version 2: results/openai/20250331_090914/harnesses/core_http_client.c:HTTPClient_AddHeader/v2.c
  - Version 3: results/openai/20250331_090914/harnesses/core_http_client.c:HTTPClient_AddHeader/v3.c
  - Size evolution: Initial 126 lines → Final 113 lines (-13 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250331_090914/verification/core_http_client.c:HTTPClient_AddHeader/v1_results.txt
  - results/openai/20250331_090914/verification/core_http_client.c:HTTPClient_AddHeader/v1_report.md
  - results/openai/20250331_090914/verification/core_http_client.c:HTTPClient_AddHeader/v2_results.txt
  - results/openai/20250331_090914/verification/core_http_client.c:HTTPClient_AddHeader/v2_report.md

### Function: HTTPClient_AddRangeHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 99
- Total coverage: 79.80%
- Function reachable lines: 49
- Function coverage: 79.59%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_090914/harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v1.c
  - Version 2: results/openai/20250331_090914/harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v2.c
  - Version 3: results/openai/20250331_090914/harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v3.c
  - Version 4: results/openai/20250331_090914/harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v4.c
  - Size evolution: Initial 93 lines → Final 99 lines (+6 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250331_090914/verification/core_http_client.c:HTTPClient_AddRangeHeader/v1_results.txt
  - results/openai/20250331_090914/verification/core_http_client.c:HTTPClient_AddRangeHeader/v1_report.md
  - results/openai/20250331_090914/verification/core_http_client.c:HTTPClient_AddRangeHeader/v2_results.txt
  - results/openai/20250331_090914/verification/core_http_client.c:HTTPClient_AddRangeHeader/v2_report.md

### Function: HTTPClient_InitializeRequestHeaders (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.

#### Unit Proof Metrics
- Total reachable lines: 171
- Total coverage: 79.53%
- Function reachable lines: 85
- Function coverage: 80.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_090914/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1.c
  - Version 2: results/openai/20250331_090914/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2.c
  - Version 3: results/openai/20250331_090914/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v3.c
  - Version 4: results/openai/20250331_090914/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v4.c
  - Size evolution: Initial 198 lines → Final 171 lines (-27 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250331_090914/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1_results.txt
  - results/openai/20250331_090914/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1_report.md
  - results/openai/20250331_090914/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2_results.txt
  - results/openai/20250331_090914/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2_report.md
  - results/openai/20250331_090914/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v3_results.txt
  - results/openai/20250331_090914/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v3_report.md
  - results/openai/20250331_090914/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v4_results.txt
  - results/openai/20250331_090914/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v4_report.md