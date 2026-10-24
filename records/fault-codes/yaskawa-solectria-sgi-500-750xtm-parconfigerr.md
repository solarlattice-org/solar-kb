---
id: fc:yaskawa-solectria-sgi-500-750xtm-parconfigerr
type: FaultCode
name: Yaskawa Solectria SGI-XTM PAR Config Err
aliases:
- PAR Config Err
- parconfigerr
- Yaskawa Solectria PAR Config Err
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: PAR Config Err
code_key: parconfigerr
vendor_severity: Informative
page: 116
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r4
    h: 867a9a79d3c2
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:configuration-error
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r4
    h: 867a9a79d3c2
  review: drafted
- claim_id: c3
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r4
    h: 867a9a79d3c2
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r4
    h: 867a9a79d3c2
  review: drafted
  review_note: 'support check: partial - Service by an authorized provider is stated, but contacting the
    manufacturer is not.'
- claim_id: c5
  rel: applies_to
  target: prod:yaskawa-solectria-sgi-500-750xtm
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r4
    h: 867a9a79d3c2
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
---
