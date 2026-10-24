---
id: fc:yaskawa-solectria-sgi-500-750xtm-facverylow
type: FaultCode
name: Yaskawa Solectria SGI-XTM Fac Very Low
aliases:
- Fac Very Low
- facverylow
- Yaskawa Solectria Fac Very Low
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Fac Very Low
code_key: facverylow
vendor_severity: Informative
page: 115
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r9
    h: b21558c992ad
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r9
    h: b21558c992ad
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
  review_note: 'support check: partial - Informative definition given but row''s membership only implied.'
- claim_id: c3
  rel: reports
  target: symptom:grid-underfrequency
  note: critically below the low limit
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r9
    h: b21558c992ad
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r9
    h: b21558c992ad
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r9
    h: b21558c992ad
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r9
    h: b21558c992ad
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:utility-consultation
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r9
    h: b21558c992ad
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:yaskawa-solectria-sgi-500-750xtm
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r9
    h: b21558c992ad
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
---
