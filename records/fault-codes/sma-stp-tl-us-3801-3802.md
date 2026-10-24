---
id: fc:sma-stp-tl-us-3801-3802
type: FaultCode
name: SMA STP-TL-US 3801-3802
aliases:
- 3801-3802
- SMA 3801-3802
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: 3801-3802
code_key: 3801-3802
code_from: 3801
code_to: 3802
page: 49
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15.r7
    h: 39b8d34b2927
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15.r7
    h: 39b8d34b2927
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15.r7
    h: 39b8d34b2927
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Only if the message appears frequently.
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15.r7
    h: 39b8d34b2927
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15.r7
    h: 39b8d34b2927
  review: drafted
  review_note: 'support check: partial - Feed-in is briefly interrupted, which is a trip, though the effect
    is only brief.'
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Feed-in is interrupted only briefly.
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15.r7
    h: 39b8d34b2927
  review: drafted
  review_note: 'support check: partial - The brief interruption implies resumption, but auto-reset is
    not explicitly stated.'
- claim_id: c7
  rel: applies_to
  target: prod:sma-stp-tl-us
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15.r7
    h: 39b8d34b2927
  review: drafted
---
