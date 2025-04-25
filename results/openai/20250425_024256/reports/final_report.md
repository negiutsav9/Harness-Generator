# CBMC Harness Generation Complete - Directory Mode - Openai

Total processing time: 4631.03 seconds
Processed 23 source files.
Analyzed 223 functions.
Identified 35 functions with memory or arithmetic operations.
Generated 34 verification harnesses.
Performed 146 harness refinements (average 4.29 per function).

## File Analysis

### core_http_client.c
Functions analyzed: 35
Functions verified: 34
Successful verifications: 26
Failed verifications: 8

## RAG Knowledge Base Statistics
Code functions stored: 332
Pattern templates: 16
Error patterns stored: 120
Successful solutions: 26

The RAG (Retrieval-Augmented Generation) knowledge base stores code functions, patterns, errors, and solutions to improve harness generation over time. Each run contributes to this knowledge base, helping future runs generate better harnesses with fewer iterations.

## Unit Proof Metrics Summary
Total reachable lines: 0
Total coverage: 0.00%
Total reachable lines for harnessed functions only: 0
Coverage of harnessed functions only: 0.00%
Number of reported errors: 0
Functions with full coverage: 25 of 34
Functions without errors: 33 of 34

### Note on Error Reporting:
- Errors are grouped by line number (one error per line)
- Errors about missing function bodies are excluded
- Loop unwinding assertions are excluded from error count

## Detailed Coverage Matrix by Function and Version

The table below shows detailed metrics for each function across different versions of the generated harnesses:

| Function | Version 1 | Version 2 | Version 3 | Version 4 | Version 5 | Version 6 | Version 7 | Version 8 | Version 9 | Version 10 | Version 11 |
| --- | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors |
| core_http_client.c:HTTPClient_AddHeader | 88.71% | 73.08% | 0 | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:HTTPClient_AddRangeHeader | 96.49% | 92.59% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:HTTPClient_InitializeRequestHeaders | 93.97% | 86.00% | 0 | 94.26% | 86.00% | 0 | 91.76% | 86.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:HTTPClient_ReadHeader | 98.04% | 93.33% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse | 0.00% | 0.00% | 0 | 96.39% | 93.88% | 0 | 96.39% | 93.88% | 0 | 96.47% | 93.88% | 0 | 96.47% | 93.88% | 0 | 43.06% | 18.37% | 0 | 51.14% | 18.37% | 0 | 51.14% | 18.37% | 0 | 50.00% | 18.37% | 0 | 51.72% | 18.37% | 0 | 94.44% | 91.84% | 0 |
| core_http_client.c:HTTPClient_Send | - | - | - | 0.00% | 0.00% | 0 | - | - | - | 0.00% | 0.00% | 0 | - | - | - | 0.00% | 0.00% | 0 | - | - | - | 0.00% | 0.00% | 0 | - | - | - | 0.00% | 0.00% | 0 | - | - | - |
| core_http_client.c:HTTPClient_SendHttpData | - | - | - | - | - | - | 0.00% | 0.00% | 0 | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:HTTPClient_SendHttpHeaders | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:HTTPClient_strerror | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:addContentLengthHeader | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 |
| core_http_client.c:addHeader | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:addRangeHeader | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 92.31% | 92.86% | 0 | 90.24% | 92.86% | 0 | 100.00% | 100.00% | 0 |
| core_http_client.c:caseInsensitiveStringCmp | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:convertInt32ToAscii | 86.67% | 81.82% | 0 | 87.10% | 81.82% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:findHeaderFieldParserCallback | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:findHeaderInResponse | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:findHeaderOnHeaderCompleteCallback | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 9.52% | 0.00% | 0 |
| core_http_client.c:findHeaderValueParserCallback | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:getFinalResponseStatus | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:httpHeaderStrncpy | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:httpParserOnBodyCallback | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:httpParserOnHeaderFieldCallback | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:httpParserOnHeaderValueCallback | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:httpParserOnHeadersCompleteCallback | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 |
| core_http_client.c:httpParserOnMessageBeginCallback | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:httpParserOnMessageCompleteCallback | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:httpParserOnStatusCallback | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:httpParserOnStatusCompleteCallback | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:initializeParsingContextForFirstResponse | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:parseHttpResponse | 91.84% | 85.19% | 0 | 92.00% | 85.19% | 0 | 92.00% | 85.19% | 0 | 92.00% | 85.19% | 0 | 92.00% | 85.19% | 0 | 92.00% | 85.19% | 0 | 91.67% | 85.19% | 0 | 90.24% | 85.19% | 0 | - | - | - | - | - | - | - | - | - |
| core_http_client.c:processCompleteHeader | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 100.00% | 100.00% | 0 |
| core_http_client.c:processLlhttpError | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| core_http_client.c:sendHttpBody | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 |

**Metrics Legend:**
- **Total %**: Percentage of all reachable lines that were covered during verification.
- **Func %**: Percentage of target function lines that were covered.
- **Errors**: Number of verification errors or failures detected.

## Performance Metrics
Average harness generation time: 10.18 seconds
Average verification time: 13.21 seconds
Average evaluation time: 0.00 seconds

## Coverage Analysis
Coverage report available at: coverage/coverage_report.html

## Summary of Results

### Function: HTTPClient_AddHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 2
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 73.08%
- Final coverage (v2): 100.00%
- Coverage improvement: 26.92%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_AddHeader/v1.c
  - Version 2: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_AddHeader/v2.c
  - Size evolution: Initial 84 lines → Final 198 lines (+114 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_AddHeader/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_AddHeader/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_AddHeader/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_AddHeader/v2_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_AddHeader/v3_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_AddHeader/v3_report.md

### Function: HTTPClient_AddRangeHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 92.59%

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v1.c

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_AddRangeHeader/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_AddRangeHeader/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_AddRangeHeader/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_AddRangeHeader/v2_report.md

### Function: HTTPClient_InitializeRequestHeaders (File: core_http_client.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 86.00%

#### Coverage Evolution
- Initial coverage (v1): 86.00%
- Final coverage (v3): 86.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1.c
  - Version 2: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2.c
  - Version 3: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v3.c
  - Size evolution: Initial 110 lines → Final 79 lines (-31 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v3_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v3_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v4_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v4_report.md

### Function: HTTPClient_ReadHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 93.33%
- Final coverage (v3): 100.00%
- Coverage improvement: 6.67%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_ReadHeader/v1.c
  - Version 2: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_ReadHeader/v2.c
  - Version 3: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_ReadHeader/v3.c
  - Size evolution: Initial 123 lines → Final 90 lines (-33 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReadHeader/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReadHeader/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReadHeader/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReadHeader/v2_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReadHeader/v3_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReadHeader/v3_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReadHeader/v4_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReadHeader/v4_report.md

### Function: HTTPClient_ReceiveAndParseHttpResponse (File: core_http_client.c)
Status: FAILED
Refinements: 10
Message: VERIFICATION FAILED: Memory leak detected
Suggestions: Ensure all allocated memory is freed in all execution paths

#### Coverage Metrics
- Function coverage: 91.84%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v11): 91.84%
- Coverage improvement: 91.84%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1.c
  - Version 2: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v2.c
  - Version 3: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v3.c
  - Version 4: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v4.c
  - Version 5: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v5.c
  - Version 6: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v6.c
  - Version 7: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v7.c
  - Version 8: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v8.c
  - Version 9: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v9.c
  - Version 10: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v10.c
  - Version 11: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v11.c
  - Size evolution: Initial 51 lines → Final 47 lines (-4 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v2_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v3_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v3_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v4_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v4_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v5_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v5_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v6_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v6_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v7_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v7_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v8_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v8_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v9_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v9_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v10_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v10_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v11_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v11_report.md

### Function: HTTPClient_Send (File: core_http_client.c)
Status: TIMEOUT
Refinements: 10
Message: CBMC verification timed out after 190 seconds.
Suggestions: The function may have complex paths requiring longer verification time. Consider using more selective file inclusion or increasing timeout.

#### Coverage Metrics
- Function coverage: 0.00%

#### Coverage Evolution
- Initial coverage (v2): 0.00%
- Final coverage (v10): 0.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_Send/v1.c
  - Version 2: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_Send/v2.c
  - Version 3: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_Send/v3.c
  - Version 4: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_Send/v4.c
  - Version 5: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_Send/v5.c
  - Version 6: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_Send/v6.c
  - Version 7: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_Send/v7.c
  - Version 8: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_Send/v8.c
  - Version 9: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_Send/v9.c
  - Version 10: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_Send/v10.c
  - Version 11: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_Send/v11.c
  - Size evolution: Initial 155 lines → Final 171 lines (+16 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_Send/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_Send/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_Send/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_Send/v2_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_Send/v3_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_Send/v3_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_Send/v4_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_Send/v4_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_Send/v5_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_Send/v5_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_Send/v6_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_Send/v6_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_Send/v7_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_Send/v7_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_Send/v8_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_Send/v8_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_Send/v9_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_Send/v9_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_Send/v10_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_Send/v10_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_Send/v11_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_Send/v11_report.md

### Function: HTTPClient_SendHttpData (File: core_http_client.c)
Status: SUCCESS
Refinements: 4
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v3): 0.00%
- Final coverage (v4): 100.00%
- Coverage improvement: 100.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_SendHttpData/v1.c
  - Version 2: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_SendHttpData/v2.c
  - Version 3: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_SendHttpData/v3.c
  - Version 4: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_SendHttpData/v4.c
  - Size evolution: Initial 55 lines → Final 85 lines (+30 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_SendHttpData/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_SendHttpData/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_SendHttpData/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_SendHttpData/v2_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_SendHttpData/v3_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_SendHttpData/v3_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_SendHttpData/v4_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_SendHttpData/v4_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_SendHttpData/v5_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_SendHttpData/v5_report.md

### Function: HTTPClient_SendHttpHeaders (File: core_http_client.c)
Status: SUCCESS
Refinements: 4
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 100.00%
- Final coverage (v4): 100.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v1.c
  - Version 2: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v2.c
  - Version 3: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v3.c
  - Version 4: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v4.c
  - Size evolution: Initial 45 lines → Final 70 lines (+25 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v2_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v3_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v3_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v4_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v4_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v5_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v5_report.md

### Function: HTTPClient_strerror (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:HTTPClient_strerror/v1.c

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_strerror/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_strerror/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_strerror/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:HTTPClient_strerror/v2_report.md

### Function: addContentLengthHeader (File: core_http_client.c)
Status: FAILED
Refinements: 10
Message: VERIFICATION FAILED: Memory leak detected
Suggestions: Ensure all allocated memory is freed in all execution paths

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 100.00%
- Final coverage (v11): 100.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:addContentLengthHeader/v1.c
  - Version 2: results/openai/20250425_024256/harnesses/core_http_client.c:addContentLengthHeader/v2.c
  - Version 3: results/openai/20250425_024256/harnesses/core_http_client.c:addContentLengthHeader/v3.c
  - Version 4: results/openai/20250425_024256/harnesses/core_http_client.c:addContentLengthHeader/v4.c
  - Version 5: results/openai/20250425_024256/harnesses/core_http_client.c:addContentLengthHeader/v5.c
  - Version 6: results/openai/20250425_024256/harnesses/core_http_client.c:addContentLengthHeader/v6.c
  - Version 7: results/openai/20250425_024256/harnesses/core_http_client.c:addContentLengthHeader/v7.c
  - Version 8: results/openai/20250425_024256/harnesses/core_http_client.c:addContentLengthHeader/v8.c
  - Version 9: results/openai/20250425_024256/harnesses/core_http_client.c:addContentLengthHeader/v9.c
  - Version 10: results/openai/20250425_024256/harnesses/core_http_client.c:addContentLengthHeader/v10.c
  - Version 11: results/openai/20250425_024256/harnesses/core_http_client.c:addContentLengthHeader/v11.c
  - Size evolution: Initial 22 lines → Final 27 lines (+5 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:addContentLengthHeader/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addContentLengthHeader/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:addContentLengthHeader/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addContentLengthHeader/v2_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:addContentLengthHeader/v3_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addContentLengthHeader/v3_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:addContentLengthHeader/v4_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addContentLengthHeader/v4_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:addContentLengthHeader/v5_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addContentLengthHeader/v5_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:addContentLengthHeader/v6_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addContentLengthHeader/v6_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:addContentLengthHeader/v7_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addContentLengthHeader/v7_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:addContentLengthHeader/v8_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addContentLengthHeader/v8_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:addContentLengthHeader/v9_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addContentLengthHeader/v9_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:addContentLengthHeader/v10_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addContentLengthHeader/v10_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:addContentLengthHeader/v11_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addContentLengthHeader/v11_report.md

### Function: addHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:addHeader/v1.c

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:addHeader/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addHeader/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:addHeader/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addHeader/v2_report.md

### Function: addRangeHeader (File: core_http_client.c)
Status: FAILED
Refinements: 10
Message: VERIFICATION FAILED: Null pointer dereference detected
Suggestions: Add null pointer checks before dereferencing pointers

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 100.00%
- Final coverage (v11): 100.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:addRangeHeader/v1.c
  - Version 2: results/openai/20250425_024256/harnesses/core_http_client.c:addRangeHeader/v2.c
  - Version 3: results/openai/20250425_024256/harnesses/core_http_client.c:addRangeHeader/v3.c
  - Version 4: results/openai/20250425_024256/harnesses/core_http_client.c:addRangeHeader/v4.c
  - Version 5: results/openai/20250425_024256/harnesses/core_http_client.c:addRangeHeader/v5.c
  - Version 6: results/openai/20250425_024256/harnesses/core_http_client.c:addRangeHeader/v6.c
  - Version 7: results/openai/20250425_024256/harnesses/core_http_client.c:addRangeHeader/v7.c
  - Version 8: results/openai/20250425_024256/harnesses/core_http_client.c:addRangeHeader/v8.c
  - Version 9: results/openai/20250425_024256/harnesses/core_http_client.c:addRangeHeader/v9.c
  - Version 10: results/openai/20250425_024256/harnesses/core_http_client.c:addRangeHeader/v10.c
  - Version 11: results/openai/20250425_024256/harnesses/core_http_client.c:addRangeHeader/v11.c
  - Size evolution: Initial 28 lines → Final 69 lines (+41 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:addRangeHeader/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addRangeHeader/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:addRangeHeader/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addRangeHeader/v2_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:addRangeHeader/v3_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addRangeHeader/v3_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:addRangeHeader/v4_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addRangeHeader/v4_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:addRangeHeader/v5_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addRangeHeader/v5_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:addRangeHeader/v6_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addRangeHeader/v6_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:addRangeHeader/v7_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addRangeHeader/v7_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:addRangeHeader/v8_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addRangeHeader/v8_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:addRangeHeader/v9_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addRangeHeader/v9_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:addRangeHeader/v10_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addRangeHeader/v10_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:addRangeHeader/v11_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:addRangeHeader/v11_report.md

### Function: caseInsensitiveStringCmp (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:caseInsensitiveStringCmp/v1.c

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:caseInsensitiveStringCmp/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:caseInsensitiveStringCmp/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:caseInsensitiveStringCmp/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:caseInsensitiveStringCmp/v2_report.md

### Function: convertInt32ToAscii (File: core_http_client.c)
Status: SUCCESS
Refinements: 2
Message: Verification successful

#### Coverage Metrics
- Function coverage: 81.82%

#### Coverage Evolution
- Initial coverage (v1): 81.82%
- Final coverage (v2): 81.82%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:convertInt32ToAscii/v1.c
  - Version 2: results/openai/20250425_024256/harnesses/core_http_client.c:convertInt32ToAscii/v2.c
  - Size evolution: Initial 32 lines → Final 42 lines (+10 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:convertInt32ToAscii/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:convertInt32ToAscii/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:convertInt32ToAscii/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:convertInt32ToAscii/v2_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:convertInt32ToAscii/v3_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:convertInt32ToAscii/v3_report.md

### Function: findHeaderFieldParserCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:findHeaderFieldParserCallback/v1.c

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderFieldParserCallback/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderFieldParserCallback/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderFieldParserCallback/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderFieldParserCallback/v2_report.md

### Function: findHeaderInResponse (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:findHeaderInResponse/v1.c

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderInResponse/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderInResponse/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderInResponse/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderInResponse/v2_report.md

### Function: findHeaderOnHeaderCompleteCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 10
Message: Verification successful

#### Coverage Metrics
- Function coverage: 0.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v11): 0.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:findHeaderOnHeaderCompleteCallback/v1.c
  - Version 2: results/openai/20250425_024256/harnesses/core_http_client.c:findHeaderOnHeaderCompleteCallback/v2.c
  - Version 3: results/openai/20250425_024256/harnesses/core_http_client.c:findHeaderOnHeaderCompleteCallback/v3.c
  - Version 4: results/openai/20250425_024256/harnesses/core_http_client.c:findHeaderOnHeaderCompleteCallback/v4.c
  - Version 5: results/openai/20250425_024256/harnesses/core_http_client.c:findHeaderOnHeaderCompleteCallback/v5.c
  - Version 6: results/openai/20250425_024256/harnesses/core_http_client.c:findHeaderOnHeaderCompleteCallback/v6.c
  - Version 7: results/openai/20250425_024256/harnesses/core_http_client.c:findHeaderOnHeaderCompleteCallback/v7.c
  - Version 8: results/openai/20250425_024256/harnesses/core_http_client.c:findHeaderOnHeaderCompleteCallback/v8.c
  - Version 9: results/openai/20250425_024256/harnesses/core_http_client.c:findHeaderOnHeaderCompleteCallback/v9.c
  - Version 10: results/openai/20250425_024256/harnesses/core_http_client.c:findHeaderOnHeaderCompleteCallback/v10.c
  - Version 11: results/openai/20250425_024256/harnesses/core_http_client.c:findHeaderOnHeaderCompleteCallback/v11.c
  - Size evolution: Initial 51 lines → Final 37 lines (-14 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v2_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v3_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v3_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v4_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v4_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v5_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v5_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v6_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v6_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v7_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v7_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v8_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v8_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v9_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v9_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v10_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v10_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v11_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v11_report.md

### Function: findHeaderValueParserCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:findHeaderValueParserCallback/v1.c

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderValueParserCallback/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderValueParserCallback/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderValueParserCallback/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:findHeaderValueParserCallback/v2_report.md

### Function: getFinalResponseStatus (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:getFinalResponseStatus/v1.c

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:getFinalResponseStatus/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:getFinalResponseStatus/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:getFinalResponseStatus/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:getFinalResponseStatus/v2_report.md

### Function: httpHeaderStrncpy (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:httpHeaderStrncpy/v1.c

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:httpHeaderStrncpy/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpHeaderStrncpy/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpHeaderStrncpy/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpHeaderStrncpy/v2_report.md

### Function: httpParserOnBodyCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnBodyCallback/v1.c

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnBodyCallback/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnBodyCallback/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnBodyCallback/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnBodyCallback/v2_report.md

### Function: httpParserOnHeaderFieldCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 100.00%
- Final coverage (v3): 100.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v1.c
  - Version 2: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v2.c
  - Version 3: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v3.c
  - Size evolution: Initial 85 lines → Final 85 lines (0 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v2_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v3_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v3_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v4_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v4_report.md

### Function: httpParserOnHeaderValueCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 100.00%
- Final coverage (v3): 100.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnHeaderValueCallback/v1.c
  - Version 2: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnHeaderValueCallback/v2.c
  - Version 3: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnHeaderValueCallback/v3.c
  - Size evolution: Initial 58 lines → Final 59 lines (+1 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeaderValueCallback/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeaderValueCallback/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeaderValueCallback/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeaderValueCallback/v2_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeaderValueCallback/v3_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeaderValueCallback/v3_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeaderValueCallback/v4_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeaderValueCallback/v4_report.md

### Function: httpParserOnHeadersCompleteCallback (File: core_http_client.c)
Status: FAILED
Refinements: 10
Message: VERIFICATION FAILED: Null pointer dereference detected
Suggestions: Add null pointer checks before dereferencing pointers

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 100.00%
- Final coverage (v11): 100.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v1.c
  - Version 2: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v2.c
  - Version 3: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v3.c
  - Version 4: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v4.c
  - Version 5: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v5.c
  - Version 6: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v6.c
  - Version 7: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v7.c
  - Version 8: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v8.c
  - Version 9: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v9.c
  - Version 10: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v10.c
  - Version 11: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v11.c
  - Size evolution: Initial 85 lines → Final 69 lines (-16 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v2_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v3_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v3_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v4_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v4_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v5_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v5_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v6_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v6_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v7_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v7_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v8_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v8_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v9_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v9_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v10_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v10_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v11_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v11_report.md

### Function: httpParserOnMessageBeginCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 100.00%
- Final coverage (v3): 100.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnMessageBeginCallback/v1.c
  - Version 2: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnMessageBeginCallback/v2.c
  - Version 3: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnMessageBeginCallback/v3.c
  - Size evolution: Initial 28 lines → Final 26 lines (-2 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnMessageBeginCallback/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnMessageBeginCallback/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnMessageBeginCallback/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnMessageBeginCallback/v2_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnMessageBeginCallback/v3_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnMessageBeginCallback/v3_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnMessageBeginCallback/v4_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnMessageBeginCallback/v4_report.md

### Function: httpParserOnMessageCompleteCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 100.00%
- Final coverage (v3): 100.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnMessageCompleteCallback/v1.c
  - Version 2: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnMessageCompleteCallback/v2.c
  - Version 3: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnMessageCompleteCallback/v3.c
  - Size evolution: Initial 26 lines → Final 25 lines (-1 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v2_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v3_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v3_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v4_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v4_report.md

### Function: httpParserOnStatusCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 100.00%
- Final coverage (v3): 100.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnStatusCallback/v1.c
  - Version 2: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnStatusCallback/v2.c
  - Version 3: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnStatusCallback/v3.c
  - Size evolution: Initial 53 lines → Final 61 lines (+8 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnStatusCallback/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnStatusCallback/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnStatusCallback/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnStatusCallback/v2_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnStatusCallback/v3_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnStatusCallback/v3_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnStatusCallback/v4_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnStatusCallback/v4_report.md

### Function: httpParserOnStatusCompleteCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:httpParserOnStatusCompleteCallback/v1.c

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v2_report.md

### Function: initializeParsingContextForFirstResponse (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:initializeParsingContextForFirstResponse/v1.c

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:initializeParsingContextForFirstResponse/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:initializeParsingContextForFirstResponse/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:initializeParsingContextForFirstResponse/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:initializeParsingContextForFirstResponse/v2_report.md

### Function: parseHttpResponse (File: core_http_client.c)
Status: SUCCESS
Refinements: 8
Message: Verification successful

#### Coverage Metrics
- Function coverage: 85.19%

#### Coverage Evolution
- Initial coverage (v1): 85.19%
- Final coverage (v8): 85.19%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:parseHttpResponse/v1.c
  - Version 2: results/openai/20250425_024256/harnesses/core_http_client.c:parseHttpResponse/v2.c
  - Version 3: results/openai/20250425_024256/harnesses/core_http_client.c:parseHttpResponse/v3.c
  - Version 4: results/openai/20250425_024256/harnesses/core_http_client.c:parseHttpResponse/v4.c
  - Version 5: results/openai/20250425_024256/harnesses/core_http_client.c:parseHttpResponse/v5.c
  - Version 6: results/openai/20250425_024256/harnesses/core_http_client.c:parseHttpResponse/v6.c
  - Size evolution: Initial 58 lines → Final 52 lines (-6 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:parseHttpResponse/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:parseHttpResponse/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:parseHttpResponse/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:parseHttpResponse/v2_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:parseHttpResponse/v3_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:parseHttpResponse/v3_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:parseHttpResponse/v4_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:parseHttpResponse/v4_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:parseHttpResponse/v5_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:parseHttpResponse/v5_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:parseHttpResponse/v6_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:parseHttpResponse/v6_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:parseHttpResponse/v7_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:parseHttpResponse/v7_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:parseHttpResponse/v8_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:parseHttpResponse/v8_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:parseHttpResponse/v9_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:parseHttpResponse/v9_report.md

### Function: processCompleteHeader (File: core_http_client.c)
Status: FAILED
Refinements: 10
Message: VERIFICATION FAILED: Memory leak detected
Suggestions: Ensure all allocated memory is freed in all execution paths

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v11): 100.00%
- Coverage improvement: 100.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:processCompleteHeader/v1.c
  - Version 2: results/openai/20250425_024256/harnesses/core_http_client.c:processCompleteHeader/v2.c
  - Version 3: results/openai/20250425_024256/harnesses/core_http_client.c:processCompleteHeader/v3.c
  - Version 4: results/openai/20250425_024256/harnesses/core_http_client.c:processCompleteHeader/v4.c
  - Version 5: results/openai/20250425_024256/harnesses/core_http_client.c:processCompleteHeader/v5.c
  - Version 6: results/openai/20250425_024256/harnesses/core_http_client.c:processCompleteHeader/v6.c
  - Version 7: results/openai/20250425_024256/harnesses/core_http_client.c:processCompleteHeader/v7.c
  - Version 8: results/openai/20250425_024256/harnesses/core_http_client.c:processCompleteHeader/v8.c
  - Version 9: results/openai/20250425_024256/harnesses/core_http_client.c:processCompleteHeader/v9.c
  - Version 10: results/openai/20250425_024256/harnesses/core_http_client.c:processCompleteHeader/v10.c
  - Version 11: results/openai/20250425_024256/harnesses/core_http_client.c:processCompleteHeader/v11.c
  - Size evolution: Initial 103 lines → Final 103 lines (0 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:processCompleteHeader/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:processCompleteHeader/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:processCompleteHeader/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:processCompleteHeader/v2_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:processCompleteHeader/v3_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:processCompleteHeader/v3_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:processCompleteHeader/v4_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:processCompleteHeader/v4_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:processCompleteHeader/v5_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:processCompleteHeader/v5_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:processCompleteHeader/v6_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:processCompleteHeader/v6_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:processCompleteHeader/v7_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:processCompleteHeader/v7_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:processCompleteHeader/v8_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:processCompleteHeader/v8_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:processCompleteHeader/v9_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:processCompleteHeader/v9_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:processCompleteHeader/v10_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:processCompleteHeader/v10_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:processCompleteHeader/v11_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:processCompleteHeader/v11_report.md

### Function: processLlhttpError (File: core_http_client.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 100.00%
- Final coverage (v3): 100.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:processLlhttpError/v1.c
  - Version 2: results/openai/20250425_024256/harnesses/core_http_client.c:processLlhttpError/v2.c
  - Version 3: results/openai/20250425_024256/harnesses/core_http_client.c:processLlhttpError/v3.c
  - Size evolution: Initial 21 lines → Final 24 lines (+3 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:processLlhttpError/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:processLlhttpError/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:processLlhttpError/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:processLlhttpError/v2_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:processLlhttpError/v3_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:processLlhttpError/v3_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:processLlhttpError/v4_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:processLlhttpError/v4_report.md

### Function: sendHttpBody (File: core_http_client.c)
Status: FAILED
Refinements: 10
Message: VERIFICATION FAILED: Unspecified verification error
Suggestions: Review the full verification output for details

#### Coverage Metrics
- Function coverage: 0.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v11): 0.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:sendHttpBody/v1.c
  - Version 2: results/openai/20250425_024256/harnesses/core_http_client.c:sendHttpBody/v2.c
  - Version 3: results/openai/20250425_024256/harnesses/core_http_client.c:sendHttpBody/v3.c
  - Version 4: results/openai/20250425_024256/harnesses/core_http_client.c:sendHttpBody/v4.c
  - Version 5: results/openai/20250425_024256/harnesses/core_http_client.c:sendHttpBody/v5.c
  - Version 6: results/openai/20250425_024256/harnesses/core_http_client.c:sendHttpBody/v6.c
  - Version 7: results/openai/20250425_024256/harnesses/core_http_client.c:sendHttpBody/v7.c
  - Version 8: results/openai/20250425_024256/harnesses/core_http_client.c:sendHttpBody/v8.c
  - Version 9: results/openai/20250425_024256/harnesses/core_http_client.c:sendHttpBody/v9.c
  - Version 10: results/openai/20250425_024256/harnesses/core_http_client.c:sendHttpBody/v10.c
  - Version 11: results/openai/20250425_024256/harnesses/core_http_client.c:sendHttpBody/v11.c
  - Size evolution: Initial 36 lines → Final 43 lines (+7 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpBody/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpBody/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpBody/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpBody/v2_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpBody/v3_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpBody/v3_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpBody/v4_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpBody/v4_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpBody/v5_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpBody/v5_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpBody/v6_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpBody/v6_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpBody/v7_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpBody/v7_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpBody/v8_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpBody/v8_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpBody/v9_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpBody/v9_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpBody/v10_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpBody/v10_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpBody/v11_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpBody/v11_report.md

### Function: sendHttpRequest (File: core_http_client.c)
Status: TIMEOUT
Refinements: 10
Message: CBMC verification timed out after 180 seconds.
Suggestions: The function may have complex paths requiring longer verification time. Consider using more selective file inclusion or increasing timeout.

#### Harness Evolution:
  - Version 1: results/openai/20250425_024256/harnesses/core_http_client.c:sendHttpRequest/v1.c
  - Version 2: results/openai/20250425_024256/harnesses/core_http_client.c:sendHttpRequest/v2.c
  - Version 3: results/openai/20250425_024256/harnesses/core_http_client.c:sendHttpRequest/v3.c
  - Version 4: results/openai/20250425_024256/harnesses/core_http_client.c:sendHttpRequest/v4.c
  - Version 5: results/openai/20250425_024256/harnesses/core_http_client.c:sendHttpRequest/v5.c
  - Version 6: results/openai/20250425_024256/harnesses/core_http_client.c:sendHttpRequest/v6.c
  - Version 7: results/openai/20250425_024256/harnesses/core_http_client.c:sendHttpRequest/v7.c
  - Version 8: results/openai/20250425_024256/harnesses/core_http_client.c:sendHttpRequest/v8.c
  - Version 9: results/openai/20250425_024256/harnesses/core_http_client.c:sendHttpRequest/v9.c
  - Version 10: results/openai/20250425_024256/harnesses/core_http_client.c:sendHttpRequest/v10.c
  - Size evolution: Initial 85 lines → Final 68 lines (-17 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpRequest/v1_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpRequest/v1_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpRequest/v2_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpRequest/v2_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpRequest/v3_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpRequest/v3_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpRequest/v4_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpRequest/v4_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpRequest/v5_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpRequest/v5_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpRequest/v6_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpRequest/v6_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpRequest/v7_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpRequest/v7_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpRequest/v8_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpRequest/v8_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpRequest/v9_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpRequest/v9_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpRequest/v10_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpRequest/v10_report.md
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpRequest/v11_results.txt
  - results/openai/20250425_024256/verification/core_http_client.c:sendHttpRequest/v11_report.md