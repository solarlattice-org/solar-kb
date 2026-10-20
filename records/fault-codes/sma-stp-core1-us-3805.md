---
id: fc:sma-stp-core1-us-3805
type: FaultCode
name: SMA CORE1-US 3805
aliases:
- '3805'
- SMA 3805
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '3805'
code_key: '3805'
page: 49
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r3
    h: ded27d4996a4
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r3
    h: ded27d4996a4
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r3
    h: ded27d4996a4
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r3
    h: ded27d4996a4
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r3
    h: ded27d4996a4
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r3
    h: ded27d4996a4
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: Feed-in is interrupted briefly.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r3
    h: ded27d4996a4
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r3
    h: ded27d4996a4
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Interruption is brief, so feed-in resumes on its own.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r3
    h: ded27d4996a4
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r3
    h: ded27d4996a4
  review: drafted
  review_note: 'support check: partial - Brief interruption implies resumption, but self-resumption is
    not explicitly stated.'
- claim_id: c7
  rel: mitigated_by
  target: mit:dc-wiring-check
  note: Applies when the message occurs frequently; also check that the array is sized correctly.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r3
    h: ded27d4996a4
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r3
    h: ded27d4996a4
  review: drafted
---
