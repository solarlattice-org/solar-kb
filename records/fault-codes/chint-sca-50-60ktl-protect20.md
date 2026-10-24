---
id: fc:chint-sca-50-60ktl-protect20
type: FaultCode
name: CPS SCA50-60KTL Protect0020
aliases:
- Protect0020
- protect20
- CPS Protect0020
- Grid relay error
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-60ktl
family_name: CPS SCA50/60KTL-DO/US-480
code: Protect0020
code_key: protect20
display_message: Grid relay error
vendor_severity: Protection
page: 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r6
    h: 758dbe74639d
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r6
    h: 758dbe74639d
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:relay-failure
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r6
    h: 758dbe74639d
  review: drafted
  review_note: 'support check: partial - Grid relay error is named, but relay failure as a failure mode
    is only loosely implied.'
- claim_id: c4
  rel: affects
  target: comp:inverter
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r6
    h: 758dbe74639d
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r6
    h: 758dbe74639d
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if a power-cycle does not clear the fault.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r6
    h: 758dbe74639d
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r6
    h: 758dbe74639d
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6
    h: a184c25be254
  review: drafted
  review_note: 'support check: partial - Protection with restart needed implies stop, but not explicitly
    stated.'
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Power-cycle first; replace inverter if fault persists.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r6
    h: 758dbe74639d
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:chint-sca-50-60ktl
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r6
    h: 758dbe74639d
  review: drafted
---
