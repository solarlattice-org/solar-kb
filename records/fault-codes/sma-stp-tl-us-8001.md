---
id: fc:sma-stp-tl-us-8001
type: FaultCode
name: SMA STP-TL-US 8001
aliases:
- '8001'
- SMA 8001
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: '8001'
code_key: '8001'
page: 53
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r4
    h: 6b87d0ce4639
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r4
    h: 6b87d0ce4639
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-power-derating
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r4
    h: 6b87d0ce4639
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:derate
  note: Reduction lasting over ten minutes due to temperature; no limit value stated
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r4
    h: 6b87d0ce4639
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r4
    h: 6b87d0ce4639
  review: drafted
  review_note: 'support check: partial - Fan cleaning is mentioned as a corrective measure, but the passage
    doesn''t say the fan is affected.'
- claim_id: c6
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r4
    h: 6b87d0ce4639
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:adequate-cooling
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r4
    h: 6b87d0ce4639
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:sma-stp-tl-us
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r4
    h: 6b87d0ce4639
  review: drafted
---
