---
id: fc:chint-sca-50-60ktl-fault20
type: FaultCode
name: CPS SCA50-60KTL Fault0020
aliases:
- Fault0020
- fault20
- CPS Fault0020
- Bus over volt Hardware
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-60ktl
family_name: CPS SCA50/60KTL-DO/US-480
code: Fault0020
code_key: fault20
display_message: Bus over volt Hardware
vendor_severity: Fault
page: 8
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r1
    h: 99c383fadafa
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r1
    h: 99c383fadafa
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-link-fault
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r1
    h: 99c383fadafa
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r1
    h: 99c383fadafa
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r1
    h: 99c383fadafa
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Replace inverter if restart does not clear the fault.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r1
    h: 99c383fadafa
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:chint-sca-50-60ktl
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r1
    h: 99c383fadafa
  review: drafted
---
