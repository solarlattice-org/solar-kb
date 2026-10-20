---
id: fc:sma-stp-core1-us-7110
type: FaultCode
name: SMA CORE1-US 7110
aliases:
- '7110'
- SMA 7110
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '7110'
code_key: '7110'
page: 50
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r6
    h: 3ad30218e05b
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r6
    h: 3ad30218e05b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:firmware-update-failure
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r6
    h: 3ad30218e05b
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r6
    h: 3ad30218e05b
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r6
    h: 3ad30218e05b
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r6
    h: 3ad30218e05b
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r6
    h: 3ad30218e05b
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r6
    h: 3ad30218e05b
  review: drafted
---
