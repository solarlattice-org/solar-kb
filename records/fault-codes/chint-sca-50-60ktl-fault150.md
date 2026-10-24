---
id: fc:chint-sca-50-60ktl-fault150
type: FaultCode
name: CPS SCA50-60KTL Fault0150
aliases:
- Fault0150
- fault150
- CPS Fault0150
- Open-loop self-check failure
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-60ktl
family_name: CPS SCA50/60KTL-DO/US-480
code: Fault0150
code_key: fault150
display_message: Open-loop self-check failure
vendor_severity: Fault
page: 9
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=12.r2
    h: 5a24e39b8229
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the code prefix
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=12.r2
    h: 5a24e39b8229
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:self-test-failure
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=12.r2
    h: 5a24e39b8229
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=12.r2
    h: 5a24e39b8229
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  note: 'First step: full AC and DC power cycle with discharge wait.'
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=12.r2
    h: 5a24e39b8229
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if the fault persists after the power cycle.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=12.r2
    h: 5a24e39b8229
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Operator power cycle clears normal case; escalate to inverter replacement if fault remains.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=12.r2
    h: 5a24e39b8229
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:chint-sca-50-60ktl
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=12.r2
    h: 5a24e39b8229
  review: drafted
---
