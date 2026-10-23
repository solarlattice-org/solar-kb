---
id: fc:chint-sca-25ktl-208-pvxovercurrent
type: FaultCode
name: CPS SCA25KTL-208 PVx Over current
aliases:
- PVx Over current
- pvxovercurrent
- CPS PVx Over current
- PVx Over current x=1,2,3
category: Inverters
make: chint
make_name: CPS
model_family: sca-25ktl-208
family_name: CPS SCA25KTL-DO/US-208
code: PVx Over current
code_key: pvxovercurrent
display_message: PVx Over current x=1,2,3
vendor_severity: Protection
page: 127
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r7
    h: b4cf763ad2d3
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r7
    h: b4cf763ad2d3
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r7
    h: b4cf763ad2d3
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51
    h: 712a20a43880
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:string-current-measurement
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r7
    h: b4cf763ad2d3
  review: drafted
  review_note: 'support check: partial - The passage says to check PV input current but does not describe
    string current measurement as the detection method.'
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r7
    h: b4cf763ad2d3
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r7
    h: b4cf763ad2d3
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r7
    h: b4cf763ad2d3
  review: drafted
  review_note: 'support check: partial - The passage gives no explicit stop or trip behaviour.'
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Check input current, then power cycle; replace inverter if fault persists.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r7
    h: b4cf763ad2d3
  review: drafted
---
