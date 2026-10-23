---
id: fc:sma-stp-core1-us-8102
type: FaultCode
name: SMA CORE1-US 8102
aliases:
- '8102'
- SMA 8102
- Communication failure
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '8102'
code_key: '8102'
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
  review: drafted
- claim_id: c3
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h289
    h: a1445dc1fa7d
  review: drafted
---
