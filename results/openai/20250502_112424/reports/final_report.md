# CBMC Harness Generation Complete - Directory Mode - Openai

Total processing time: 206.31 seconds
Processed 3 source files.
Analyzed 10 functions.
Identified 8 functions with memory or arithmetic operations.
Generated 7 verification harnesses.
Performed 11 harness refinements (average 1.57 per function).

## File Analysis

### defender.c
Functions analyzed: 8
Functions verified: 7
Successful verifications: 7
Failed verifications: 0

## RAG Knowledge Base Statistics
Code functions stored: 109
Pattern templates: 16
Error patterns stored: 6
Successful solutions: 6

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
| defender.c:Defender_GetTopic | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| defender.c:Defender_MatchTopic | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 0.00% | 0.00% | 0 | 100.00% | 100.00% | 0 |
| defender.c:extractThingNameLength | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| defender.c:getTopicLength | 93.33% | 90.48% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| defender.c:matchApi | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| defender.c:matchBridge | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| defender.c:matchPrefix | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |

**Metrics Legend:**
- **Total %**: Percentage of all reachable lines that were covered during verification.
- **Func %**: Percentage of target function lines that were covered.
- **Errors**: Number of verification errors or failures detected.

## Performance Metrics
Total execution time: 206.31 seconds
Average harness generation time: 6.09 seconds
Average verification time: 0.36 seconds
Average evaluation time: 0.37 seconds


### Function Timing Breakdown

| Function | Total Time (s) | Generation (s) | Verification (s) | Evaluation (s) | Refinements |
| -------- | -------------- | -------------- | ---------------- | -------------- | ----------- |
| defender.c:matchApi | 11.27 | 10.61 | 0.40 | 0.27 | 1 |
| defender.c:matchPrefix | 11.26 | 10.58 | 0.39 | 0.30 | 1 |
| defender.c:Defender_MatchTopic | 8.81 | 8.29 | 0.52 | 0.00 | 5 |
| defender.c:Defender_GetTopic | 5.97 | 5.04 | 0.65 | 0.29 | 1 |
| defender.c:matchBridge | 5.74 | 5.00 | 0.39 | 0.35 | 1 |
| defender.c:extractThingNameLength | 5.73 | 4.91 | 0.35 | 0.47 | 1 |
| defender.c:getTopicLength | 4.75 | 4.34 | 0.20 | 0.21 | 1 |
|  | 1.08 | 0.00 | 0.00 | 1.08 | 0 |

## Coverage Analysis
Coverage report available at: coverage/coverage_report.html

## Summary of Results

### Function: Defender_GetTopic (File: defender.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250502_112424/harnesses/defender.c:Defender_GetTopic/v1.c

#### Verification Reports: 
  - results/openai/20250502_112424/verification/defender.c:Defender_GetTopic/v1_results.txt
  - results/openai/20250502_112424/verification/defender.c:Defender_GetTopic/v1_report.md
  - results/openai/20250502_112424/verification/defender.c:Defender_GetTopic/v2_results.txt
  - results/openai/20250502_112424/verification/defender.c:Defender_GetTopic/v2_report.md

### Function: Defender_MatchTopic (File: defender.c)
Status: SUCCESS
Refinements: 5
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v6): 100.00%
- Coverage improvement: 100.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250502_112424/harnesses/defender.c:Defender_MatchTopic/v1.c
  - Version 2: results/openai/20250502_112424/harnesses/defender.c:Defender_MatchTopic/v2.c
  - Version 3: results/openai/20250502_112424/harnesses/defender.c:Defender_MatchTopic/v3.c
  - Version 4: results/openai/20250502_112424/harnesses/defender.c:Defender_MatchTopic/v4.c
  - Version 5: results/openai/20250502_112424/harnesses/defender.c:Defender_MatchTopic/v5.c
  - Version 6: results/openai/20250502_112424/harnesses/defender.c:Defender_MatchTopic/v6.c
  - Size evolution: Initial 90 lines → Final 101 lines (+11 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250502_112424/verification/defender.c:Defender_MatchTopic/v1_results.txt
  - results/openai/20250502_112424/verification/defender.c:Defender_MatchTopic/v1_report.md
  - results/openai/20250502_112424/verification/defender.c:Defender_MatchTopic/v2_results.txt
  - results/openai/20250502_112424/verification/defender.c:Defender_MatchTopic/v2_report.md
  - results/openai/20250502_112424/verification/defender.c:Defender_MatchTopic/v3_results.txt
  - results/openai/20250502_112424/verification/defender.c:Defender_MatchTopic/v3_report.md
  - results/openai/20250502_112424/verification/defender.c:Defender_MatchTopic/v4_results.txt
  - results/openai/20250502_112424/verification/defender.c:Defender_MatchTopic/v4_report.md
  - results/openai/20250502_112424/verification/defender.c:Defender_MatchTopic/v5_results.txt
  - results/openai/20250502_112424/verification/defender.c:Defender_MatchTopic/v5_report.md
  - results/openai/20250502_112424/verification/defender.c:Defender_MatchTopic/v6_results.txt
  - results/openai/20250502_112424/verification/defender.c:Defender_MatchTopic/v6_report.md

### Function: extractThingNameLength (File: defender.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250502_112424/harnesses/defender.c:extractThingNameLength/v1.c

#### Verification Reports: 
  - results/openai/20250502_112424/verification/defender.c:extractThingNameLength/v1_results.txt
  - results/openai/20250502_112424/verification/defender.c:extractThingNameLength/v1_report.md
  - results/openai/20250502_112424/verification/defender.c:extractThingNameLength/v2_results.txt
  - results/openai/20250502_112424/verification/defender.c:extractThingNameLength/v2_report.md

### Function: getTopicLength (File: defender.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 90.48%

#### Harness Evolution:
  - Version 1: results/openai/20250502_112424/harnesses/defender.c:getTopicLength/v1.c

#### Verification Reports: 
  - results/openai/20250502_112424/verification/defender.c:getTopicLength/v1_results.txt
  - results/openai/20250502_112424/verification/defender.c:getTopicLength/v1_report.md
  - results/openai/20250502_112424/verification/defender.c:getTopicLength/v2_results.txt
  - results/openai/20250502_112424/verification/defender.c:getTopicLength/v2_report.md

### Function: matchApi (File: defender.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250502_112424/harnesses/defender.c:matchApi/v1.c

#### Verification Reports: 
  - results/openai/20250502_112424/verification/defender.c:matchApi/v1_results.txt
  - results/openai/20250502_112424/verification/defender.c:matchApi/v1_report.md
  - results/openai/20250502_112424/verification/defender.c:matchApi/v2_results.txt
  - results/openai/20250502_112424/verification/defender.c:matchApi/v2_report.md

### Function: matchBridge (File: defender.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250502_112424/harnesses/defender.c:matchBridge/v1.c

#### Verification Reports: 
  - results/openai/20250502_112424/verification/defender.c:matchBridge/v1_results.txt
  - results/openai/20250502_112424/verification/defender.c:matchBridge/v1_report.md
  - results/openai/20250502_112424/verification/defender.c:matchBridge/v2_results.txt
  - results/openai/20250502_112424/verification/defender.c:matchBridge/v2_report.md

### Function: matchPrefix (File: defender.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250502_112424/harnesses/defender.c:matchPrefix/v1.c

#### Verification Reports: 
  - results/openai/20250502_112424/verification/defender.c:matchPrefix/v1_results.txt
  - results/openai/20250502_112424/verification/defender.c:matchPrefix/v1_report.md
  - results/openai/20250502_112424/verification/defender.c:matchPrefix/v2_results.txt
  - results/openai/20250502_112424/verification/defender.c:matchPrefix/v2_report.md