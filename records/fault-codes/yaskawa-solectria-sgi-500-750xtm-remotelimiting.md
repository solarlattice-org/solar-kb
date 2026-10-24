---
id: fc:yaskawa-solectria-sgi-500-750xtm-remotelimiting
type: FaultCode
name: Yaskawa Solectria SGI-XTM Remote Limiting
aliases:
- Remote Limiting
- remotelimiting
- Yaskawa Solectria Remote Limiting
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Remote Limiting
code_key: remotelimiting
vendor_severity: Informative
page: 116
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r12
    h: 6ace6a9f8f00
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:remote-power-limit
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r12
    h: 6ace6a9f8f00
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r12
    h: 6ace6a9f8f00
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:derate
  note: Temporary current limit set via Modbus or UI; no value stated.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r12
    h: 6ace6a9f8f00
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:yaskawa-solectria-sgi-500-750xtm
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r12
    h: 6ace6a9f8f00
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
---
