# CBMC Harness Generation Complete - Directory Mode

Total processing time: 1539.36 seconds
Processed 9 source files.
Analyzed 179 functions.
Identified 35 functions with memory or arithmetic operations.
Generated 35 verification harnesses.
Performed 80 harness refinements (average 2.29 per function).

## File Analysis

### core_http_client.c
Functions analyzed: 35
Functions verified: 35
Successful verifications: 13
Failed verifications: 22

## Performance Metrics
Average harness generation time: 5.69 seconds
Average verification time: 8.91 seconds
Average evaluation time: 5.18 seconds

## Summary of Results

### Function: HTTPClient_AddHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:HTTPClient_AddHeader/v1.c
  - Version 2: harnesses/core_http_client.c:HTTPClient_AddHeader/v2.c
  - Size evolution: Initial 63 lines → Final 114 lines (+51 lines)
  - Refinement result: Successfully addressed all verification issues
Verification Reports: 
  - verification/core_http_client.c:HTTPClient_AddHeader/v1_results.txt
  - verification/core_http_client.c:HTTPClient_AddHeader/v1_report.md
  - verification/core_http_client.c:HTTPClient_AddHeader/v2_results.txt
  - verification/core_http_client.c:HTTPClient_AddHeader/v2_report.md

### Function: HTTPClient_AddRangeHeader (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v1.c
  - Version 2: harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v2.c
  - Version 3: harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v3.c
  - Size evolution: Initial 57 lines → Final 72 lines (+15 lines)
  - Refinement result: Some issues remain after 3 refinements
Verification Reports: 
  - verification/core_http_client.c:HTTPClient_AddRangeHeader/v1_results.txt
  - verification/core_http_client.c:HTTPClient_AddRangeHeader/v1_report.md
  - verification/core_http_client.c:HTTPClient_AddRangeHeader/v2_results.txt
  - verification/core_http_client.c:HTTPClient_AddRangeHeader/v2_report.md
  - verification/core_http_client.c:HTTPClient_AddRangeHeader/v3_results.txt
  - verification/core_http_client.c:HTTPClient_AddRangeHeader/v3_report.md
  - verification/core_http_client.c:HTTPClient_AddRangeHeader/v4_results.txt
  - verification/core_http_client.c:HTTPClient_AddRangeHeader/v4_report.md

### Function: HTTPClient_InitializeRequestHeaders (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1.c
  - Version 2: harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2.c
  - Size evolution: Initial 66 lines → Final 84 lines (+18 lines)
  - Refinement result: Successfully addressed all verification issues
Verification Reports: 
  - verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1_results.txt
  - verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1_report.md
  - verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2_results.txt
  - verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2_report.md

### Function: HTTPClient_ReadHeader (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:HTTPClient_ReadHeader/v1.c
  - Version 2: harnesses/core_http_client.c:HTTPClient_ReadHeader/v2.c
  - Version 3: harnesses/core_http_client.c:HTTPClient_ReadHeader/v3.c
  - Size evolution: Initial 53 lines → Final 73 lines (+20 lines)
  - Refinement result: Some issues remain after 3 refinements
Verification Reports: 
  - verification/core_http_client.c:HTTPClient_ReadHeader/v1_results.txt
  - verification/core_http_client.c:HTTPClient_ReadHeader/v1_report.md
  - verification/core_http_client.c:HTTPClient_ReadHeader/v2_results.txt
  - verification/core_http_client.c:HTTPClient_ReadHeader/v2_report.md
  - verification/core_http_client.c:HTTPClient_ReadHeader/v3_results.txt
  - verification/core_http_client.c:HTTPClient_ReadHeader/v3_report.md
  - verification/core_http_client.c:HTTPClient_ReadHeader/v4_results.txt
  - verification/core_http_client.c:HTTPClient_ReadHeader/v4_report.md

### Function: HTTPClient_ReceiveAndParseHttpResponse (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Command returned error code 10. Error: file verification/src/HTTPClient_ReceiveAndParseHttpResponse_harness.c line 85 function main: function 'nondet_size_t' is not declared
file verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 ...
Suggestions: Check the CBMC command and harness for errors.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1.c
  - Version 2: harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v2.c
  - Version 3: harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v3.c
  - Size evolution: Initial 80 lines → Final 105 lines (+25 lines)
  - Refinement result: Some issues remain after 3 refinements
Verification Reports: 
  - verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1_results.txt
  - verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1_report.md
  - verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v2_results.txt
  - verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v2_report.md
  - verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v3_results.txt
  - verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v3_report.md
  - verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v4_results.txt
  - verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v4_report.md

### Function: HTTPClient_Send (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Command returned error code 6. Error: file verification/src/HTTPClient_Send_harness.c line 66 function main: function 'nondet_bool' is not declared
file verification/src/HTTPClient_Send_harness.c line 73 function main: function 'nondet_si...
Suggestions: Check the CBMC command and harness for errors.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:HTTPClient_Send/v1.c
  - Version 2: harnesses/core_http_client.c:HTTPClient_Send/v2.c
  - Version 3: harnesses/core_http_client.c:HTTPClient_Send/v3.c
  - Size evolution: Initial 81 lines → Final 103 lines (+22 lines)
  - Refinement result: Some issues remain after 3 refinements
Verification Reports: 
  - verification/core_http_client.c:HTTPClient_Send/v1_results.txt
  - verification/core_http_client.c:HTTPClient_Send/v1_report.md
  - verification/core_http_client.c:HTTPClient_Send/v2_results.txt
  - verification/core_http_client.c:HTTPClient_Send/v2_report.md
  - verification/core_http_client.c:HTTPClient_Send/v3_results.txt
  - verification/core_http_client.c:HTTPClient_Send/v3_report.md
  - verification/core_http_client.c:HTTPClient_Send/v4_results.txt
  - verification/core_http_client.c:HTTPClient_Send/v4_report.md

### Function: HTTPClient_SendHttpData (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:HTTPClient_SendHttpData/v1.c
  - Version 2: harnesses/core_http_client.c:HTTPClient_SendHttpData/v2.c
  - Size evolution: Initial 56 lines → Final 66 lines (+10 lines)
  - Refinement result: Successfully addressed all verification issues
Verification Reports: 
  - verification/core_http_client.c:HTTPClient_SendHttpData/v1_results.txt
  - verification/core_http_client.c:HTTPClient_SendHttpData/v1_report.md
  - verification/core_http_client.c:HTTPClient_SendHttpData/v2_results.txt
  - verification/core_http_client.c:HTTPClient_SendHttpData/v2_report.md

### Function: HTTPClient_SendHttpHeaders (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Command returned error code 6. Error: file verification/src/HTTPClient_SendHttpHeaders_harness.c line 46 function HTTPClient_SendHttpHeaders: failed to find symbol 'HTTP_SEND_DISABLE_CONTENT_LENGTH_FLAG'
CONVERSION ERROR
...
Suggestions: Check the CBMC command and harness for errors.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v1.c
  - Version 2: harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v2.c
  - Version 3: harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v3.c
  - Size evolution: Initial 58 lines → Final 112 lines (+54 lines)
  - Refinement result: Some issues remain after 3 refinements
Verification Reports: 
  - verification/core_http_client.c:HTTPClient_SendHttpHeaders/v1_results.txt
  - verification/core_http_client.c:HTTPClient_SendHttpHeaders/v1_report.md
  - verification/core_http_client.c:HTTPClient_SendHttpHeaders/v2_results.txt
  - verification/core_http_client.c:HTTPClient_SendHttpHeaders/v2_report.md
  - verification/core_http_client.c:HTTPClient_SendHttpHeaders/v3_results.txt
  - verification/core_http_client.c:HTTPClient_SendHttpHeaders/v3_report.md
  - verification/core_http_client.c:HTTPClient_SendHttpHeaders/v4_results.txt
  - verification/core_http_client.c:HTTPClient_SendHttpHeaders/v4_report.md

### Function: HTTPClient_strerror (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:HTTPClient_strerror/v1.c
  - Version 2: harnesses/core_http_client.c:HTTPClient_strerror/v2.c
  - Size evolution: Initial 35 lines → Final 113 lines (+78 lines)
  - Refinement result: Successfully addressed all verification issues
Verification Reports: 
  - verification/core_http_client.c:HTTPClient_strerror/v1_results.txt
  - verification/core_http_client.c:HTTPClient_strerror/v1_report.md
  - verification/core_http_client.c:HTTPClient_strerror/v2_results.txt
  - verification/core_http_client.c:HTTPClient_strerror/v2_report.md

### Function: addContentLengthHeader (File: core_http_client.c)
Status: TIMEOUT
Refinements: 3
Message: CBMC verification timed out after 60 seconds.
Suggestions: The function may have complex paths requiring longer verification time. Consider simplifying.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:addContentLengthHeader/v1.c
  - Version 2: harnesses/core_http_client.c:addContentLengthHeader/v2.c
  - Version 3: harnesses/core_http_client.c:addContentLengthHeader/v3.c
  - Size evolution: Initial 40 lines → Final 87 lines (+47 lines)
  - Refinement result: Some issues remain after 3 refinements
Verification Reports: 
  - verification/core_http_client.c:addContentLengthHeader/v1_results.txt
  - verification/core_http_client.c:addContentLengthHeader/v1_report.md
  - verification/core_http_client.c:addContentLengthHeader/v2_results.txt
  - verification/core_http_client.c:addContentLengthHeader/v2_report.md
  - verification/core_http_client.c:addContentLengthHeader/v3_results.txt
  - verification/core_http_client.c:addContentLengthHeader/v3_report.md
  - verification/core_http_client.c:addContentLengthHeader/v4_results.txt
  - verification/core_http_client.c:addContentLengthHeader/v4_report.md

### Function: addHeader (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Command returned error code 6. Error: file verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 function llhttp_execute: function 'malloc' is not declared
file verification/src/addHeader_harness.c line 114 function main: function '...
Suggestions: Check the CBMC command and harness for errors.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:addHeader/v1.c
  - Version 2: harnesses/core_http_client.c:addHeader/v2.c
  - Version 3: harnesses/core_http_client.c:addHeader/v3.c
  - Size evolution: Initial 64 lines → Final 131 lines (+67 lines)
  - Refinement result: Some issues remain after 3 refinements
Verification Reports: 
  - verification/core_http_client.c:addHeader/v1_results.txt
  - verification/core_http_client.c:addHeader/v1_report.md
  - verification/core_http_client.c:addHeader/v2_results.txt
  - verification/core_http_client.c:addHeader/v2_report.md
  - verification/core_http_client.c:addHeader/v3_results.txt
  - verification/core_http_client.c:addHeader/v3_report.md
  - verification/core_http_client.c:addHeader/v4_results.txt
  - verification/core_http_client.c:addHeader/v4_report.md

### Function: addRangeHeader (File: core_http_client.c)
Status: TIMEOUT
Refinements: 3
Message: CBMC verification timed out after 60 seconds.
Suggestions: The function may have complex paths requiring longer verification time. Consider simplifying.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:addRangeHeader/v1.c
  - Version 2: harnesses/core_http_client.c:addRangeHeader/v2.c
  - Version 3: harnesses/core_http_client.c:addRangeHeader/v3.c
  - Size evolution: Initial 56 lines → Final 124 lines (+68 lines)
  - Refinement result: Some issues remain after 3 refinements
Verification Reports: 
  - verification/core_http_client.c:addRangeHeader/v1_results.txt
  - verification/core_http_client.c:addRangeHeader/v1_report.md
  - verification/core_http_client.c:addRangeHeader/v2_results.txt
  - verification/core_http_client.c:addRangeHeader/v2_report.md
  - verification/core_http_client.c:addRangeHeader/v3_results.txt
  - verification/core_http_client.c:addRangeHeader/v3_report.md
  - verification/core_http_client.c:addRangeHeader/v4_results.txt
  - verification/core_http_client.c:addRangeHeader/v4_report.md

### Function: caseInsensitiveStringCmp (File: core_http_client.c)
Status: TIMEOUT
Refinements: 3
Message: CBMC verification timed out after 60 seconds.
Suggestions: The function may have complex paths requiring longer verification time. Consider simplifying.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:caseInsensitiveStringCmp/v1.c
  - Version 2: harnesses/core_http_client.c:caseInsensitiveStringCmp/v2.c
  - Version 3: harnesses/core_http_client.c:caseInsensitiveStringCmp/v3.c
  - Size evolution: Initial 29 lines → Final 71 lines (+42 lines)
  - Refinement result: Some issues remain after 3 refinements
Verification Reports: 
  - verification/core_http_client.c:caseInsensitiveStringCmp/v1_results.txt
  - verification/core_http_client.c:caseInsensitiveStringCmp/v1_report.md
  - verification/core_http_client.c:caseInsensitiveStringCmp/v2_results.txt
  - verification/core_http_client.c:caseInsensitiveStringCmp/v2_report.md
  - verification/core_http_client.c:caseInsensitiveStringCmp/v3_results.txt
  - verification/core_http_client.c:caseInsensitiveStringCmp/v3_report.md
  - verification/core_http_client.c:caseInsensitiveStringCmp/v4_results.txt
  - verification/core_http_client.c:caseInsensitiveStringCmp/v4_report.md

### Function: convertInt32ToAscii (File: core_http_client.c)
Status: TIMEOUT
Refinements: 3
Message: CBMC verification timed out after 60 seconds.
Suggestions: The function may have complex paths requiring longer verification time. Consider simplifying.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:convertInt32ToAscii/v1.c
  - Version 2: harnesses/core_http_client.c:convertInt32ToAscii/v2.c
  - Version 3: harnesses/core_http_client.c:convertInt32ToAscii/v3.c
  - Size evolution: Initial 23 lines → Final 63 lines (+40 lines)
  - Refinement result: Some issues remain after 3 refinements
Verification Reports: 
  - verification/core_http_client.c:convertInt32ToAscii/v1_results.txt
  - verification/core_http_client.c:convertInt32ToAscii/v1_report.md
  - verification/core_http_client.c:convertInt32ToAscii/v2_results.txt
  - verification/core_http_client.c:convertInt32ToAscii/v2_report.md
  - verification/core_http_client.c:convertInt32ToAscii/v3_results.txt
  - verification/core_http_client.c:convertInt32ToAscii/v3_report.md
  - verification/core_http_client.c:convertInt32ToAscii/v4_results.txt
  - verification/core_http_client.c:convertInt32ToAscii/v4_report.md

### Function: findHeaderFieldParserCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:findHeaderFieldParserCallback/v1.c
  - Version 2: harnesses/core_http_client.c:findHeaderFieldParserCallback/v2.c
  - Size evolution: Initial 51 lines → Final 92 lines (+41 lines)
  - Refinement result: Successfully addressed all verification issues
Verification Reports: 
  - verification/core_http_client.c:findHeaderFieldParserCallback/v1_results.txt
  - verification/core_http_client.c:findHeaderFieldParserCallback/v1_report.md
  - verification/core_http_client.c:findHeaderFieldParserCallback/v2_results.txt
  - verification/core_http_client.c:findHeaderFieldParserCallback/v2_report.md

### Function: findHeaderInResponse (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:findHeaderInResponse/v1.c
  - Version 2: harnesses/core_http_client.c:findHeaderInResponse/v2.c
  - Version 3: harnesses/core_http_client.c:findHeaderInResponse/v3.c
  - Size evolution: Initial 79 lines → Final 99 lines (+20 lines)
  - Refinement result: Some issues remain after 3 refinements
Verification Reports: 
  - verification/core_http_client.c:findHeaderInResponse/v1_results.txt
  - verification/core_http_client.c:findHeaderInResponse/v1_report.md
  - verification/core_http_client.c:findHeaderInResponse/v2_results.txt
  - verification/core_http_client.c:findHeaderInResponse/v2_report.md
  - verification/core_http_client.c:findHeaderInResponse/v3_results.txt
  - verification/core_http_client.c:findHeaderInResponse/v3_report.md
  - verification/core_http_client.c:findHeaderInResponse/v4_results.txt
  - verification/core_http_client.c:findHeaderInResponse/v4_report.md

### Function: findHeaderOnHeaderCompleteCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:findHeaderOnHeaderCompleteCallback/v1.c
  - Version 2: harnesses/core_http_client.c:findHeaderOnHeaderCompleteCallback/v2.c
  - Size evolution: Initial 32 lines → Final 48 lines (+16 lines)
  - Refinement result: Successfully addressed all verification issues
Verification Reports: 
  - verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v1_results.txt
  - verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v1_report.md
  - verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v2_results.txt
  - verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v2_report.md

### Function: findHeaderValueParserCallback (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:findHeaderValueParserCallback/v1.c
  - Version 2: harnesses/core_http_client.c:findHeaderValueParserCallback/v2.c
  - Version 3: harnesses/core_http_client.c:findHeaderValueParserCallback/v3.c
  - Size evolution: Initial 55 lines → Final 112 lines (+57 lines)
  - Refinement result: Some issues remain after 3 refinements
Verification Reports: 
  - verification/core_http_client.c:findHeaderValueParserCallback/v1_results.txt
  - verification/core_http_client.c:findHeaderValueParserCallback/v1_report.md
  - verification/core_http_client.c:findHeaderValueParserCallback/v2_results.txt
  - verification/core_http_client.c:findHeaderValueParserCallback/v2_report.md
  - verification/core_http_client.c:findHeaderValueParserCallback/v3_results.txt
  - verification/core_http_client.c:findHeaderValueParserCallback/v3_report.md
  - verification/core_http_client.c:findHeaderValueParserCallback/v4_results.txt
  - verification/core_http_client.c:findHeaderValueParserCallback/v4_report.md

### Function: getFinalResponseStatus (File: core_http_client.c)
Status: SUCCESS
Refinements: 2
Message: VERIFICATION SUCCESSFUL: No issues detected.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:getFinalResponseStatus/v1.c
  - Version 2: harnesses/core_http_client.c:getFinalResponseStatus/v2.c
  - Version 3: harnesses/core_http_client.c:getFinalResponseStatus/v3.c
  - Size evolution: Initial 43 lines → Final 94 lines (+51 lines)
  - Refinement result: Successfully addressed all verification issues
Verification Reports: 
  - verification/core_http_client.c:getFinalResponseStatus/v1_results.txt
  - verification/core_http_client.c:getFinalResponseStatus/v1_report.md
  - verification/core_http_client.c:getFinalResponseStatus/v2_results.txt
  - verification/core_http_client.c:getFinalResponseStatus/v2_report.md
  - verification/core_http_client.c:getFinalResponseStatus/v3_results.txt
  - verification/core_http_client.c:getFinalResponseStatus/v3_report.md

### Function: httpHeaderStrncpy (File: core_http_client.c)
Status: TIMEOUT
Refinements: 3
Message: CBMC verification timed out after 60 seconds.
Suggestions: The function may have complex paths requiring longer verification time. Consider simplifying.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:httpHeaderStrncpy/v1.c
  - Version 2: harnesses/core_http_client.c:httpHeaderStrncpy/v2.c
  - Version 3: harnesses/core_http_client.c:httpHeaderStrncpy/v3.c
  - Size evolution: Initial 32 lines → Final 89 lines (+57 lines)
  - Refinement result: Some issues remain after 3 refinements
Verification Reports: 
  - verification/core_http_client.c:httpHeaderStrncpy/v1_results.txt
  - verification/core_http_client.c:httpHeaderStrncpy/v1_report.md
  - verification/core_http_client.c:httpHeaderStrncpy/v2_results.txt
  - verification/core_http_client.c:httpHeaderStrncpy/v2_report.md
  - verification/core_http_client.c:httpHeaderStrncpy/v3_results.txt
  - verification/core_http_client.c:httpHeaderStrncpy/v3_report.md
  - verification/core_http_client.c:httpHeaderStrncpy/v4_results.txt
  - verification/core_http_client.c:httpHeaderStrncpy/v4_report.md

### Function: httpParserOnBodyCallback (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Command returned error code 6. Error: file verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 function llhttp_execute: function 'malloc' is not declared
file verification/src/httpParserOnBodyCallback_harness.c line 74 function ma...
Suggestions: Check the CBMC command and harness for errors.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:httpParserOnBodyCallback/v1.c
  - Version 2: harnesses/core_http_client.c:httpParserOnBodyCallback/v2.c
  - Version 3: harnesses/core_http_client.c:httpParserOnBodyCallback/v3.c
  - Size evolution: Initial 55 lines → Final 79 lines (+24 lines)
  - Refinement result: Some issues remain after 3 refinements
Verification Reports: 
  - verification/core_http_client.c:httpParserOnBodyCallback/v1_results.txt
  - verification/core_http_client.c:httpParserOnBodyCallback/v1_report.md
  - verification/core_http_client.c:httpParserOnBodyCallback/v2_results.txt
  - verification/core_http_client.c:httpParserOnBodyCallback/v2_report.md
  - verification/core_http_client.c:httpParserOnBodyCallback/v3_results.txt
  - verification/core_http_client.c:httpParserOnBodyCallback/v3_report.md
  - verification/core_http_client.c:httpParserOnBodyCallback/v4_results.txt
  - verification/core_http_client.c:httpParserOnBodyCallback/v4_report.md

### Function: httpParserOnHeaderFieldCallback (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v1.c
  - Version 2: harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v2.c
  - Version 3: harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v3.c
  - Size evolution: Initial 64 lines → Final 73 lines (+9 lines)
  - Refinement result: Some issues remain after 3 refinements
Verification Reports: 
  - verification/core_http_client.c:httpParserOnHeaderFieldCallback/v1_results.txt
  - verification/core_http_client.c:httpParserOnHeaderFieldCallback/v1_report.md
  - verification/core_http_client.c:httpParserOnHeaderFieldCallback/v2_results.txt
  - verification/core_http_client.c:httpParserOnHeaderFieldCallback/v2_report.md
  - verification/core_http_client.c:httpParserOnHeaderFieldCallback/v3_results.txt
  - verification/core_http_client.c:httpParserOnHeaderFieldCallback/v3_report.md
  - verification/core_http_client.c:httpParserOnHeaderFieldCallback/v4_results.txt
  - verification/core_http_client.c:httpParserOnHeaderFieldCallback/v4_report.md

### Function: httpParserOnHeaderValueCallback (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:httpParserOnHeaderValueCallback/v1.c
  - Version 2: harnesses/core_http_client.c:httpParserOnHeaderValueCallback/v2.c
  - Version 3: harnesses/core_http_client.c:httpParserOnHeaderValueCallback/v3.c
  - Size evolution: Initial 46 lines → Final 88 lines (+42 lines)
  - Refinement result: Some issues remain after 3 refinements
Verification Reports: 
  - verification/core_http_client.c:httpParserOnHeaderValueCallback/v1_results.txt
  - verification/core_http_client.c:httpParserOnHeaderValueCallback/v1_report.md
  - verification/core_http_client.c:httpParserOnHeaderValueCallback/v2_results.txt
  - verification/core_http_client.c:httpParserOnHeaderValueCallback/v2_report.md
  - verification/core_http_client.c:httpParserOnHeaderValueCallback/v3_results.txt
  - verification/core_http_client.c:httpParserOnHeaderValueCallback/v3_report.md
  - verification/core_http_client.c:httpParserOnHeaderValueCallback/v4_results.txt
  - verification/core_http_client.c:httpParserOnHeaderValueCallback/v4_report.md

### Function: httpParserOnHeadersCompleteCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v1.c
  - Version 2: harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v2.c
  - Size evolution: Initial 67 lines → Final 83 lines (+16 lines)
  - Refinement result: Successfully addressed all verification issues
Verification Reports: 
  - verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v1_results.txt
  - verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v1_report.md
  - verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v2_results.txt
  - verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v2_report.md

### Function: httpParserOnMessageBeginCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:httpParserOnMessageBeginCallback/v1.c
  - Version 2: harnesses/core_http_client.c:httpParserOnMessageBeginCallback/v2.c
  - Size evolution: Initial 36 lines → Final 49 lines (+13 lines)
  - Refinement result: Successfully addressed all verification issues
Verification Reports: 
  - verification/core_http_client.c:httpParserOnMessageBeginCallback/v1_results.txt
  - verification/core_http_client.c:httpParserOnMessageBeginCallback/v1_report.md
  - verification/core_http_client.c:httpParserOnMessageBeginCallback/v2_results.txt
  - verification/core_http_client.c:httpParserOnMessageBeginCallback/v2_report.md

### Function: httpParserOnMessageCompleteCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:httpParserOnMessageCompleteCallback/v1.c
  - Version 2: harnesses/core_http_client.c:httpParserOnMessageCompleteCallback/v2.c
  - Size evolution: Initial 36 lines → Final 49 lines (+13 lines)
  - Refinement result: Successfully addressed all verification issues
Verification Reports: 
  - verification/core_http_client.c:httpParserOnMessageCompleteCallback/v1_results.txt
  - verification/core_http_client.c:httpParserOnMessageCompleteCallback/v1_report.md
  - verification/core_http_client.c:httpParserOnMessageCompleteCallback/v2_results.txt
  - verification/core_http_client.c:httpParserOnMessageCompleteCallback/v2_report.md

### Function: httpParserOnStatusCallback (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:httpParserOnStatusCallback/v1.c
  - Version 2: harnesses/core_http_client.c:httpParserOnStatusCallback/v2.c
  - Version 3: harnesses/core_http_client.c:httpParserOnStatusCallback/v3.c
  - Size evolution: Initial 58 lines → Final 104 lines (+46 lines)
  - Refinement result: Some issues remain after 3 refinements
Verification Reports: 
  - verification/core_http_client.c:httpParserOnStatusCallback/v1_results.txt
  - verification/core_http_client.c:httpParserOnStatusCallback/v1_report.md
  - verification/core_http_client.c:httpParserOnStatusCallback/v2_results.txt
  - verification/core_http_client.c:httpParserOnStatusCallback/v2_report.md
  - verification/core_http_client.c:httpParserOnStatusCallback/v3_results.txt
  - verification/core_http_client.c:httpParserOnStatusCallback/v3_report.md
  - verification/core_http_client.c:httpParserOnStatusCallback/v4_results.txt
  - verification/core_http_client.c:httpParserOnStatusCallback/v4_report.md

### Function: httpParserOnStatusCompleteCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:httpParserOnStatusCompleteCallback/v1.c
  - Version 2: harnesses/core_http_client.c:httpParserOnStatusCompleteCallback/v2.c
  - Size evolution: Initial 53 lines → Final 79 lines (+26 lines)
  - Refinement result: Successfully addressed all verification issues
Verification Reports: 
  - verification/core_http_client.c:httpParserOnStatusCompleteCallback/v1_results.txt
  - verification/core_http_client.c:httpParserOnStatusCompleteCallback/v1_report.md
  - verification/core_http_client.c:httpParserOnStatusCompleteCallback/v2_results.txt
  - verification/core_http_client.c:httpParserOnStatusCompleteCallback/v2_report.md

### Function: initializeParsingContextForFirstResponse (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Command returned error code 6. Error: file verification/stubs/HTTPClient_Send_llhttp_execute.c line 65 function llhttp_execute: function 'malloc' is not declared
file verification/sources/http_cbmc_state.c line 266 function allocateHttpRe...
Suggestions: Check the CBMC command and harness for errors.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:initializeParsingContextForFirstResponse/v1.c
  - Version 2: harnesses/core_http_client.c:initializeParsingContextForFirstResponse/v2.c
  - Version 3: harnesses/core_http_client.c:initializeParsingContextForFirstResponse/v3.c
  - Size evolution: Initial 48 lines → Final 83 lines (+35 lines)
  - Refinement result: Some issues remain after 3 refinements
Verification Reports: 
  - verification/core_http_client.c:initializeParsingContextForFirstResponse/v1_results.txt
  - verification/core_http_client.c:initializeParsingContextForFirstResponse/v1_report.md
  - verification/core_http_client.c:initializeParsingContextForFirstResponse/v2_results.txt
  - verification/core_http_client.c:initializeParsingContextForFirstResponse/v2_report.md
  - verification/core_http_client.c:initializeParsingContextForFirstResponse/v3_results.txt
  - verification/core_http_client.c:initializeParsingContextForFirstResponse/v3_report.md
  - verification/core_http_client.c:initializeParsingContextForFirstResponse/v4_results.txt
  - verification/core_http_client.c:initializeParsingContextForFirstResponse/v4_report.md

### Function: parseHttpResponse (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: PARSING ERROR: Could not parse the harness.
Suggestions: Check for missing include files or syntax errors.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:parseHttpResponse/v1.c
  - Version 2: harnesses/core_http_client.c:parseHttpResponse/v2.c
  - Version 3: harnesses/core_http_client.c:parseHttpResponse/v3.c
  - Size evolution: Initial 54 lines → Final 62 lines (+8 lines)
  - Refinement result: Some issues remain after 3 refinements
Verification Reports: 
  - verification/core_http_client.c:parseHttpResponse/v1_results.txt
  - verification/core_http_client.c:parseHttpResponse/v1_report.md
  - verification/core_http_client.c:parseHttpResponse/v2_results.txt
  - verification/core_http_client.c:parseHttpResponse/v2_report.md
  - verification/core_http_client.c:parseHttpResponse/v3_results.txt
  - verification/core_http_client.c:parseHttpResponse/v3_report.md
  - verification/core_http_client.c:parseHttpResponse/v4_results.txt
  - verification/core_http_client.c:parseHttpResponse/v4_report.md

### Function: processCompleteHeader (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:processCompleteHeader/v1.c
  - Version 2: harnesses/core_http_client.c:processCompleteHeader/v2.c
  - Version 3: harnesses/core_http_client.c:processCompleteHeader/v3.c
  - Size evolution: Initial 69 lines → Final 104 lines (+35 lines)
  - Refinement result: Some issues remain after 3 refinements
Verification Reports: 
  - verification/core_http_client.c:processCompleteHeader/v1_results.txt
  - verification/core_http_client.c:processCompleteHeader/v1_report.md
  - verification/core_http_client.c:processCompleteHeader/v2_results.txt
  - verification/core_http_client.c:processCompleteHeader/v2_report.md
  - verification/core_http_client.c:processCompleteHeader/v3_results.txt
  - verification/core_http_client.c:processCompleteHeader/v3_report.md
  - verification/core_http_client.c:processCompleteHeader/v4_results.txt
  - verification/core_http_client.c:processCompleteHeader/v4_report.md

### Function: processLlhttpError (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: PARSING ERROR: Could not parse the harness.
Suggestions: Check for missing include files or syntax errors.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:processLlhttpError/v1.c
  - Version 2: harnesses/core_http_client.c:processLlhttpError/v2.c
  - Version 3: harnesses/core_http_client.c:processLlhttpError/v3.c
  - Size evolution: Initial 27 lines → Final 35 lines (+8 lines)
  - Refinement result: Some issues remain after 3 refinements
Verification Reports: 
  - verification/core_http_client.c:processLlhttpError/v1_results.txt
  - verification/core_http_client.c:processLlhttpError/v1_report.md
  - verification/core_http_client.c:processLlhttpError/v2_results.txt
  - verification/core_http_client.c:processLlhttpError/v2_report.md
  - verification/core_http_client.c:processLlhttpError/v3_results.txt
  - verification/core_http_client.c:processLlhttpError/v3_report.md
  - verification/core_http_client.c:processLlhttpError/v4_results.txt
  - verification/core_http_client.c:processLlhttpError/v4_report.md

### Function: sendHttpBody (File: core_http_client.c)
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Null pointer dereference detected.
Suggestions: Add null pointer checks before dereferencing.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:sendHttpBody/v1.c
  - Version 2: harnesses/core_http_client.c:sendHttpBody/v2.c
  - Version 3: harnesses/core_http_client.c:sendHttpBody/v3.c
  - Size evolution: Initial 49 lines → Final 90 lines (+41 lines)
  - Refinement result: Some issues remain after 3 refinements
Verification Reports: 
  - verification/core_http_client.c:sendHttpBody/v1_results.txt
  - verification/core_http_client.c:sendHttpBody/v1_report.md
  - verification/core_http_client.c:sendHttpBody/v2_results.txt
  - verification/core_http_client.c:sendHttpBody/v2_report.md
  - verification/core_http_client.c:sendHttpBody/v3_results.txt
  - verification/core_http_client.c:sendHttpBody/v3_report.md
  - verification/core_http_client.c:sendHttpBody/v4_results.txt
  - verification/core_http_client.c:sendHttpBody/v4_report.md

### Function: sendHttpRequest (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:sendHttpRequest/v1.c
  - Version 2: harnesses/core_http_client.c:sendHttpRequest/v2.c
  - Size evolution: Initial 70 lines → Final 84 lines (+14 lines)
  - Refinement result: Successfully addressed all verification issues
Verification Reports: 
  - verification/core_http_client.c:sendHttpRequest/v1_results.txt
  - verification/core_http_client.c:sendHttpRequest/v1_report.md
  - verification/core_http_client.c:sendHttpRequest/v2_results.txt
  - verification/core_http_client.c:sendHttpRequest/v2_report.md

### Function: writeRequestLine (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: VERIFICATION SUCCESSFUL: No issues detected.
Harness Evolution:
  - Version 1: harnesses/core_http_client.c:writeRequestLine/v1.c
  - Version 2: harnesses/core_http_client.c:writeRequestLine/v2.c
  - Size evolution: Initial 61 lines → Final 124 lines (+63 lines)
  - Refinement result: Successfully addressed all verification issues
Verification Reports: 
  - verification/core_http_client.c:writeRequestLine/v1_results.txt
  - verification/core_http_client.c:writeRequestLine/v1_report.md
  - verification/core_http_client.c:writeRequestLine/v2_results.txt
  - verification/core_http_client.c:writeRequestLine/v2_report.md