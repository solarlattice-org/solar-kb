---
id: fc:sma-stp-core1-us-8101
type: FaultCode
name: SMA CORE1-US 8101
aliases:
- '8101'
- SMA 8101
- Communication failure
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '8101'
code_key: '8101'
display_message: Communication failure
page: 54
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h287
    h: 304a3b0ee66d
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h289
    h: a1445dc1fa7d
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:communication-loss
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h287
    h: 304a3b0ee66d
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h289
    h: a1445dc1fa7d
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h420
    h: 425aae51d4ca
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.30
    h: e5acec2bf63c
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h422
    h: 417f2f122215
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h289
    h: a1445dc1fa7d
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h421
    h: cca77e1e7cd3
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h422
    h: 417f2f122215
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-stp-core1-us
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h287
    h: 304a3b0ee66d
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h289
    h: a1445dc1fa7d
  review: drafted
---
