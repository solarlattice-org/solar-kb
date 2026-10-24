---
id: fc:yaskawa-solectria-sgi-500-750xtm-dcconterr
type: FaultCode
name: Yaskawa Solectria SGI-XTM DC Cont. Err
aliases:
- DC Cont. Err
- dcconterr
- Yaskawa Solectria DC Cont. Err
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: DC Cont. Err
code_key: dcconterr
vendor_severity: Informative
page: 115
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r3
    h: 2c57a7643e44
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r3
    h: 2c57a7643e44
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
  review_note: 'review: partial - The vendor files this under Informative messages (sec 12.2, status information),
    but the row describes a contactor failure that needs a service…'
- claim_id: c3
  rel: reports
  target: symptom:dc-contactor-stuck
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r3
    h: 2c57a7643e44
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:dc-contactor
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r3
    h: 2c57a7643e44
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r3
    h: 2c57a7643e44
  review: drafted
  review_note: 'support check: partial - Row says inverter may need servicing by an authorized provider,
    but does not say contact manufacturer.'
- claim_id: c6
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r3
    h: 2c57a7643e44
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:yaskawa-solectria-sgi-500-750xtm
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r3
    h: 2c57a7643e44
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
---
