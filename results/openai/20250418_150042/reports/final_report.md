# CBMC Harness Generation Complete - Directory Mode - Openai

Total processing time: 7116.41 seconds
Processed 18 source files.
Analyzed 210 functions.
Identified 109 functions with memory or arithmetic operations.
Generated 50 verification harnesses.
Performed 268 harness refinements (average 5.36 per function).

## File Analysis

### core_mqtt.c
Functions analyzed: 47
Functions verified: 47
Successful verifications: 29
Failed verifications: 18

### core_mqtt_serializer.c
Functions analyzed: 43
Functions verified: 3
Successful verifications: 2
Failed verifications: 1

### core_mqtt_state.c
Functions analyzed: 19
Functions verified: 0

## RAG Knowledge Base Statistics
Code functions stored: 233
Pattern templates: 16
Error patterns stored: 237
Successful solutions: 31

The RAG (Retrieval-Augmented Generation) knowledge base stores code functions, patterns, errors, and solutions to improve harness generation over time. Each run contributes to this knowledge base, helping future runs generate better harnesses with fewer iterations.

## Unit Proof Metrics Summary
Total reachable lines: 0
Total coverage: 0.00%
Total reachable lines for harnessed functions only: 0
Coverage of harnessed functions only: 0.00%
Number of reported errors: 0
Functions with full coverage: 12 of 50
Functions without errors: 0 of 50

### Note on Error Reporting:
- Errors are grouped by line number (one error per line)
- Errors about missing function bodies are excluded
- Loop unwinding assertions are excluded from error count

## Detailed Coverage Matrix by Function and Version

The table below shows detailed metrics for each function across different versions of the generated harnesses:

| Function | Version 1 |||| Version 2 |||| Version 3 |||| Version 4 |||| Version 5 |||| Version 6 |||| Version 7 |||| Version 8 |||| Version 9 |||| Version 10 |||
| --- | Total % | Func % | Errors || Total % | Func % | Errors || Total % | Func % | Errors || Total % | Func % | Errors || Total % | Func % | Errors || Total % | Func % | Errors || Total % | Func % | Errors || Total % | Func % | Errors || Total % | Func % | Errors || Total % | Func % | Errors |
| core_mqtt.c:MQTT_CancelCallback | 92.31% | 81.82% | N/A || 93.10% | 81.82% | N/A || 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:MQTT_CheckConnectStatus | 85.19% | 75.00% | N/A || 85.71% | 75.00% | N/A || 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:MQTT_Connect | 80.65% | 72.09% | N/A || 80.33% | 72.09% | N/A || 84.42% | 72.09% | N/A || 82.35% | 72.09% | N/A || 84.81% | 72.09% | N/A || 82.35% | 72.09% | N/A || 84.21% | 72.09% | N/A || 82.61% | 72.09% | N/A || 85.37% | 72.09% | N/A || 82.61% | 72.09% | N/A |
| core_mqtt.c:MQTT_Disconnect | 100.00% | 100.00% | N/A || 98.15% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A |
| core_mqtt.c:MQTT_GetBytesInMQTTVec | 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A |
| core_mqtt.c:MQTT_GetPacketId | 89.47% | 77.78% | N/A || 90.00% | 77.78% | N/A || 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:MQTT_GetSubAckStatusCodes | 100.00% | 100.00% | N/A || 97.33% | 100.00% | N/A || 95.65% | 91.30% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:MQTT_Init | 0.00% | 0.00% | N/A || 95.36% | 72.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:MQTT_InitRetransmits | 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:MQTT_InitStatefulQoS | 0.00% | 0.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:MQTT_MatchTopic | 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:MQTT_Ping | 80.00% | 73.33% | N/A || 80.49% | 73.33% | N/A || 100.00% | 100.00% | N/A || 97.14% | 96.67% | N/A || 75.00% | 70.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A |
| core_mqtt.c:MQTT_ProcessLoop | 0.00% | 0.00% | N/A || - | - | - || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A |
| core_mqtt.c:MQTT_Publish | 70.37% | 62.79% | N/A || 75.76% | 62.79% | N/A || 90.16% | 86.05% | N/A || 61.43% | 37.21% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:MQTT_ReceiveLoop | 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A |
| core_mqtt.c:MQTT_SerializeMQTTVec | 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A |
| core_mqtt.c:MQTT_Status_strerror | 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:MQTT_Subscribe | 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 100.00% | 100.00% | N/A || 97.50% | 100.00% | N/A |
| core_mqtt.c:MQTT_Unsubscribe | 85.29% | 78.26% | N/A || 86.11% | 78.26% | N/A || 100.00% | 100.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A |
| core_mqtt.c:addEncodedStringToVector | 58.54% | 0.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:calculateElapsedTime | 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A |
| core_mqtt.c:discardPacket | 30.77% | 0.00% | N/A || 37.21% | 0.00% | N/A || 27.03% | 0.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:discardStoredPacket | 51.92% | 0.00% | N/A || 51.92% | 0.00% | N/A || 50.00% | 0.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:getAckFromPacketType | 21.05% | 0.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:getAckTypeToSend | 15.79% | 0.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:handleCleanSession | 0.00% | 0.00% | N/A || 76.71% | 0.00% | N/A || 75.00% | 0.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:handleIncomingAck | 29.55% | 0.00% | N/A || 29.55% | 0.00% | N/A || 22.50% | 0.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:handleIncomingPublish | 22.92% | 0.00% | N/A || 30.19% | 0.00% | N/A || 27.45% | 0.00% | N/A || 26.00% | 0.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:handleKeepAlive | 20.00% | 0.00% | N/A || 25.00% | 0.00% | N/A || 29.41% | 0.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:handlePublishAcks | 32.61% | 0.00% | N/A || 44.64% | 0.00% | N/A || 31.11% | 0.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:handleUncleanSessionResumption | 20.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A |
| core_mqtt.c:matchEndWildcardsSpecialCases | 54.17% | 0.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:matchTopicFilter | 33.33% | 0.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:matchWildcards | 53.52% | 0.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:receiveConnack | 0.00% | 0.00% | N/A || 48.57% | 0.00% | N/A || 29.41% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A |
| core_mqtt.c:receivePacket | 54.55% | 0.00% | N/A || 57.14% | 0.00% | N/A || 50.00% | 0.00% | N/A || 53.12% | 0.00% | N/A || 46.43% | 0.00% | N/A || 53.12% | 0.00% | N/A || 46.43% | 0.00% | N/A || 53.12% | 0.00% | N/A || 46.43% | 0.00% | N/A || 53.12% | 0.00% | N/A |
| core_mqtt.c:receiveSingleIteration | 19.35% | 0.00% | N/A || 21.88% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A |
| core_mqtt.c:recvExact | 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A |
| core_mqtt.c:sendBuffer | 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A |
| core_mqtt.c:sendConnectWithoutCopy | 22.58% | 0.00% | N/A || 48.94% | 0.00% | N/A || 36.28% | 0.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:sendMessageVector | 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A |
| core_mqtt.c:sendPublishAcks | 20.00% | 0.00% | N/A || 23.40% | 0.00% | N/A || 26.53% | 0.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:sendPublishWithoutCopy | 42.50% | 0.00% | N/A || 45.24% | 0.00% | N/A || 40.26% | 0.00% | N/A || 38.67% | 0.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:sendSubscribeWithoutCopy | 29.85% | 0.00% | N/A || 33.80% | 0.00% | N/A || 31.88% | 0.00% | N/A || 32.86% | 0.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:sendUnsubscribeWithoutCopy | 34.92% | 0.00% | N/A || 46.05% | 0.00% | N/A || 35.94% | 0.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt.c:validatePublishParams | 71.43% | 0.00% | N/A || 75.44% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A |
| core_mqtt.c:validateSubscribeUnsubscribeParams | 52.63% | 0.00% | N/A || 55.00% | 0.00% | N/A || 57.14% | 0.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt_serializer.c:MQTT_DeserializeAck | 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A || 0.00% | 0.00% | N/A |
| core_mqtt_serializer.c:MQTT_DeserializePublish | 100.00% | 100.00% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |
| core_mqtt_serializer.c:MQTT_GetConnectPacketSize | 97.89% | 92.31% | N/A || 98.06% | 92.31% | N/A || 91.30% | 76.92% | N/A || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - || - | - | - |

**Metrics Legend:**
- **Total %**: Percentage of all reachable lines that were covered during verification.
- **Func %**: Percentage of target function lines that were covered.
- **Errors**: Number of verification errors or failures detected.

## Performance Metrics
Average harness generation time: 12.08 seconds
Average verification time: 2.54 seconds
Average evaluation time: 0.00 seconds

## Coverage Analysis
Coverage report available at: coverage/coverage_report.html

## Summary of Results

### Function: MQTT_CancelCallback (File: core_mqtt.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 81.82%
- Final coverage (v3): 100.00%
- Coverage improvement: 18.18%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_CancelCallback/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_CancelCallback/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_CancelCallback/v3.c
  - Size evolution: Initial 46 lines → Final 39 lines (-7 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_CancelCallback/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_CancelCallback/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_CancelCallback/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_CancelCallback/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_CancelCallback/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_CancelCallback/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_CancelCallback/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_CancelCallback/v4_report.md

### Function: MQTT_CheckConnectStatus (File: core_mqtt.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 75.00%
- Final coverage (v3): 100.00%
- Coverage improvement: 25.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_CheckConnectStatus/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_CheckConnectStatus/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_CheckConnectStatus/v3.c
  - Size evolution: Initial 35 lines → Final 34 lines (-1 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_CheckConnectStatus/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_CheckConnectStatus/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_CheckConnectStatus/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_CheckConnectStatus/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_CheckConnectStatus/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_CheckConnectStatus/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_CheckConnectStatus/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_CheckConnectStatus/v4_report.md

### Function: MQTT_Connect (File: core_mqtt.c)
Status: FAILED
Refinements: 10
Message: VERIFICATION FAILED: Null pointer dereference detected
Suggestions: Add null pointer checks before dereferencing pointers

#### Coverage Metrics
- Function coverage: 72.09%

#### Coverage Evolution
- Initial coverage (v1): 72.09%
- Final coverage (v10): 72.09%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Connect/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Connect/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Connect/v3.c
  - Version 4: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Connect/v4.c
  - Version 5: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Connect/v5.c
  - Version 6: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Connect/v6.c
  - Version 7: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Connect/v7.c
  - Version 8: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Connect/v8.c
  - Version 9: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Connect/v9.c
  - Version 10: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Connect/v10.c
  - Size evolution: Initial 52 lines → Final 63 lines (+11 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Connect/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Connect/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Connect/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Connect/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Connect/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Connect/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Connect/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Connect/v4_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Connect/v5_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Connect/v5_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Connect/v6_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Connect/v6_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Connect/v7_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Connect/v7_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Connect/v8_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Connect/v8_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Connect/v9_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Connect/v9_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Connect/v10_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Connect/v10_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Connect/v11_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Connect/v11_report.md

### Function: MQTT_Disconnect (File: core_mqtt.c)
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
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Disconnect/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Disconnect/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Disconnect/v3.c
  - Version 4: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Disconnect/v4.c
  - Version 5: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Disconnect/v5.c
  - Version 6: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Disconnect/v6.c
  - Version 7: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Disconnect/v7.c
  - Version 8: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Disconnect/v8.c
  - Version 9: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Disconnect/v9.c
  - Version 10: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Disconnect/v10.c
  - Size evolution: Initial 51 lines → Final 64 lines (+13 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Disconnect/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Disconnect/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Disconnect/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Disconnect/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Disconnect/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Disconnect/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Disconnect/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Disconnect/v4_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Disconnect/v5_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Disconnect/v5_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Disconnect/v6_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Disconnect/v6_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Disconnect/v7_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Disconnect/v7_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Disconnect/v8_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Disconnect/v8_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Disconnect/v9_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Disconnect/v9_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Disconnect/v10_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Disconnect/v10_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Disconnect/v11_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Disconnect/v11_report.md

### Function: MQTT_GetBytesInMQTTVec (File: core_mqtt.c)
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
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_GetBytesInMQTTVec/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_GetBytesInMQTTVec/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_GetBytesInMQTTVec/v3.c
  - Version 4: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_GetBytesInMQTTVec/v4.c
  - Version 5: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_GetBytesInMQTTVec/v5.c
  - Version 6: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_GetBytesInMQTTVec/v6.c
  - Version 7: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_GetBytesInMQTTVec/v7.c
  - Version 8: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_GetBytesInMQTTVec/v8.c
  - Version 9: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_GetBytesInMQTTVec/v9.c
  - Version 10: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_GetBytesInMQTTVec/v10.c
  - Size evolution: Initial 57 lines → Final 171 lines (+114 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetBytesInMQTTVec/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetBytesInMQTTVec/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetBytesInMQTTVec/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetBytesInMQTTVec/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetBytesInMQTTVec/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetBytesInMQTTVec/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetBytesInMQTTVec/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetBytesInMQTTVec/v4_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetBytesInMQTTVec/v5_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetBytesInMQTTVec/v5_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetBytesInMQTTVec/v6_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetBytesInMQTTVec/v6_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetBytesInMQTTVec/v7_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetBytesInMQTTVec/v7_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetBytesInMQTTVec/v8_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetBytesInMQTTVec/v8_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetBytesInMQTTVec/v9_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetBytesInMQTTVec/v9_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetBytesInMQTTVec/v10_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetBytesInMQTTVec/v10_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetBytesInMQTTVec/v11_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetBytesInMQTTVec/v11_report.md

### Function: MQTT_GetPacketId (File: core_mqtt.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 77.78%
- Final coverage (v3): 100.00%
- Coverage improvement: 22.22%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_GetPacketId/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_GetPacketId/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_GetPacketId/v3.c
  - Size evolution: Initial 33 lines → Final 29 lines (-4 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetPacketId/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetPacketId/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetPacketId/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetPacketId/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetPacketId/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetPacketId/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetPacketId/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetPacketId/v4_report.md

### Function: MQTT_GetSubAckStatusCodes (File: core_mqtt.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 91.30%

#### Coverage Evolution
- Initial coverage (v1): 100.00%
- Final coverage (v3): 91.30%
- Coverage improvement: -8.70%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_GetSubAckStatusCodes/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_GetSubAckStatusCodes/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_GetSubAckStatusCodes/v3.c
  - Size evolution: Initial 96 lines → Final 58 lines (-38 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetSubAckStatusCodes/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetSubAckStatusCodes/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetSubAckStatusCodes/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetSubAckStatusCodes/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetSubAckStatusCodes/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetSubAckStatusCodes/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetSubAckStatusCodes/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_GetSubAckStatusCodes/v4_report.md

### Function: MQTT_Init (File: core_mqtt.c)
Status: SUCCESS
Refinements: 2
Message: Verification successful

#### Coverage Metrics
- Function coverage: 72.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v2): 72.00%
- Coverage improvement: 72.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Init/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Init/v2.c
  - Size evolution: Initial 61 lines → Final 190 lines (+129 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Init/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Init/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Init/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Init/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Init/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Init/v3_report.md

### Function: MQTT_InitRetransmits (File: core_mqtt.c)
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
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_InitRetransmits/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_InitRetransmits/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_InitRetransmits/v3.c
  - Size evolution: Initial 57 lines → Final 58 lines (+1 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_InitRetransmits/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_InitRetransmits/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_InitRetransmits/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_InitRetransmits/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_InitRetransmits/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_InitRetransmits/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_InitRetransmits/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_InitRetransmits/v4_report.md

### Function: MQTT_InitStatefulQoS (File: core_mqtt.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v3): 100.00%
- Coverage improvement: 100.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_InitStatefulQoS/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_InitStatefulQoS/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_InitStatefulQoS/v3.c
  - Size evolution: Initial 83 lines → Final 127 lines (+44 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_InitStatefulQoS/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_InitStatefulQoS/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_InitStatefulQoS/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_InitStatefulQoS/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_InitStatefulQoS/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_InitStatefulQoS/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_InitStatefulQoS/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_InitStatefulQoS/v4_report.md

### Function: MQTT_MatchTopic (File: core_mqtt.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_MatchTopic/v1.c

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_MatchTopic/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_MatchTopic/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_MatchTopic/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_MatchTopic/v2_report.md

### Function: MQTT_Ping (File: core_mqtt.c)
Status: FAILED
Refinements: 10
Message: VERIFICATION FAILED: Unspecified verification error
Suggestions: Review the full verification output for details

#### Coverage Metrics
- Function coverage: 0.00%

#### Coverage Evolution
- Initial coverage (v1): 73.33%
- Final coverage (v10): 0.00%
- Coverage improvement: -73.33%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Ping/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Ping/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Ping/v3.c
  - Version 4: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Ping/v4.c
  - Version 5: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Ping/v5.c
  - Version 6: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Ping/v6.c
  - Version 7: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Ping/v7.c
  - Version 8: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Ping/v8.c
  - Version 9: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Ping/v9.c
  - Version 10: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Ping/v10.c
  - Size evolution: Initial 38 lines → Final 132 lines (+94 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Ping/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Ping/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Ping/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Ping/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Ping/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Ping/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Ping/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Ping/v4_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Ping/v5_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Ping/v5_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Ping/v6_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Ping/v6_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Ping/v7_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Ping/v7_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Ping/v8_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Ping/v8_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Ping/v9_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Ping/v9_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Ping/v10_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Ping/v10_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Ping/v11_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Ping/v11_report.md

### Function: MQTT_ProcessLoop (File: core_mqtt.c)
Status: FAILED
Refinements: 10
Message: VERIFICATION FAILED: Null pointer dereference detected
Suggestions: Add null pointer checks before dereferencing pointers

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v10): 100.00%
- Coverage improvement: 100.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_ProcessLoop/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_ProcessLoop/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_ProcessLoop/v3.c
  - Version 4: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_ProcessLoop/v4.c
  - Version 5: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_ProcessLoop/v5.c
  - Version 6: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_ProcessLoop/v6.c
  - Version 7: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_ProcessLoop/v7.c
  - Version 8: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_ProcessLoop/v8.c
  - Version 9: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_ProcessLoop/v9.c
  - Version 10: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_ProcessLoop/v10.c
  - Size evolution: Initial 61 lines → Final 67 lines (+6 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ProcessLoop/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ProcessLoop/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ProcessLoop/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ProcessLoop/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ProcessLoop/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ProcessLoop/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ProcessLoop/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ProcessLoop/v4_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ProcessLoop/v5_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ProcessLoop/v5_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ProcessLoop/v6_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ProcessLoop/v6_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ProcessLoop/v7_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ProcessLoop/v7_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ProcessLoop/v8_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ProcessLoop/v8_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ProcessLoop/v9_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ProcessLoop/v9_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ProcessLoop/v10_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ProcessLoop/v10_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ProcessLoop/v11_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ProcessLoop/v11_report.md

### Function: MQTT_Publish (File: core_mqtt.c)
Status: SUCCESS
Refinements: 4
Message: Verification successful

#### Coverage Metrics
- Function coverage: 37.21%

#### Coverage Evolution
- Initial coverage (v1): 62.79%
- Final coverage (v4): 37.21%
- Coverage improvement: -25.58%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Publish/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Publish/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Publish/v3.c
  - Version 4: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Publish/v4.c
  - Size evolution: Initial 42 lines → Final 68 lines (+26 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Publish/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Publish/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Publish/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Publish/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Publish/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Publish/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Publish/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Publish/v4_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Publish/v5_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Publish/v5_report.md

### Function: MQTT_ReceiveLoop (File: core_mqtt.c)
Status: FAILED
Refinements: 10
Message: VERIFICATION FAILED: Null pointer dereference detected
Suggestions: Add null pointer checks before dereferencing pointers. Also consider simplifying the harness to improve verification speed

#### Coverage Metrics
- Function coverage: 100.00%

#### Coverage Evolution
- Initial coverage (v1): 100.00%
- Final coverage (v10): 100.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_ReceiveLoop/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_ReceiveLoop/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_ReceiveLoop/v3.c
  - Version 4: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_ReceiveLoop/v4.c
  - Version 5: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_ReceiveLoop/v5.c
  - Version 6: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_ReceiveLoop/v6.c
  - Version 7: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_ReceiveLoop/v7.c
  - Version 8: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_ReceiveLoop/v8.c
  - Version 9: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_ReceiveLoop/v9.c
  - Version 10: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_ReceiveLoop/v10.c
  - Size evolution: Initial 62 lines → Final 79 lines (+17 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ReceiveLoop/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ReceiveLoop/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ReceiveLoop/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ReceiveLoop/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ReceiveLoop/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ReceiveLoop/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ReceiveLoop/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ReceiveLoop/v4_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ReceiveLoop/v5_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ReceiveLoop/v5_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ReceiveLoop/v6_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ReceiveLoop/v6_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ReceiveLoop/v7_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ReceiveLoop/v7_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ReceiveLoop/v8_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ReceiveLoop/v8_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ReceiveLoop/v9_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ReceiveLoop/v9_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ReceiveLoop/v10_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ReceiveLoop/v10_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ReceiveLoop/v11_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_ReceiveLoop/v11_report.md

### Function: MQTT_SerializeMQTTVec (File: core_mqtt.c)
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
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_SerializeMQTTVec/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_SerializeMQTTVec/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_SerializeMQTTVec/v3.c
  - Version 4: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_SerializeMQTTVec/v4.c
  - Version 5: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_SerializeMQTTVec/v5.c
  - Version 6: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_SerializeMQTTVec/v6.c
  - Version 7: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_SerializeMQTTVec/v7.c
  - Version 8: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_SerializeMQTTVec/v8.c
  - Version 9: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_SerializeMQTTVec/v9.c
  - Version 10: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_SerializeMQTTVec/v10.c
  - Size evolution: Initial 69 lines → Final 127 lines (+58 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_SerializeMQTTVec/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_SerializeMQTTVec/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_SerializeMQTTVec/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_SerializeMQTTVec/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_SerializeMQTTVec/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_SerializeMQTTVec/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_SerializeMQTTVec/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_SerializeMQTTVec/v4_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_SerializeMQTTVec/v5_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_SerializeMQTTVec/v5_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_SerializeMQTTVec/v6_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_SerializeMQTTVec/v6_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_SerializeMQTTVec/v7_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_SerializeMQTTVec/v7_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_SerializeMQTTVec/v8_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_SerializeMQTTVec/v8_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_SerializeMQTTVec/v9_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_SerializeMQTTVec/v9_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_SerializeMQTTVec/v10_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_SerializeMQTTVec/v10_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_SerializeMQTTVec/v11_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_SerializeMQTTVec/v11_report.md

### Function: MQTT_Status_strerror (File: core_mqtt.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Status_strerror/v1.c

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Status_strerror/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Status_strerror/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Status_strerror/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Status_strerror/v2_report.md

### Function: MQTT_Subscribe (File: core_mqtt.c)
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
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Subscribe/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Subscribe/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Subscribe/v3.c
  - Version 4: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Subscribe/v4.c
  - Version 5: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Subscribe/v5.c
  - Version 6: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Subscribe/v6.c
  - Version 7: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Subscribe/v7.c
  - Version 8: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Subscribe/v8.c
  - Version 9: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Subscribe/v9.c
  - Version 10: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Subscribe/v10.c
  - Size evolution: Initial 35 lines → Final 55 lines (+20 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Subscribe/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Subscribe/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Subscribe/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Subscribe/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Subscribe/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Subscribe/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Subscribe/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Subscribe/v4_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Subscribe/v5_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Subscribe/v5_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Subscribe/v6_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Subscribe/v6_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Subscribe/v7_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Subscribe/v7_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Subscribe/v8_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Subscribe/v8_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Subscribe/v9_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Subscribe/v9_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Subscribe/v10_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Subscribe/v10_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Subscribe/v11_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Subscribe/v11_report.md

### Function: MQTT_Unsubscribe (File: core_mqtt.c)
Status: FAILED
Refinements: 10
Message: VERIFICATION FAILED: Unspecified verification error
Suggestions: Review the full verification output for details

#### Coverage Metrics
- Function coverage: 0.00%

#### Coverage Evolution
- Initial coverage (v1): 78.26%
- Final coverage (v10): 0.00%
- Coverage improvement: -78.26%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Unsubscribe/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Unsubscribe/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Unsubscribe/v3.c
  - Version 4: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Unsubscribe/v4.c
  - Version 5: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Unsubscribe/v5.c
  - Version 6: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Unsubscribe/v6.c
  - Version 7: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Unsubscribe/v7.c
  - Version 8: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Unsubscribe/v8.c
  - Version 9: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Unsubscribe/v9.c
  - Version 10: results/openai/20250418_150042/harnesses/core_mqtt.c:MQTT_Unsubscribe/v10.c
  - Size evolution: Initial 38 lines → Final 157 lines (+119 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Unsubscribe/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Unsubscribe/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Unsubscribe/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Unsubscribe/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Unsubscribe/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Unsubscribe/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Unsubscribe/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Unsubscribe/v4_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Unsubscribe/v5_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Unsubscribe/v5_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Unsubscribe/v6_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Unsubscribe/v6_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Unsubscribe/v7_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Unsubscribe/v7_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Unsubscribe/v8_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Unsubscribe/v8_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Unsubscribe/v9_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Unsubscribe/v9_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Unsubscribe/v10_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Unsubscribe/v10_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Unsubscribe/v11_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:MQTT_Unsubscribe/v11_report.md

### Function: addEncodedStringToVector (File: core_mqtt.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 0.00%

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:addEncodedStringToVector/v1.c

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:addEncodedStringToVector/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:addEncodedStringToVector/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:addEncodedStringToVector/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:addEncodedStringToVector/v2_report.md

### Function: calculateElapsedTime (File: core_mqtt.c)
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
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:calculateElapsedTime/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:calculateElapsedTime/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:calculateElapsedTime/v3.c
  - Version 4: results/openai/20250418_150042/harnesses/core_mqtt.c:calculateElapsedTime/v4.c
  - Version 5: results/openai/20250418_150042/harnesses/core_mqtt.c:calculateElapsedTime/v5.c
  - Version 6: results/openai/20250418_150042/harnesses/core_mqtt.c:calculateElapsedTime/v6.c
  - Version 7: results/openai/20250418_150042/harnesses/core_mqtt.c:calculateElapsedTime/v7.c
  - Version 8: results/openai/20250418_150042/harnesses/core_mqtt.c:calculateElapsedTime/v8.c
  - Version 9: results/openai/20250418_150042/harnesses/core_mqtt.c:calculateElapsedTime/v9.c
  - Version 10: results/openai/20250418_150042/harnesses/core_mqtt.c:calculateElapsedTime/v10.c
  - Size evolution: Initial 23 lines → Final 117 lines (+94 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:calculateElapsedTime/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:calculateElapsedTime/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:calculateElapsedTime/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:calculateElapsedTime/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:calculateElapsedTime/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:calculateElapsedTime/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:calculateElapsedTime/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:calculateElapsedTime/v4_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:calculateElapsedTime/v5_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:calculateElapsedTime/v5_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:calculateElapsedTime/v6_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:calculateElapsedTime/v6_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:calculateElapsedTime/v7_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:calculateElapsedTime/v7_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:calculateElapsedTime/v8_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:calculateElapsedTime/v8_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:calculateElapsedTime/v9_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:calculateElapsedTime/v9_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:calculateElapsedTime/v10_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:calculateElapsedTime/v10_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:calculateElapsedTime/v11_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:calculateElapsedTime/v11_report.md

### Function: discardPacket (File: core_mqtt.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 0.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v3): 0.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:discardPacket/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:discardPacket/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:discardPacket/v3.c
  - Size evolution: Initial 43 lines → Final 36 lines (-7 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:discardPacket/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:discardPacket/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:discardPacket/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:discardPacket/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:discardPacket/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:discardPacket/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:discardPacket/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:discardPacket/v4_report.md

### Function: discardStoredPacket (File: core_mqtt.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 0.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v3): 0.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:discardStoredPacket/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:discardStoredPacket/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:discardStoredPacket/v3.c
  - Size evolution: Initial 57 lines → Final 49 lines (-8 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:discardStoredPacket/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:discardStoredPacket/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:discardStoredPacket/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:discardStoredPacket/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:discardStoredPacket/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:discardStoredPacket/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:discardStoredPacket/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:discardStoredPacket/v4_report.md

### Function: getAckFromPacketType (File: core_mqtt.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 0.00%

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:getAckFromPacketType/v1.c

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:getAckFromPacketType/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:getAckFromPacketType/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:getAckFromPacketType/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:getAckFromPacketType/v2_report.md

### Function: getAckTypeToSend (File: core_mqtt.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 0.00%

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:getAckTypeToSend/v1.c

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:getAckTypeToSend/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:getAckTypeToSend/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:getAckTypeToSend/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:getAckTypeToSend/v2_report.md

### Function: handleCleanSession (File: core_mqtt.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 0.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v3): 0.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:handleCleanSession/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:handleCleanSession/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:handleCleanSession/v3.c
  - Size evolution: Initial 87 lines → Final 116 lines (+29 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:handleCleanSession/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleCleanSession/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handleCleanSession/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleCleanSession/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handleCleanSession/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleCleanSession/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handleCleanSession/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleCleanSession/v4_report.md

### Function: handleIncomingAck (File: core_mqtt.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 0.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v3): 0.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:handleIncomingAck/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:handleIncomingAck/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:handleIncomingAck/v3.c
  - Size evolution: Initial 60 lines → Final 42 lines (-18 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:handleIncomingAck/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleIncomingAck/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handleIncomingAck/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleIncomingAck/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handleIncomingAck/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleIncomingAck/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handleIncomingAck/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleIncomingAck/v4_report.md

### Function: handleIncomingPublish (File: core_mqtt.c)
Status: SUCCESS
Refinements: 4
Message: Verification successful

#### Coverage Metrics
- Function coverage: 0.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v4): 0.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:handleIncomingPublish/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:handleIncomingPublish/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:handleIncomingPublish/v3.c
  - Version 4: results/openai/20250418_150042/harnesses/core_mqtt.c:handleIncomingPublish/v4.c
  - Size evolution: Initial 32 lines → Final 38 lines (+6 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:handleIncomingPublish/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleIncomingPublish/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handleIncomingPublish/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleIncomingPublish/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handleIncomingPublish/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleIncomingPublish/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handleIncomingPublish/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleIncomingPublish/v4_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handleIncomingPublish/v5_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleIncomingPublish/v5_report.md

### Function: handleKeepAlive (File: core_mqtt.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 0.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v3): 0.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:handleKeepAlive/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:handleKeepAlive/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:handleKeepAlive/v3.c
  - Size evolution: Initial 36 lines → Final 36 lines (0 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:handleKeepAlive/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleKeepAlive/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handleKeepAlive/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleKeepAlive/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handleKeepAlive/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleKeepAlive/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handleKeepAlive/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleKeepAlive/v4_report.md

### Function: handlePublishAcks (File: core_mqtt.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 0.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v3): 0.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:handlePublishAcks/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:handlePublishAcks/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:handlePublishAcks/v3.c
  - Size evolution: Initial 43 lines → Final 43 lines (0 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:handlePublishAcks/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handlePublishAcks/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handlePublishAcks/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handlePublishAcks/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handlePublishAcks/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handlePublishAcks/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handlePublishAcks/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handlePublishAcks/v4_report.md

### Function: handleUncleanSessionResumption (File: core_mqtt.c)
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
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:handleUncleanSessionResumption/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:handleUncleanSessionResumption/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:handleUncleanSessionResumption/v3.c
  - Version 4: results/openai/20250418_150042/harnesses/core_mqtt.c:handleUncleanSessionResumption/v4.c
  - Version 5: results/openai/20250418_150042/harnesses/core_mqtt.c:handleUncleanSessionResumption/v5.c
  - Version 6: results/openai/20250418_150042/harnesses/core_mqtt.c:handleUncleanSessionResumption/v6.c
  - Version 7: results/openai/20250418_150042/harnesses/core_mqtt.c:handleUncleanSessionResumption/v7.c
  - Version 8: results/openai/20250418_150042/harnesses/core_mqtt.c:handleUncleanSessionResumption/v8.c
  - Version 9: results/openai/20250418_150042/harnesses/core_mqtt.c:handleUncleanSessionResumption/v9.c
  - Version 10: results/openai/20250418_150042/harnesses/core_mqtt.c:handleUncleanSessionResumption/v10.c
  - Size evolution: Initial 24 lines → Final 199 lines (+175 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:handleUncleanSessionResumption/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleUncleanSessionResumption/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handleUncleanSessionResumption/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleUncleanSessionResumption/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handleUncleanSessionResumption/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleUncleanSessionResumption/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handleUncleanSessionResumption/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleUncleanSessionResumption/v4_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handleUncleanSessionResumption/v5_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleUncleanSessionResumption/v5_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handleUncleanSessionResumption/v6_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleUncleanSessionResumption/v6_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handleUncleanSessionResumption/v7_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleUncleanSessionResumption/v7_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handleUncleanSessionResumption/v8_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleUncleanSessionResumption/v8_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handleUncleanSessionResumption/v9_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleUncleanSessionResumption/v9_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handleUncleanSessionResumption/v10_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleUncleanSessionResumption/v10_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:handleUncleanSessionResumption/v11_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:handleUncleanSessionResumption/v11_report.md

### Function: matchEndWildcardsSpecialCases (File: core_mqtt.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 0.00%

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:matchEndWildcardsSpecialCases/v1.c

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:matchEndWildcardsSpecialCases/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:matchEndWildcardsSpecialCases/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:matchEndWildcardsSpecialCases/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:matchEndWildcardsSpecialCases/v2_report.md

### Function: matchTopicFilter (File: core_mqtt.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 0.00%

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:matchTopicFilter/v1.c

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:matchTopicFilter/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:matchTopicFilter/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:matchTopicFilter/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:matchTopicFilter/v2_report.md

### Function: matchWildcards (File: core_mqtt.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 0.00%

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:matchWildcards/v1.c

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:matchWildcards/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:matchWildcards/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:matchWildcards/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:matchWildcards/v2_report.md

### Function: receiveConnack (File: core_mqtt.c)
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
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:receiveConnack/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:receiveConnack/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:receiveConnack/v3.c
  - Version 4: results/openai/20250418_150042/harnesses/core_mqtt.c:receiveConnack/v4.c
  - Version 5: results/openai/20250418_150042/harnesses/core_mqtt.c:receiveConnack/v5.c
  - Version 6: results/openai/20250418_150042/harnesses/core_mqtt.c:receiveConnack/v6.c
  - Version 7: results/openai/20250418_150042/harnesses/core_mqtt.c:receiveConnack/v7.c
  - Version 8: results/openai/20250418_150042/harnesses/core_mqtt.c:receiveConnack/v8.c
  - Version 9: results/openai/20250418_150042/harnesses/core_mqtt.c:receiveConnack/v9.c
  - Version 10: results/openai/20250418_150042/harnesses/core_mqtt.c:receiveConnack/v10.c
  - Size evolution: Initial 58 lines → Final 172 lines (+114 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveConnack/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveConnack/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveConnack/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveConnack/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveConnack/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveConnack/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveConnack/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveConnack/v4_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveConnack/v5_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveConnack/v5_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveConnack/v6_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveConnack/v6_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveConnack/v7_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveConnack/v7_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveConnack/v8_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveConnack/v8_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveConnack/v9_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveConnack/v9_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveConnack/v10_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveConnack/v10_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveConnack/v11_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveConnack/v11_report.md

### Function: receivePacket (File: core_mqtt.c)
Status: FAILED
Refinements: 10
Message: VERIFICATION FAILED: Memory leak detected
Suggestions: Ensure all allocated memory is freed in all execution paths

#### Coverage Metrics
- Function coverage: 0.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v10): 0.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:receivePacket/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:receivePacket/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:receivePacket/v3.c
  - Version 4: results/openai/20250418_150042/harnesses/core_mqtt.c:receivePacket/v4.c
  - Version 5: results/openai/20250418_150042/harnesses/core_mqtt.c:receivePacket/v5.c
  - Version 6: results/openai/20250418_150042/harnesses/core_mqtt.c:receivePacket/v6.c
  - Version 7: results/openai/20250418_150042/harnesses/core_mqtt.c:receivePacket/v7.c
  - Version 8: results/openai/20250418_150042/harnesses/core_mqtt.c:receivePacket/v8.c
  - Version 9: results/openai/20250418_150042/harnesses/core_mqtt.c:receivePacket/v9.c
  - Version 10: results/openai/20250418_150042/harnesses/core_mqtt.c:receivePacket/v10.c
  - Size evolution: Initial 47 lines → Final 42 lines (-5 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:receivePacket/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receivePacket/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receivePacket/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receivePacket/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receivePacket/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receivePacket/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receivePacket/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receivePacket/v4_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receivePacket/v5_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receivePacket/v5_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receivePacket/v6_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receivePacket/v6_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receivePacket/v7_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receivePacket/v7_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receivePacket/v8_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receivePacket/v8_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receivePacket/v9_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receivePacket/v9_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receivePacket/v10_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receivePacket/v10_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receivePacket/v11_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receivePacket/v11_report.md

### Function: receiveSingleIteration (File: core_mqtt.c)
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
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:receiveSingleIteration/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:receiveSingleIteration/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:receiveSingleIteration/v3.c
  - Version 4: results/openai/20250418_150042/harnesses/core_mqtt.c:receiveSingleIteration/v4.c
  - Version 5: results/openai/20250418_150042/harnesses/core_mqtt.c:receiveSingleIteration/v5.c
  - Version 6: results/openai/20250418_150042/harnesses/core_mqtt.c:receiveSingleIteration/v6.c
  - Version 7: results/openai/20250418_150042/harnesses/core_mqtt.c:receiveSingleIteration/v7.c
  - Version 8: results/openai/20250418_150042/harnesses/core_mqtt.c:receiveSingleIteration/v8.c
  - Version 9: results/openai/20250418_150042/harnesses/core_mqtt.c:receiveSingleIteration/v9.c
  - Version 10: results/openai/20250418_150042/harnesses/core_mqtt.c:receiveSingleIteration/v10.c
  - Size evolution: Initial 57 lines → Final 293 lines (+236 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveSingleIteration/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveSingleIteration/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveSingleIteration/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveSingleIteration/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveSingleIteration/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveSingleIteration/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveSingleIteration/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveSingleIteration/v4_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveSingleIteration/v5_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveSingleIteration/v5_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveSingleIteration/v6_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveSingleIteration/v6_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveSingleIteration/v7_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveSingleIteration/v7_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveSingleIteration/v8_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveSingleIteration/v8_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveSingleIteration/v9_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveSingleIteration/v9_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveSingleIteration/v10_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveSingleIteration/v10_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveSingleIteration/v11_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:receiveSingleIteration/v11_report.md

### Function: recvExact (File: core_mqtt.c)
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
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:recvExact/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:recvExact/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:recvExact/v3.c
  - Version 4: results/openai/20250418_150042/harnesses/core_mqtt.c:recvExact/v4.c
  - Version 5: results/openai/20250418_150042/harnesses/core_mqtt.c:recvExact/v5.c
  - Version 6: results/openai/20250418_150042/harnesses/core_mqtt.c:recvExact/v6.c
  - Version 7: results/openai/20250418_150042/harnesses/core_mqtt.c:recvExact/v7.c
  - Version 8: results/openai/20250418_150042/harnesses/core_mqtt.c:recvExact/v8.c
  - Version 9: results/openai/20250418_150042/harnesses/core_mqtt.c:recvExact/v9.c
  - Version 10: results/openai/20250418_150042/harnesses/core_mqtt.c:recvExact/v10.c
  - Size evolution: Initial 76 lines → Final 450 lines (+374 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:recvExact/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:recvExact/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:recvExact/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:recvExact/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:recvExact/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:recvExact/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:recvExact/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:recvExact/v4_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:recvExact/v5_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:recvExact/v5_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:recvExact/v6_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:recvExact/v6_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:recvExact/v7_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:recvExact/v7_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:recvExact/v8_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:recvExact/v8_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:recvExact/v9_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:recvExact/v9_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:recvExact/v10_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:recvExact/v10_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:recvExact/v11_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:recvExact/v11_report.md

### Function: sendBuffer (File: core_mqtt.c)
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
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:sendBuffer/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:sendBuffer/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:sendBuffer/v3.c
  - Version 4: results/openai/20250418_150042/harnesses/core_mqtt.c:sendBuffer/v4.c
  - Version 5: results/openai/20250418_150042/harnesses/core_mqtt.c:sendBuffer/v5.c
  - Version 6: results/openai/20250418_150042/harnesses/core_mqtt.c:sendBuffer/v6.c
  - Version 7: results/openai/20250418_150042/harnesses/core_mqtt.c:sendBuffer/v7.c
  - Version 8: results/openai/20250418_150042/harnesses/core_mqtt.c:sendBuffer/v8.c
  - Version 9: results/openai/20250418_150042/harnesses/core_mqtt.c:sendBuffer/v9.c
  - Version 10: results/openai/20250418_150042/harnesses/core_mqtt.c:sendBuffer/v10.c
  - Size evolution: Initial 55 lines → Final 178 lines (+123 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:sendBuffer/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendBuffer/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendBuffer/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendBuffer/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendBuffer/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendBuffer/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendBuffer/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendBuffer/v4_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendBuffer/v5_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendBuffer/v5_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendBuffer/v6_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendBuffer/v6_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendBuffer/v7_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendBuffer/v7_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendBuffer/v8_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendBuffer/v8_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendBuffer/v9_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendBuffer/v9_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendBuffer/v10_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendBuffer/v10_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendBuffer/v11_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendBuffer/v11_report.md

### Function: sendConnectWithoutCopy (File: core_mqtt.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 0.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v3): 0.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:sendConnectWithoutCopy/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:sendConnectWithoutCopy/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:sendConnectWithoutCopy/v3.c
  - Size evolution: Initial 54 lines → Final 76 lines (+22 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:sendConnectWithoutCopy/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendConnectWithoutCopy/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendConnectWithoutCopy/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendConnectWithoutCopy/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendConnectWithoutCopy/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendConnectWithoutCopy/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendConnectWithoutCopy/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendConnectWithoutCopy/v4_report.md

### Function: sendMessageVector (File: core_mqtt.c)
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
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:sendMessageVector/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:sendMessageVector/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:sendMessageVector/v3.c
  - Version 4: results/openai/20250418_150042/harnesses/core_mqtt.c:sendMessageVector/v4.c
  - Version 5: results/openai/20250418_150042/harnesses/core_mqtt.c:sendMessageVector/v5.c
  - Version 6: results/openai/20250418_150042/harnesses/core_mqtt.c:sendMessageVector/v6.c
  - Version 7: results/openai/20250418_150042/harnesses/core_mqtt.c:sendMessageVector/v7.c
  - Version 8: results/openai/20250418_150042/harnesses/core_mqtt.c:sendMessageVector/v8.c
  - Version 9: results/openai/20250418_150042/harnesses/core_mqtt.c:sendMessageVector/v9.c
  - Version 10: results/openai/20250418_150042/harnesses/core_mqtt.c:sendMessageVector/v10.c
  - Size evolution: Initial 111 lines → Final 280 lines (+169 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:sendMessageVector/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendMessageVector/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendMessageVector/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendMessageVector/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendMessageVector/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendMessageVector/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendMessageVector/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendMessageVector/v4_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendMessageVector/v5_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendMessageVector/v5_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendMessageVector/v6_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendMessageVector/v6_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendMessageVector/v7_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendMessageVector/v7_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendMessageVector/v8_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendMessageVector/v8_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendMessageVector/v9_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendMessageVector/v9_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendMessageVector/v10_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendMessageVector/v10_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendMessageVector/v11_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendMessageVector/v11_report.md

### Function: sendPublishAcks (File: core_mqtt.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 0.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v3): 0.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:sendPublishAcks/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:sendPublishAcks/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:sendPublishAcks/v3.c
  - Size evolution: Initial 39 lines → Final 44 lines (+5 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:sendPublishAcks/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendPublishAcks/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendPublishAcks/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendPublishAcks/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendPublishAcks/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendPublishAcks/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendPublishAcks/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendPublishAcks/v4_report.md

### Function: sendPublishWithoutCopy (File: core_mqtt.c)
Status: SUCCESS
Refinements: 4
Message: Verification successful

#### Coverage Metrics
- Function coverage: 0.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v4): 0.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:sendPublishWithoutCopy/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:sendPublishWithoutCopy/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:sendPublishWithoutCopy/v3.c
  - Version 4: results/openai/20250418_150042/harnesses/core_mqtt.c:sendPublishWithoutCopy/v4.c
  - Size evolution: Initial 85 lines → Final 82 lines (-3 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:sendPublishWithoutCopy/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendPublishWithoutCopy/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendPublishWithoutCopy/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendPublishWithoutCopy/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendPublishWithoutCopy/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendPublishWithoutCopy/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendPublishWithoutCopy/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendPublishWithoutCopy/v4_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendPublishWithoutCopy/v5_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendPublishWithoutCopy/v5_report.md

### Function: sendSubscribeWithoutCopy (File: core_mqtt.c)
Status: SUCCESS
Refinements: 4
Message: Verification successful

#### Coverage Metrics
- Function coverage: 0.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v4): 0.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:sendSubscribeWithoutCopy/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:sendSubscribeWithoutCopy/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:sendSubscribeWithoutCopy/v3.c
  - Version 4: results/openai/20250418_150042/harnesses/core_mqtt.c:sendSubscribeWithoutCopy/v4.c
  - Size evolution: Initial 60 lines → Final 61 lines (+1 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:sendSubscribeWithoutCopy/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendSubscribeWithoutCopy/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendSubscribeWithoutCopy/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendSubscribeWithoutCopy/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendSubscribeWithoutCopy/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendSubscribeWithoutCopy/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendSubscribeWithoutCopy/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendSubscribeWithoutCopy/v4_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendSubscribeWithoutCopy/v5_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendSubscribeWithoutCopy/v5_report.md

### Function: sendUnsubscribeWithoutCopy (File: core_mqtt.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 0.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v3): 0.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:sendUnsubscribeWithoutCopy/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:sendUnsubscribeWithoutCopy/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:sendUnsubscribeWithoutCopy/v3.c
  - Size evolution: Initial 58 lines → Final 62 lines (+4 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:sendUnsubscribeWithoutCopy/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendUnsubscribeWithoutCopy/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendUnsubscribeWithoutCopy/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendUnsubscribeWithoutCopy/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendUnsubscribeWithoutCopy/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendUnsubscribeWithoutCopy/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:sendUnsubscribeWithoutCopy/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:sendUnsubscribeWithoutCopy/v4_report.md

### Function: validatePublishParams (File: core_mqtt.c)
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
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:validatePublishParams/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:validatePublishParams/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:validatePublishParams/v3.c
  - Version 4: results/openai/20250418_150042/harnesses/core_mqtt.c:validatePublishParams/v4.c
  - Version 5: results/openai/20250418_150042/harnesses/core_mqtt.c:validatePublishParams/v5.c
  - Version 6: results/openai/20250418_150042/harnesses/core_mqtt.c:validatePublishParams/v6.c
  - Version 7: results/openai/20250418_150042/harnesses/core_mqtt.c:validatePublishParams/v7.c
  - Version 8: results/openai/20250418_150042/harnesses/core_mqtt.c:validatePublishParams/v8.c
  - Version 9: results/openai/20250418_150042/harnesses/core_mqtt.c:validatePublishParams/v9.c
  - Version 10: results/openai/20250418_150042/harnesses/core_mqtt.c:validatePublishParams/v10.c
  - Size evolution: Initial 89 lines → Final 374 lines (+285 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:validatePublishParams/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:validatePublishParams/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:validatePublishParams/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:validatePublishParams/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:validatePublishParams/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:validatePublishParams/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:validatePublishParams/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:validatePublishParams/v4_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:validatePublishParams/v5_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:validatePublishParams/v5_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:validatePublishParams/v6_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:validatePublishParams/v6_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:validatePublishParams/v7_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:validatePublishParams/v7_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:validatePublishParams/v8_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:validatePublishParams/v8_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:validatePublishParams/v9_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:validatePublishParams/v9_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:validatePublishParams/v10_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:validatePublishParams/v10_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:validatePublishParams/v11_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:validatePublishParams/v11_report.md

### Function: validateSubscribeUnsubscribeParams (File: core_mqtt.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 0.00%

#### Coverage Evolution
- Initial coverage (v1): 0.00%
- Final coverage (v3): 0.00%
- Coverage improvement: 0.00%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt.c:validateSubscribeUnsubscribeParams/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt.c:validateSubscribeUnsubscribeParams/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt.c:validateSubscribeUnsubscribeParams/v3.c
  - Size evolution: Initial 63 lines → Final 67 lines (+4 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt.c:validateSubscribeUnsubscribeParams/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:validateSubscribeUnsubscribeParams/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:validateSubscribeUnsubscribeParams/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:validateSubscribeUnsubscribeParams/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:validateSubscribeUnsubscribeParams/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:validateSubscribeUnsubscribeParams/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt.c:validateSubscribeUnsubscribeParams/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt.c:validateSubscribeUnsubscribeParams/v4_report.md

### Function: MQTT_DeserializeAck (File: core_mqtt_serializer.c)
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
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt_serializer.c:MQTT_DeserializeAck/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt_serializer.c:MQTT_DeserializeAck/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt_serializer.c:MQTT_DeserializeAck/v3.c
  - Version 4: results/openai/20250418_150042/harnesses/core_mqtt_serializer.c:MQTT_DeserializeAck/v4.c
  - Version 5: results/openai/20250418_150042/harnesses/core_mqtt_serializer.c:MQTT_DeserializeAck/v5.c
  - Version 6: results/openai/20250418_150042/harnesses/core_mqtt_serializer.c:MQTT_DeserializeAck/v6.c
  - Version 7: results/openai/20250418_150042/harnesses/core_mqtt_serializer.c:MQTT_DeserializeAck/v7.c
  - Version 8: results/openai/20250418_150042/harnesses/core_mqtt_serializer.c:MQTT_DeserializeAck/v8.c
  - Version 9: results/openai/20250418_150042/harnesses/core_mqtt_serializer.c:MQTT_DeserializeAck/v9.c
  - Version 10: results/openai/20250418_150042/harnesses/core_mqtt_serializer.c:MQTT_DeserializeAck/v10.c
  - Size evolution: Initial 103 lines → Final 308 lines (+205 lines)
  - Refinement result: Some issues remain after 10 refinements

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializeAck/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializeAck/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializeAck/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializeAck/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializeAck/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializeAck/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializeAck/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializeAck/v4_report.md
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializeAck/v5_results.txt
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializeAck/v5_report.md
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializeAck/v6_results.txt
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializeAck/v6_report.md
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializeAck/v7_results.txt
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializeAck/v7_report.md
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializeAck/v8_results.txt
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializeAck/v8_report.md
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializeAck/v9_results.txt
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializeAck/v9_report.md
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializeAck/v10_results.txt
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializeAck/v10_report.md
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializeAck/v11_results.txt
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializeAck/v11_report.md

### Function: MQTT_DeserializePublish (File: core_mqtt_serializer.c)
Status: SUCCESS
Refinements: 1
Message: Verification successful

#### Coverage Metrics
- Function coverage: 100.00%

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt_serializer.c:MQTT_DeserializePublish/v1.c

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializePublish/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializePublish/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializePublish/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_DeserializePublish/v2_report.md

### Function: MQTT_GetConnectPacketSize (File: core_mqtt_serializer.c)
Status: SUCCESS
Refinements: 3
Message: Verification successful

#### Coverage Metrics
- Function coverage: 76.92%

#### Coverage Evolution
- Initial coverage (v1): 92.31%
- Final coverage (v3): 76.92%
- Coverage improvement: -15.38%
- Error reduction: 0

#### Harness Evolution:
  - Version 1: results/openai/20250418_150042/harnesses/core_mqtt_serializer.c:MQTT_GetConnectPacketSize/v1.c
  - Version 2: results/openai/20250418_150042/harnesses/core_mqtt_serializer.c:MQTT_GetConnectPacketSize/v2.c
  - Version 3: results/openai/20250418_150042/harnesses/core_mqtt_serializer.c:MQTT_GetConnectPacketSize/v3.c
  - Size evolution: Initial 140 lines → Final 90 lines (-50 lines)
  - Refinement result: Successfully addressed all verification issues

#### Verification Reports: 
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_GetConnectPacketSize/v1_results.txt
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_GetConnectPacketSize/v1_report.md
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_GetConnectPacketSize/v2_results.txt
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_GetConnectPacketSize/v2_report.md
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_GetConnectPacketSize/v3_results.txt
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_GetConnectPacketSize/v3_report.md
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_GetConnectPacketSize/v4_results.txt
  - results/openai/20250418_150042/verification/core_mqtt_serializer.c:MQTT_GetConnectPacketSize/v4_report.md