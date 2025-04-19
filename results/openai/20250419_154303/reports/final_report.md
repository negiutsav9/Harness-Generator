# CBMC Harness Generation Complete - Directory Mode - Openai

Total processing time: 3306.65 seconds
Processed 23 source files.
Analyzed 223 functions.
Identified 35 functions with memory or arithmetic operations.
Generated 35 verification harnesses.
Performed 126 harness refinements (average 3.60 per function).

## File Analysis

### core_http_client.c
Functions analyzed: 35
Functions verified: 35
Successful verifications: 28
Failed verifications: 7

## RAG Knowledge Base Statistics
Code functions stored: 332
Pattern templates: 16
Error patterns stored: 98
Successful solutions: 28

The RAG (Retrieval-Augmented Generation) knowledge base stores code functions, patterns, errors, and solutions to improve harness generation over time. Each run contributes to this knowledge base, helping future runs generate better harnesses with fewer iterations.

## Unit Proof Metrics Summary
Total reachable lines: 0
Total coverage: 0.00%
Total reachable lines for harnessed functions only: 0
Coverage of harnessed functions only: 0.00%
Number of reported errors: 0
Functions with full coverage: 23 of 35
Functions without errors: 0 of 35

### Note on Error Reporting:
- Errors are grouped by line number (one error per line)
- Errors about missing function bodies are excluded
- Loop unwinding assertions are excluded from error count

## Detailed Coverage Matrix by Function and Version

The table below shows detailed metrics for each function across different versions of the generated harnesses:

| Function | Version 1 |||| Version 2 |||| Version 3 |||| Version 4 |||| Version 5 |||| Version 6 |||| Version 7 |||| Version 8 |||| Version 9 |||| Version 10 |||
| --- | Total % | Func % | Errors || Total % | Func % | Errors || Total % | Func % | Errors || Total % | Func % | Errors || Total % | Func % | Errors || Total % | Func % | Errors || Total % | Func % | Errors || Total % | Func % | Errors || Total % | Func % | Errors || Total % | Func % | Errors |
| core_http_client.c:HTTPClient_AddHeader | 100.00% | 100.00% | N/A || 93.90% | 80.77% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:HTTPClient_AddRangeHeader | 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:HTTPClient_InitializeRequestHeaders | 97.35% | 94.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:HTTPClient_ReadHeader | 97.80% | 93.33% | N/A || 97.92% | 93.33% | N/A || 97.96% | 93.33% | N/A || 97.96% | 93.33% | N/A || 97.59% | 93.33% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse | 94.81% | 91.84% | N/A || 95.00% | 91.84% | N/A || 94.87% | 91.84% | N/A || 94.59% | 91.84% | N/A || 95.56% | 91.84% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:HTTPClient_Send | - | - | - || 0.00% | 0.00% | N/A || 93.91% | 41.38% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:HTTPClient_SendHttpData | - | - | - || 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:HTTPClient_SendHttpHeaders | 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 98.99% | 100.00% | N/A || 99.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || - | - | - |
| core_http_client.c:HTTPClient_strerror | 98.80% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:addContentLengthHeader | 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A |
| core_http_client.c:addHeader | 93.94% | 89.19% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:addRangeHeader | 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A |
| core_http_client.c:caseInsensitiveStringCmp | 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:convertInt32ToAscii | 86.67% | 81.82% | N/A || 87.10% | 81.82% | N/A || 87.88% | 81.82% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:findHeaderFieldParserCallback | 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:findHeaderInResponse | 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:findHeaderOnHeaderCompleteCallback | 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:findHeaderValueParserCallback | 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:getFinalResponseStatus | 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:httpHeaderStrncpy | 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:httpParserOnBodyCallback | 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:httpParserOnHeaderFieldCallback | 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 0.00% | 0.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A |
| core_http_client.c:httpParserOnHeaderValueCallback | 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:httpParserOnHeadersCompleteCallback | 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A |
| core_http_client.c:httpParserOnMessageBeginCallback | 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:httpParserOnMessageCompleteCallback | 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:httpParserOnStatusCallback | 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:httpParserOnStatusCompleteCallback | 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:initializeParsingContextForFirstResponse | 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:parseHttpResponse | 94.74% | 88.89% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:processCompleteHeader | 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A |
| core_http_client.c:processLlhttpError | 4.17% | 0.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_http_client.c:sendHttpBody | 0.00% | 0.00% | N/A || - | - | - || 0.00% | 0.00% | N/A || - | - | - || 0.00% | 0.00% | N/A || - | - | - || 0.00% | 0.00% | N/A || - | - | - || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A |
| core_http_client.c:writeRequestLine | 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |

**Metrics Legend:**
- **Total %**: Percentage of all reachable lines that were covered during verification.
- **Func %**: Percentage of target function lines that were covered.
- **Errors**: Number of verification errors or failures detected.

## Performance Metrics
Average harness generation time: 7.53 seconds
Average verification time: 8.09 seconds
Average evaluation time: 0.00 seconds

## Coverage Analysis
Coverage report available at: coverage/coverage_report.html

## Summary of Results

### Function: HTTPClient_AddHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 2
Message: Verification successful

#### Coverage Metrics
- Function coverage: 80.77%

#### Coverage Evolution
- Initial coverage (v1): 100.00%
- Final coverage (v2): 80.77%
- Coverage improvement: -19.23%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_AddHeader/v1.c
  - Version 2: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_AddHeader/v2.c
  - Size evolution: Initial 132 lines → Final 129 lines (-3 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_AddHeader/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_AddHeader/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_AddHeader/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_AddHeader/v2_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_AddHeader/v3_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_AddHeader/v3_report.md

### Function: HTTPClient_AddRangeHeader (File: core_http_client.c)
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
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v1.c
  - Version 2: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v2.c
  - Version 3: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_AddRangeHeader/v3.c
  - Size evolution: Initial 122 lines → Final 119 lines (-3 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_AddRangeHeader/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_AddRangeHeader/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_AddRangeHeader/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_AddRangeHeader/v2_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_AddRangeHeader/v3_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_AddRangeHeader/v3_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_AddRangeHeader/v4_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_AddRangeHeader/v4_report.md

### Function: HTTPClient_InitializeRequestHeaders (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 94.00%

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1.c

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_InitializeRequestHeaders/v2_report.md

### Function: HTTPClient_ReadHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 5
Message: Verification successful

#### Coverage Metrics
- Function coverage: 93.33%

#### Coverage Evolution
- Initial coverage (v1): 93.33%
- Final coverage (v5): 93.33%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_ReadHeader/v1.c
  - Version 2: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_ReadHeader/v2.c
  - Version 3: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_ReadHeader/v3.c
  - Version 4: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_ReadHeader/v4.c
  - Version 5: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_ReadHeader/v5.c
  - Size evolution: Initial 130 lines → Final 100 lines (-30 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReadHeader/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReadHeader/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReadHeader/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReadHeader/v2_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReadHeader/v3_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReadHeader/v3_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReadHeader/v4_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReadHeader/v4_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReadHeader/v5_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReadHeader/v5_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReadHeader/v6_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReadHeader/v6_report.md

### Function: HTTPClient_ReceiveAndParseHttpResponse (File: core_http_client.c)
Status: SUCCESS
Refinements: 5
Message: Verification successful

#### Coverage Metrics
- Function coverage: 91.84%

#### Coverage Evolution
- Initial coverage (v1): 91.84%
- Final coverage (v5): 91.84%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1.c
  - Version 2: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v2.c
  - Version 3: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v3.c
  - Version 4: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v4.c
  - Version 5: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v5.c
  - Size evolution: Initial 70 lines → Final 86 lines (+16 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v2_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v3_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v3_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v4_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v4_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v5_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v5_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v6_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_ReceiveAndParseHttpResponse/v6_report.md

### Function: HTTPClient_Send (File: core_http_client.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 41.38%

#### Coverage Evolution
- Initial coverage (v2): 0.00%
- Final coverage (v3): 41.38%
- Coverage improvement: 41.38%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_Send/v1.c
  - Version 2: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_Send/v2.c
  - Version 3: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_Send/v3.c
  - Size evolution: Initial 192 lines → Final 359 lines (+167 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_Send/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_Send/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_Send/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_Send/v2_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_Send/v3_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_Send/v3_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_Send/v4_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_Send/v4_report.md

### Function: HTTPClient_SendHttpData (File: core_http_client.c)
Status: SUCCESS
Refinements: 2
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_SendHttpData/v1.c
  - Version 2: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_SendHttpData/v2.c
  - Size evolution: Initial 61 lines → Final 61 lines (0 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpData/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpData/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpData/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpData/v2_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpData/v3_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpData/v3_report.md

### Function: HTTPClient_SendHttpHeaders (File: core_http_client.c)
Status: SUCCESS
Refinements: 9
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v9): 100.00%
- Coverage improvement: 100.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v1.c
  - Version 2: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v2.c
  - Version 3: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v3.c
  - Version 4: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v4.c
  - Version 5: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v5.c
  - Version 6: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v6.c
  - Version 7: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v7.c
  - Version 8: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v8.c
  - Version 9: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_SendHttpHeaders/v9.c
  - Size evolution: Initial 75 lines → Final 92 lines (+17 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v2_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v3_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v3_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v4_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v4_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v5_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v5_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v6_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v6_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v7_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v7_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v8_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v8_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v9_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v9_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v10_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_SendHttpHeaders/v10_report.md

### Function: HTTPClient_strerror (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:HTTPClient_strerror/v1.c

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_strerror/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_strerror/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_strerror/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:HTTPClient_strerror/v2_report.md

### Function: addContentLengthHeader (File: core_http_client.c)
Status: FAILED
Refinements: 10
Message: VERIFICATION FAILED: Memory leak detected
Suggestions: Ensure all allocated memory is freed in all execution paths

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 100.00%
- Final coverage (v10): 100.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:addContentLengthHeader/v1.c
  - Version 2: results/openai/20250419_154303/harnesses/core_http_client.c:addContentLengthHeader/v2.c
  - Version 3: results/openai/20250419_154303/harnesses/core_http_client.c:addContentLengthHeader/v3.c
  - Version 4: results/openai/20250419_154303/harnesses/core_http_client.c:addContentLengthHeader/v4.c
  - Version 5: results/openai/20250419_154303/harnesses/core_http_client.c:addContentLengthHeader/v5.c
  - Version 6: results/openai/20250419_154303/harnesses/core_http_client.c:addContentLengthHeader/v6.c
  - Version 7: results/openai/20250419_154303/harnesses/core_http_client.c:addContentLengthHeader/v7.c
  - Version 8: results/openai/20250419_154303/harnesses/core_http_client.c:addContentLengthHeader/v8.c
  - Version 9: results/openai/20250419_154303/harnesses/core_http_client.c:addContentLengthHeader/v9.c
  - Version 10: results/openai/20250419_154303/harnesses/core_http_client.c:addContentLengthHeader/v10.c
  - Size evolution: Initial 31 lines → Final 32 lines (+1 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:addContentLengthHeader/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addContentLengthHeader/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:addContentLengthHeader/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addContentLengthHeader/v2_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:addContentLengthHeader/v3_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addContentLengthHeader/v3_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:addContentLengthHeader/v4_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addContentLengthHeader/v4_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:addContentLengthHeader/v5_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addContentLengthHeader/v5_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:addContentLengthHeader/v6_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addContentLengthHeader/v6_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:addContentLengthHeader/v7_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addContentLengthHeader/v7_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:addContentLengthHeader/v8_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addContentLengthHeader/v8_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:addContentLengthHeader/v9_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addContentLengthHeader/v9_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:addContentLengthHeader/v10_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addContentLengthHeader/v10_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:addContentLengthHeader/v11_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addContentLengthHeader/v11_report.md

### Function: addHeader (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 89.19%

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:addHeader/v1.c

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:addHeader/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addHeader/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:addHeader/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addHeader/v2_report.md

### Function: addRangeHeader (File: core_http_client.c)
Status: FAILED
Refinements: 10
Message: VERIFICATION FAILED: Null pointer dereference detected
Suggestions: Add null pointer checks before dereferencing pointers

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 100.00%
- Final coverage (v10): 100.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:addRangeHeader/v1.c
  - Version 2: results/openai/20250419_154303/harnesses/core_http_client.c:addRangeHeader/v2.c
  - Version 3: results/openai/20250419_154303/harnesses/core_http_client.c:addRangeHeader/v3.c
  - Version 4: results/openai/20250419_154303/harnesses/core_http_client.c:addRangeHeader/v4.c
  - Version 5: results/openai/20250419_154303/harnesses/core_http_client.c:addRangeHeader/v5.c
  - Version 6: results/openai/20250419_154303/harnesses/core_http_client.c:addRangeHeader/v6.c
  - Version 7: results/openai/20250419_154303/harnesses/core_http_client.c:addRangeHeader/v7.c
  - Version 8: results/openai/20250419_154303/harnesses/core_http_client.c:addRangeHeader/v8.c
  - Version 9: results/openai/20250419_154303/harnesses/core_http_client.c:addRangeHeader/v9.c
  - Version 10: results/openai/20250419_154303/harnesses/core_http_client.c:addRangeHeader/v10.c
  - Size evolution: Initial 75 lines → Final 57 lines (-18 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:addRangeHeader/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addRangeHeader/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:addRangeHeader/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addRangeHeader/v2_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:addRangeHeader/v3_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addRangeHeader/v3_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:addRangeHeader/v4_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addRangeHeader/v4_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:addRangeHeader/v5_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addRangeHeader/v5_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:addRangeHeader/v6_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addRangeHeader/v6_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:addRangeHeader/v7_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addRangeHeader/v7_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:addRangeHeader/v8_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addRangeHeader/v8_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:addRangeHeader/v9_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addRangeHeader/v9_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:addRangeHeader/v10_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addRangeHeader/v10_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:addRangeHeader/v11_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:addRangeHeader/v11_report.md

### Function: caseInsensitiveStringCmp (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:caseInsensitiveStringCmp/v1.c

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:caseInsensitiveStringCmp/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:caseInsensitiveStringCmp/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:caseInsensitiveStringCmp/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:caseInsensitiveStringCmp/v2_report.md

### Function: convertInt32ToAscii (File: core_http_client.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 81.82%

#### Coverage Evolution
- Initial coverage (v1): 81.82%
- Final coverage (v3): 81.82%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:convertInt32ToAscii/v1.c
  - Version 2: results/openai/20250419_154303/harnesses/core_http_client.c:convertInt32ToAscii/v2.c
  - Version 3: results/openai/20250419_154303/harnesses/core_http_client.c:convertInt32ToAscii/v3.c
  - Size evolution: Initial 37 lines → Final 47 lines (+10 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:convertInt32ToAscii/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:convertInt32ToAscii/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:convertInt32ToAscii/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:convertInt32ToAscii/v2_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:convertInt32ToAscii/v3_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:convertInt32ToAscii/v3_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:convertInt32ToAscii/v4_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:convertInt32ToAscii/v4_report.md

### Function: findHeaderFieldParserCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:findHeaderFieldParserCallback/v1.c

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:findHeaderFieldParserCallback/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:findHeaderFieldParserCallback/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:findHeaderFieldParserCallback/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:findHeaderFieldParserCallback/v2_report.md

### Function: findHeaderInResponse (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:findHeaderInResponse/v1.c

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:findHeaderInResponse/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:findHeaderInResponse/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:findHeaderInResponse/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:findHeaderInResponse/v2_report.md

### Function: findHeaderOnHeaderCompleteCallback (File: core_http_client.c)
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
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:findHeaderOnHeaderCompleteCallback/v1.c
  - Version 2: results/openai/20250419_154303/harnesses/core_http_client.c:findHeaderOnHeaderCompleteCallback/v2.c
  - Version 3: results/openai/20250419_154303/harnesses/core_http_client.c:findHeaderOnHeaderCompleteCallback/v3.c
  - Size evolution: Initial 47 lines → Final 42 lines (-5 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v2_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v3_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v3_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v4_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:findHeaderOnHeaderCompleteCallback/v4_report.md

### Function: findHeaderValueParserCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:findHeaderValueParserCallback/v1.c

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:findHeaderValueParserCallback/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:findHeaderValueParserCallback/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:findHeaderValueParserCallback/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:findHeaderValueParserCallback/v2_report.md

### Function: getFinalResponseStatus (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:getFinalResponseStatus/v1.c

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:getFinalResponseStatus/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:getFinalResponseStatus/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:getFinalResponseStatus/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:getFinalResponseStatus/v2_report.md

### Function: httpHeaderStrncpy (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:httpHeaderStrncpy/v1.c

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:httpHeaderStrncpy/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpHeaderStrncpy/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpHeaderStrncpy/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpHeaderStrncpy/v2_report.md

### Function: httpParserOnBodyCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnBodyCallback/v1.c

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnBodyCallback/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnBodyCallback/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnBodyCallback/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnBodyCallback/v2_report.md

### Function: httpParserOnHeaderFieldCallback (File: core_http_client.c)
Status: FAILED
Refinements: 10
Message: VERIFICATION FAILED: Null pointer dereference detected
Suggestions: Add null pointer checks before dereferencing pointers

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 100.00%
- Final coverage (v10): 100.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v1.c
  - Version 2: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v2.c
  - Version 3: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v3.c
  - Version 4: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v4.c
  - Version 5: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v5.c
  - Version 6: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v6.c
  - Version 7: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v7.c
  - Version 8: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v8.c
  - Version 9: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v9.c
  - Version 10: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnHeaderFieldCallback/v10.c
  - Size evolution: Initial 81 lines → Final 91 lines (+10 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v2_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v3_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v3_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v4_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v4_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v5_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v5_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v6_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v6_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v7_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v7_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v8_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v8_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v9_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v9_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v10_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v10_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v11_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderFieldCallback/v11_report.md

### Function: httpParserOnHeaderValueCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnHeaderValueCallback/v1.c

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderValueCallback/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderValueCallback/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderValueCallback/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeaderValueCallback/v2_report.md

### Function: httpParserOnHeadersCompleteCallback (File: core_http_client.c)
Status: FAILED
Refinements: 10
Message: VERIFICATION FAILED: Null pointer dereference detected
Suggestions: Add null pointer checks before dereferencing pointers

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 100.00%
- Final coverage (v10): 100.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v1.c
  - Version 2: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v2.c
  - Version 3: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v3.c
  - Version 4: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v4.c
  - Version 5: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v5.c
  - Version 6: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v6.c
  - Version 7: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v7.c
  - Version 8: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v8.c
  - Version 9: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v9.c
  - Version 10: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnHeadersCompleteCallback/v10.c
  - Size evolution: Initial 87 lines → Final 107 lines (+20 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v2_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v3_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v3_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v4_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v4_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v5_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v5_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v6_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v6_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v7_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v7_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v8_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v8_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v9_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v9_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v10_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v10_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v11_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnHeadersCompleteCallback/v11_report.md

### Function: httpParserOnMessageBeginCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnMessageBeginCallback/v1.c

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnMessageBeginCallback/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnMessageBeginCallback/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnMessageBeginCallback/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnMessageBeginCallback/v2_report.md

### Function: httpParserOnMessageCompleteCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnMessageCompleteCallback/v1.c

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnMessageCompleteCallback/v2_report.md

### Function: httpParserOnStatusCallback (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnStatusCallback/v1.c

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnStatusCallback/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnStatusCallback/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnStatusCallback/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnStatusCallback/v2_report.md

### Function: httpParserOnStatusCompleteCallback (File: core_http_client.c)
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
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnStatusCompleteCallback/v1.c
  - Version 2: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnStatusCompleteCallback/v2.c
  - Version 3: results/openai/20250419_154303/harnesses/core_http_client.c:httpParserOnStatusCompleteCallback/v3.c
  - Size evolution: Initial 45 lines → Final 36 lines (-9 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v2_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v3_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v3_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v4_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:httpParserOnStatusCompleteCallback/v4_report.md

### Function: initializeParsingContextForFirstResponse (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:initializeParsingContextForFirstResponse/v1.c

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:initializeParsingContextForFirstResponse/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:initializeParsingContextForFirstResponse/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:initializeParsingContextForFirstResponse/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:initializeParsingContextForFirstResponse/v2_report.md

### Function: parseHttpResponse (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 88.89%

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:parseHttpResponse/v1.c

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:parseHttpResponse/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:parseHttpResponse/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:parseHttpResponse/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:parseHttpResponse/v2_report.md

### Function: processCompleteHeader (File: core_http_client.c)
Status: FAILED
Refinements: 10
Message: PREPROCESSING ERROR: GCC preprocessing failed - check for syntax errors
Suggestions: Fix syntax errors and ensure all necessary includes are available

#### Coverage Metrics
- Function coverage: 0.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v10): 0.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:processCompleteHeader/v1.c
  - Version 2: results/openai/20250419_154303/harnesses/core_http_client.c:processCompleteHeader/v2.c
  - Version 3: results/openai/20250419_154303/harnesses/core_http_client.c:processCompleteHeader/v3.c
  - Version 4: results/openai/20250419_154303/harnesses/core_http_client.c:processCompleteHeader/v4.c
  - Version 5: results/openai/20250419_154303/harnesses/core_http_client.c:processCompleteHeader/v5.c
  - Version 6: results/openai/20250419_154303/harnesses/core_http_client.c:processCompleteHeader/v6.c
  - Version 7: results/openai/20250419_154303/harnesses/core_http_client.c:processCompleteHeader/v7.c
  - Version 8: results/openai/20250419_154303/harnesses/core_http_client.c:processCompleteHeader/v8.c
  - Version 9: results/openai/20250419_154303/harnesses/core_http_client.c:processCompleteHeader/v9.c
  - Version 10: results/openai/20250419_154303/harnesses/core_http_client.c:processCompleteHeader/v10.c
  - Size evolution: Initial 114 lines → Final 220 lines (+106 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:processCompleteHeader/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:processCompleteHeader/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:processCompleteHeader/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:processCompleteHeader/v2_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:processCompleteHeader/v3_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:processCompleteHeader/v3_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:processCompleteHeader/v4_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:processCompleteHeader/v4_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:processCompleteHeader/v5_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:processCompleteHeader/v5_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:processCompleteHeader/v6_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:processCompleteHeader/v6_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:processCompleteHeader/v7_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:processCompleteHeader/v7_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:processCompleteHeader/v8_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:processCompleteHeader/v8_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:processCompleteHeader/v9_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:processCompleteHeader/v9_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:processCompleteHeader/v10_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:processCompleteHeader/v10_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:processCompleteHeader/v11_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:processCompleteHeader/v11_report.md

### Function: processLlhttpError (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 0.00%

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:processLlhttpError/v1.c

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:processLlhttpError/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:processLlhttpError/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:processLlhttpError/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:processLlhttpError/v2_report.md

### Function: sendHttpBody (File: core_http_client.c)
Status: FAILED
Refinements: 10
Message: VERIFICATION FAILED: Unspecified verification error
Suggestions: Review the full verification output for details

#### Coverage Metrics
- Function coverage: 0.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v10): 0.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:sendHttpBody/v1.c
  - Version 2: results/openai/20250419_154303/harnesses/core_http_client.c:sendHttpBody/v2.c
  - Version 3: results/openai/20250419_154303/harnesses/core_http_client.c:sendHttpBody/v3.c
  - Version 4: results/openai/20250419_154303/harnesses/core_http_client.c:sendHttpBody/v4.c
  - Version 5: results/openai/20250419_154303/harnesses/core_http_client.c:sendHttpBody/v5.c
  - Version 6: results/openai/20250419_154303/harnesses/core_http_client.c:sendHttpBody/v6.c
  - Version 7: results/openai/20250419_154303/harnesses/core_http_client.c:sendHttpBody/v7.c
  - Version 8: results/openai/20250419_154303/harnesses/core_http_client.c:sendHttpBody/v8.c
  - Version 9: results/openai/20250419_154303/harnesses/core_http_client.c:sendHttpBody/v9.c
  - Version 10: results/openai/20250419_154303/harnesses/core_http_client.c:sendHttpBody/v10.c
  - Size evolution: Initial 61 lines → Final 107 lines (+46 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpBody/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpBody/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpBody/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpBody/v2_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpBody/v3_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpBody/v3_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpBody/v4_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpBody/v4_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpBody/v5_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpBody/v5_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpBody/v6_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpBody/v6_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpBody/v7_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpBody/v7_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpBody/v8_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpBody/v8_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpBody/v9_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpBody/v9_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpBody/v10_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpBody/v10_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpBody/v11_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpBody/v11_report.md

### Function: sendHttpRequest (File: core_http_client.c)
Status: TIMEOUT
Refinements: 10
Message: CBMC verification timed out after 180 seconds.
Suggestions: The function may have complex paths requiring longer verification time. Consider using more selective file inclusion or increasing timeout.

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:sendHttpRequest/v1.c
  - Version 2: results/openai/20250419_154303/harnesses/core_http_client.c:sendHttpRequest/v2.c
  - Version 3: results/openai/20250419_154303/harnesses/core_http_client.c:sendHttpRequest/v3.c
  - Version 4: results/openai/20250419_154303/harnesses/core_http_client.c:sendHttpRequest/v4.c
  - Version 5: results/openai/20250419_154303/harnesses/core_http_client.c:sendHttpRequest/v5.c
  - Version 6: results/openai/20250419_154303/harnesses/core_http_client.c:sendHttpRequest/v6.c
  - Version 7: results/openai/20250419_154303/harnesses/core_http_client.c:sendHttpRequest/v7.c
  - Version 8: results/openai/20250419_154303/harnesses/core_http_client.c:sendHttpRequest/v8.c
  - Version 9: results/openai/20250419_154303/harnesses/core_http_client.c:sendHttpRequest/v9.c
  - Version 10: results/openai/20250419_154303/harnesses/core_http_client.c:sendHttpRequest/v10.c
  - Size evolution: Initial 84 lines → Final 60 lines (-24 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpRequest/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpRequest/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpRequest/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpRequest/v2_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpRequest/v3_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpRequest/v3_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpRequest/v4_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpRequest/v4_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpRequest/v5_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpRequest/v5_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpRequest/v6_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpRequest/v6_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpRequest/v7_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpRequest/v7_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpRequest/v8_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpRequest/v8_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpRequest/v9_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpRequest/v9_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpRequest/v10_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpRequest/v10_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpRequest/v11_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:sendHttpRequest/v11_report.md

### Function: writeRequestLine (File: core_http_client.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250419_154303/harnesses/core_http_client.c:writeRequestLine/v1.c

#### Verification Reports: 
  - results/openai/20250419_154303/verification/core_http_client.c:writeRequestLine/v1_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:writeRequestLine/v1_report.md
  - results/openai/20250419_154303/verification/core_http_client.c:writeRequestLine/v2_results.txt
  - results/openai/20250419_154303/verification/core_http_client.c:writeRequestLine/v2_report.md