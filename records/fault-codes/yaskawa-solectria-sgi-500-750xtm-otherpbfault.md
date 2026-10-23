---
id: fc:yaskawa-solectria-sgi-500-750xtm-otherpbfault
type: FaultCode
name: Yaskawa Solectria SGI-XTM Other PB Fault
aliases:
- Other PB Fault
- otherpbfault
- Yaskawa Solectria Other PB Fault
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Other PB Fault
code_key: otherpbfault
vendor_severity: Informative
page: 116
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r1
    h: 30dec1a12a36
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:power-stage-fault
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r1
    h: 30dec1a12a36
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r1
    h: 30dec1a12a36
  review: drafted
  review_note: 'support check: partial - Power stage error is stated, but the inverter bridge is not named.'
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r1
    h: 30dec1a12a36
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r1
    h: 30dec1a12a36
  review: drafted
---
