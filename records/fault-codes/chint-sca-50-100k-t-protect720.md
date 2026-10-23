---
id: fc:chint-sca-50-100k-t-protect720
type: FaultCode
name: CPS SCA50-100K-T Protect0720
aliases:
- Protect0720
- protect720
- CPS Protect0720
- Product model exception
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Protect0720
code_key: protect720
display_message: Product model exception
vendor_severity: Protection
page: 140
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r5
    h: 66d96188afa7
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r5
    h: 66d96188afa7
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:configuration-error
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r5
    h: 66d96188afa7
  review: drafted
  review_note: 'support check: partial - Product model exception loosely suggests a configuration error
    but it isn''t explicitly stated.'
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r5
    h: 66d96188afa7
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Escalation if the alarm persists after restart.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r5
    h: 66d96188afa7
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle first; service if the alarm persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=58.r5
    h: 66d96188afa7
  review: drafted
---
