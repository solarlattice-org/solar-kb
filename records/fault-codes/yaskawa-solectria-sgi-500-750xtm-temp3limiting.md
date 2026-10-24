---
id: fc:yaskawa-solectria-sgi-500-750xtm-temp3limiting
type: FaultCode
name: Yaskawa Solectria SGI-XTM Temp 3 Limiting
aliases:
- Temp 3 Limiting
- temp3limiting
- Yaskawa Solectria Temp 3 Limiting
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Temp 3 Limiting
code_key: temp3limiting
vendor_severity: Informative
page: 116
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r19
    h: fe719a74c034
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r19
    h: fe719a74c034
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:derate
  note: No reduced-output number is stated.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r19
    h: fe719a74c034
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if inspection proves necessary; the row hedges this.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r19
    h: fe719a74c034
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:yaskawa-solectria-sgi-500-750xtm
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r19
    h: fe719a74c034
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
---
