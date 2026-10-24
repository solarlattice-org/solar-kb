---
id: fc:chint-sca-50-100k-t-pfault0
type: FaultCode
name: CPS SCA50-100K-T PFault0000
aliases:
- PFault0000
- pfault0
- CPS PFault0000
- Bus Sum High Fault
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: PFault0000
code_key: pfault0
display_message: Bus Sum High Fault
page: 151
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r1
    h: 3937d376d785
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r1
    h: 3937d376d785
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69
    h: ea31ef6dd96a
  review: drafted
  review_note: 'support check: partial - The table lists PFault0000 as a hardware fault with a ''Fault''
    name, but it does not say what the device…'
- claim_id: c3
  rel: reports
  target: symptom:dc-bus-overvoltage
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r1
    h: 3937d376d785
  review: drafted
  review_note: 'support check: partial - ''Bus Sum High Fault'' plus the PV voltage limit of 1000 V suggests
    a high DC bus voltage, but the…'
- claim_id: c4
  rel: detected_by
  target: method:dc-voltage-measurement
  note: Compare the measured DC terminal voltage with the displayed value; open-circuit PV voltage must
    stay below the stated limit.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r1
    h: 3937d376d785
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:pv-input-terminal
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r1
    h: 3937d376d785
  review: drafted
  review_note: 'support check: partial - The row refers to the DC terminals in the wire box, which only
    loosely implies the PV input terminal.'
- claim_id: c6
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69.r1
    h: 3937d376d785
  review: drafted
---
