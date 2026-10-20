---
id: fc:solis-s5-gc-us-ovtem
type: FaultCode
name: Solis S5-GC OV-TEM
aliases:
- OV-TEM
- ovtem
- Solis OV-TEM
- Temperature Protect ion
category: Inverters
make: solis
make_name: Solis
model_family: s5-gc-us
family_name: Solis S5-GC(75-125)K-US
code: OV-TEM
code_key: ovtem
display_message: Temperature Protect ion
page: 71
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r2
    h: 98bb900b2b7d
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r2
    h: 98bb900b2b7d
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c3
  rel: affects
  target: comp:inverter
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r2
    h: 98bb900b2b7d
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r2
    h: 98bb900b2b7d
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c5
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r2
    h: 98bb900b2b7d
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:direct-sun-avoidance
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r2
    h: 98bb900b2b7d
  review: drafted
  review_note: 'support check: partial - Passage asks whether the inverter is in direct sunshine, implying
    avoidance, but doesn''t explicitly say to avoid or shade it.'
- claim_id: c7
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r2
    h: 98bb900b2b7d
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15
    h: cb7b6f9ed265
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Table is titled ''Fault messages'' and lists OV-TEM, but the
    row doesn''t state device behavior (stop/trip); classification only implied by…'
---
