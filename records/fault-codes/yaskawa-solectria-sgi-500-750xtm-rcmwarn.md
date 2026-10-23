---
id: fc:yaskawa-solectria-sgi-500-750xtm-rcmwarn
type: FaultCode
name: Yaskawa Solectria SGI-XTM RCM Warn
aliases:
- RCM Warn
- rcmwarn
- Yaskawa Solectria RCM Warn
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: RCM Warn
code_key: rcmwarn
vendor_severity: Informative
page: 116
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r11
    h: 038cb6458432
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:high-leakage-current
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r11
    h: 038cb6458432
  review: drafted
  review_note: 'support check: partial - Row mentions an RCM fault (alarm only) but does not state high
    leakage current explicitly.'
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r11
    h: 038cb6458432
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: has_production_effect
  target: ec:no-production-effect
  note: Residual current condition is alarm only.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r11
    h: 038cb6458432
  review: drafted
  review_note: 'support check: partial - Alarm only implies no stop, but no production effect is not explicitly
    stated.'
---
