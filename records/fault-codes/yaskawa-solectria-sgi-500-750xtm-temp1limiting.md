---
id: fc:yaskawa-solectria-sgi-500-750xtm-temp1limiting
type: FaultCode
name: Yaskawa Solectria SGI-XTM Temp 1 Limiting
aliases:
- Temp 1 Limiting
- temp1limiting
- Yaskawa Solectria Temp 1 Limiting
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Temp 1 Limiting
code_key: temp1limiting
vendor_severity: Informative
page: 116
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r17
    h: 6c3bdc843570
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r17
    h: 6c3bdc843570
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:derate
  note: Output limited by internal temperature; no value stated.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r17
    h: 6c3bdc843570
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:yaskawa-solectria-sgi-500-750xtm
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r17
    h: 6c3bdc843570
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
---
