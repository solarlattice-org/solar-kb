---
id: fc:yaskawa-solectria-sgi-500-750xtm-lowdcpower
type: FaultCode
name: Yaskawa Solectria SGI-XTM Low DC Power
aliases:
- Low DC Power
- lowdcpower
- Yaskawa Solectria Low DC Power
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Low DC Power
code_key: lowdcpower
vendor_severity: Informative
page: 115
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r14
    h: 1215bd0134cd
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:insufficient-dc-power
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r14
    h: 1215bd0134cd
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r14
    h: 1215bd0134cd
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Inverter idles, not feeding in.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r14
    h: 1215bd0134cd
  review: drafted
  review_note: 'support check: partial - Idle state waiting for power implies not feeding in, but trip
    classification is not stated and it''s a status message.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r14
    h: 1215bd0134cd
  review: drafted
  review_note: 'support check: partial - Idle waiting for more power with no action needed implies it
    resolves itself, but auto-reset is not explicitly stated.'
- claim_id: c6
  rel: applies_to
  target: prod:yaskawa-solectria-sgi-500-750xtm
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r14
    h: 1215bd0134cd
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
---
