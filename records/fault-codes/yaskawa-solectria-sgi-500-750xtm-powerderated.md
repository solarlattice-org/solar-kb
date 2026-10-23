---
id: fc:yaskawa-solectria-sgi-500-750xtm-powerderated
type: FaultCode
name: Yaskawa Solectria SGI-XTM Power Derated
aliases:
- Power Derated
- powerderated
- Yaskawa Solectria Power Derated
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Power Derated
code_key: powerderated
vendor_severity: Informative
page: 116
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r5
    h: 614bf5f8dd14
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-power-derating
  note: Derating caused by temperature.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r5
    h: 614bf5f8dd14
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r5
    h: 614bf5f8dd14
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - Output is limited and it''s logged, but nothing states a warning
    class (u3 says informative).'
- claim_id: c4
  rel: has_production_effect
  target: ec:derate
  note: No derate value stated.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r5
    h: 614bf5f8dd14
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r5
    h: 614bf5f8dd14
  review: drafted
  review_note: 'support check: partial - Row says unit may need inspection/service by an authorized provider,
    but derate is due to temperature and ''no action needed'';…'
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r5
    h: 614bf5f8dd14
  review: drafted
  review_note: 'support check: partial - Passage mentions inspection and service by authorized provider,
    not specifically contacting the manufacturer.'
---
