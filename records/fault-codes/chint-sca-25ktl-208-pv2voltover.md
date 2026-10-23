---
id: fc:chint-sca-25ktl-208-pv2voltover
type: FaultCode
name: CPS SCA25KTL-208 PV2VoltOver
aliases:
- PV2VoltOver
- pv2voltover
- CPS PV2VoltOver
- PVx Over Volt x=1,2,3
category: Inverters
make: chint
make_name: CPS
model_family: sca-25ktl-208
family_name: CPS SCA25KTL-DO/US-208
code: PV2VoltOver
code_key: pv2voltover
display_message: PVx Over Volt x=1,2,3
vendor_severity: Protection
page: 127
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r8
    h: 8c9d9abc3eb9
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r8
    h: 8c9d9abc3eb9
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r8
    h: 8c9d9abc3eb9
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51
    h: 712a20a43880
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r8
    h: 8c9d9abc3eb9
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r8
    h: 8c9d9abc3eb9
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: When displayed voltage matches the meter reading within tolerance.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r8
    h: 8c9d9abc3eb9
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-replacement
  note: When displayed voltage deviates from the meter reading.
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=51.r8
    h: 8c9d9abc3eb9
  review: drafted
---
