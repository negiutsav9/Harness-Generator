# CBMC Harness Generation Complete - Directory Mode - Openai

Total processing time: 2789.57 seconds
Processed 23 source files.
Analyzed 223 functions.
Identified 39 functions with memory or arithmetic operations.
Generated 38 verification harnesses.
Performed 159 harness refinements (average 3.31 per function).

## File Analysis

### core_http_client.c
Functions analyzed: 35
Functions verified: 35
Successful verifications: 8
Failed verifications: 27

### pattern
Functions analyzed: 4
Functions verified: 3
Successful verifications: 1
Failed verifications: 2

## Unit Proof Metrics Summary
Total reachable lines: 2418
Total coverage: 79.28%
Total reachable lines for harnessed functions only: 1204
Coverage of harnessed functions only: 78.74%
Number of reported errors: 0
Functions with full coverage: 0 of 38
Functions without errors: 24 of 38

### Note on Error Reporting:
- Errors are grouped by line number (one error per line)
- Errors about missing function bodies are excluded
- Loop unwinding assertions are excluded from error count

## Performance Metrics
Average harness generation time: 8.50 seconds
Average verification time: 15.56 seconds
Average evaluation time: 0.02 seconds

## Summary of Results

### Function: HTTPClient_AddHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 121
- Total coverage: 79.34%
- Function reachable lines: 60
- Function coverage: 80.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_AddHeader/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_AddHeader/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_AddHeader/v3.c
  - Size evolution: Initial 117 lines → Final 121 lines (+4 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_AddHeader/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_AddHeader/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_AddHeader/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_AddHeader/v2_report.md

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
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v3.c
  - Version 4: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v4.c
  - Size evolution: Initial 93 lines → Final 99 lines (+6 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_AddRangeHeader/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_AddRangeHeader/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_AddRangeHeader/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_AddRangeHeader/v2_report.md

### Function: HTTPClient_InitializeRequestHeaders (File: core_http_client.c)
Status: FAILED
Refinements: 6
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.

#### Unit Proof Metrics
- Total reachable lines: 255
- Total coverage: 80.00%
- Function reachable lines: 127
- Function coverage: 79.53%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v3.c
  - Version 4: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v4.c
  - Version 5: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v5.c
  - Size evolution: Initial 153 lines → Final 255 lines (+102 lines)
  - Refinement result: Some issues remain after 6 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v3_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v4_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v4_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v5_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v5_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v6_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v6_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v7_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v7_report.md

### Function: HTTPClient_ReadHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 5
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 187
- Total coverage: 79.68%
- Function reachable lines: 93
- Function coverage: 79.57%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_ReadHeader/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_ReadHeader/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_ReadHeader/v3.c
  - Version 4: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_ReadHeader/v4.c
  - Version 5: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_ReadHeader/v5.c
  - Version 6: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_ReadHeader/v6.c
  - Version 7: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_ReadHeader/v7.c
  - Version 8: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_ReadHeader/v8.c
  - Version 9: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_ReadHeader/v9.c
  - Size evolution: Initial 103 lines → Final 187 lines (+84 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_ReadHeader/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_ReadHeader/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_ReadHeader/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_ReadHeader/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_ReadHeader/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_ReadHeader/v3_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_ReadHeader/v4_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_ReadHeader/v4_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_ReadHeader/v5_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_ReadHeader/v5_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_ReadHeader/v6_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_ReadHeader/v6_report.md

### Function: HTTPClient_ReceiveAndParseHttpResponse (File: core_http_client.c)
Status: TIMEOUT
Refinements: 2
Message: CBMC verification timed out after 60 seconds.
Suggestions: The function may have complex paths requiring longer verification time. Consider simplifying.

#### Unit Proof Metrics
- Total reachable lines: N/A (timeout)
- Total coverage: N/A (timeout)
- Function reachable lines: N/A (timeout)
- Function coverage: N/A (timeout)
- Reported errors: N/A (timeout)

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v3.c
  - Size evolution: Initial 140 lines → Final 132 lines (-8 lines)
  - Refinement result: Some issues remain after 2 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v3_report.md

### Function: HTTPClient_Send (File: core_http_client.c)
Status: TIMEOUT
Refinements: 2
Message: CBMC verification timed out after 60 seconds.
Suggestions: The function may have complex paths requiring longer verification time. Consider simplifying.

#### Unit Proof Metrics
- Total reachable lines: N/A (timeout)
- Total coverage: N/A (timeout)
- Function reachable lines: N/A (timeout)
- Function coverage: N/A (timeout)
- Reported errors: N/A (timeout)

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_Send/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_Send/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_Send/v3.c
  - Size evolution: Initial 185 lines → Final 163 lines (-22 lines)
  - Refinement result: Some issues remain after 2 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_Send/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_Send/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_Send/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_Send/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_Send/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_Send/v3_report.md

### Function: HTTPClient_SendHttpData (File: core_http_client.c)
Status: TIMEOUT
Refinements: 3
Message: CBMC verification timed out after 60 seconds.
Suggestions: The function may have complex paths requiring longer verification time. Consider simplifying.

#### Unit Proof Metrics
- Total reachable lines: N/A (timeout)
- Total coverage: N/A (timeout)
- Function reachable lines: N/A (timeout)
- Function coverage: N/A (timeout)
- Reported errors: N/A (timeout)

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_SendHttpData/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_SendHttpData/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_SendHttpData/v3.c
  - Version 4: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_SendHttpData/v4.c
  - Size evolution: Initial 106 lines → Final 93 lines (-13 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_SendHttpData/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_SendHttpData/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_SendHttpData/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_SendHttpData/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_SendHttpData/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_SendHttpData/v3_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_SendHttpData/v4_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_SendHttpData/v4_report.md

### Function: HTTPClient_SendHttpHeaders (File: core_http_client.c)
Status: TIMEOUT
Refinements: 1
Message: CBMC verification timed out after 60 seconds.
Suggestions: The function may have complex paths requiring longer verification time. Consider simplifying.

#### Unit Proof Metrics
- Total reachable lines: N/A (timeout)
- Total coverage: N/A (timeout)
- Function reachable lines: N/A (timeout)
- Function coverage: N/A (timeout)
- Reported errors: N/A (timeout)

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v2.c
  - Size evolution: Initial 70 lines → Final 67 lines (-3 lines)
  - Refinement result: Some issues remain after 1 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v2_report.md

### Function: HTTPClient_strerror (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 90
- Total coverage: 80.00%
- Function reachable lines: 45
- Function coverage: 80.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_strerror/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:HTTPClient_strerror/v2.c
  - Size evolution: Initial 109 lines → Final 90 lines (-19 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_strerror/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_strerror/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_strerror/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:HTTPClient_strerror/v2_report.md

### Function: addContentLengthHeader (File: core_http_client.c)
Status: TIMEOUT
Refinements: 4
Message: CBMC verification timed out after 60 seconds.
Suggestions: The function may have complex paths requiring longer verification time. Consider simplifying.

#### Unit Proof Metrics
- Total reachable lines: N/A (timeout)
- Total coverage: N/A (timeout)
- Function reachable lines: N/A (timeout)
- Function coverage: N/A (timeout)
- Reported errors: N/A (timeout)

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:addContentLengthHeader/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:addContentLengthHeader/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/core_http_client.c:addContentLengthHeader/v3.c
  - Version 4: results/openai/20250331_120906/harnesses/core_http_client.c:addContentLengthHeader/v4.c
  - Version 5: results/openai/20250331_120906/harnesses/core_http_client.c:addContentLengthHeader/v5.c
  - Version 6: results/openai/20250331_120906/harnesses/core_http_client.c:addContentLengthHeader/v6.c
  - Size evolution: Initial 73 lines → Final 102 lines (+29 lines)
  - Refinement result: Some issues remain after 4 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:addContentLengthHeader/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:addContentLengthHeader/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:addContentLengthHeader/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:addContentLengthHeader/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:addContentLengthHeader/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:addContentLengthHeader/v3_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:addContentLengthHeader/v4_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:addContentLengthHeader/v4_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:addContentLengthHeader/v5_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:addContentLengthHeader/v5_report.md

### Function: addHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 2
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 114
- Total coverage: 79.82%
- Function reachable lines: 57
- Function coverage: 78.95%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:addHeader/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:addHeader/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/core_http_client.c:addHeader/v3.c
  - Version 4: results/openai/20250331_120906/harnesses/core_http_client.c:addHeader/v4.c
  - Size evolution: Initial 130 lines → Final 114 lines (-16 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:addHeader/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:addHeader/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:addHeader/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:addHeader/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:addHeader/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:addHeader/v3_report.md

### Function: addRangeHeader (File: core_http_client.c)
Status: TIMEOUT
Refinements: 2
Message: CBMC verification timed out after 60 seconds.
Suggestions: The function may have complex paths requiring longer verification time. Consider simplifying.

#### Unit Proof Metrics
- Total reachable lines: N/A (timeout)
- Total coverage: N/A (timeout)
- Function reachable lines: N/A (timeout)
- Function coverage: N/A (timeout)
- Reported errors: N/A (timeout)

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:addRangeHeader/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:addRangeHeader/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/core_http_client.c:addRangeHeader/v3.c
  - Version 4: results/openai/20250331_120906/harnesses/core_http_client.c:addRangeHeader/v4.c
  - Size evolution: Initial 95 lines → Final 105 lines (+10 lines)
  - Refinement result: Some issues remain after 2 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:addRangeHeader/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:addRangeHeader/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:addRangeHeader/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:addRangeHeader/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:addRangeHeader/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:addRangeHeader/v3_report.md

### Function: caseInsensitiveStringCmp (File: core_http_client.c)
Status: TIMEOUT
Refinements: 0
Message: CBMC verification timed out after 60 seconds.
Suggestions: The function may have complex paths requiring longer verification time. Consider simplifying.

#### Unit Proof Metrics
- Total reachable lines: N/A (timeout)
- Total coverage: N/A (timeout)
- Function reachable lines: N/A (timeout)
- Function coverage: N/A (timeout)
- Reported errors: N/A (timeout)

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:caseInsensitiveStringCmp/v1.c

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:caseInsensitiveStringCmp/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:caseInsensitiveStringCmp/v1_report.md

### Function: convertInt32ToAscii (File: core_http_client.c)
Status: TIMEOUT
Refinements: 0
Message: CBMC verification timed out after 60 seconds.
Suggestions: The function may have complex paths requiring longer verification time. Consider simplifying.

#### Unit Proof Metrics
- Total reachable lines: N/A (timeout)
- Total coverage: N/A (timeout)
- Function reachable lines: N/A (timeout)
- Function coverage: N/A (timeout)
- Reported errors: N/A (timeout)

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:convertInt32ToAscii/v1.c

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:convertInt32ToAscii/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:convertInt32ToAscii/v1_report.md

### Function: findHeaderFieldParserCallback (File: core_http_client.c)
Status: FAILED
Refinements: 6
Message: VERIFICATION FAILED: Command returned error code 6. Error: file results/openai/20250331_120906/verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 function llhttp_execute: function 'malloc' is not declared
file results/openai/20250331_120906/verificat...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 82
- Total coverage: 79.27%
- Function reachable lines: 41
- Function coverage: 78.05%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:findHeaderFieldParserCallback/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:findHeaderFieldParserCallback/v2.c
  - Size evolution: Initial 82 lines → Final 82 lines (0 lines)
  - Refinement result: Some issues remain after 6 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderFieldParserCallback/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderFieldParserCallback/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderFieldParserCallback/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderFieldParserCallback/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderFieldParserCallback/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderFieldParserCallback/v3_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderFieldParserCallback/v4_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderFieldParserCallback/v4_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderFieldParserCallback/v5_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderFieldParserCallback/v5_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderFieldParserCallback/v6_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderFieldParserCallback/v6_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderFieldParserCallback/v7_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderFieldParserCallback/v7_report.md

### Function: findHeaderInResponse (File: core_http_client.c)
Status: FAILED
Refinements: 6
Message: PREPROCESSING ERROR: GCC preprocessing failed - check for syntax errors
Suggestions: Fix syntax errors and ensure all macros are properly defined

#### Unit Proof Metrics
- Total reachable lines: N/A (preprocessing error)
- Total coverage: N/A (preprocessing error)
- Function reachable lines: N/A (preprocessing error)
- Function coverage: N/A (preprocessing error)
- Reported errors: N/A (preprocessing error)

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:findHeaderInResponse/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:findHeaderInResponse/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/core_http_client.c:findHeaderInResponse/v3.c
  - Version 4: results/openai/20250331_120906/harnesses/core_http_client.c:findHeaderInResponse/v4.c
  - Version 5: results/openai/20250331_120906/harnesses/core_http_client.c:findHeaderInResponse/v5.c
  - Version 6: results/openai/20250331_120906/harnesses/core_http_client.c:findHeaderInResponse/v6.c
  - Size evolution: Initial 105 lines → Final 114 lines (+9 lines)
  - Refinement result: Some issues remain after 6 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderInResponse/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderInResponse/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderInResponse/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderInResponse/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderInResponse/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderInResponse/v3_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderInResponse/v4_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderInResponse/v4_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderInResponse/v5_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderInResponse/v5_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderInResponse/v6_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderInResponse/v6_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderInResponse/v7_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderInResponse/v7_report.md

### Function: findHeaderOnHeaderCompleteCallback (File: core_http_client.c)
Status: FAILED
Refinements: 6
Message: VERIFICATION FAILED: Command returned error code 6. Error: file results/openai/20250331_120906/verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 function llhttp_execute: function 'malloc' is not declared
file results/openai/20250331_120906/verificat...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 56
- Total coverage: 78.57%
- Function reachable lines: 28
- Function coverage: 78.57%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:findHeaderOnHeaderCompleteCallback/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:findHeaderOnHeaderCompleteCallback/v2.c
  - Size evolution: Initial 56 lines → Final 56 lines (0 lines)
  - Refinement result: Some issues remain after 6 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v3_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v4_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v4_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v5_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v5_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v6_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v6_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v7_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v7_report.md

### Function: findHeaderValueParserCallback (File: core_http_client.c)
Status: FAILED
Refinements: 6
Message: VERIFICATION FAILED: Command returned error code 6. Error: file results/openai/20250331_120906/verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 function llhttp_execute: function 'malloc' is not declared
file results/openai/20250331_120906/verificat...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 103
- Total coverage: 79.61%
- Function reachable lines: 51
- Function coverage: 78.43%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:findHeaderValueParserCallback/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:findHeaderValueParserCallback/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/core_http_client.c:findHeaderValueParserCallback/v3.c
  - Size evolution: Initial 102 lines → Final 103 lines (+1 lines)
  - Refinement result: Some issues remain after 6 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderValueParserCallback/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderValueParserCallback/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderValueParserCallback/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderValueParserCallback/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderValueParserCallback/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderValueParserCallback/v3_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderValueParserCallback/v4_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderValueParserCallback/v4_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderValueParserCallback/v5_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderValueParserCallback/v5_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderValueParserCallback/v6_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderValueParserCallback/v6_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderValueParserCallback/v7_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:findHeaderValueParserCallback/v7_report.md

### Function: getFinalResponseStatus (File: core_http_client.c)
Status: FAILED
Refinements: 6
Message: PREPROCESSING ERROR: GCC preprocessing failed - check for syntax errors
Suggestions: Fix syntax errors and ensure all macros are properly defined

#### Unit Proof Metrics
- Total reachable lines: N/A (preprocessing error)
- Total coverage: N/A (preprocessing error)
- Function reachable lines: N/A (preprocessing error)
- Function coverage: N/A (preprocessing error)
- Reported errors: N/A (preprocessing error)

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:getFinalResponseStatus/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:getFinalResponseStatus/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/core_http_client.c:getFinalResponseStatus/v3.c
  - Version 4: results/openai/20250331_120906/harnesses/core_http_client.c:getFinalResponseStatus/v4.c
  - Size evolution: Initial 79 lines → Final 60 lines (-19 lines)
  - Refinement result: Some issues remain after 6 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:getFinalResponseStatus/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:getFinalResponseStatus/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:getFinalResponseStatus/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:getFinalResponseStatus/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:getFinalResponseStatus/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:getFinalResponseStatus/v3_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:getFinalResponseStatus/v4_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:getFinalResponseStatus/v4_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:getFinalResponseStatus/v5_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:getFinalResponseStatus/v5_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:getFinalResponseStatus/v6_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:getFinalResponseStatus/v6_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:getFinalResponseStatus/v7_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:getFinalResponseStatus/v7_report.md

### Function: httpHeaderStrncpy (File: core_http_client.c)
Status: TIMEOUT
Refinements: 0
Message: CBMC verification timed out after 60 seconds.
Suggestions: The function may have complex paths requiring longer verification time. Consider simplifying.

#### Unit Proof Metrics
- Total reachable lines: N/A (timeout)
- Total coverage: N/A (timeout)
- Function reachable lines: N/A (timeout)
- Function coverage: N/A (timeout)
- Reported errors: N/A (timeout)

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:httpHeaderStrncpy/v1.c

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:httpHeaderStrncpy/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpHeaderStrncpy/v1_report.md

### Function: httpParserOnBodyCallback (File: core_http_client.c)
Status: FAILED
Refinements: 6
Message: VERIFICATION FAILED: Command returned error code 6. Error: file results/openai/20250331_120906/verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 function llhttp_execute: function 'malloc' is not declared
file results/openai/20250331_120906/verificat...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 96
- Total coverage: 79.17%
- Function reachable lines: 48
- Function coverage: 79.17%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:httpParserOnBodyCallback/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:httpParserOnBodyCallback/v2.c
  - Size evolution: Initial 96 lines → Final 96 lines (0 lines)
  - Refinement result: Some issues remain after 6 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnBodyCallback/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnBodyCallback/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnBodyCallback/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnBodyCallback/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnBodyCallback/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnBodyCallback/v3_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnBodyCallback/v4_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnBodyCallback/v4_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnBodyCallback/v5_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnBodyCallback/v5_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnBodyCallback/v6_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnBodyCallback/v6_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnBodyCallback/v7_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnBodyCallback/v7_report.md

### Function: httpParserOnHeaderFieldCallback (File: core_http_client.c)
Status: FAILED
Refinements: 6
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.

#### Unit Proof Metrics
- Total reachable lines: 116
- Total coverage: 79.31%
- Function reachable lines: 58
- Function coverage: 79.31%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v3.c
  - Size evolution: Initial 77 lines → Final 116 lines (+39 lines)
  - Refinement result: Some issues remain after 6 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v3_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v4_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v4_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v5_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v5_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v6_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v6_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v7_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v7_report.md

### Function: httpParserOnHeaderValueCallback (File: core_http_client.c)
Status: FAILED
Refinements: 6
Message: VERIFICATION FAILED: Command returned error code 6. Error: file results/openai/20250331_120906/verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 function llhttp_execute: function 'malloc' is not declared
file results/openai/20250331_120906/verificat...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 63
- Total coverage: 79.37%
- Function reachable lines: 31
- Function coverage: 77.42%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:httpParserOnHeaderValueCallback/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:httpParserOnHeaderValueCallback/v2.c
  - Size evolution: Initial 63 lines → Final 63 lines (0 lines)
  - Refinement result: Some issues remain after 6 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderValueCallback/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderValueCallback/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderValueCallback/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderValueCallback/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderValueCallback/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderValueCallback/v3_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderValueCallback/v4_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderValueCallback/v4_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderValueCallback/v5_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderValueCallback/v5_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderValueCallback/v6_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderValueCallback/v6_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderValueCallback/v7_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeaderValueCallback/v7_report.md

### Function: httpParserOnHeadersCompleteCallback (File: core_http_client.c)
Status: FAILED
Refinements: 6
Message: VERIFICATION FAILED: Command returned error code 6. Error: file results/openai/20250331_120906/verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 function llhttp_execute: function 'malloc' is not declared
file results/openai/20250331_120906/verificat...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 122
- Total coverage: 79.51%
- Function reachable lines: 61
- Function coverage: 78.69%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v3.c
  - Version 4: results/openai/20250331_120906/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v4.c
  - Size evolution: Initial 138 lines → Final 122 lines (-16 lines)
  - Refinement result: Some issues remain after 6 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v3_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v4_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v4_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v5_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v5_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v6_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v6_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v7_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v7_report.md

### Function: httpParserOnMessageBeginCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 40
- Total coverage: 80.00%
- Function reachable lines: 20
- Function coverage: 80.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:httpParserOnMessageBeginCallback/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:httpParserOnMessageBeginCallback/v2.c
  - Size evolution: Initial 49 lines → Final 40 lines (-9 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnMessageBeginCallback/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnMessageBeginCallback/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnMessageBeginCallback/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnMessageBeginCallback/v2_report.md

### Function: httpParserOnMessageCompleteCallback (File: core_http_client.c)
Status: FAILED
Refinements: 6
Message: VERIFICATION FAILED: Command returned error code 6. Error: file results/openai/20250331_120906/verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 function llhttp_execute: function 'malloc' is not declared
file results/openai/20250331_120906/verificat...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 46
- Total coverage: 78.26%
- Function reachable lines: 23
- Function coverage: 78.26%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:httpParserOnMessageCompleteCallback/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:httpParserOnMessageCompleteCallback/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/core_http_client.c:httpParserOnMessageCompleteCallback/v3.c
  - Size evolution: Initial 46 lines → Final 46 lines (0 lines)
  - Refinement result: Some issues remain after 6 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v3_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v4_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v4_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v5_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v5_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v6_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v6_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v7_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v7_report.md

### Function: httpParserOnStatusCallback (File: core_http_client.c)
Status: FAILED
Refinements: 6
Message: VERIFICATION FAILED: Command returned error code 6. Error: file results/openai/20250331_120906/verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 function llhttp_execute: function 'malloc' is not declared
file results/openai/20250331_120906/verificat...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 77
- Total coverage: 79.22%
- Function reachable lines: 38
- Function coverage: 78.95%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:httpParserOnStatusCallback/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:httpParserOnStatusCallback/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/core_http_client.c:httpParserOnStatusCallback/v3.c
  - Size evolution: Initial 84 lines → Final 77 lines (-7 lines)
  - Refinement result: Some issues remain after 6 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnStatusCallback/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnStatusCallback/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnStatusCallback/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnStatusCallback/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnStatusCallback/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnStatusCallback/v3_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnStatusCallback/v4_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnStatusCallback/v4_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnStatusCallback/v5_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnStatusCallback/v5_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnStatusCallback/v6_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnStatusCallback/v6_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnStatusCallback/v7_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnStatusCallback/v7_report.md

### Function: httpParserOnStatusCompleteCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 2
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 52
- Total coverage: 78.85%
- Function reachable lines: 26
- Function coverage: 76.92%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:httpParserOnStatusCompleteCallback/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:httpParserOnStatusCompleteCallback/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/core_http_client.c:httpParserOnStatusCompleteCallback/v3.c
  - Size evolution: Initial 66 lines → Final 52 lines (-14 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v3_report.md

### Function: initializeParsingContextForFirstResponse (File: core_http_client.c)
Status: FAILED
Refinements: 6
Message: VERIFICATION FAILED: Command returned error code 6. Error: file results/openai/20250331_120906/verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 function llhttp_execute: function 'malloc' is not declared
file results/openai/20250331_120906/verificat...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 66
- Total coverage: 78.79%
- Function reachable lines: 33
- Function coverage: 78.79%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:initializeParsingContextForFirstResponse/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:initializeParsingContextForFirstResponse/v2.c
  - Size evolution: Initial 77 lines → Final 66 lines (-11 lines)
  - Refinement result: Some issues remain after 6 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:initializeParsingContextForFirstResponse/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:initializeParsingContextForFirstResponse/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:initializeParsingContextForFirstResponse/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:initializeParsingContextForFirstResponse/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:initializeParsingContextForFirstResponse/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:initializeParsingContextForFirstResponse/v3_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:initializeParsingContextForFirstResponse/v4_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:initializeParsingContextForFirstResponse/v4_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:initializeParsingContextForFirstResponse/v5_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:initializeParsingContextForFirstResponse/v5_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:initializeParsingContextForFirstResponse/v6_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:initializeParsingContextForFirstResponse/v6_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:initializeParsingContextForFirstResponse/v7_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:initializeParsingContextForFirstResponse/v7_report.md

### Function: parseHttpResponse (File: core_http_client.c)
Status: FAILED
Refinements: 6
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.

#### Unit Proof Metrics
- Total reachable lines: 182
- Total coverage: 79.67%
- Function reachable lines: 91
- Function coverage: 79.12%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:parseHttpResponse/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:parseHttpResponse/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/core_http_client.c:parseHttpResponse/v3.c
  - Version 4: results/openai/20250331_120906/harnesses/core_http_client.c:parseHttpResponse/v4.c
  - Size evolution: Initial 78 lines → Final 182 lines (+104 lines)
  - Refinement result: Some issues remain after 6 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:parseHttpResponse/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:parseHttpResponse/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:parseHttpResponse/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:parseHttpResponse/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:parseHttpResponse/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:parseHttpResponse/v3_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:parseHttpResponse/v4_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:parseHttpResponse/v4_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:parseHttpResponse/v5_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:parseHttpResponse/v5_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:parseHttpResponse/v6_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:parseHttpResponse/v6_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:parseHttpResponse/v7_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:parseHttpResponse/v7_report.md

### Function: processCompleteHeader (File: core_http_client.c)
Status: FAILED
Refinements: 6
Message: VERIFICATION FAILED: Command returned error code 6. Error: file results/openai/20250331_120906/verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 function llhttp_execute: function 'malloc' is not declared
file results/openai/20250331_120906/verificat...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 91
- Total coverage: 79.12%
- Function reachable lines: 45
- Function coverage: 80.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:processCompleteHeader/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:processCompleteHeader/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/core_http_client.c:processCompleteHeader/v3.c
  - Size evolution: Initial 91 lines → Final 92 lines (+1 lines)
  - Refinement result: Some issues remain after 6 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:processCompleteHeader/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:processCompleteHeader/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:processCompleteHeader/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:processCompleteHeader/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:processCompleteHeader/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:processCompleteHeader/v3_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:processCompleteHeader/v4_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:processCompleteHeader/v4_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:processCompleteHeader/v5_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:processCompleteHeader/v5_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:processCompleteHeader/v6_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:processCompleteHeader/v6_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:processCompleteHeader/v7_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:processCompleteHeader/v7_report.md

### Function: processLlhttpError (File: core_http_client.c)
Status: FAILED
Refinements: 6
Message: VERIFICATION FAILED: Command returned error code 6. Error: file results/openai/20250331_120906/verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 function llhttp_execute: function 'malloc' is not declared
file results/openai/20250331_120906/verificat...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 89
- Total coverage: 79.78%
- Function reachable lines: 44
- Function coverage: 79.55%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:processLlhttpError/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:processLlhttpError/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/core_http_client.c:processLlhttpError/v3.c
  - Version 4: results/openai/20250331_120906/harnesses/core_http_client.c:processLlhttpError/v4.c
  - Version 5: results/openai/20250331_120906/harnesses/core_http_client.c:processLlhttpError/v5.c
  - Size evolution: Initial 89 lines → Final 89 lines (0 lines)
  - Refinement result: Some issues remain after 6 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:processLlhttpError/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:processLlhttpError/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:processLlhttpError/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:processLlhttpError/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:processLlhttpError/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:processLlhttpError/v3_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:processLlhttpError/v4_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:processLlhttpError/v4_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:processLlhttpError/v5_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:processLlhttpError/v5_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:processLlhttpError/v6_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:processLlhttpError/v6_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:processLlhttpError/v7_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:processLlhttpError/v7_report.md

### Function: sendHttpBody (File: core_http_client.c)
Status: TIMEOUT
Refinements: 2
Message: CBMC verification timed out after 60 seconds.
Suggestions: The function may have complex paths requiring longer verification time. Consider simplifying.

#### Unit Proof Metrics
- Total reachable lines: N/A (timeout)
- Total coverage: N/A (timeout)
- Function reachable lines: N/A (timeout)
- Function coverage: N/A (timeout)
- Reported errors: N/A (timeout)

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:sendHttpBody/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:sendHttpBody/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/core_http_client.c:sendHttpBody/v3.c
  - Size evolution: Initial 61 lines → Final 52 lines (-9 lines)
  - Refinement result: Some issues remain after 2 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:sendHttpBody/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:sendHttpBody/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:sendHttpBody/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:sendHttpBody/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:sendHttpBody/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:sendHttpBody/v3_report.md

### Function: sendHttpRequest (File: core_http_client.c)
Status: TIMEOUT
Refinements: 1
Message: CBMC verification timed out after 60 seconds.
Suggestions: The function may have complex paths requiring longer verification time. Consider simplifying.

#### Unit Proof Metrics
- Total reachable lines: N/A (timeout)
- Total coverage: N/A (timeout)
- Function reachable lines: N/A (timeout)
- Function coverage: N/A (timeout)
- Reported errors: N/A (timeout)

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:sendHttpRequest/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:sendHttpRequest/v2.c
  - Size evolution: Initial 112 lines → Final 74 lines (-38 lines)
  - Refinement result: Some issues remain after 1 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:sendHttpRequest/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:sendHttpRequest/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:sendHttpRequest/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:sendHttpRequest/v2_report.md

### Function: writeRequestLine (File: core_http_client.c)
Status: SUCCESS
Refinements: 2
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 102
- Total coverage: 79.41%
- Function reachable lines: 51
- Function coverage: 78.43%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/core_http_client.c:writeRequestLine/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/core_http_client.c:writeRequestLine/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/core_http_client.c:writeRequestLine/v3.c
  - Size evolution: Initial 116 lines → Final 102 lines (-14 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250331_120906/verification/core_http_client.c:writeRequestLine/v1_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:writeRequestLine/v1_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:writeRequestLine/v2_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:writeRequestLine/v2_report.md
  - results/openai/20250331_120906/verification/core_http_client.c:writeRequestLine/v3_results.txt
  - results/openai/20250331_120906/verification/core_http_client.c:writeRequestLine/v3_report.md

### Function: core_http_client.c:for (File: pattern)
Status: TIMEOUT
Refinements: 0
Message: CBMC verification timed out after 60 seconds.
Suggestions: The function may have complex paths requiring longer verification time. Consider simplifying.

#### Unit Proof Metrics
- Total reachable lines: N/A (timeout)
- Total coverage: N/A (timeout)
- Function reachable lines: N/A (timeout)
- Function coverage: N/A (timeout)
- Reported errors: N/A (timeout)

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/pattern:core_http_client.c:for/v1.c

#### Verification Reports: 
  - results/openai/20250331_120906/verification/pattern:core_http_client.c:for/v1_results.txt
  - results/openai/20250331_120906/verification/pattern:core_http_client.c:for/v1_report.md

### Function: core_http_client.c:if (File: pattern)
Status: FAILED
Refinements: 6
Message: VERIFICATION FAILED: Command returned error code 6. Error: file results/openai/20250331_120906/verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 function llhttp_execute: function 'malloc' is not declared
file results/openai/20250331_120906/verificat...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 72
- Total coverage: 79.17%
- Function reachable lines: 36
- Function coverage: 77.78%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/pattern:core_http_client.c:if/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/pattern:core_http_client.c:if/v2.c
  - Size evolution: Initial 73 lines → Final 72 lines (-1 lines)
  - Refinement result: Some issues remain after 6 refinements

#### Verification Reports: 
  - results/openai/20250331_120906/verification/pattern:core_http_client.c:if/v1_results.txt
  - results/openai/20250331_120906/verification/pattern:core_http_client.c:if/v1_report.md
  - results/openai/20250331_120906/verification/pattern:core_http_client.c:if/v2_results.txt
  - results/openai/20250331_120906/verification/pattern:core_http_client.c:if/v2_report.md
  - results/openai/20250331_120906/verification/pattern:core_http_client.c:if/v3_results.txt
  - results/openai/20250331_120906/verification/pattern:core_http_client.c:if/v3_report.md
  - results/openai/20250331_120906/verification/pattern:core_http_client.c:if/v4_results.txt
  - results/openai/20250331_120906/verification/pattern:core_http_client.c:if/v4_report.md
  - results/openai/20250331_120906/verification/pattern:core_http_client.c:if/v5_results.txt
  - results/openai/20250331_120906/verification/pattern:core_http_client.c:if/v5_report.md
  - results/openai/20250331_120906/verification/pattern:core_http_client.c:if/v6_results.txt
  - results/openai/20250331_120906/verification/pattern:core_http_client.c:if/v6_report.md
  - results/openai/20250331_120906/verification/pattern:core_http_client.c:if/v7_results.txt
  - results/openai/20250331_120906/verification/pattern:core_http_client.c:if/v7_report.md

### Function: core_http_client.c:switch (File: pattern)
Status: SUCCESS
Refinements: 2
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 97
- Total coverage: 79.38%
- Function reachable lines: 48
- Function coverage: 79.17%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250331_120906/harnesses/pattern:core_http_client.c:switch/v1.c
  - Version 2: results/openai/20250331_120906/harnesses/pattern:core_http_client.c:switch/v2.c
  - Version 3: results/openai/20250331_120906/harnesses/pattern:core_http_client.c:switch/v3.c
  - Size evolution: Initial 117 lines → Final 97 lines (-20 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250331_120906/verification/pattern:core_http_client.c:switch/v1_results.txt
  - results/openai/20250331_120906/verification/pattern:core_http_client.c:switch/v1_report.md
  - results/openai/20250331_120906/verification/pattern:core_http_client.c:switch/v2_results.txt
  - results/openai/20250331_120906/verification/pattern:core_http_client.c:switch/v2_report.md
  - results/openai/20250331_120906/verification/pattern:core_http_client.c:switch/v3_results.txt
  - results/openai/20250331_120906/verification/pattern:core_http_client.c:switch/v3_report.md