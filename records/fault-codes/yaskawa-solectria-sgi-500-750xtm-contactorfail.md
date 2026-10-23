---
id: fc:yaskawa-solectria-sgi-500-750xtm-contactorfail
type: FaultCode
name: Yaskawa Solectria SGI-XTM Contactor Fail
aliases:
- Contactor Fail
- contactorfail
- Yaskawa Solectria Contactor Fail
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: sgi-500-750xtm
family_name: Solectria SGI 500/750XTM
code: Contactor Fail
code_key: contactorfail
vendor_severity: Critical
page: 114
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r1
    h: 3af90367bdf1
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.1
    h: d40755519b21
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:switch-status-fault
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r1
    h: 3af90367bdf1
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:filter-contactor
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r1
    h: 3af90367bdf1
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r1
    h: 3af90367bdf1
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: sec=12.1
    h: d40755519b21
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: Contactor failing to close prevents connection.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r1
    h: 3af90367bdf1
  review: drafted
  review_note: 'support check: partial - The contactor failing to close implies no connection, but the
    passage doesn''t state that production stops.'
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r1
    h: 3af90367bdf1
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Restart first; authorized service if it persists.
  cite:
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=30.r1
    h: 3af90367bdf1
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Restart is the corrective action, but clearing by it isn''t explicitly
    stated.'
---
