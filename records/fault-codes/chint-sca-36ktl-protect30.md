---
id: fc:chint-sca-36ktl-protect30
type: FaultCode
name: CPS SCA36KTL Protect0030
aliases:
- Protect0030
- protect30
- CPS Protect0030
- Inverter Over Current
category: Inverters
make: chint
make_name: CPS
model_family: sca-36ktl
family_name: CPS SCA36KTL-DO/US-480
code: Protect0030
code_key: protect30
display_message: Inverter Over Current
vendor_severity: Protection
page: 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r3
    h: eb83a32c1f6c
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r3
    h: eb83a32c1f6c
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r3
    h: eb83a32c1f6c
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r3
    h: eb83a32c1f6c
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  note: If restart does not clear the fault.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r3
    h: eb83a32c1f6c
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: AC/DC power cycle first; replace inverter if persistent.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r3
    h: eb83a32c1f6c
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:chint-sca-36ktl
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r3
    h: eb83a32c1f6c
  review: drafted
---
