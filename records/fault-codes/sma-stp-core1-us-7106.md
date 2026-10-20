---
id: fc:sma-stp-core1-us-7106
type: FaultCode
name: SMA CORE1-US 7106
aliases:
- '7106'
- SMA 7106
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '7106'
code_key: '7106'
page: 50
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r5
    h: d3bbcbdb79a2
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r5
    h: d3bbcbdb79a2
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:firmware-update-failure
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r5
    h: d3bbcbdb79a2
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r5
    h: d3bbcbdb79a2
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r5
    h: d3bbcbdb79a2
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r5
    h: d3bbcbdb79a2
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c5
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r5
    h: d3bbcbdb79a2
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r5
    h: d3bbcbdb79a2
  review: drafted
---
