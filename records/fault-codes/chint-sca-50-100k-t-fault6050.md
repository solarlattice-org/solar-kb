---
id: fc:chint-sca-50-100k-t-fault6050
type: FaultCode
name: CPS SCA50-100K-T Fault6050
aliases:
- Fault6050
- fault6050
- CPS Fault6050
- CT Board Abnormal Communicatio n Alarm
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Fault6050
code_key: fault6050
display_message: CT Board Abnormal Communicatio n Alarm
vendor_severity: Fault
page: 149
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=67.r4
    h: 86d458bae487
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=67.r4
    h: 86d458bae487
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=67.r4
    h: 86d458bae487
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the alarm persists after the observation period.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=67.r4
    h: 86d458bae487
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Expected to clear by itself within minutes; service if it persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=67.r4
    h: 86d458bae487
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=67.r4
    h: 86d458bae487
  review: drafted
---
