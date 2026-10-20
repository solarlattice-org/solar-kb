---
id: fc:chint-sca-36ktl-protect230
type: FaultCode
name: CPS SCA36KTL Protect0230
aliases:
- Protect0230
- protect230
- CPS Protect0230
- Inverter open-loop self-test fault
category: Inverters
make: chint
make_name: CPS
model_family: sca-36ktl
family_name: CPS SCA36KTL-DO/US-480
code: Protect0230
code_key: protect230
display_message: Inverter open-loop self-test fault
vendor_severity: Protection
page: 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=10.r1
    h: b5e7005e49d2
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=10.r1
    h: b5e7005e49d2
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=10.r1
    h: b5e7005e49d2
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=10.r1
    h: b5e7005e49d2
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=10.r1
    h: b5e7005e49d2
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Replace inverter if restart does not clear the fault.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=10.r1
    h: b5e7005e49d2
  review: drafted
---
