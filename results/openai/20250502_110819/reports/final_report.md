# CBMC Harness Generation Complete - Openai

Total processing time: 52.11 seconds
Analyzed 6 functions.
Identified 6 functions with memory or arithmetic operations.
Generated 5 verification harnesses.
Performed 7 harness refinements (average 1.40 per function).

## RAG Knowledge Base Statistics
Code functions stored: 9
Pattern templates: 16
Error patterns stored: 3
Successful solutions: 4

The RAG (Retrieval-Augmented Generation) knowledge base stores code functions, patterns, errors, and solutions to improve harness generation over time. Each run contributes to this knowledge base, helping future runs generate better harnesses with fewer iterations.

## Unit Proof Metrics Summary
Total reachable lines: 0
Total coverage: 0.00%
Total reachable lines for harnessed functions only: 0
Coverage of harnessed functions only: 0.00%
Number of reported errors: 0
Functions with full coverage: 5 of 5
Functions without errors: 5 of 5

### Note on Error Reporting:
- Errors are grouped by line number (one error per line)
- Errors about missing function bodies are excluded
- Loop unwinding assertions are excluded from error count

## Detailed Coverage Matrix by Function and Version

The table below shows detailed metrics for each function across different versions of the generated harnesses:

| Function | Version 1 | Version 2 | Version 3 | Version 4 |
| --- | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors | Total % | Func % | Errors |
| bubble_sort | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - |
| create_array | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - |
| filter_array | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - |
| find_median | 100.00% | 100.00% | 0 | 100.00% | 100.00% | 0 | 96.55% | 85.71% | 0 | 100.00% | 100.00% | 0 |
| merge_sorted_arrays | 100.00% | 100.00% | 0 | - | - | - | - | - | - | - | - | - |

**Metrics Legend:**
- **Total %**: Percentage of all reachable lines that were covered during verification.
- **Func %**: Percentage of target function lines that were covered.
- **Errors**: Number of verification errors or failures detected.

## Performance Metrics
Total execution time: 52.11 seconds
Average harness generation time: 2.76 seconds
Average verification time: 0.33 seconds
Average evaluation time: 0.50 seconds


### Function Timing Breakdown

| Function | Total Time (s) | Generation (s) | Verification (s) | Evaluation (s) | Refinements |
| -------- | -------------- | -------------- | ---------------- | -------------- | ----------- |
| create_array | 6.13 | 4.68 | 0.44 | 1.00 | 1 |
| merge_sorted_arrays | 4.39 | 3.78 | 0.39 | 0.21 | 1 |
| filter_array | 4.01 | 3.40 | 0.37 | 0.25 | 1 |
| bubble_sort | 3.11 | 2.22 | 0.38 | 0.51 | 1 |
| find_median | 2.85 | 2.45 | 0.40 | 0.00 | 3 |
|  | 1.01 | 0.00 | 0.00 | 1.01 | 0 |

## Coverage Analysis
Coverage report available at: coverage/coverage_report.html

## Summary of Results

### Function: bubble_sort
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250502_110819/harnesses/bubble_sort/v1.c

#### Verification Reports: 
  - results/openai/20250502_110819/verification/bubble_sort/v1_results.txt
  - results/openai/20250502_110819/verification/bubble_sort/v1_report.md
  - results/openai/20250502_110819/verification/bubble_sort/v2_results.txt
  - results/openai/20250502_110819/verification/bubble_sort/v2_report.md

### Function: create_array
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250502_110819/harnesses/create_array/v1.c

#### Verification Reports: 
  - results/openai/20250502_110819/verification/create_array/v1_results.txt
  - results/openai/20250502_110819/verification/create_array/v1_report.md
  - results/openai/20250502_110819/verification/create_array/v2_results.txt
  - results/openai/20250502_110819/verification/create_array/v2_report.md

### Function: merge_sorted_arrays
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250502_110819/harnesses/merge_sorted_arrays/v1.c

#### Verification Reports: 
  - results/openai/20250502_110819/verification/merge_sorted_arrays/v1_results.txt
  - results/openai/20250502_110819/verification/merge_sorted_arrays/v1_report.md
  - results/openai/20250502_110819/verification/merge_sorted_arrays/v2_results.txt
  - results/openai/20250502_110819/verification/merge_sorted_arrays/v2_report.md

### Function: filter_array
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250502_110819/harnesses/filter_array/v1.c

#### Verification Reports: 
  - results/openai/20250502_110819/verification/filter_array/v1_results.txt
  - results/openai/20250502_110819/verification/filter_array/v1_report.md
  - results/openai/20250502_110819/verification/filter_array/v2_results.txt
  - results/openai/20250502_110819/verification/filter_array/v2_report.md

### Function: find_median
Status: FAILED
Refinements: 3
Message: VERIFICATION FAILED: Arithmetic overflow detected
Suggestions: Add checks to prevent integer overflow

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 100.00%
- Final coverage (v4): 100.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250502_110819/harnesses/find_median/v1.c
  - Version 2: results/openai/20250502_110819/harnesses/find_median/v2.c
  - Version 3: results/openai/20250502_110819/harnesses/find_median/v3.c
  - Version 4: results/openai/20250502_110819/harnesses/find_median/v4.c
  - Size evolution: Initial 33 lines → Final 34 lines (+1 lines)
  - Refinement result: Some issues remain after 3 refinements

#### Verification Reports: 
  - results/openai/20250502_110819/verification/find_median/v1_results.txt
  - results/openai/20250502_110819/verification/find_median/v1_report.md
  - results/openai/20250502_110819/verification/find_median/v2_results.txt
  - results/openai/20250502_110819/verification/find_median/v2_report.md
  - results/openai/20250502_110819/verification/find_median/v3_results.txt
  - results/openai/20250502_110819/verification/find_median/v3_report.md
  - results/openai/20250502_110819/verification/find_median/v4_results.txt
  - results/openai/20250502_110819/verification/find_median/v4_report.md