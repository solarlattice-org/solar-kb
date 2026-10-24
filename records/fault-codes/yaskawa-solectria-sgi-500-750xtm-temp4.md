---
id: fc:yaskawa-solectria-sgi-500-750xtm-temp4
type: FaultCode
name: Yaskawa Solectria SGI-XTM Temp 4
aliases:
- Temp 4
- temp4
- Yaskawa Solectria Temp 4
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Temp 4
code_key: temp4
vendor_severity: Informative
page: 116
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r20
    h: 0c004e581e57
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: has_production_effect
  target: ec:derate
  note: Row text is truncated; it states only that output was limited, with no cause or number.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r20
    h: 0c004e581e57
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:yaskawa-solectria-sgi-500-750xtm
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r20
    h: 0c004e581e57
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
---
