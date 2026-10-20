---
id: fc:chint-sca-36ktl-fault80
type: FaultCode
name: CPS SCA36KTL Fault0080
aliases:
- Fault0080
- fault80
- CPS Fault0080
- Bus Hardware overcurrent fault
category: Inverters
make: chint
make_name: CPS
model_family: sca-36ktl
family_name: CPS SCA36KTL-DO/US-480
code: Fault0080
code_key: fault80
display_message: Bus Hardware overcurrent fault
vendor_severity: Fault
page: 8
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r3
    h: 85d01f84874b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r3
    h: 85d01f84874b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-link-fault
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r3
    h: 85d01f84874b
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r3
    h: 85d01f84874b
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r3
    h: 85d01f84874b
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Replace inverter if restart does not clear the fault.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=11.r3
    h: 85d01f84874b
  review: drafted
---
