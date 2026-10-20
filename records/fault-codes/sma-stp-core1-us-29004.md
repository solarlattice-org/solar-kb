---
id: fc:sma-stp-core1-us-29004
type: FaultCode
name: SMA CORE1-US 29004
aliases:
- '29004'
- SMA 29004
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '29004'
code_key: '29004'
page: 59
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=26.r15
    h: 1851894a0a87
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=15.r15
    h: 1851894a0a87
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:informational
  note: 'Configuration message: grid parameters could not be changed.'
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=26.r15
    h: 1851894a0a87
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=15.r15
    h: 1851894a0a87
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
  review_note: 'support check: partial - Row states that grid parameters can''t be changed, but its message-type
    is not clearly informational (could be a warning).'
---
