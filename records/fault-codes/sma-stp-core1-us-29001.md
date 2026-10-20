---
id: fc:sma-stp-core1-us-29001
type: FaultCode
name: SMA CORE1-US 29001
aliases:
- '29001'
- SMA 29001
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '29001'
code_key: '29001'
page: 59
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=26.r14
    h: 7b359b92f3c5
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=15.r14
    h: 7b359b92f3c5
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:informational
  note: Protected parameters unlocked; they relock automatically after 10 feed-in hours.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=26.r14
    h: 7b359b92f3c5
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=15.r14
    h: 7b359b92f3c5
  review: drafted
---
