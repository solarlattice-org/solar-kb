---
id: fc:chint-sca-50-100k-t-fault5060
type: FaultCode
name: CPS SCA50-100K-T Fault5060
aliases:
- Fault5060
- fault5060
- CPS Fault5060
- AC Bulkhead Connector Abnormal
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Fault5060
code_key: fault5060
display_message: AC Bulkhead Connector Abnormal
vendor_severity: Fault
page: 148
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r2
    h: 9804233173c9
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r2
    h: 9804233173c9
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:connector-abnormal
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r2
    h: 9804233173c9
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:ac-connector
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r2
    h: 9804233173c9
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r2
    h: 9804233173c9
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle first; contact service if the alarm persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=66.r2
    h: 9804233173c9
  review: drafted
  review_note: 'support check: partial - Power-cycle then contact service is stated, but the row doesn''t
    say the fault clears by manual reset explicitly; it''s implied…'
---
