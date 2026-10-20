---
id: fc:sma-stp-core1-us-4301
type: FaultCode
name: SMA CORE1-US 4301
aliases:
- '4301'
- SMA 4301
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '4301'
code_key: '4301'
page: 49
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r4
    h: 941ab92a0300
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r4
    h: 941ab92a0300
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:arc-fault
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r4
    h: 941ab92a0300
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r4
    h: 941ab92a0300
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c4
  rel: has_recovery
  target: ec:manual-reset
  note: Applies only when the arc-fault interrupter has triggered operation inhibition.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r4
    h: 941ab92a0300
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r4
    h: 941ab92a0300
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
