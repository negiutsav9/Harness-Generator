# CBMC Harness Generation Complete - Directory Mode - Openai

Total processing time: 155.67 seconds
Processed 3 source files.
Analyzed 10 functions.
Identified 8 functions with memory or arithmetic operations.
Generated 8 verification harnesses.
Performed 18 harness refinements (average 2.25 per function).

## File Analysis

### defender.c
Functions analyzed: 8
Functions verified: 8
Successful verifications: 7
Failed verifications: 1

## RAG Knowledge Base Statistics
Code functions stored: 109
Pattern templates: 16
Error patterns stored: 11
Successful solutions: 7

The RAG (Retrieval-Augmented Generation) knowledge base stores code functions, patterns, errors, and solutions to improve harness generation over time. Each run contributes to this knowledge base, helping future runs generate better harnesses with fewer iterations.

## Unit Proof Metrics Summary
Total reachable lines: 0
Total coverage: 0.00%
Total reachable lines for harnessed functions only: 0
Coverage of harnessed functions only: 0.00%
Number of reported errors: 0
Functions with full coverage: 6 of 8
Functions without errors: 8 of 8

### Note on Error Reporting:
- Errors are grouped by line number (one error per line)
- Errors about missing function bodies are excluded
- Loop unwinding assertions are excluded from error count

## Detailed Coverage Matrix by Function and Version

The table below shows detailed metrics for each function across different versions of the generated harnesses:

| Function | Version 1 | Version 2 | Version 3 | Version 4 | Version 5 | Version 6 | Version 7 | Version 8 | Version 9 | Version 10 |
| --- | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors |
| defender.c:Defender_GetTopic | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| defender.c:Defender_MatchTopic | 97.18% | 95.74% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| defender.c:extractThingNameLength | 97.30% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| defender.c:getTopicLength | 93.33% | 90.48% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| defender.c:matchApi | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| defender.c:matchBridge | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| defender.c:matchPrefix | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| defender.c:writeFormatAndSuffix | 92.45% | 85.19% | 0 | 92.59% | 85.19% | 0 | 92.73% | 85.19% | 0 | 92.73% | 85.19% | 0 | 92.73% | 85.19% | 0 | 92.98% | 85.19% | 0 | 89.71% | 85.19% | 0 | 87.10% | 85.19% | 0 | 91.53% | 85.19% | 0 | 90.00% | 85.19% | 0 |

**Metrics Legend:**
- **Total %**: Percentage of all reachable lines that were covered during verification.
- **Func %**: Percentage of target function lines that were covered.
- **Errors**: Number of verification errors or failures detected.

## Performance Metrics
Average harness generation time: 7.18 seconds
Average verification time: 0.46 seconds
Average evaluation time: 0.00 seconds

## Coverage Analysis
Coverage report available at: coverage/coverage_report.html

## Summary of Results

### Function: Defender_GetTopic (File: defender.c)
Status: SUCCESS
Refinements: 2
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 100.00%
- Final coverage (v2): 100.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250422_133907/harnesses/defender.c:Defender_GetTopic/v1.c
  - Version 2: results/openai/20250422_133907/harnesses/defender.c:Defender_GetTopic/v2.c
  - Size evolution: Initial 84 lines → Final 113 lines (+29 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250422_133907/verification/defender.c:Defender_GetTopic/v1_results.txt
  - results/openai/20250422_133907/verification/defender.c:Defender_GetTopic/v1_report.md
  - results/openai/20250422_133907/verification/defender.c:Defender_GetTopic/v2_results.txt
  - results/openai/20250422_133907/verification/defender.c:Defender_GetTopic/v2_report.md
  - results/openai/20250422_133907/verification/defender.c:Defender_GetTopic/v3_results.txt
  - results/openai/20250422_133907/verification/defender.c:Defender_GetTopic/v3_report.md

### Function: Defender_MatchTopic (File: defender.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 95.74%

#### Harness Evolution:
  - Version 1: results/openai/20250422_133907/harnesses/defender.c:Defender_MatchTopic/v1.c

#### Verification Reports: 
  - results/openai/20250422_133907/verification/defender.c:Defender_MatchTopic/v1_results.txt
  - results/openai/20250422_133907/verification/defender.c:Defender_MatchTopic/v1_report.md
  - results/openai/20250422_133907/verification/defender.c:Defender_MatchTopic/v2_results.txt
  - results/openai/20250422_133907/verification/defender.c:Defender_MatchTopic/v2_report.md

### Function: extractThingNameLength (File: defender.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250422_133907/harnesses/defender.c:extractThingNameLength/v1.c

#### Verification Reports: 
  - results/openai/20250422_133907/verification/defender.c:extractThingNameLength/v1_results.txt
  - results/openai/20250422_133907/verification/defender.c:extractThingNameLength/v1_report.md
  - results/openai/20250422_133907/verification/defender.c:extractThingNameLength/v2_results.txt
  - results/openai/20250422_133907/verification/defender.c:extractThingNameLength/v2_report.md

### Function: getTopicLength (File: defender.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 90.48%

#### Harness Evolution:
  - Version 1: results/openai/20250422_133907/harnesses/defender.c:getTopicLength/v1.c

#### Verification Reports: 
  - results/openai/20250422_133907/verification/defender.c:getTopicLength/v1_results.txt
  - results/openai/20250422_133907/verification/defender.c:getTopicLength/v1_report.md
  - results/openai/20250422_133907/verification/defender.c:getTopicLength/v2_results.txt
  - results/openai/20250422_133907/verification/defender.c:getTopicLength/v2_report.md

### Function: matchApi (File: defender.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250422_133907/harnesses/defender.c:matchApi/v1.c

#### Verification Reports: 
  - results/openai/20250422_133907/verification/defender.c:matchApi/v1_results.txt
  - results/openai/20250422_133907/verification/defender.c:matchApi/v1_report.md
  - results/openai/20250422_133907/verification/defender.c:matchApi/v2_results.txt
  - results/openai/20250422_133907/verification/defender.c:matchApi/v2_report.md

### Function: matchBridge (File: defender.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250422_133907/harnesses/defender.c:matchBridge/v1.c

#### Verification Reports: 
  - results/openai/20250422_133907/verification/defender.c:matchBridge/v1_results.txt
  - results/openai/20250422_133907/verification/defender.c:matchBridge/v1_report.md
  - results/openai/20250422_133907/verification/defender.c:matchBridge/v2_results.txt
  - results/openai/20250422_133907/verification/defender.c:matchBridge/v2_report.md

### Function: matchPrefix (File: defender.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250422_133907/harnesses/defender.c:matchPrefix/v1.c

#### Verification Reports: 
  - results/openai/20250422_133907/verification/defender.c:matchPrefix/v1_results.txt
  - results/openai/20250422_133907/verification/defender.c:matchPrefix/v1_report.md
  - results/openai/20250422_133907/verification/defender.c:matchPrefix/v2_results.txt
  - results/openai/20250422_133907/verification/defender.c:matchPrefix/v2_report.md

### Function: writeFormatAndSuffix (File: defender.c)
Status: FAILED
Refinements: 10
Message: VERIFICATION FAILED: Unspecified verification error
Suggestions: Review the full verification output for details

#### Coverage Metrics
- Function coverage: 85.19%

#### Coverage Evolution
- Initial coverage (v1): 85.19%
- Final coverage (v10): 85.19%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250422_133907/harnesses/defender.c:writeFormatAndSuffix/v1.c
  - Version 2: results/openai/20250422_133907/harnesses/defender.c:writeFormatAndSuffix/v2.c
  - Version 3: results/openai/20250422_133907/harnesses/defender.c:writeFormatAndSuffix/v3.c
  - Version 4: results/openai/20250422_133907/harnesses/defender.c:writeFormatAndSuffix/v4.c
  - Version 5: results/openai/20250422_133907/harnesses/defender.c:writeFormatAndSuffix/v5.c
  - Version 6: results/openai/20250422_133907/harnesses/defender.c:writeFormatAndSuffix/v6.c
  - Version 7: results/openai/20250422_133907/harnesses/defender.c:writeFormatAndSuffix/v7.c
  - Version 8: results/openai/20250422_133907/harnesses/defender.c:writeFormatAndSuffix/v8.c
  - Version 9: results/openai/20250422_133907/harnesses/defender.c:writeFormatAndSuffix/v9.c
  - Version 10: results/openai/20250422_133907/harnesses/defender.c:writeFormatAndSuffix/v10.c
  - Size evolution: Initial 82 lines → Final 118 lines (+36 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250422_133907/verification/defender.c:writeFormatAndSuffix/v1_results.txt
  - results/openai/20250422_133907/verification/defender.c:writeFormatAndSuffix/v1_report.md
  - results/openai/20250422_133907/verification/defender.c:writeFormatAndSuffix/v2_results.txt
  - results/openai/20250422_133907/verification/defender.c:writeFormatAndSuffix/v2_report.md
  - results/openai/20250422_133907/verification/defender.c:writeFormatAndSuffix/v3_results.txt
  - results/openai/20250422_133907/verification/defender.c:writeFormatAndSuffix/v3_report.md
  - results/openai/20250422_133907/verification/defender.c:writeFormatAndSuffix/v4_results.txt
  - results/openai/20250422_133907/verification/defender.c:writeFormatAndSuffix/v4_report.md
  - results/openai/20250422_133907/verification/defender.c:writeFormatAndSuffix/v5_results.txt
  - results/openai/20250422_133907/verification/defender.c:writeFormatAndSuffix/v5_report.md
  - results/openai/20250422_133907/verification/defender.c:writeFormatAndSuffix/v6_results.txt
  - results/openai/20250422_133907/verification/defender.c:writeFormatAndSuffix/v6_report.md
  - results/openai/20250422_133907/verification/defender.c:writeFormatAndSuffix/v7_results.txt
  - results/openai/20250422_133907/verification/defender.c:writeFormatAndSuffix/v7_report.md
  - results/openai/20250422_133907/verification/defender.c:writeFormatAndSuffix/v8_results.txt
  - results/openai/20250422_133907/verification/defender.c:writeFormatAndSuffix/v8_report.md
  - results/openai/20250422_133907/verification/defender.c:writeFormatAndSuffix/v9_results.txt
  - results/openai/20250422_133907/verification/defender.c:writeFormatAndSuffix/v9_report.md
  - results/openai/20250422_133907/verification/defender.c:writeFormatAndSuffix/v10_results.txt
  - results/openai/20250422_133907/verification/defender.c:writeFormatAndSuffix/v10_report.md
  - results/openai/20250422_133907/verification/defender.c:writeFormatAndSuffix/v11_results.txt
  - results/openai/20250422_133907/verification/defender.c:writeFormatAndSuffix/v11_report.md