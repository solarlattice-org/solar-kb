---
id: fc:sma-stp-core1-us-8208
type: FaultCode
name: SMA CORE1-US 8208
aliases:
- '8208'
- SMA 8208
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '8208'
code_key: '8208'
page: 54
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h290
    h: d2530629076c
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-kb-stp-us-41-event-8208
  cite:
  - src: src:sma-kb-stp-us-41-event-8208
    loc: sec=h1
    h: 8a7e46329fd1
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h290
    h: d2530629076c
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h292
    h: 7840645dc2cd
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h292
    h: 7840645dc2cd
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h293
    h: c87e8fc90a2c
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h292
    h: 7840645dc2cd
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h293
    h: c87e8fc90a2c
  review: drafted
---
