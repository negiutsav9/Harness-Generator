# CBMC Harness Generation Complete - Directory Mode - Openai

Total processing time: 329.43 seconds
Processed 3 source files.
Analyzed 10 functions.
Identified 8 functions with memory or arithmetic operations.
Generated 7 verification harnesses.
Performed 27 harness refinements (average 3.86 per function).

## File Analysis

### defender.c
Functions analyzed: 8
Functions verified: 7
Successful verifications: 5
Failed verifications: 2

## RAG Knowledge Base Statistics
Code functions stored: 109
Pattern templates: 16
Error patterns stored: 22
Successful solutions: 5

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

| Function | Version 1 | Version 2 | Version 3 | Version 4 | Version 5 | Version 6 |
| --- | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors |
| defender.c:Defender_GetTopic | 95.00% | 91.30% | 1 | 95.24% | 91.30% | 1 | 96.00% | 91.30% | 1 | 95.56% | 91.30% | 1 | 96.00% | 91.30% | 1 | 91.49% | 82.61% | 1 |
| defender.c:Defender_MatchTopic | 97.18% | 95.74% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| defender.c:extractThingNameLength | 100.00% | 100.00% | 1 | 100.00% | 100.00% | 1 | 100.00% | 100.00% | 1 | 100.00% | 100.00% | 1 | 100.00% | 100.00% | 0 | - | - | - |
| defender.c:getTopicLength | 93.10% | 90.48% | 1 | 100.00% | 100.00% | 1 | 100.00% | 100.00% | 1 | 100.00% | 100.00% | 0 | - | - | - | - | - | - |
| defender.c:matchApi | 93.33% | 100.00% | 1 | 94.03% | 100.00% | 1 | 94.03% | 100.00% | 1 | 93.10% | 100.00% | 1 | 93.10% | 100.00% | 1 | 100.00% | 100.00% | 1 |
| defender.c:matchBridge | 100.00% | 100.00% | 1 | 100.00% | 100.00% | 1 | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - |
| defender.c:matchPrefix | 100.00% | 100.00% | 1 | 100.00% | 100.00% | 1 | 100.00% | 100.00% | 1 | 100.00% | 100.00% | 0 | - | - | - | - | - | - |

**Metrics Legend:**
- **Total %**: Percentage of all reachable lines that were covered during verification.
- **Func %**: Percentage of target function lines that were covered.
- **Errors**: Number of verification errors or failures detected.

## Performance Metrics
Total execution time: 329.43 seconds
Average harness generation time: 5.29 seconds
Average verification time: 0.36 seconds
Average evaluation time: 0.33 seconds


### Function Timing Breakdown

| Function | Total Time (s) | Generation (s) | Verification (s) | Evaluation (s) | Refinements |
| -------- | -------------- | -------------- | ---------------- | -------------- | ----------- |
| defender.c:matchApi | 7.60 | 7.15 | 0.44 | 0.00 | 5 |
| defender.c:Defender_GetTopic | 7.15 | 6.53 | 0.62 | 0.00 | 5 |
| defender.c:matchPrefix | 7.00 | 6.27 | 0.42 | 0.30 | 4 |
| defender.c:extractThingNameLength | 6.75 | 5.94 | 0.35 | 0.47 | 5 |
| defender.c:Defender_MatchTopic | 6.74 | 5.95 | 0.48 | 0.30 | 1 |
| defender.c:matchBridge | 6.38 | 5.46 | 0.39 | 0.54 | 3 |
| defender.c:getTopicLength | 5.40 | 5.02 | 0.20 | 0.18 | 4 |
|  | 0.81 | 0.00 | 0.00 | 0.81 | 0 |

## Coverage Analysis
Coverage report available at: coverage/coverage_report.html

## Summary of Results

### Function: Defender_GetTopic (File: defender.c)
Status: FAILED
Refinements: 5
Message: PREPROCESSING ERROR: Macro definition error: file results/openai/20250502_115056/verification/includes/defender_config.h line 52: results/openai/20250502_115056/verification/includes/defender_config.h:52:13: warning: 'LogError' macro redefined [-Wmacro-redefined]; file results/openai/20250502_115056/verification/includes/defender_config.h line 54: results/openai/20250502_115056/verification/includes/defender_config.h:54:13: warning: 'LogWarn' macro redefined [-Wmacro-redefined]
Suggestions: Fix macro definitions and ensure they are properly defined

#### Coverage Metrics
- Function coverage: 82.61%

#### Coverage Evolution
- Initial coverage (v1): 91.30%
- Final coverage (v6): 82.61%
- Coverage improvement: -8.70%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250502_115056/harnesses/defender.c:Defender_GetTopic/v1.c
  - Version 2: results/openai/20250502_115056/harnesses/defender.c:Defender_GetTopic/v2.c
  - Version 3: results/openai/20250502_115056/harnesses/defender.c:Defender_GetTopic/v3.c
  - Version 4: results/openai/20250502_115056/harnesses/defender.c:Defender_GetTopic/v4.c
  - Version 5: results/openai/20250502_115056/harnesses/defender.c:Defender_GetTopic/v5.c
  - Version 6: results/openai/20250502_115056/harnesses/defender.c:Defender_GetTopic/v6.c
  - Size evolution: Initial 50 lines → Final 61 lines (+11 lines)
  - Refinement result: Some issues remain after 5 refinements

#### Verification Reports: 
  - results/openai/20250502_115056/verification/defender.c:Defender_GetTopic/v1_results.txt
  - results/openai/20250502_115056/verification/defender.c:Defender_GetTopic/v1_report.md
  - results/openai/20250502_115056/verification/defender.c:Defender_GetTopic/v2_results.txt
  - results/openai/20250502_115056/verification/defender.c:Defender_GetTopic/v2_report.md
  - results/openai/20250502_115056/verification/defender.c:Defender_GetTopic/v3_results.txt
  - results/openai/20250502_115056/verification/defender.c:Defender_GetTopic/v3_report.md
  - results/openai/20250502_115056/verification/defender.c:Defender_GetTopic/v4_results.txt
  - results/openai/20250502_115056/verification/defender.c:Defender_GetTopic/v4_report.md
  - results/openai/20250502_115056/verification/defender.c:Defender_GetTopic/v5_results.txt
  - results/openai/20250502_115056/verification/defender.c:Defender_GetTopic/v5_report.md
  - results/openai/20250502_115056/verification/defender.c:Defender_GetTopic/v6_results.txt
  - results/openai/20250502_115056/verification/defender.c:Defender_GetTopic/v6_report.md

### Function: Defender_MatchTopic (File: defender.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 95.74%

#### Harness Evolution:
  - Version 1: results/openai/20250502_115056/harnesses/defender.c:Defender_MatchTopic/v1.c

#### Verification Reports: 
  - results/openai/20250502_115056/verification/defender.c:Defender_MatchTopic/v1_results.txt
  - results/openai/20250502_115056/verification/defender.c:Defender_MatchTopic/v1_report.md
  - results/openai/20250502_115056/verification/defender.c:Defender_MatchTopic/v2_results.txt
  - results/openai/20250502_115056/verification/defender.c:Defender_MatchTopic/v2_report.md

### Function: extractThingNameLength (File: defender.c)
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
  - Version 1: results/openai/20250502_115056/harnesses/defender.c:extractThingNameLength/v1.c
  - Version 2: results/openai/20250502_115056/harnesses/defender.c:extractThingNameLength/v2.c
  - Version 3: results/openai/20250502_115056/harnesses/defender.c:extractThingNameLength/v3.c
  - Version 4: results/openai/20250502_115056/harnesses/defender.c:extractThingNameLength/v4.c
  - Version 5: results/openai/20250502_115056/harnesses/defender.c:extractThingNameLength/v5.c
  - Size evolution: Initial 43 lines → Final 44 lines (+1 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250502_115056/verification/defender.c:extractThingNameLength/v1_results.txt
  - results/openai/20250502_115056/verification/defender.c:extractThingNameLength/v1_report.md
  - results/openai/20250502_115056/verification/defender.c:extractThingNameLength/v2_results.txt
  - results/openai/20250502_115056/verification/defender.c:extractThingNameLength/v2_report.md
  - results/openai/20250502_115056/verification/defender.c:extractThingNameLength/v3_results.txt
  - results/openai/20250502_115056/verification/defender.c:extractThingNameLength/v3_report.md
  - results/openai/20250502_115056/verification/defender.c:extractThingNameLength/v4_results.txt
  - results/openai/20250502_115056/verification/defender.c:extractThingNameLength/v4_report.md
  - results/openai/20250502_115056/verification/defender.c:extractThingNameLength/v5_results.txt
  - results/openai/20250502_115056/verification/defender.c:extractThingNameLength/v5_report.md
  - results/openai/20250502_115056/verification/defender.c:extractThingNameLength/v6_results.txt
  - results/openai/20250502_115056/verification/defender.c:extractThingNameLength/v6_report.md

### Function: getTopicLength (File: defender.c)
Status: SUCCESS
Refinements: 4
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 90.48%
- Final coverage (v4): 100.00%
- Coverage improvement: 9.52%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250502_115056/harnesses/defender.c:getTopicLength/v1.c
  - Version 2: results/openai/20250502_115056/harnesses/defender.c:getTopicLength/v2.c
  - Version 3: results/openai/20250502_115056/harnesses/defender.c:getTopicLength/v3.c
  - Version 4: results/openai/20250502_115056/harnesses/defender.c:getTopicLength/v4.c
  - Size evolution: Initial 35 lines → Final 28 lines (-7 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250502_115056/verification/defender.c:getTopicLength/v1_results.txt
  - results/openai/20250502_115056/verification/defender.c:getTopicLength/v1_report.md
  - results/openai/20250502_115056/verification/defender.c:getTopicLength/v2_results.txt
  - results/openai/20250502_115056/verification/defender.c:getTopicLength/v2_report.md
  - results/openai/20250502_115056/verification/defender.c:getTopicLength/v3_results.txt
  - results/openai/20250502_115056/verification/defender.c:getTopicLength/v3_report.md
  - results/openai/20250502_115056/verification/defender.c:getTopicLength/v4_results.txt
  - results/openai/20250502_115056/verification/defender.c:getTopicLength/v4_report.md
  - results/openai/20250502_115056/verification/defender.c:getTopicLength/v5_results.txt
  - results/openai/20250502_115056/verification/defender.c:getTopicLength/v5_report.md

### Function: matchApi (File: defender.c)
Status: FAILED
Refinements: 5
Message: PREPROCESSING ERROR: Macro definition error: file results/openai/20250502_115056/verification/includes/defender_config.h line 52: results/openai/20250502_115056/verification/includes/defender_config.h:52:13: warning: 'LogError' macro redefined [-Wmacro-redefined]; file results/openai/20250502_115056/verification/includes/defender_config.h line 54: results/openai/20250502_115056/verification/includes/defender_config.h:54:13: warning: 'LogWarn' macro redefined [-Wmacro-redefined]
Suggestions: Fix macro definitions and ensure they are properly defined

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 100.00%
- Final coverage (v6): 100.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250502_115056/harnesses/defender.c:matchApi/v1.c
  - Version 2: results/openai/20250502_115056/harnesses/defender.c:matchApi/v2.c
  - Version 3: results/openai/20250502_115056/harnesses/defender.c:matchApi/v3.c
  - Version 4: results/openai/20250502_115056/harnesses/defender.c:matchApi/v4.c
  - Version 5: results/openai/20250502_115056/harnesses/defender.c:matchApi/v5.c
  - Version 6: results/openai/20250502_115056/harnesses/defender.c:matchApi/v6.c
  - Size evolution: Initial 59 lines → Final 54 lines (-5 lines)
  - Refinement result: Some issues remain after 5 refinements

#### Verification Reports: 
  - results/openai/20250502_115056/verification/defender.c:matchApi/v1_results.txt
  - results/openai/20250502_115056/verification/defender.c:matchApi/v1_report.md
  - results/openai/20250502_115056/verification/defender.c:matchApi/v2_results.txt
  - results/openai/20250502_115056/verification/defender.c:matchApi/v2_report.md
  - results/openai/20250502_115056/verification/defender.c:matchApi/v3_results.txt
  - results/openai/20250502_115056/verification/defender.c:matchApi/v3_report.md
  - results/openai/20250502_115056/verification/defender.c:matchApi/v4_results.txt
  - results/openai/20250502_115056/verification/defender.c:matchApi/v4_report.md
  - results/openai/20250502_115056/verification/defender.c:matchApi/v5_results.txt
  - results/openai/20250502_115056/verification/defender.c:matchApi/v5_report.md
  - results/openai/20250502_115056/verification/defender.c:matchApi/v6_results.txt
  - results/openai/20250502_115056/verification/defender.c:matchApi/v6_report.md

### Function: matchBridge (File: defender.c)
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
  - Version 1: results/openai/20250502_115056/harnesses/defender.c:matchBridge/v1.c
  - Version 2: results/openai/20250502_115056/harnesses/defender.c:matchBridge/v2.c
  - Version 3: results/openai/20250502_115056/harnesses/defender.c:matchBridge/v3.c
  - Size evolution: Initial 43 lines → Final 38 lines (-5 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250502_115056/verification/defender.c:matchBridge/v1_results.txt
  - results/openai/20250502_115056/verification/defender.c:matchBridge/v1_report.md
  - results/openai/20250502_115056/verification/defender.c:matchBridge/v2_results.txt
  - results/openai/20250502_115056/verification/defender.c:matchBridge/v2_report.md
  - results/openai/20250502_115056/verification/defender.c:matchBridge/v3_results.txt
  - results/openai/20250502_115056/verification/defender.c:matchBridge/v3_report.md
  - results/openai/20250502_115056/verification/defender.c:matchBridge/v4_results.txt
  - results/openai/20250502_115056/verification/defender.c:matchBridge/v4_report.md

### Function: matchPrefix (File: defender.c)
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
  - Version 1: results/openai/20250502_115056/harnesses/defender.c:matchPrefix/v1.c
  - Version 2: results/openai/20250502_115056/harnesses/defender.c:matchPrefix/v2.c
  - Version 3: results/openai/20250502_115056/harnesses/defender.c:matchPrefix/v3.c
  - Version 4: results/openai/20250502_115056/harnesses/defender.c:matchPrefix/v4.c
  - Size evolution: Initial 46 lines → Final 40 lines (-6 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250502_115056/verification/defender.c:matchPrefix/v1_results.txt
  - results/openai/20250502_115056/verification/defender.c:matchPrefix/v1_report.md
  - results/openai/20250502_115056/verification/defender.c:matchPrefix/v2_results.txt
  - results/openai/20250502_115056/verification/defender.c:matchPrefix/v2_report.md
  - results/openai/20250502_115056/verification/defender.c:matchPrefix/v3_results.txt
  - results/openai/20250502_115056/verification/defender.c:matchPrefix/v3_report.md
  - results/openai/20250502_115056/verification/defender.c:matchPrefix/v4_results.txt
  - results/openai/20250502_115056/verification/defender.c:matchPrefix/v4_report.md
  - results/openai/20250502_115056/verification/defender.c:matchPrefix/v5_results.txt
  - results/openai/20250502_115056/verification/defender.c:matchPrefix/v5_report.md