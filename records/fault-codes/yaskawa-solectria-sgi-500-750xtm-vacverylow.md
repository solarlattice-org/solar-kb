---
id: fc:yaskawa-solectria-sgi-500-750xtm-vacverylow
type: FaultCode
name: Yaskawa Solectria SGI-XTM Vac Very Low
aliases:
- Vac Very Low
- vacverylow
- Yaskawa Solectria Vac Very Low
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Vac Very Low
code_key: vacverylow
vendor_severity: Informative
page: 117
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r4
    h: 1e3197609faa
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r4
    h: 1e3197609faa
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r4
    h: 1e3197609faa
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r4
    h: 1e3197609faa
  review: drafted
  review_note: 'support check: partial - The row implies the inverter stops and restarts when VAC returns
    to normal. It never explicitly says production stops or…'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: The inverter restarts once grid voltage is back in range.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r4
    h: 1e3197609faa
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:yaskawa-solectria-sgi-500-750xtm
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r4
    h: 1e3197609faa
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
---
