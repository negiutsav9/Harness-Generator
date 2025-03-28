# CBMC Harness Generation Complete - Directory Mode - Openai

Total processing time: 298.23 seconds
Processed 9 source files.
Analyzed 179 functions.
Identified 35 functions with memory or arithmetic operations.
Generated 35 verification harnesses.
Performed 21 harness refinements (average 0.60 per function).

## File Analysis

### core_http_client.c
Functions analyzed: 35
Functions verified: 35
Successful verifications: 28
Failed verifications: 7

## Unit Proof Metrics Summary
Total reachable lines: 0
Total coverage: 0.00%
Total reachable lines for harnessed functions only: 0
Coverage of harnessed functions only: 0.00%
Number of reported errors: 0
Functions with full coverage: 0 of 35
Functions without errors: 35 of 35

### Note on Error Reporting:
- Errors are grouped by line number (one error per line)
- Errors about missing function bodies are excluded
- Loop unwinding assertions are excluded from error count

## Performance Metrics
Average harness generation time: 3.35 seconds
Average verification time: 0.34 seconds
Average evaluation time: 1.08 seconds

## Summary of Results

### Function: HTTPClient_AddHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:HTTPClient_AddHeader/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_AddHeader/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_AddHeader/v1_report.md

### Function: HTTPClient_AddRangeHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_AddRangeHeader/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_AddRangeHeader/v1_report.md

### Function: HTTPClient_InitializeRequestHeaders (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1_report.md

### Function: HTTPClient_ReadHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:HTTPClient_ReadHeader/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_ReadHeader/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_ReadHeader/v1_report.md

### Function: HTTPClient_ReceiveAndParseHttpResponse (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1_report.md

### Function: HTTPClient_Send (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:HTTPClient_Send/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_Send/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_Send/v1_report.md

### Function: HTTPClient_SendHttpData (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: PARSING ERROR: 'http_client.h' file not found
Suggestions: Fix the parsing error in file results/openai/20250327_213135/verification/src/HTTPClient_SendHttpData_harness.c line 8: results/openai/20250327_213135/verification/src/HTTPClient_SendHttpData_harness.c:8:10.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:HTTPClient_SendHttpData/v1.c
  - Version 2: results/openai/20250327_213135/harnesses/core_http_client.c:HTTPClient_SendHttpData/v2.c
  - Version 3: results/openai/20250327_213135/harnesses/core_http_client.c:HTTPClient_SendHttpData/v3.c
  - Size evolution: Initial 43 lines → Final 51 lines (+8 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_SendHttpData/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_SendHttpData/v1_report.md
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_SendHttpData/v2_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_SendHttpData/v2_report.md
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_SendHttpData/v3_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_SendHttpData/v3_report.md
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_SendHttpData/v4_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_SendHttpData/v4_report.md

### Function: HTTPClient_SendHttpHeaders (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v1_report.md

### Function: HTTPClient_strerror (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:HTTPClient_strerror/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_strerror/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:HTTPClient_strerror/v1_report.md

### Function: addContentLengthHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:addContentLengthHeader/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:addContentLengthHeader/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:addContentLengthHeader/v1_report.md

### Function: addHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:addHeader/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:addHeader/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:addHeader/v1_report.md

### Function: addRangeHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:addRangeHeader/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:addRangeHeader/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:addRangeHeader/v1_report.md

### Function: caseInsensitiveStringCmp (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:caseInsensitiveStringCmp/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:caseInsensitiveStringCmp/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:caseInsensitiveStringCmp/v1_report.md

### Function: convertInt32ToAscii (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:convertInt32ToAscii/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:convertInt32ToAscii/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:convertInt32ToAscii/v1_report.md

### Function: findHeaderFieldParserCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:findHeaderFieldParserCallback/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:findHeaderFieldParserCallback/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:findHeaderFieldParserCallback/v1_report.md

### Function: findHeaderInResponse (File: core_http_client.c)
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
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:findHeaderInResponse/v1.c
  - Version 2: results/openai/20250327_213135/harnesses/core_http_client.c:findHeaderInResponse/v2.c
  - Version 3: results/openai/20250327_213135/harnesses/core_http_client.c:findHeaderInResponse/v3.c
  - Size evolution: Initial 71 lines → Final 93 lines (+22 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:findHeaderInResponse/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:findHeaderInResponse/v1_report.md
  - results/openai/20250327_213135/verification/core_http_client.c:findHeaderInResponse/v2_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:findHeaderInResponse/v2_report.md
  - results/openai/20250327_213135/verification/core_http_client.c:findHeaderInResponse/v3_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:findHeaderInResponse/v3_report.md
  - results/openai/20250327_213135/verification/core_http_client.c:findHeaderInResponse/v4_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:findHeaderInResponse/v4_report.md

### Function: findHeaderOnHeaderCompleteCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:findHeaderOnHeaderCompleteCallback/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v1_report.md

### Function: findHeaderValueParserCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:findHeaderValueParserCallback/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:findHeaderValueParserCallback/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:findHeaderValueParserCallback/v1_report.md

### Function: getFinalResponseStatus (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:getFinalResponseStatus/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:getFinalResponseStatus/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:getFinalResponseStatus/v1_report.md

### Function: httpHeaderStrncpy (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Command returned error code 6. Error: --cover is incompatible with --unwinding-assertions, so unwinding-assertions will be defaulted to false
file results/openai/20250327_213135/verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 ...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:httpHeaderStrncpy/v1.c
  - Version 2: results/openai/20250327_213135/harnesses/core_http_client.c:httpHeaderStrncpy/v2.c
  - Version 3: results/openai/20250327_213135/harnesses/core_http_client.c:httpHeaderStrncpy/v3.c
  - Size evolution: Initial 43 lines → Final 56 lines (+13 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:httpHeaderStrncpy/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:httpHeaderStrncpy/v1_report.md
  - results/openai/20250327_213135/verification/core_http_client.c:httpHeaderStrncpy/v2_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:httpHeaderStrncpy/v2_report.md
  - results/openai/20250327_213135/verification/core_http_client.c:httpHeaderStrncpy/v3_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:httpHeaderStrncpy/v3_report.md
  - results/openai/20250327_213135/verification/core_http_client.c:httpHeaderStrncpy/v4_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:httpHeaderStrncpy/v4_report.md

### Function: httpParserOnBodyCallback (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Command returned error code 6. Error: --cover is incompatible with --unwinding-assertions, so unwinding-assertions will be defaulted to false
file results/openai/20250327_213135/verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 ...
Suggestions: Check the CBMC command and harness for errors.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:httpParserOnBodyCallback/v1.c
  - Version 2: results/openai/20250327_213135/harnesses/core_http_client.c:httpParserOnBodyCallback/v2.c
  - Version 3: results/openai/20250327_213135/harnesses/core_http_client.c:httpParserOnBodyCallback/v3.c
  - Size evolution: Initial 69 lines → Final 72 lines (+3 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:httpParserOnBodyCallback/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:httpParserOnBodyCallback/v1_report.md
  - results/openai/20250327_213135/verification/core_http_client.c:httpParserOnBodyCallback/v2_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:httpParserOnBodyCallback/v2_report.md
  - results/openai/20250327_213135/verification/core_http_client.c:httpParserOnBodyCallback/v3_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:httpParserOnBodyCallback/v3_report.md
  - results/openai/20250327_213135/verification/core_http_client.c:httpParserOnBodyCallback/v4_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:httpParserOnBodyCallback/v4_report.md

### Function: httpParserOnHeaderFieldCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v1_report.md

### Function: httpParserOnHeaderValueCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:httpParserOnHeaderValueCallback/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:httpParserOnHeaderValueCallback/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:httpParserOnHeaderValueCallback/v1_report.md

### Function: httpParserOnHeadersCompleteCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v1_report.md

### Function: httpParserOnMessageBeginCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:httpParserOnMessageBeginCallback/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:httpParserOnMessageBeginCallback/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:httpParserOnMessageBeginCallback/v1_report.md

### Function: httpParserOnMessageCompleteCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:httpParserOnMessageCompleteCallback/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v1_report.md

### Function: httpParserOnStatusCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:httpParserOnStatusCallback/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:httpParserOnStatusCallback/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:httpParserOnStatusCallback/v1_report.md

### Function: httpParserOnStatusCompleteCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:httpParserOnStatusCompleteCallback/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v1_report.md

### Function: initializeParsingContextForFirstResponse (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:initializeParsingContextForFirstResponse/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:initializeParsingContextForFirstResponse/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:initializeParsingContextForFirstResponse/v1_report.md

### Function: parseHttpResponse (File: core_http_client.c)
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
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:parseHttpResponse/v1.c
  - Version 2: results/openai/20250327_213135/harnesses/core_http_client.c:parseHttpResponse/v2.c
  - Version 3: results/openai/20250327_213135/harnesses/core_http_client.c:parseHttpResponse/v3.c
  - Size evolution: Initial 56 lines → Final 80 lines (+24 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:parseHttpResponse/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:parseHttpResponse/v1_report.md
  - results/openai/20250327_213135/verification/core_http_client.c:parseHttpResponse/v2_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:parseHttpResponse/v2_report.md
  - results/openai/20250327_213135/verification/core_http_client.c:parseHttpResponse/v3_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:parseHttpResponse/v3_report.md
  - results/openai/20250327_213135/verification/core_http_client.c:parseHttpResponse/v4_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:parseHttpResponse/v4_report.md

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
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:processCompleteHeader/v1.c
  - Version 2: results/openai/20250327_213135/harnesses/core_http_client.c:processCompleteHeader/v2.c
  - Version 3: results/openai/20250327_213135/harnesses/core_http_client.c:processCompleteHeader/v3.c
  - Size evolution: Initial 61 lines → Final 78 lines (+17 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:processCompleteHeader/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:processCompleteHeader/v1_report.md
  - results/openai/20250327_213135/verification/core_http_client.c:processCompleteHeader/v2_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:processCompleteHeader/v2_report.md
  - results/openai/20250327_213135/verification/core_http_client.c:processCompleteHeader/v3_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:processCompleteHeader/v3_report.md
  - results/openai/20250327_213135/verification/core_http_client.c:processCompleteHeader/v4_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:processCompleteHeader/v4_report.md

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
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:processLlhttpError/v1.c
  - Version 2: results/openai/20250327_213135/harnesses/core_http_client.c:processLlhttpError/v2.c
  - Version 3: results/openai/20250327_213135/harnesses/core_http_client.c:processLlhttpError/v3.c
  - Size evolution: Initial 36 lines → Final 45 lines (+9 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:processLlhttpError/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:processLlhttpError/v1_report.md
  - results/openai/20250327_213135/verification/core_http_client.c:processLlhttpError/v2_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:processLlhttpError/v2_report.md
  - results/openai/20250327_213135/verification/core_http_client.c:processLlhttpError/v3_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:processLlhttpError/v3_report.md
  - results/openai/20250327_213135/verification/core_http_client.c:processLlhttpError/v4_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:processLlhttpError/v4_report.md

### Function: sendHttpBody (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:sendHttpBody/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:sendHttpBody/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:sendHttpBody/v1_report.md

### Function: sendHttpRequest (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:sendHttpRequest/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:sendHttpRequest/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:sendHttpRequest/v1_report.md

### Function: writeRequestLine (File: core_http_client.c)
Status: SUCCESS
Refinements: 0
Message: VERIFICATION SUCCESSFUL: No issues detected.

#### Unit Proof Metrics
- Total reachable lines: 0
- Total coverage: 0.00%
- Function reachable lines: 0
- Function coverage: 0.00%
- Reported errors: 0

#### Harness Evolution:
  - Version 1: results/openai/20250327_213135/harnesses/core_http_client.c:writeRequestLine/v1.c

#### Verification Reports: 
  - results/openai/20250327_213135/verification/core_http_client.c:writeRequestLine/v1_results.txt
  - results/openai/20250327_213135/verification/core_http_client.c:writeRequestLine/v1_report.md