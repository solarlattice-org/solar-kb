---
id: fc:chint-sca-25ktl-208-pvxreverse
type: FaultCode
name: CPS SCA25KTL-208 PVxReverse
aliases:
- PVxReverse
- pvxreverse
- CPS PVxReverse
- PVx input reverse connection x=1,2,3
category: Inverters
make: chint
make_name: CPS
model_family: sca-25ktl-208
family_name: CPS SCA25KTL-DO/US-208
code: PVxReverse
code_key: pvxreverse
display_message: PVx input reverse connection x=1,2,3
vendor_severity: Protection
page: 127
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r6
    h: 5ce1c03d127e
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r6
    h: 5ce1c03d127e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r6
    h: 5ce1c03d127e
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51
    h: 712a20a43880
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r6
    h: 5ce1c03d127e
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r6
    h: 5ce1c03d127e
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:string-isolation
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r6
    h: 5ce1c03d127e
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:dc-wiring-check
  note: Correct the reversed string connection.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r6
    h: 5ce1c03d127e
  review: drafted
- claim_id: c8
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r6
    h: 5ce1c03d127e
  review: drafted
  review_note: 'support check: partial - The passage gives no explicit stop or trip behaviour, only a
    protection-type fault.'
---
