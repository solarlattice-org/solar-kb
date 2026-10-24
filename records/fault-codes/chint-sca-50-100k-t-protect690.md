---
id: fc:chint-sca-50-100k-t-protect690
type: FaultCode
name: CPS SCA50-100K-T Protect0690
aliases:
- Protect0690
- protect690
- CPS Protect0690
- Capture phase locked loop check exception
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0690
code_key: protect690
display_message: Capture phase locked loop check exception
vendor_severity: Protection
page: 140
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r3
    h: adbb4340b7fd
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r3
    h: adbb4340b7fd
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-sync-failure
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r3
    h: adbb4340b7fd
  review: drafted
  review_note: 'support check: partial - Phase locked loop check exception implies grid synchronization
    problem but isn''t explicitly stated.'
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r3
    h: adbb4340b7fd
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Escalation if the alarm persists after restart.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r3
    h: adbb4340b7fd
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle first; service if the alarm persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r3
    h: adbb4340b7fd
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r3
    h: adbb4340b7fd
  review: drafted
---
