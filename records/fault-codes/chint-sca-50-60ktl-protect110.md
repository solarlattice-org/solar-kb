---
id: fc:chint-sca-50-60ktl-protect110
type: FaultCode
name: CPS SCA50-60KTL Protect0110
aliases:
- Protect0110
- protect110
- CPS Protect0110
- BUS over voltage (firmware)
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-60ktl
family_name: CPS SCA50/60KTL-DO/US-480
code: Protect0110
code_key: protect110
display_message: BUS over voltage (firmware)
vendor_severity: Protection
page: 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r1
    h: b133e912c4c1
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r1
    h: b133e912c4c1
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-link-fault
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r1
    h: b133e912c4c1
  review: drafted
  review_note: 'support check: partial - Bus over voltage (firmware) approximates a DC link fault but
    is not stated as such.'
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r1
    h: b133e912c4c1
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r1
    h: b133e912c4c1
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle first; replace inverter if fault persists.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=9.r1
    h: b133e912c4c1
  review: drafted
---
