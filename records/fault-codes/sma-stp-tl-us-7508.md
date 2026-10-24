---
id: fc:sma-stp-tl-us-7508
type: FaultCode
name: SMA STP-TL-US 7508
aliases:
- '7508'
- SMA 7508
- External fan fault > Replace fan
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: '7508'
code_key: '7508'
display_message: External fan fault > Replace fan
page: 53
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r2
    h: 0b13c0690224
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:fan-fault-alarm
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r2
    h: 0b13c0690224
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:fan-failure
  note: A fan is blocked
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r2
    h: 0b13c0690224
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r2
    h: 0b13c0690224
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  note: Clean fans first; replace fan if message persists
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r2
    h: 0b13c0690224
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:fan-replacement
  note: Only if message persists after cleaning
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r2
    h: 0b13c0690224
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:sma-stp-tl-us
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r2
    h: 0b13c0690224
  review: drafted
---
