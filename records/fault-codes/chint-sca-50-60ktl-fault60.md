---
id: fc:chint-sca-50-60ktl-fault60
type: FaultCode
name: CPS SCA50-60KTL Fault0060
aliases:
- Fault0060
- fault60
- CPS Fault0060
- CPLD Fault
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-60ktl
family_name: CPS SCA50/60KTL-DO/US-480
code: Fault0060
code_key: fault60
display_message: CPLD Fault
vendor_severity: Fault
page: 8
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r2
    h: c1cf3e6f00c2
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r2
    h: c1cf3e6f00c2
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r2
    h: c1cf3e6f00c2
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:control-board
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r2
    h: c1cf3e6f00c2
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r2
    h: c1cf3e6f00c2
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Replace control board or inverter if restart does not clear it.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r2
    h: c1cf3e6f00c2
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:chint-sca-50-60ktl
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r2
    h: c1cf3e6f00c2
  review: drafted
---
