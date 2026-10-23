---
id: fc:chint-sca-50-100k-t-pfault80
type: FaultCode
name: CPS SCA50-100K-T PFault0080
aliases:
- PFault0080
- pfault80
- CPS PFault0080
- Inv HW Overcurr Fault
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: PFault0080
code_key: pfault80
display_message: Inv HW Overcurr Fault
page: 152
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=70.r3
    h: a8a1ed50bb62
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:overcurrent
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=70.r3
    h: a8a1ed50bb62
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=70.r3
    h: a8a1ed50bb62
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=69
    h: ea31ef6dd96a
  review: drafted
  review_note: 'support check: partial - Listed as hardware fault requiring restart, implying fault, but
    not explicitly classified.'
- claim_id: c4
  rel: has_recovery
  target: ec:manual-reset
  note: Power cycle first; contact service if the fault persists
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=70.r3
    h: a8a1ed50bb62
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=70.r3
    h: a8a1ed50bb62
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=70.r3
    h: a8a1ed50bb62
  review: drafted
---
