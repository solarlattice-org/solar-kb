---
id: fc:sma-stp-core1-us-10251
type: FaultCode
name: SMA CORE1-US 10251
aliases:
- '10251'
- SMA 10251
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '10251'
code_key: '10251'
page: 57
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h304
    h: 65cda487bb76
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Status change message; a separate error message may accompany it.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h304
    h: 65cda487bb76
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h271
    h: 56d48c599e10
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-stp-core1-us
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h304
    h: 65cda487bb76
  review: drafted
---
