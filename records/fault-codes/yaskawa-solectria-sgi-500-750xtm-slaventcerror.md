---
id: fc:yaskawa-solectria-sgi-500-750xtm-slaventcerror
type: FaultCode
name: Yaskawa Solectria SGI-XTM Slave NTC Error
aliases:
- Slave NTC Error
- slaventcerror
- Yaskawa Solectria Slave NTC Error
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Slave NTC Error
code_key: slaventcerror
vendor_severity: Informative
page: 116
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r14
    h: 9ee33abec10d
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:temperature-sensor-fault
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r14
    h: 9ee33abec10d
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:temperature-sensor
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r14
    h: 9ee33abec10d
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r14
    h: 9ee33abec10d
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r14
    h: 9ee33abec10d
  review: drafted
---
