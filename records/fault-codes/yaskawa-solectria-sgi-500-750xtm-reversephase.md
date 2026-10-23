---
id: fc:yaskawa-solectria-sgi-500-750xtm-reversephase
type: FaultCode
name: Yaskawa Solectria SGI-XTM Reverse Phase
aliases:
- Reverse Phase
- reversephase
- Yaskawa Solectria Reverse Phase
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Reverse Phase
code_key: reversephase
vendor_severity: Informative
page: 116
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r13
    h: 1e53ae5f741f
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.2
    h: 36342d216ed4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:phase-sequence-error
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r13
    h: 1e53ae5f741f
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r13
    h: 1e53ae5f741f
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:manual-reset
  note: Restart after phase wiring is corrected.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r13
    h: 1e53ae5f741f
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c5
  rel: mitigated_by
  target: mit:phase-sequence-correction
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=32.r13
    h: 1e53ae5f741f
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
