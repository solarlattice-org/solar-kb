---
id: fc:chint-sca-25ktl-208-eepromerr
type: FaultCode
name: CPS SCA25KTL-208 EepromErr
aliases:
- EepromErr
- eepromerr
- CPS EepromErr
category: Inverters
make: chint
make_name: CPS
model_family: sca-25ktl-208
family_name: CPS SCA25KTL-DO/US-208
code: EepromErr
code_key: eepromerr
vendor_severity: Alarm
page: 125
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r7
    h: c288812d88ea
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  note: from the Type column
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r7
    h: c288812d88ea
  review: drafted
- claim_id: c3
  rel: has_recovery
  target: ec:auto-reset
  note: Observe whether the alarm clears on its own
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r7
    h: c288812d88ea
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:chint-sca-25ktl-208
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=49.r7
    h: c288812d88ea
  review: drafted
---
