---
id: fc:yaskawa-solectria-sgi-500-750xtm-dcovershoot
type: FaultCode
name: Yaskawa Solectria SGI-XTM DC Overshoot
aliases:
- DC Overshoot
- dcovershoot
- Yaskawa Solectria DC Overshoot
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: DC Overshoot
code_key: dcovershoot
vendor_severity: Informative
page: 115
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r4
    h: c9d357d29290
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r4
    h: c9d357d29290
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - Informative section defines messages as status info, but the
    row itself isn''t explicitly stated as listed there; corrective action involves…'
- claim_id: c3
  rel: reports
  target: symptom:dc-bus-overvoltage
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r4
    h: c9d357d29290
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r4
    h: c9d357d29290
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: only if the condition persists after restart
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r4
    h: c9d357d29290
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: restart first; persistent cases point to array sizing
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r4
    h: c9d357d29290
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:yaskawa-solectria-sgi-500-750xtm
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=31.r4
    h: c9d357d29290
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
---
