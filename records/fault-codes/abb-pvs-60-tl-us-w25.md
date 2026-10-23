---
id: fc:abb-pvs-60-tl-us-w25
type: FaultCode
name: ABB / FIMER PVS-60-TL W025
aliases:
- W025
- w25
- ABB / FIMER W025
- P-reductionEnd
category: Inverters
make: abb
make_name: ABB / FIMER
model_family: pvs-60-tl-us
family_name: FIMER PVS-60-TL-US
code: W025
code_key: w25
display_message: P-reductionEnd
vendor_severity: Warning
page: 154
claims:
- claim_id: c1
  rel: defined_in
  target: src:abb-fimer-pvs-60-tl-us-product-manual-revb
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r1
    h: a2452b364435
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the code prefix
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r1
    h: a2452b364435
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:power-limitation-ended
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r1
    h: a2452b364435
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:no-production-effect
  note: Inverter has left a power limitation state; no check needed
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=45.r1
    h: a2452b364435
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
