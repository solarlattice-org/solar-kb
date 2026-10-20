---
id: fc:chint-sca-36ktl-fault130
type: FaultCode
name: CPS SCA36KTL Fault0130
aliases:
- Fault0130
- fault130
- CPS Fault0130
- Bus over total voltage
category: Inverters
make: chint
make_name: CPS
model_family: sca-36ktl
family_name: CPS SCA36KTL-DO/US-480
code: Fault0130
code_key: fault130
display_message: Bus over total voltage
vendor_severity: Fault
page: 9
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=12.r1
    h: 0945baa8041b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=12.r1
    h: 0945baa8041b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-link-fault
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=12.r1
    h: 0945baa8041b
  review: drafted
  review_note: 'support check: partial - Bus over total voltage plausibly means a DC link/bus fault, but
    the passage does not name it a DC link fault.'
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=12.r1
    h: 0945baa8041b
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=12.r1
    h: 0945baa8041b
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Replace inverter if restart does not clear the fault.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=12.r1
    h: 0945baa8041b
  review: drafted
---
