---
id: fc:yaskawa-solectria-sgi-500-750xtm-waitforgrid
type: FaultCode
name: Yaskawa Solectria SGI-XTM Wait for Grid
aliases:
- Wait for Grid
- waitforgrid
- Yaskawa Solectria Wait for Grid
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Wait for Grid
code_key: waitforgrid
vendor_severity: Informative
page: 117
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r6
    h: b099fdff73ea
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-loss
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r6
    h: b099fdff73ea
  review: drafted
  review_note: 'support check: partial - The row says grid voltage may not be present and to check it
    on all phases, which is close to…'
- claim_id: c3
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r6
    h: b099fdff73ea
  review: drafted
  review_note: 'support check: partial - The row says to check grid voltage on all phases. It does not
    state that the condition is detected by…'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: The inverter waits and does not feed in while grid voltage is absent.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r6
    h: b099fdff73ea
  review: drafted
  review_note: 'support check: partial - The row says grid voltage may not be present and the inverter
    waits. It doesn''t explicitly say there is no…'
- claim_id: c5
  rel: applies_to
  target: prod:yaskawa-solectria-sgi-500-750xtm
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r6
    h: b099fdff73ea
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
---
