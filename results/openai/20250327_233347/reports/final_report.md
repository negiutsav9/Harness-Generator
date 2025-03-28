# CBMC Harness Generation Complete - Directory Mode - Openai

Total processing time: 1597.33 seconds
Processed 9 source files.
Analyzed 179 functions.
Identified 35 functions with memory or arithmetic operations.
Generated 35 verification harnesses.
Performed 85 harness refinements (average 2.43 per function).

## File Analysis

### core_http_client.c
Functions analyzed: 35
Functions verified: 35
Successful verifications: 13
Failed verifications: 22

## Unit Proof Metrics Summary
Total reachable lines: 4636
Total coverage: 11.00%
Total reachable lines for harnessed functions only: 4002
Coverage of harnessed functions only: 0.00%
Number of reported errors: 0
Functions with full coverage: 0 of 35
Functions without errors: 29 of 35

### Note on Error Reporting:
- Errors are grouped by line number (one error per line)
- Errors about missing function bodies are excluded
- Loop unwinding assertions are excluded from error count

## Performance Metrics
Average harness generation time: 4.86 seconds
Average verification time: 11.10 seconds
Average evaluation time: 4.85 seconds

## Summary of Results

### Function: HTTPClient_AddHeader (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.

#### Unit Proof Metrics
- Total reachable lines: 219
- Total coverage: 14.16%
- Function reachable lines: 174
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_AddHeader/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_AddHeader/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_AddHeader/v3.c
  - Size evolution: Initial 66 lines → Final 85 lines (+19 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_AddHeader/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_AddHeader/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_AddHeader/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_AddHeader/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_AddHeader/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_AddHeader/v3_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_AddHeader/v4_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_AddHeader/v4_report.md

### Function: HTTPClient_AddRangeHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 2
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 207
- Total coverage: 12.56%
- Function reachable lines: 174
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v3.c
  - Size evolution: Initial 55 lines → Final 106 lines (+51 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_AddRangeHeader/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_AddRangeHeader/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_AddRangeHeader/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_AddRangeHeader/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_AddRangeHeader/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_AddRangeHeader/v3_report.md

### Function: HTTPClient_InitializeRequestHeaders (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.

#### Unit Proof Metrics
- Total reachable lines: 184
- Total coverage: 5.43%
- Function reachable lines: 174
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2.c
  - Size evolution: Initial 66 lines → Final 69 lines (+3 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v3_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v4_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v4_report.md

### Function: HTTPClient_ReadHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 2
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 235
- Total coverage: 23.83%
- Function reachable lines: 174
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_ReadHeader/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_ReadHeader/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_ReadHeader/v3.c
  - Size evolution: Initial 64 lines → Final 127 lines (+63 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_ReadHeader/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_ReadHeader/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_ReadHeader/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_ReadHeader/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_ReadHeader/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_ReadHeader/v3_report.md

### Function: HTTPClient_ReceiveAndParseHttpResponse (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.

#### Unit Proof Metrics
- Total reachable lines: 190
- Total coverage: 7.37%
- Function reachable lines: 174
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v3.c
  - Size evolution: Initial 66 lines → Final 89 lines (+23 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v3_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v4_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v4_report.md

### Function: HTTPClient_Send (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Command returned error code 6. Error: file results/openai/20250327_233347/verification/src/HTTPClient_Send_harness.c line 57 function main: function 'nondet_bool' is not declared
file results/openai/20250327_233347/verification/src/HTTPCl...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_Send/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_Send/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_Send/v3.c
  - Size evolution: Initial 74 lines → Final 126 lines (+52 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_Send/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_Send/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_Send/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_Send/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_Send/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_Send/v3_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_Send/v4_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_Send/v4_report.md

### Function: HTTPClient_SendHttpData (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Command returned error code 6. Error: file results/openai/20250327_233347/verification/src/HTTPClient_SendHttpData_harness.c line 55 function main: function 'nondet_int' is not declared
file results/openai/20250327_233347/verification/src...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_SendHttpData/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_SendHttpData/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_SendHttpData/v3.c
  - Size evolution: Initial 59 lines → Final 88 lines (+29 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_SendHttpData/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_SendHttpData/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_SendHttpData/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_SendHttpData/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_SendHttpData/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_SendHttpData/v3_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_SendHttpData/v4_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_SendHttpData/v4_report.md

### Function: HTTPClient_SendHttpHeaders (File: core_http_client.c)
Status: SUCCESS
Refinements: 2
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 207
- Total coverage: 15.94%
- Function reachable lines: 174
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v3.c
  - Size evolution: Initial 61 lines → Final 119 lines (+58 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v3_report.md

### Function: HTTPClient_strerror (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 221
- Total coverage: 16.74%
- Function reachable lines: 174
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_strerror/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:HTTPClient_strerror/v2.c
  - Size evolution: Initial 39 lines → Final 118 lines (+79 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_strerror/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_strerror/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_strerror/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:HTTPClient_strerror/v2_report.md

### Function: addContentLengthHeader (File: core_http_client.c)
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
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:addContentLengthHeader/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:addContentLengthHeader/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:addContentLengthHeader/v3.c
  - Size evolution: Initial 41 lines → Final 92 lines (+51 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:addContentLengthHeader/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:addContentLengthHeader/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:addContentLengthHeader/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:addContentLengthHeader/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:addContentLengthHeader/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:addContentLengthHeader/v3_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:addContentLengthHeader/v4_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:addContentLengthHeader/v4_report.md

### Function: addHeader (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Command returned error code 6. Error: file results/openai/20250327_233347/verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 function llhttp_execute: function 'malloc' is not declared
file results/openai/20250327_233347/verificat...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:addHeader/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:addHeader/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:addHeader/v3.c
  - Size evolution: Initial 61 lines → Final 84 lines (+23 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:addHeader/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:addHeader/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:addHeader/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:addHeader/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:addHeader/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:addHeader/v3_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:addHeader/v4_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:addHeader/v4_report.md

### Function: addRangeHeader (File: core_http_client.c)
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
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:addRangeHeader/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:addRangeHeader/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:addRangeHeader/v3.c
  - Size evolution: Initial 53 lines → Final 130 lines (+77 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:addRangeHeader/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:addRangeHeader/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:addRangeHeader/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:addRangeHeader/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:addRangeHeader/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:addRangeHeader/v3_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:addRangeHeader/v4_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:addRangeHeader/v4_report.md

### Function: caseInsensitiveStringCmp (File: core_http_client.c)
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
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:caseInsensitiveStringCmp/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:caseInsensitiveStringCmp/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:caseInsensitiveStringCmp/v3.c
  - Size evolution: Initial 28 lines → Final 61 lines (+33 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:caseInsensitiveStringCmp/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:caseInsensitiveStringCmp/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:caseInsensitiveStringCmp/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:caseInsensitiveStringCmp/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:caseInsensitiveStringCmp/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:caseInsensitiveStringCmp/v3_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:caseInsensitiveStringCmp/v4_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:caseInsensitiveStringCmp/v4_report.md

### Function: convertInt32ToAscii (File: core_http_client.c)
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
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:convertInt32ToAscii/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:convertInt32ToAscii/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:convertInt32ToAscii/v3.c
  - Size evolution: Initial 21 lines → Final 55 lines (+34 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:convertInt32ToAscii/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:convertInt32ToAscii/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:convertInt32ToAscii/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:convertInt32ToAscii/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:convertInt32ToAscii/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:convertInt32ToAscii/v3_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:convertInt32ToAscii/v4_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:convertInt32ToAscii/v4_report.md

### Function: findHeaderFieldParserCallback (File: core_http_client.c)
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
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:findHeaderFieldParserCallback/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:findHeaderFieldParserCallback/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:findHeaderFieldParserCallback/v3.c
  - Size evolution: Initial 56 lines → Final 87 lines (+31 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderFieldParserCallback/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderFieldParserCallback/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderFieldParserCallback/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderFieldParserCallback/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderFieldParserCallback/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderFieldParserCallback/v3_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderFieldParserCallback/v4_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderFieldParserCallback/v4_report.md

### Function: findHeaderInResponse (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Command returned error code 6. Error: file results/openai/20250327_233347/verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 function llhttp_execute: function 'malloc' is not declared
file results/openai/20250327_233347/verificat...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:findHeaderInResponse/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:findHeaderInResponse/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:findHeaderInResponse/v3.c
  - Size evolution: Initial 59 lines → Final 124 lines (+65 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderInResponse/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderInResponse/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderInResponse/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderInResponse/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderInResponse/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderInResponse/v3_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderInResponse/v4_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderInResponse/v4_report.md

### Function: findHeaderOnHeaderCompleteCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 184
- Total coverage: 5.43%
- Function reachable lines: 174
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:findHeaderOnHeaderCompleteCallback/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:findHeaderOnHeaderCompleteCallback/v2.c
  - Size evolution: Initial 37 lines → Final 55 lines (+18 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v2_report.md

### Function: findHeaderValueParserCallback (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.

#### Unit Proof Metrics
- Total reachable lines: 200
- Total coverage: 12.50%
- Function reachable lines: 174
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:findHeaderValueParserCallback/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:findHeaderValueParserCallback/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:findHeaderValueParserCallback/v3.c
  - Size evolution: Initial 60 lines → Final 70 lines (+10 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderValueParserCallback/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderValueParserCallback/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderValueParserCallback/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderValueParserCallback/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderValueParserCallback/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderValueParserCallback/v3_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderValueParserCallback/v4_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:findHeaderValueParserCallback/v4_report.md

### Function: getFinalResponseStatus (File: core_http_client.c)
Status: SUCCESS
Refinements: 2
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 201
- Total coverage: 8.96%
- Function reachable lines: 174
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:getFinalResponseStatus/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:getFinalResponseStatus/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:getFinalResponseStatus/v3.c
  - Size evolution: Initial 43 lines → Final 85 lines (+42 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:getFinalResponseStatus/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:getFinalResponseStatus/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:getFinalResponseStatus/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:getFinalResponseStatus/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:getFinalResponseStatus/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:getFinalResponseStatus/v3_report.md

### Function: httpHeaderStrncpy (File: core_http_client.c)
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
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:httpHeaderStrncpy/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:httpHeaderStrncpy/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:httpHeaderStrncpy/v3.c
  - Size evolution: Initial 43 lines → Final 55 lines (+12 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:httpHeaderStrncpy/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpHeaderStrncpy/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:httpHeaderStrncpy/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpHeaderStrncpy/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:httpHeaderStrncpy/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpHeaderStrncpy/v3_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:httpHeaderStrncpy/v4_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpHeaderStrncpy/v4_report.md

### Function: httpParserOnBodyCallback (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.

#### Unit Proof Metrics
- Total reachable lines: 189
- Total coverage: 5.82%
- Function reachable lines: 174
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:httpParserOnBodyCallback/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:httpParserOnBodyCallback/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:httpParserOnBodyCallback/v3.c
  - Size evolution: Initial 68 lines → Final 78 lines (+10 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnBodyCallback/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnBodyCallback/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnBodyCallback/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnBodyCallback/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnBodyCallback/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnBodyCallback/v3_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnBodyCallback/v4_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnBodyCallback/v4_report.md

### Function: httpParserOnHeaderFieldCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 2
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 221
- Total coverage: 16.29%
- Function reachable lines: 174
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v3.c
  - Size evolution: Initial 54 lines → Final 97 lines (+43 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v3_report.md

### Function: httpParserOnHeaderValueCallback (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.

#### Unit Proof Metrics
- Total reachable lines: 202
- Total coverage: 12.87%
- Function reachable lines: 174
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:httpParserOnHeaderValueCallback/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:httpParserOnHeaderValueCallback/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:httpParserOnHeaderValueCallback/v3.c
  - Size evolution: Initial 52 lines → Final 92 lines (+40 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnHeaderValueCallback/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnHeaderValueCallback/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnHeaderValueCallback/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnHeaderValueCallback/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnHeaderValueCallback/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnHeaderValueCallback/v3_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnHeaderValueCallback/v4_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnHeaderValueCallback/v4_report.md

### Function: httpParserOnHeadersCompleteCallback (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.

#### Unit Proof Metrics
- Total reachable lines: 192
- Total coverage: 6.77%
- Function reachable lines: 174
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v3.c
  - Size evolution: Initial 80 lines → Final 97 lines (+17 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v3_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v4_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v4_report.md

### Function: httpParserOnMessageBeginCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 191
- Total coverage: 8.90%
- Function reachable lines: 174
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:httpParserOnMessageBeginCallback/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:httpParserOnMessageBeginCallback/v2.c
  - Size evolution: Initial 36 lines → Final 49 lines (+13 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnMessageBeginCallback/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnMessageBeginCallback/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnMessageBeginCallback/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnMessageBeginCallback/v2_report.md

### Function: httpParserOnMessageCompleteCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 192
- Total coverage: 9.38%
- Function reachable lines: 174
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:httpParserOnMessageCompleteCallback/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:httpParserOnMessageCompleteCallback/v2.c
  - Size evolution: Initial 36 lines → Final 51 lines (+15 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v2_report.md

### Function: httpParserOnStatusCallback (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.

#### Unit Proof Metrics
- Total reachable lines: 190
- Total coverage: 6.32%
- Function reachable lines: 174
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:httpParserOnStatusCallback/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:httpParserOnStatusCallback/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:httpParserOnStatusCallback/v3.c
  - Size evolution: Initial 54 lines → Final 66 lines (+12 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnStatusCallback/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnStatusCallback/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnStatusCallback/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnStatusCallback/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnStatusCallback/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnStatusCallback/v3_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnStatusCallback/v4_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnStatusCallback/v4_report.md

### Function: httpParserOnStatusCompleteCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 195
- Total coverage: 10.77%
- Function reachable lines: 174
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:httpParserOnStatusCompleteCallback/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:httpParserOnStatusCompleteCallback/v2.c
  - Size evolution: Initial 45 lines → Final 75 lines (+30 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v2_report.md

### Function: initializeParsingContextForFirstResponse (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 216
- Total coverage: 3.24%
- Function reachable lines: 174
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:initializeParsingContextForFirstResponse/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:initializeParsingContextForFirstResponse/v2.c
  - Size evolution: Initial 71 lines → Final 108 lines (+37 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:initializeParsingContextForFirstResponse/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:initializeParsingContextForFirstResponse/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:initializeParsingContextForFirstResponse/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:initializeParsingContextForFirstResponse/v2_report.md

### Function: parseHttpResponse (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 185
- Total coverage: 3.78%
- Function reachable lines: 174
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:parseHttpResponse/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:parseHttpResponse/v2.c
  - Size evolution: Initial 53 lines → Final 63 lines (+10 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:parseHttpResponse/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:parseHttpResponse/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:parseHttpResponse/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:parseHttpResponse/v2_report.md

### Function: processCompleteHeader (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: PARSING ERROR: Could not parse the harness.
Suggestions: Check for missing include files or syntax errors.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:processCompleteHeader/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:processCompleteHeader/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:processCompleteHeader/v3.c
  - Size evolution: Initial 60 lines → Final 92 lines (+32 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:processCompleteHeader/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:processCompleteHeader/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:processCompleteHeader/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:processCompleteHeader/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:processCompleteHeader/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:processCompleteHeader/v3_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:processCompleteHeader/v4_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:processCompleteHeader/v4_report.md

### Function: processLlhttpError (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: PARSING ERROR: Could not parse the harness.
Suggestions: Check for missing include files or syntax errors.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:processLlhttpError/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:processLlhttpError/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:processLlhttpError/v3.c
  - Size evolution: Initial 25 lines → Final 39 lines (+14 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:processLlhttpError/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:processLlhttpError/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:processLlhttpError/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:processLlhttpError/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:processLlhttpError/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:processLlhttpError/v3_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:processLlhttpError/v4_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:processLlhttpError/v4_report.md

### Function: sendHttpBody (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.

#### Unit Proof Metrics
- Total reachable lines: 192
- Total coverage: 8.33%
- Function reachable lines: 174
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:sendHttpBody/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:sendHttpBody/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:sendHttpBody/v3.c
  - Size evolution: Initial 42 lines → Final 79 lines (+37 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:sendHttpBody/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:sendHttpBody/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:sendHttpBody/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:sendHttpBody/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:sendHttpBody/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:sendHttpBody/v3_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:sendHttpBody/v4_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:sendHttpBody/v4_report.md

### Function: sendHttpRequest (File: core_http_client.c)
Status: SUCCESS
Refinements: 2
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 210
- Total coverage: 16.67%
- Function reachable lines: 174
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:sendHttpRequest/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:sendHttpRequest/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:sendHttpRequest/v3.c
  - Size evolution: Initial 73 lines → Final 122 lines (+49 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:sendHttpRequest/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:sendHttpRequest/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:sendHttpRequest/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:sendHttpRequest/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:sendHttpRequest/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:sendHttpRequest/v3_report.md

### Function: writeRequestLine (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.

#### Unit Proof Metrics
- Total reachable lines: 213
- Total coverage: 18.31%
- Function reachable lines: 174
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_233347/harnesses/core_http_client.c:writeRequestLine/v1.c
  - Version 2: results/openai/20250327_233347/harnesses/core_http_client.c:writeRequestLine/v2.c
  - Version 3: results/openai/20250327_233347/harnesses/core_http_client.c:writeRequestLine/v3.c
  - Size evolution: Initial 64 lines → Final 152 lines (+88 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_233347/verification/core_http_client.c:writeRequestLine/v1_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:writeRequestLine/v1_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:writeRequestLine/v2_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:writeRequestLine/v2_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:writeRequestLine/v3_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:writeRequestLine/v3_report.md
  - results/openai/20250327_233347/verification/core_http_client.c:writeRequestLine/v4_results.txt
  - results/openai/20250327_233347/verification/core_http_client.c:writeRequestLine/v4_report.md