---
id: fc:yaskawa-solectria-sgi-500-750xtm-parbackuperr
type: FaultCode
name: Yaskawa Solectria SGI-XTM PAR Backup Err
aliases:
- PAR Backup Err
- parbackuperr
- Yaskawa Solectria PAR Backup Err
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: PAR Backup Err
code_key: parbackuperr
vendor_severity: Informative
page: 116
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r3
    h: 694c76d00b47
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:configuration-error
  note: Configuration backup error.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r3
    h: 694c76d00b47
  review: drafted
- claim_id: c3
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r3
    h: 694c76d00b47
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r3
    h: 694c76d00b47
  review: drafted
  review_note: 'support check: partial - Service by an authorized provider is stated, but contacting the
    manufacturer is not.'
- claim_id: c5
  rel: applies_to
  target: prod:yaskawa-solectria-sgi-500-750xtm
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r3
    h: 694c76d00b47
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
---
