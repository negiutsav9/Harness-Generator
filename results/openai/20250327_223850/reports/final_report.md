# CBMC Harness Generation Complete - Directory Mode - Openai

Total processing time: 840.94 seconds
Processed 9 source files.
Analyzed 179 functions.
Identified 35 functions with memory or arithmetic operations.
Generated 35 verification harnesses.
Performed 72 harness refinements (average 2.06 per function).

## File Analysis

### core_http_client.c
Functions analyzed: 35
Functions verified: 35
Successful verifications: 19
Failed verifications: 16

## Unit Proof Metrics Summary
Total reachable lines: 546758829
Total coverage: 223850.00%
Total reachable lines for harnessed functions only: 546758829
Coverage of harnessed functions only: 223850.00%
Number of reported errors: 0
Functions with full coverage: 0 of 35
Functions without errors: 33 of 35

### Note on Error Reporting:
- Errors are grouped by line number (one error per line)
- Errors about missing function bodies are excluded
- Loop unwinding assertions are excluded from error count

## Performance Metrics
Average harness generation time: 3.85 seconds
Average verification time: 4.23 seconds
Average evaluation time: 4.22 seconds

## Summary of Results

### Function: HTTPClient_AddHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 2
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_AddHeader/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_AddHeader/v2.c
  - Version 3: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_AddHeader/v3.c
  - Size evolution: Initial 59 lines → Final 92 lines (+33 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_AddHeader/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_AddHeader/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_AddHeader/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_AddHeader/v2_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_AddHeader/v3_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_AddHeader/v3_report.md

### Function: HTTPClient_AddRangeHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v2.c
  - Size evolution: Initial 57 lines → Final 107 lines (+50 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_AddRangeHeader/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_AddRangeHeader/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_AddRangeHeader/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_AddRangeHeader/v2_report.md

### Function: HTTPClient_InitializeRequestHeaders (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Command returned error code 6. Error: file results/openai/20250327_223850/verification/src/HTTPClient_InitializeRequestHeaders_harness.c line 95 function HTTPClient_InitializeRequestHeaders: failed to find symbol 'HTTP_REQUEST_NO_USER_AGE...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2.c
  - Version 3: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v3.c
  - Size evolution: Initial 66 lines → Final 169 lines (+103 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v3_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v3_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v4_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v4_report.md

### Function: HTTPClient_ReadHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_ReadHeader/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_ReadHeader/v2.c
  - Size evolution: Initial 68 lines → Final 100 lines (+32 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_ReadHeader/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_ReadHeader/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_ReadHeader/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_ReadHeader/v2_report.md

### Function: HTTPClient_ReceiveAndParseHttpResponse (File: core_http_client.c)
Status: SUCCESS
Refinements: 2
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v2.c
  - Version 3: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v3.c
  - Size evolution: Initial 74 lines → Final 88 lines (+14 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v2_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v3_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v3_report.md

### Function: HTTPClient_Send (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Command returned error code 6. Error: file results/openai/20250327_223850/verification/src/HTTPClient_Send_harness.c line 66 function main: failed to find symbol 'HTTP_MINIMUM_REQUEST_LINE_LENGTH'
CONVERSION ERROR
...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_Send/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_Send/v2.c
  - Version 3: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_Send/v3.c
  - Size evolution: Initial 72 lines → Final 119 lines (+47 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_Send/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_Send/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_Send/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_Send/v2_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_Send/v3_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_Send/v3_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_Send/v4_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_Send/v4_report.md

### Function: HTTPClient_SendHttpData (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_SendHttpData/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_SendHttpData/v2.c
  - Version 3: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_SendHttpData/v3.c
  - Size evolution: Initial 53 lines → Final 75 lines (+22 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_SendHttpData/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_SendHttpData/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_SendHttpData/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_SendHttpData/v2_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_SendHttpData/v3_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_SendHttpData/v3_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_SendHttpData/v4_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_SendHttpData/v4_report.md

### Function: HTTPClient_SendHttpHeaders (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v2.c
  - Size evolution: Initial 61 lines → Final 83 lines (+22 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v2_report.md

### Function: HTTPClient_strerror (File: core_http_client.c)
Status: SUCCESS
Refinements: 2
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_strerror/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_strerror/v2.c
  - Version 3: results/openai/20250327_223850/harnesses/core_http_client.c:HTTPClient_strerror/v3.c
  - Size evolution: Initial 38 lines → Final 121 lines (+83 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_strerror/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_strerror/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_strerror/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_strerror/v2_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_strerror/v3_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:HTTPClient_strerror/v3_report.md

### Function: addContentLengthHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:addContentLengthHeader/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:addContentLengthHeader/v2.c
  - Size evolution: Initial 47 lines → Final 81 lines (+34 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:addContentLengthHeader/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:addContentLengthHeader/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:addContentLengthHeader/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:addContentLengthHeader/v2_report.md

### Function: addHeader (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Command returned error code 6. Error: file results/openai/20250327_223850/verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 function llhttp_execute: function 'malloc' is not declared
file results/openai/20250327_223850/verificat...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:addHeader/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:addHeader/v2.c
  - Version 3: results/openai/20250327_223850/harnesses/core_http_client.c:addHeader/v3.c
  - Size evolution: Initial 60 lines → Final 81 lines (+21 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:addHeader/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:addHeader/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:addHeader/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:addHeader/v2_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:addHeader/v3_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:addHeader/v3_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:addHeader/v4_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:addHeader/v4_report.md

### Function: addRangeHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:addRangeHeader/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:addRangeHeader/v2.c
  - Size evolution: Initial 52 lines → Final 103 lines (+51 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:addRangeHeader/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:addRangeHeader/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:addRangeHeader/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:addRangeHeader/v2_report.md

### Function: caseInsensitiveStringCmp (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Command returned error code 6. Error: file results/openai/20250327_223850/verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 function llhttp_execute: function 'malloc' is not declared
file results/openai/20250327_223850/verificat...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:caseInsensitiveStringCmp/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:caseInsensitiveStringCmp/v2.c
  - Version 3: results/openai/20250327_223850/harnesses/core_http_client.c:caseInsensitiveStringCmp/v3.c
  - Size evolution: Initial 27 lines → Final 32 lines (+5 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:caseInsensitiveStringCmp/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:caseInsensitiveStringCmp/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:caseInsensitiveStringCmp/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:caseInsensitiveStringCmp/v2_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:caseInsensitiveStringCmp/v3_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:caseInsensitiveStringCmp/v3_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:caseInsensitiveStringCmp/v4_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:caseInsensitiveStringCmp/v4_report.md

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
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:convertInt32ToAscii/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:convertInt32ToAscii/v2.c
  - Version 3: results/openai/20250327_223850/harnesses/core_http_client.c:convertInt32ToAscii/v3.c
  - Size evolution: Initial 22 lines → Final 56 lines (+34 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:convertInt32ToAscii/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:convertInt32ToAscii/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:convertInt32ToAscii/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:convertInt32ToAscii/v2_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:convertInt32ToAscii/v3_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:convertInt32ToAscii/v3_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:convertInt32ToAscii/v4_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:convertInt32ToAscii/v4_report.md

### Function: findHeaderFieldParserCallback (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:findHeaderFieldParserCallback/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:findHeaderFieldParserCallback/v2.c
  - Version 3: results/openai/20250327_223850/harnesses/core_http_client.c:findHeaderFieldParserCallback/v3.c
  - Size evolution: Initial 54 lines → Final 63 lines (+9 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderFieldParserCallback/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderFieldParserCallback/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderFieldParserCallback/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderFieldParserCallback/v2_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderFieldParserCallback/v3_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderFieldParserCallback/v3_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderFieldParserCallback/v4_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderFieldParserCallback/v4_report.md

### Function: findHeaderInResponse (File: core_http_client.c)
Status: SUCCESS
Refinements: 2
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:findHeaderInResponse/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:findHeaderInResponse/v2.c
  - Version 3: results/openai/20250327_223850/harnesses/core_http_client.c:findHeaderInResponse/v3.c
  - Size evolution: Initial 52 lines → Final 75 lines (+23 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderInResponse/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderInResponse/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderInResponse/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderInResponse/v2_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderInResponse/v3_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderInResponse/v3_report.md

### Function: findHeaderOnHeaderCompleteCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:findHeaderOnHeaderCompleteCallback/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:findHeaderOnHeaderCompleteCallback/v2.c
  - Size evolution: Initial 33 lines → Final 45 lines (+12 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v2_report.md

### Function: findHeaderValueParserCallback (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Command returned error code 6. Error: file results/openai/20250327_223850/verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 function llhttp_execute: function 'malloc' is not declared
file results/openai/20250327_223850/verificat...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:findHeaderValueParserCallback/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:findHeaderValueParserCallback/v2.c
  - Version 3: results/openai/20250327_223850/harnesses/core_http_client.c:findHeaderValueParserCallback/v3.c
  - Size evolution: Initial 55 lines → Final 67 lines (+12 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderValueParserCallback/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderValueParserCallback/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderValueParserCallback/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderValueParserCallback/v2_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderValueParserCallback/v3_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderValueParserCallback/v3_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderValueParserCallback/v4_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:findHeaderValueParserCallback/v4_report.md

### Function: getFinalResponseStatus (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:getFinalResponseStatus/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:getFinalResponseStatus/v2.c
  - Size evolution: Initial 46 lines → Final 85 lines (+39 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:getFinalResponseStatus/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:getFinalResponseStatus/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:getFinalResponseStatus/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:getFinalResponseStatus/v2_report.md

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
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:httpHeaderStrncpy/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:httpHeaderStrncpy/v2.c
  - Version 3: results/openai/20250327_223850/harnesses/core_http_client.c:httpHeaderStrncpy/v3.c
  - Size evolution: Initial 40 lines → Final 47 lines (+7 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:httpHeaderStrncpy/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpHeaderStrncpy/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:httpHeaderStrncpy/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpHeaderStrncpy/v2_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:httpHeaderStrncpy/v3_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpHeaderStrncpy/v3_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:httpHeaderStrncpy/v4_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpHeaderStrncpy/v4_report.md

### Function: httpParserOnBodyCallback (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:httpParserOnBodyCallback/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:httpParserOnBodyCallback/v2.c
  - Version 3: results/openai/20250327_223850/harnesses/core_http_client.c:httpParserOnBodyCallback/v3.c
  - Size evolution: Initial 64 lines → Final 108 lines (+44 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnBodyCallback/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnBodyCallback/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnBodyCallback/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnBodyCallback/v2_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnBodyCallback/v3_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnBodyCallback/v3_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnBodyCallback/v4_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnBodyCallback/v4_report.md

### Function: httpParserOnHeaderFieldCallback (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v2.c
  - Version 3: results/openai/20250327_223850/harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v3.c
  - Size evolution: Initial 65 lines → Final 84 lines (+19 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v2_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v3_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v3_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v4_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v4_report.md

### Function: httpParserOnHeaderValueCallback (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:httpParserOnHeaderValueCallback/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:httpParserOnHeaderValueCallback/v2.c
  - Version 3: results/openai/20250327_223850/harnesses/core_http_client.c:httpParserOnHeaderValueCallback/v3.c
  - Size evolution: Initial 46 lines → Final 54 lines (+8 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeaderValueCallback/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeaderValueCallback/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeaderValueCallback/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeaderValueCallback/v2_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeaderValueCallback/v3_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeaderValueCallback/v3_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeaderValueCallback/v4_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeaderValueCallback/v4_report.md

### Function: httpParserOnHeadersCompleteCallback (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v2.c
  - Version 3: results/openai/20250327_223850/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v3.c
  - Size evolution: Initial 74 lines → Final 140 lines (+66 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v2_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v3_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v3_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v4_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v4_report.md

### Function: httpParserOnMessageBeginCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:httpParserOnMessageBeginCallback/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:httpParserOnMessageBeginCallback/v2.c
  - Size evolution: Initial 32 lines → Final 46 lines (+14 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnMessageBeginCallback/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnMessageBeginCallback/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnMessageBeginCallback/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnMessageBeginCallback/v2_report.md

### Function: httpParserOnMessageCompleteCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:httpParserOnMessageCompleteCallback/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:httpParserOnMessageCompleteCallback/v2.c
  - Size evolution: Initial 36 lines → Final 49 lines (+13 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v2_report.md

### Function: httpParserOnStatusCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:httpParserOnStatusCallback/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:httpParserOnStatusCallback/v2.c
  - Size evolution: Initial 54 lines → Final 87 lines (+33 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnStatusCallback/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnStatusCallback/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnStatusCallback/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnStatusCallback/v2_report.md

### Function: httpParserOnStatusCompleteCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:httpParserOnStatusCompleteCallback/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:httpParserOnStatusCompleteCallback/v2.c
  - Size evolution: Initial 50 lines → Final 72 lines (+22 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v2_report.md

### Function: initializeParsingContextForFirstResponse (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:initializeParsingContextForFirstResponse/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:initializeParsingContextForFirstResponse/v2.c
  - Version 3: results/openai/20250327_223850/harnesses/core_http_client.c:initializeParsingContextForFirstResponse/v3.c
  - Size evolution: Initial 59 lines → Final 68 lines (+9 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:initializeParsingContextForFirstResponse/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:initializeParsingContextForFirstResponse/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:initializeParsingContextForFirstResponse/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:initializeParsingContextForFirstResponse/v2_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:initializeParsingContextForFirstResponse/v3_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:initializeParsingContextForFirstResponse/v3_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:initializeParsingContextForFirstResponse/v4_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:initializeParsingContextForFirstResponse/v4_report.md

### Function: parseHttpResponse (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:parseHttpResponse/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:parseHttpResponse/v2.c
  - Size evolution: Initial 53 lines → Final 77 lines (+24 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:parseHttpResponse/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:parseHttpResponse/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:parseHttpResponse/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:parseHttpResponse/v2_report.md

### Function: processCompleteHeader (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:processCompleteHeader/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:processCompleteHeader/v2.c
  - Version 3: results/openai/20250327_223850/harnesses/core_http_client.c:processCompleteHeader/v3.c
  - Size evolution: Initial 53 lines → Final 103 lines (+50 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:processCompleteHeader/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:processCompleteHeader/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:processCompleteHeader/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:processCompleteHeader/v2_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:processCompleteHeader/v3_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:processCompleteHeader/v3_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:processCompleteHeader/v4_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:processCompleteHeader/v4_report.md

### Function: processLlhttpError (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Command returned error code 6. Error: file results/openai/20250327_223850/verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 function llhttp_execute: function 'malloc' is not declared
file results/openai/20250327_223850/verificat...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:processLlhttpError/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:processLlhttpError/v2.c
  - Version 3: results/openai/20250327_223850/harnesses/core_http_client.c:processLlhttpError/v3.c
  - Size evolution: Initial 42 lines → Final 48 lines (+6 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:processLlhttpError/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:processLlhttpError/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:processLlhttpError/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:processLlhttpError/v2_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:processLlhttpError/v3_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:processLlhttpError/v3_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:processLlhttpError/v4_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:processLlhttpError/v4_report.md

### Function: sendHttpBody (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:sendHttpBody/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:sendHttpBody/v2.c
  - Size evolution: Initial 41 lines → Final 83 lines (+42 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:sendHttpBody/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:sendHttpBody/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:sendHttpBody/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:sendHttpBody/v2_report.md

### Function: sendHttpRequest (File: core_http_client.c)
Status: SUCCESS
Refinements: 2
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:sendHttpRequest/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:sendHttpRequest/v2.c
  - Version 3: results/openai/20250327_223850/harnesses/core_http_client.c:sendHttpRequest/v3.c
  - Size evolution: Initial 74 lines → Final 112 lines (+38 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:sendHttpRequest/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:sendHttpRequest/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:sendHttpRequest/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:sendHttpRequest/v2_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:sendHttpRequest/v3_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:sendHttpRequest/v3_report.md

### Function: writeRequestLine (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 20250327
- Total coverage: 223850.00%
- Function reachable lines: 20250327
- Function coverage: 223850.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_223850/harnesses/core_http_client.c:writeRequestLine/v1.c
  - Version 2: results/openai/20250327_223850/harnesses/core_http_client.c:writeRequestLine/v2.c
  - Size evolution: Initial 86 lines → Final 144 lines (+58 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250327_223850/verification/core_http_client.c:writeRequestLine/v1_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:writeRequestLine/v1_report.md
  - results/openai/20250327_223850/verification/core_http_client.c:writeRequestLine/v2_results.txt
  - results/openai/20250327_223850/verification/core_http_client.c:writeRequestLine/v2_report.md