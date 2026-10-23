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
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=27.r14
    h: 7b359b92f3c5
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:informational
  note: Valid access code unlocks protected parameters; relocked after ten feed-in hours.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=26.r14
    h: 7b359b92f3c5
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=15.r14
    h: 7b359b92f3c5
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=27.r14
    h: 7b359b92f3c5
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=22.r4
    h: 5b705d8ca944
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=22.r1
    h: feb329ccb9a2
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.106
    h: 3fe6f8a961d3
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h579
    h: 84a4128cefd9
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h580
    h: 85e1e30c57bb
  review: drafted
---
