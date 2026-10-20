---
id: fc:sma-stp-core1-us-7102
type: FaultCode
name: SMA CORE1-US 7102
aliases:
- '7102'
- SMA 7102
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '7102'
code_key: '7102'
page: 50
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r3
    h: 6022b2728800
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r3
    h: 6022b2728800
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:configuration-error
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r3
    h: 6022b2728800
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r3
    h: 6022b2728800
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r3
    h: 6022b2728800
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r3
    h: 6022b2728800
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c5
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r3
    h: 6022b2728800
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r3
    h: 6022b2728800
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:reload-parameter-file
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r3
    h: 6022b2728800
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r3
    h: 6022b2728800
  review: drafted
---
