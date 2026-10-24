---
id: fc:chint-sca-50-100k-t-fault0-150
type: FaultCode
name: CPS SCA50-100K-T Fault0000-0150
aliases:
- Fault0000-0150
- fault0-150
- CPS Fault0000-0150
- PV1…PV16 SwitchConnec tError
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-100k-t
family_name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
code: Fault0000-0150
code_key: fault0-150
code_from: 0
code_to: 150
display_message: PV1…PV16 SwitchConnec tError
vendor_severity: Fault
page: 144
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=62.r4
    h: 89cfb1df0d42
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=62.r4
    h: 89cfb1df0d42
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:pv-input-abnormal
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=62.r4
    h: 89cfb1df0d42
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-disconnect-switch
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=62.r4
    h: 89cfb1df0d42
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:polarity-measurement
  note: Used when alarm does not clear by itself.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=62.r4
    h: 89cfb1df0d42
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:dc-wiring-check
  note: Correct reversed string connection if alarm persists; then service.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=62.r4
    h: 89cfb1df0d42
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Even after self-clearing, DC switches are cycled and inverter restarted; wiring check then service
    if persisting.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=62.r4
    h: 89cfb1df0d42
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:chint-sca-50-100k-t
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=62.r4
    h: 89cfb1df0d42
  review: drafted
---
