---
id: fc:sma-sbse-us-50-8104
type: FaultCode
name: SMA SBSE-US-50 8104
aliases:
- '8104'
- SMA 8104
- Communication impaired
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '8104'
code_key: '8104'
display_message: Communication impaired
page: 115
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.58
    h: 92fc024c6aed
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h704
    h: 425aae51d4ca
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
---
