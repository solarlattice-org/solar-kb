---
id: fc:chint-sca-50-60ktl-protect70
type: FaultCode
name: CPS SCA50-60KTL Protect0070
aliases:
- Protect0070
- protect70
- CPS Protect0070
- Bus imbalance
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-60ktl
family_name: CPS SCA50/60KTL-DO/US-480
code: Protect0070
code_key: protect70
display_message: Bus imbalance
vendor_severity: Protection
page: 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r2
    h: bb2b32a0ddaa
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r2
    h: bb2b32a0ddaa
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-link-fault
  note: DC bus imbalance.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r2
    h: bb2b32a0ddaa
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r2
    h: bb2b32a0ddaa
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Raise DC current limit to tolerate grid phase imbalance.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r2
    h: bb2b32a0ddaa
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  note: If alarm persists after adjustment.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r2
    h: bb2b32a0ddaa
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:chint-sca-50-60ktl
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r2
    h: bb2b32a0ddaa
  review: drafted
---
