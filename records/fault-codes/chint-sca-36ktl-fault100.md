---
id: fc:chint-sca-36ktl-fault100
type: FaultCode
name: CPS SCA36KTL Fault0100
aliases:
- Fault0100
- fault100
- CPS Fault0100
- Grid relay fault
category: Inverters
make: chint
make_name: CPS
model_family: sca-36ktl
family_name: CPS SCA36KTL-DO/US-480
code: Fault0100
code_key: fault100
display_message: Grid relay fault
vendor_severity: Fault
page: 8
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r5
    h: 647e672a17f1
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r5
    h: 647e672a17f1
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:relay-failure
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r5
    h: 647e672a17f1
  review: drafted
  review_note: 'support check: partial - Grid relay fault implies relay failure, but not stated as failure
    explicitly.'
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r5
    h: 647e672a17f1
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Replace inverter if restart does not clear the fault.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r5
    h: 647e672a17f1
  review: drafted
---
