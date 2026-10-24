---
id: fc:chint-sca-50-100k-t-pfault10
type: FaultCode
name: CPS SCA50-100K-T PFault0010
aliases:
- PFault0010
- pfault10
- CPS PFault0010
- Power Fault
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: PFault0010
code_key: pfault10
display_message: Power Fault
page: 151
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r2
    h: dc329cbbdf0f
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r2
    h: dc329cbbdf0f
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69
    h: ea31ef6dd96a
  review: drafted
  review_note: 'support check: partial - The table lists a hardware ''Power Fault'', but it does not state
    the device''s behaviour.'
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r2
    h: dc329cbbdf0f
  review: drafted
  review_note: 'support check: partial - ''Power Fault'' is a hardware fault, but the row does not say
    ''internal device fault''. It is only loosely implied.'
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r2
    h: dc329cbbdf0f
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle AC and DC first; contact service if it persists.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r2
    h: dc329cbbdf0f
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r2
    h: dc329cbbdf0f
  review: drafted
---
