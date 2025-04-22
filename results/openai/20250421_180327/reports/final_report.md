# CBMC Harness Generation Complete - Directory Mode - Openai

Total processing time: 337.21 seconds
Processed 3 source files.
Analyzed 10 functions.
Identified 8 functions with memory or arithmetic operations.
Generated 7 verification harnesses.
Performed 47 harness refinements (average 6.71 per function).

## File Analysis

### defender.c
Functions analyzed: 8
Functions verified: 7
Successful verifications: 3
Failed verifications: 4

## RAG Knowledge Base Statistics
Code functions stored: 109
Pattern templates: 16
Error patterns stored: 44
Successful solutions: 3

The RAG (Retrieval-Augmented Generation) knowledge base stores code functions, patterns, errors, and solutions to improve harness generation over time. Each run contributes to this knowledge base, helping future runs generate better harnesses with fewer iterations.

## Unit Proof Metrics Summary
Total reachable lines: 0
Total coverage: 0.00%
Total reachable lines for harnessed functions only: 0
Coverage of harnessed functions only: 0.00%
Number of reported errors: 0
Functions with full coverage: 6 of 7
Functions without errors: 7 of 7

### Note on Error Reporting:
- Errors are grouped by line number (one error per line)
- Errors about missing function bodies are excluded
- Loop unwinding assertions are excluded from error count

## Detailed Coverage Matrix by Function and Version

The table below shows detailed metrics for each function across different versions of the generated harnesses:

| Function | Version 1 | Version 2 | Version 3 | Version 4 | Version 5 | Version 6 | Version 7 | Version 8 | Version 9 | Version 10 | Version 11 |
| --- | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors |
| defender.c:Defender_GetTopic | 96.00% | 91.30% | 0 | 96.00% | 91.30% | 0 | 96.23% | 91.30% | 0 | 96.23% | 91.30% | 0 | 96.00% | 91.30% | 0 | 95.92% | 91.30% | 0 | 95.92% | 91.30% | 0 | 95.92% | 91.30% | 0 | 95.92% | 91.30% | 0 | 95.92% | 91.30% | 0 | 100.00% | 100.00% | 0 |
| defender.c:Defender_MatchTopic | 97.18% | 95.74% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| defender.c:extractThingNameLength | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| defender.c:getTopicLength | 93.10% | 90.48% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 93.55% | 90.48% | 0 |
| defender.c:matchApi | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| defender.c:matchBridge | 89.29% | 100.00% | 0 | 92.00% | 100.00% | 0 | 92.00% | 100.00% | 0 | 92.00% | 100.00% | 0 | 92.00% | 100.00% | 0 | 92.00% | 100.00% | 0 | 73.91% | 44.44% | 0 | 84.62% | 100.00% | 0 | 84.62% | 100.00% | 0 | 84.62% | 100.00% | 0 | 100.00% | 100.00% | 0 |
| defender.c:matchPrefix | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 |

**Metrics Legend:**
- **Total %**: Percentage of all reachable lines that were covered during verification.
- **Func %**: Percentage of target function lines that were covered.
- **Errors**: Number of verification errors or failures detected.

## Performance Metrics
Average harness generation time: 4.93 seconds
Average verification time: 0.42 seconds
Average evaluation time: 0.00 seconds

## Coverage Analysis
Coverage report available at: coverage/coverage_report.html

## Summary of Results

### Function: Defender_GetTopic (File: defender.c)
Status: FAILED
Refinements: 10
Message: PREPROCESSING ERROR: Macro definition error: file results/openai/20250421_180327/verification/includes/defender_config.h line 52: results/openai/20250421_180327/verification/includes/defender_config.h:52:13: warning: 'LogError' macro redefined [-Wmacro-redefined]; file results/openai/20250421_180327/verification/includes/defender_config.h line 54: results/openai/20250421_180327/verification/includes/defender_config.h:54:13: warning: 'LogWarn' macro redefined [-Wmacro-redefined]
Suggestions: Fix macro definitions and ensure they are properly defined

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 91.30%
- Final coverage (v11): 100.00%
- Coverage improvement: 8.70%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250421_180327/harnesses/defender.c:Defender_GetTopic/v1.c
  - Version 2: results/openai/20250421_180327/harnesses/defender.c:Defender_GetTopic/v2.c
  - Version 3: results/openai/20250421_180327/harnesses/defender.c:Defender_GetTopic/v3.c
  - Version 4: results/openai/20250421_180327/harnesses/defender.c:Defender_GetTopic/v4.c
  - Version 5: results/openai/20250421_180327/harnesses/defender.c:Defender_GetTopic/v5.c
  - Version 6: results/openai/20250421_180327/harnesses/defender.c:Defender_GetTopic/v6.c
  - Version 7: results/openai/20250421_180327/harnesses/defender.c:Defender_GetTopic/v7.c
  - Version 8: results/openai/20250421_180327/harnesses/defender.c:Defender_GetTopic/v8.c
  - Version 9: results/openai/20250421_180327/harnesses/defender.c:Defender_GetTopic/v9.c
  - Size evolution: Initial 77 lines → Final 87 lines (+10 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250421_180327/verification/defender.c:Defender_GetTopic/v1_results.txt
  - results/openai/20250421_180327/verification/defender.c:Defender_GetTopic/v1_report.md
  - results/openai/20250421_180327/verification/defender.c:Defender_GetTopic/v2_results.txt
  - results/openai/20250421_180327/verification/defender.c:Defender_GetTopic/v2_report.md
  - results/openai/20250421_180327/verification/defender.c:Defender_GetTopic/v3_results.txt
  - results/openai/20250421_180327/verification/defender.c:Defender_GetTopic/v3_report.md
  - results/openai/20250421_180327/verification/defender.c:Defender_GetTopic/v4_results.txt
  - results/openai/20250421_180327/verification/defender.c:Defender_GetTopic/v4_report.md
  - results/openai/20250421_180327/verification/defender.c:Defender_GetTopic/v5_results.txt
  - results/openai/20250421_180327/verification/defender.c:Defender_GetTopic/v5_report.md
  - results/openai/20250421_180327/verification/defender.c:Defender_GetTopic/v6_results.txt
  - results/openai/20250421_180327/verification/defender.c:Defender_GetTopic/v6_report.md
  - results/openai/20250421_180327/verification/defender.c:Defender_GetTopic/v7_results.txt
  - results/openai/20250421_180327/verification/defender.c:Defender_GetTopic/v7_report.md
  - results/openai/20250421_180327/verification/defender.c:Defender_GetTopic/v8_results.txt
  - results/openai/20250421_180327/verification/defender.c:Defender_GetTopic/v8_report.md
  - results/openai/20250421_180327/verification/defender.c:Defender_GetTopic/v9_results.txt
  - results/openai/20250421_180327/verification/defender.c:Defender_GetTopic/v9_report.md
  - results/openai/20250421_180327/verification/defender.c:Defender_GetTopic/v10_results.txt
  - results/openai/20250421_180327/verification/defender.c:Defender_GetTopic/v10_report.md
  - results/openai/20250421_180327/verification/defender.c:Defender_GetTopic/v11_results.txt
  - results/openai/20250421_180327/verification/defender.c:Defender_GetTopic/v11_report.md

### Function: Defender_MatchTopic (File: defender.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 95.74%

#### Harness Evolution:
  - Version 1: results/openai/20250421_180327/harnesses/defender.c:Defender_MatchTopic/v1.c

#### Verification Reports: 
  - results/openai/20250421_180327/verification/defender.c:Defender_MatchTopic/v1_results.txt
  - results/openai/20250421_180327/verification/defender.c:Defender_MatchTopic/v1_report.md
  - results/openai/20250421_180327/verification/defender.c:Defender_MatchTopic/v2_results.txt
  - results/openai/20250421_180327/verification/defender.c:Defender_MatchTopic/v2_report.md

### Function: extractThingNameLength (File: defender.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250421_180327/harnesses/defender.c:extractThingNameLength/v1.c

#### Verification Reports: 
  - results/openai/20250421_180327/verification/defender.c:extractThingNameLength/v1_results.txt
  - results/openai/20250421_180327/verification/defender.c:extractThingNameLength/v1_report.md
  - results/openai/20250421_180327/verification/defender.c:extractThingNameLength/v2_results.txt
  - results/openai/20250421_180327/verification/defender.c:extractThingNameLength/v2_report.md

### Function: getTopicLength (File: defender.c)
Status: FAILED
Refinements: 10
Message: PREPROCESSING ERROR: Macro definition error: file results/openai/20250421_180327/verification/includes/defender_config.h line 52: results/openai/20250421_180327/verification/includes/defender_config.h:52:13: warning: 'LogError' macro redefined [-Wmacro-redefined]; file results/openai/20250421_180327/verification/includes/defender_config.h line 54: results/openai/20250421_180327/verification/includes/defender_config.h:54:13: warning: 'LogWarn' macro redefined [-Wmacro-redefined]
Suggestions: Fix macro definitions and ensure they are properly defined

#### Coverage Metrics
- Function coverage: 90.48%

#### Coverage Evolution
- Initial coverage (v1): 90.48%
- Final coverage (v11): 90.48%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250421_180327/harnesses/defender.c:getTopicLength/v1.c
  - Version 2: results/openai/20250421_180327/harnesses/defender.c:getTopicLength/v2.c
  - Version 3: results/openai/20250421_180327/harnesses/defender.c:getTopicLength/v3.c
  - Version 4: results/openai/20250421_180327/harnesses/defender.c:getTopicLength/v4.c
  - Version 5: results/openai/20250421_180327/harnesses/defender.c:getTopicLength/v5.c
  - Version 6: results/openai/20250421_180327/harnesses/defender.c:getTopicLength/v6.c
  - Version 7: results/openai/20250421_180327/harnesses/defender.c:getTopicLength/v7.c
  - Version 8: results/openai/20250421_180327/harnesses/defender.c:getTopicLength/v8.c
  - Version 9: results/openai/20250421_180327/harnesses/defender.c:getTopicLength/v9.c
  - Version 10: results/openai/20250421_180327/harnesses/defender.c:getTopicLength/v10.c
  - Size evolution: Initial 39 lines → Final 44 lines (+5 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250421_180327/verification/defender.c:getTopicLength/v1_results.txt
  - results/openai/20250421_180327/verification/defender.c:getTopicLength/v1_report.md
  - results/openai/20250421_180327/verification/defender.c:getTopicLength/v2_results.txt
  - results/openai/20250421_180327/verification/defender.c:getTopicLength/v2_report.md
  - results/openai/20250421_180327/verification/defender.c:getTopicLength/v3_results.txt
  - results/openai/20250421_180327/verification/defender.c:getTopicLength/v3_report.md
  - results/openai/20250421_180327/verification/defender.c:getTopicLength/v4_results.txt
  - results/openai/20250421_180327/verification/defender.c:getTopicLength/v4_report.md
  - results/openai/20250421_180327/verification/defender.c:getTopicLength/v5_results.txt
  - results/openai/20250421_180327/verification/defender.c:getTopicLength/v5_report.md
  - results/openai/20250421_180327/verification/defender.c:getTopicLength/v6_results.txt
  - results/openai/20250421_180327/verification/defender.c:getTopicLength/v6_report.md
  - results/openai/20250421_180327/verification/defender.c:getTopicLength/v7_results.txt
  - results/openai/20250421_180327/verification/defender.c:getTopicLength/v7_report.md
  - results/openai/20250421_180327/verification/defender.c:getTopicLength/v8_results.txt
  - results/openai/20250421_180327/verification/defender.c:getTopicLength/v8_report.md
  - results/openai/20250421_180327/verification/defender.c:getTopicLength/v9_results.txt
  - results/openai/20250421_180327/verification/defender.c:getTopicLength/v9_report.md
  - results/openai/20250421_180327/verification/defender.c:getTopicLength/v10_results.txt
  - results/openai/20250421_180327/verification/defender.c:getTopicLength/v10_report.md
  - results/openai/20250421_180327/verification/defender.c:getTopicLength/v11_results.txt
  - results/openai/20250421_180327/verification/defender.c:getTopicLength/v11_report.md

### Function: matchApi (File: defender.c)
Status: SUCCESS
Refinements: 5
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 100.00%
- Final coverage (v5): 100.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250421_180327/harnesses/defender.c:matchApi/v1.c
  - Version 2: results/openai/20250421_180327/harnesses/defender.c:matchApi/v2.c
  - Version 3: results/openai/20250421_180327/harnesses/defender.c:matchApi/v3.c
  - Version 4: results/openai/20250421_180327/harnesses/defender.c:matchApi/v4.c
  - Size evolution: Initial 62 lines → Final 51 lines (-11 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250421_180327/verification/defender.c:matchApi/v1_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchApi/v1_report.md
  - results/openai/20250421_180327/verification/defender.c:matchApi/v2_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchApi/v2_report.md
  - results/openai/20250421_180327/verification/defender.c:matchApi/v3_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchApi/v3_report.md
  - results/openai/20250421_180327/verification/defender.c:matchApi/v4_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchApi/v4_report.md
  - results/openai/20250421_180327/verification/defender.c:matchApi/v5_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchApi/v5_report.md
  - results/openai/20250421_180327/verification/defender.c:matchApi/v6_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchApi/v6_report.md

### Function: matchBridge (File: defender.c)
Status: FAILED
Refinements: 10
Message: PREPROCESSING ERROR: Macro definition error: file results/openai/20250421_180327/verification/includes/defender_config.h line 52: results/openai/20250421_180327/verification/includes/defender_config.h:52:13: warning: 'LogError' macro redefined [-Wmacro-redefined]; file results/openai/20250421_180327/verification/includes/defender_config.h line 54: results/openai/20250421_180327/verification/includes/defender_config.h:54:13: warning: 'LogWarn' macro redefined [-Wmacro-redefined]
Suggestions: Fix macro definitions and ensure they are properly defined

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 100.00%
- Final coverage (v11): 100.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250421_180327/harnesses/defender.c:matchBridge/v1.c
  - Version 2: results/openai/20250421_180327/harnesses/defender.c:matchBridge/v2.c
  - Version 3: results/openai/20250421_180327/harnesses/defender.c:matchBridge/v3.c
  - Version 4: results/openai/20250421_180327/harnesses/defender.c:matchBridge/v4.c
  - Version 5: results/openai/20250421_180327/harnesses/defender.c:matchBridge/v5.c
  - Version 6: results/openai/20250421_180327/harnesses/defender.c:matchBridge/v6.c
  - Version 7: results/openai/20250421_180327/harnesses/defender.c:matchBridge/v7.c
  - Version 8: results/openai/20250421_180327/harnesses/defender.c:matchBridge/v8.c
  - Version 9: results/openai/20250421_180327/harnesses/defender.c:matchBridge/v9.c
  - Version 10: results/openai/20250421_180327/harnesses/defender.c:matchBridge/v10.c
  - Size evolution: Initial 53 lines → Final 47 lines (-6 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250421_180327/verification/defender.c:matchBridge/v1_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchBridge/v1_report.md
  - results/openai/20250421_180327/verification/defender.c:matchBridge/v2_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchBridge/v2_report.md
  - results/openai/20250421_180327/verification/defender.c:matchBridge/v3_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchBridge/v3_report.md
  - results/openai/20250421_180327/verification/defender.c:matchBridge/v4_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchBridge/v4_report.md
  - results/openai/20250421_180327/verification/defender.c:matchBridge/v5_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchBridge/v5_report.md
  - results/openai/20250421_180327/verification/defender.c:matchBridge/v6_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchBridge/v6_report.md
  - results/openai/20250421_180327/verification/defender.c:matchBridge/v7_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchBridge/v7_report.md
  - results/openai/20250421_180327/verification/defender.c:matchBridge/v8_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchBridge/v8_report.md
  - results/openai/20250421_180327/verification/defender.c:matchBridge/v9_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchBridge/v9_report.md
  - results/openai/20250421_180327/verification/defender.c:matchBridge/v10_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchBridge/v10_report.md
  - results/openai/20250421_180327/verification/defender.c:matchBridge/v11_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchBridge/v11_report.md

### Function: matchPrefix (File: defender.c)
Status: FAILED
Refinements: 10
Message: PREPROCESSING ERROR: Macro definition error: file results/openai/20250421_180327/verification/includes/defender_config.h line 52: results/openai/20250421_180327/verification/includes/defender_config.h:52:13: warning: 'LogError' macro redefined [-Wmacro-redefined]; file results/openai/20250421_180327/verification/includes/defender_config.h line 54: results/openai/20250421_180327/verification/includes/defender_config.h:54:13: warning: 'LogWarn' macro redefined [-Wmacro-redefined]
Suggestions: Fix macro definitions and ensure they are properly defined

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 100.00%
- Final coverage (v11): 100.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250421_180327/harnesses/defender.c:matchPrefix/v1.c
  - Version 2: results/openai/20250421_180327/harnesses/defender.c:matchPrefix/v2.c
  - Version 3: results/openai/20250421_180327/harnesses/defender.c:matchPrefix/v3.c
  - Version 4: results/openai/20250421_180327/harnesses/defender.c:matchPrefix/v4.c
  - Version 5: results/openai/20250421_180327/harnesses/defender.c:matchPrefix/v5.c
  - Version 6: results/openai/20250421_180327/harnesses/defender.c:matchPrefix/v6.c
  - Version 7: results/openai/20250421_180327/harnesses/defender.c:matchPrefix/v7.c
  - Size evolution: Initial 43 lines → Final 39 lines (-4 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250421_180327/verification/defender.c:matchPrefix/v1_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchPrefix/v1_report.md
  - results/openai/20250421_180327/verification/defender.c:matchPrefix/v2_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchPrefix/v2_report.md
  - results/openai/20250421_180327/verification/defender.c:matchPrefix/v3_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchPrefix/v3_report.md
  - results/openai/20250421_180327/verification/defender.c:matchPrefix/v4_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchPrefix/v4_report.md
  - results/openai/20250421_180327/verification/defender.c:matchPrefix/v5_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchPrefix/v5_report.md
  - results/openai/20250421_180327/verification/defender.c:matchPrefix/v6_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchPrefix/v6_report.md
  - results/openai/20250421_180327/verification/defender.c:matchPrefix/v7_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchPrefix/v7_report.md
  - results/openai/20250421_180327/verification/defender.c:matchPrefix/v8_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchPrefix/v8_report.md
  - results/openai/20250421_180327/verification/defender.c:matchPrefix/v9_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchPrefix/v9_report.md
  - results/openai/20250421_180327/verification/defender.c:matchPrefix/v10_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchPrefix/v10_report.md
  - results/openai/20250421_180327/verification/defender.c:matchPrefix/v11_results.txt
  - results/openai/20250421_180327/verification/defender.c:matchPrefix/v11_report.md