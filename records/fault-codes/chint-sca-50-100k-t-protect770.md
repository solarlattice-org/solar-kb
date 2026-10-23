---
id: fc:chint-sca-50-100k-t-protect770
type: FaultCode
name: CPS SCA50-100K-T Protect0770
aliases:
- Protect0770
- protect770
- CPS Protect0770
- ARCComAbn
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0770
code_key: protect770
display_message: ARCComAbn
vendor_severity: Protection
page: 141
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=59.r3
    h: dd24c0d1f325
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=59.r3
    h: dd24c0d1f325
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=59.r3
    h: dd24c0d1f325
  review: drafted
  review_note: 'support check: partial - Arc communication abnormal implies communication failure but
    internal is not explicitly stated.'
- claim_id: c4
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=59.r3
    h: dd24c0d1f325
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - Arc communication abnormal implies arc detection board but the
    component isn''t explicitly named.'
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=59.r3
    h: dd24c0d1f325
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Escalation if the alarm persists after restart.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=59.r3
    h: dd24c0d1f325
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle first; service if the alarm persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=59.r3
    h: dd24c0d1f325
  review: drafted
---
