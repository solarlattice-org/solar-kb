---
id: fc:chint-sca-50-60ktl-gridvoutlim
type: FaultCode
name: CPS SCA50-60KTL GridV.OutLim
aliases:
- GridV.OutLim
- gridvoutlim
- CPS GridV.OutLim
category: Inverters
make: chint
make_name: CPS
model_family: sca-50-60ktl
family_name: CPS SCA50/60KTL-DO/US-480
code: GridV.OutLim
code_key: gridvoutlim
vendor_severity: Protection
page: 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r4
    h: ae10c12f715d
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r4
    h: ae10c12f715d
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-voltage-out-of-range
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r4
    h: ae10c12f715d
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:grid-settings-check
  note: Verify AC connections and voltage range before restarting.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r4
    h: ae10c12f715d
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r4
    h: ae10c12f715d
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  note: Protection type; restart instruction implies the inverter stopped.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r4
    h: ae10c12f715d
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6
    h: a184c25be254
  review: drafted
  review_note: 'support check: partial - Row is a Protection type with restart instruction, but trip/stop
    is only implied, not stated.'
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r4
    h: ae10c12f715d
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:chint-sca-50-60ktl
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r4
    h: ae10c12f715d
  review: drafted
---
