---
id: fc:yaskawa-solectria-sgi-500-750xtm-mpptracking
type: FaultCode
name: Yaskawa Solectria SGI-XTM MPP Tracking
aliases:
- MPP Tracking
- mpptracking
- Yaskawa Solectria MPP Tracking
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: MPP Tracking
code_key: mpptracking
vendor_severity: Informative
page: 115
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r16
    h: 71ba0cc54799
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r16
    h: 71ba0cc54799
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r16
    h: 71ba0cc54799
  review: drafted
  review_note: 'support check: partial - MPPT algorithm active with no action needed implies normal production,
    but no production effect is not explicit.'
---
