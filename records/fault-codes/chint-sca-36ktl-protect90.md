---
id: fc:chint-sca-36ktl-protect90
type: FaultCode
name: CPS SCA36KTL Protect0090
aliases:
- Protect0090
- protect90
- CPS Protect0090
- Bus over voltage
category: Inverters
make: chint
make_name: CPS
model_family: sca-36ktl
family_name: CPS SCA36KTL-DO/US-480
code: Protect0090
code_key: protect90
display_message: Bus over voltage
vendor_severity: Protection
page: 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r1
    h: d4706207afda
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r1
    h: d4706207afda
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-link-fault
  note: DC bus overvoltage.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r1
    h: d4706207afda
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r1
    h: d4706207afda
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r1
    h: d4706207afda
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  note: If restart does not clear the fault.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r1
    h: d4706207afda
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: AC/DC power cycle first; replace inverter if persistent.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r1
    h: d4706207afda
  review: drafted
---
