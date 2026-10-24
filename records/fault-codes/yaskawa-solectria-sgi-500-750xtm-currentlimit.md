---
id: fc:yaskawa-solectria-sgi-500-750xtm-currentlimit
type: FaultCode
name: Yaskawa Solectria SGI-XTM Current Limit
aliases:
- Current Limit
- currentlimit
- Yaskawa Solectria Current Limit
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Current Limit
code_key: currentlimit
vendor_severity: Informative
page: 115
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r2
    h: e11eeb592422
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r2
    h: e11eeb592422
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
  review_note: 'support check: partial - The row is under informative messages, but the section is not
    shown for this row''s own listing and the current…'
- claim_id: c3
  rel: reports
  target: symptom:inverter-power-derating
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r2
    h: e11eeb592422
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:derate
  note: output capped at current limit; no reduced-output value stated
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r2
    h: e11eeb592422
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r2
    h: e11eeb592422
  review: drafted
  review_note: 'support check: partial - Fans are mentioned only as a check item in the corrective actions;
    the passage does not state that the cooling…'
- claim_id: c6
  rel: detected_by
  target: method:fan-function-check
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r2
    h: e11eeb592422
  review: drafted
  review_note: 'support check: partial - Checking that fans are operating is a corrective action, not
    the detection method for the message.'
- claim_id: c7
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: when high input power from string sizing is the cause
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r2
    h: e11eeb592422
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  note: when high temperature is the cause
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r2
    h: e11eeb592422
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:yaskawa-solectria-sgi-500-750xtm
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r2
    h: e11eeb592422
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
---
