---
id: fc:sma-stp-core1-us-7330
type: FaultCode
name: SMA CORE1-US 7330
aliases:
- '7330'
- SMA 7330
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '7330'
code_key: '7330'
page: 51
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=20.r1
    h: bc08bcd11a95
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=9.r1
    h: bc08bcd11a95
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=21.r1
    h: bc08bcd11a95
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:firmware-update-failure
  note: Update package not suitable for this inverter.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=20.r1
    h: bc08bcd11a95
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=9.r1
    h: bc08bcd11a95
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=21.r1
    h: bc08bcd11a95
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h377
    h: d330f7b2eab4
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c5
  rel: applies_to
  target: prod:sma-stp-core1-us
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=20.r1
    h: bc08bcd11a95
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=9.r1
    h: bc08bcd11a95
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=21.r1
    h: bc08bcd11a95
  review: drafted
---
