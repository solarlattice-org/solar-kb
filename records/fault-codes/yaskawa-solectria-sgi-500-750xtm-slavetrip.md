---
id: fc:yaskawa-solectria-sgi-500-750xtm-slavetrip
type: FaultCode
name: Yaskawa Solectria SGI-XTM Slave Trip
aliases:
- Slave Trip
- slavetrip
- Yaskawa Solectria Slave Trip
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Slave Trip
code_key: slavetrip
vendor_severity: Informative
page: 116
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r16
    h: a4778a75b108
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:power-stage-fault
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r16
    h: a4778a75b108
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r16
    h: a4778a75b108
  review: drafted
  review_note: 'support check: partial - Power stage failure implies the bridge but the inverter bridge
    is not named in the passage.'
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r16
    h: a4778a75b108
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r16
    h: a4778a75b108
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:yaskawa-solectria-sgi-500-750xtm
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r16
    h: a4778a75b108
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
---
