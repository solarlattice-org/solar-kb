---
id: fc:chint-sca-50-60ktl-protect150
type: FaultCode
name: CPS SCA50-60KTL Protect0150
aliases:
- Protect0150
- protect150
- CPS Protect0150
- Mini MCU Fault
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-60ktl
family_name: CPS SCA50/60KTL-DO/US-480
code: Protect0150
code_key: protect150
display_message: Mini MCU Fault
vendor_severity: PROTECTION
page: 6
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r3
    h: 73ba725d1aa0
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r3
    h: 73ba725d1aa0
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r3
    h: 73ba725d1aa0
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:control-board
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r3
    h: 73ba725d1aa0
  review: drafted
  review_note: 'support check: partial - Mini MCU fault is internal, but a control board is not explicitly
    named.'
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r3
    h: 73ba725d1aa0
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r3
    h: 73ba725d1aa0
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle first; replace inverter if fault persists.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r3
    h: 73ba725d1aa0
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:chint-sca-50-60ktl
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=8.r3
    h: 73ba725d1aa0
  review: drafted
---
