---
id: fc:yaskawa-solectria-sgi-500-750xtm-vaclow
type: FaultCode
name: Yaskawa Solectria SGI-XTM Vac Low
aliases:
- Vac Low
- vaclow
- Yaskawa Solectria Vac Low
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Vac Low
code_key: vaclow
vendor_severity: Informative
page: 117
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r2
    h: 97779e8ae2f5
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r2
    h: 97779e8ae2f5
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r2
    h: 97779e8ae2f5
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r2
    h: 97779e8ae2f5
  review: drafted
  review_note: 'support check: partial - Restart upon VAC recovery implies it stopped, but a trip is not
    explicitly stated.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: The inverter restarts once grid voltage is back in range.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r2
    h: 97779e8ae2f5
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:yaskawa-solectria-sgi-500-750xtm
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r2
    h: 97779e8ae2f5
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
---
