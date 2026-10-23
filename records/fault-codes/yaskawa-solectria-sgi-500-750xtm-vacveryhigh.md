---
id: fc:yaskawa-solectria-sgi-500-750xtm-vacveryhigh
type: FaultCode
name: Yaskawa Solectria SGI-XTM Vac Very High
aliases:
- Vac Very High
- vacveryhigh
- Yaskawa Solectria Vac Very High
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Vac Very High
code_key: vacveryhigh
vendor_severity: Informative
page: 117
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r3
    h: 191ee2db9ceb
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r3
    h: 191ee2db9ceb
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r3
    h: 191ee2db9ceb
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r3
    h: 191ee2db9ceb
  review: drafted
  review_note: 'support check: partial - Restart upon VAC recovery implies it stopped, but a trip is not
    explicitly stated.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: The inverter restarts once grid voltage is back in range.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r3
    h: 191ee2db9ceb
  review: drafted
---
