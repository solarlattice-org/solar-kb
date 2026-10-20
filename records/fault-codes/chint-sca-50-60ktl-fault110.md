---
id: fc:chint-sca-50-60ktl-fault110
type: FaultCode
name: CPS SCA50-60KTL Fault0110
aliases:
- Fault0110
- fault110
- CPS Fault0110
- Bus imbalance
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-60ktl
family_name: CPS SCA50/60KTL-DO/US-480
code: Fault0110
code_key: fault110
display_message: Bus imbalance
vendor_severity: Fault
page: 8
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r6
    h: 1b64d5e6888e
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r6
    h: 1b64d5e6888e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-link-fault
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r6
    h: 1b64d5e6888e
  review: drafted
  review_note: 'support check: partial - Fault0110 is a ''Bus imbalance'' fault, which loosely relates
    to the DC bus, but the passage never names it a…'
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Raise DC current limit first; replace inverter if alarm persists.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r6
    h: 1b64d5e6888e
  review: drafted
---
