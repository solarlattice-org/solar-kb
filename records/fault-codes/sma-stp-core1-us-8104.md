---
id: fc:sma-stp-core1-us-8104
type: FaultCode
name: SMA CORE1-US 8104
aliases:
- '8104'
- SMA 8104
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '8104'
code_key: '8104'
page: 54
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h289
    h: a1445dc1fa7d
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:communication-loss
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.58
    h: 92fc024c6aed
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h704
    h: 425aae51d4ca
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h290
    h: d2530629076c
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h706
    h: 417f2f122215
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h290
    h: d2530629076c
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h705
    h: cca77e1e7cd3
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h706
    h: 417f2f122215
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-stp-core1-us
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h289
    h: a1445dc1fa7d
  review: drafted
---
