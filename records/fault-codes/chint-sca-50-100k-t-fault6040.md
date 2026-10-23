---
id: fc:chint-sca-50-100k-t-fault6040
type: FaultCode
name: CPS SCA50-100K-T Fault6040
aliases:
- Fault6040
- fault6040
- CPS Fault6040
- Core Board OverTempera tureFault
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Fault6040
code_key: fault6040
display_message: Core Board OverTempera tureFault
vendor_severity: Fault
page: 149
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=67.r5
    h: b7c83a42fd73
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=67.r5
    h: b7c83a42fd73
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=67.r5
    h: b7c83a42fd73
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:control-board
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=67.r5
    h: b7c83a42fd73
  review: drafted
  review_note: 'support check: partial - Core board is named, but mapping it to the control board is not
    stated in the passage.'
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the alarm persists after the observation period.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=67.r5
    h: b7c83a42fd73
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Expected to clear by itself within minutes; service if it persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=67.r5
    h: b7c83a42fd73
  review: drafted
---
