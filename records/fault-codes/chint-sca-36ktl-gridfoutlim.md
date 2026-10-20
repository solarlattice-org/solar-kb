---
id: fc:chint-sca-36ktl-gridfoutlim
type: FaultCode
name: CPS SCA36KTL GridF.OutLim
aliases:
- GridF.OutLim
- gridfoutlim
- CPS GridF.OutLim
category: Inverters
make: chint
make_name: CPS
model_family: sca-36ktl
family_name: CPS SCA36KTL-DO/US-480
code: GridF.OutLim
code_key: gridfoutlim
vendor_severity: Protection
page: 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r5
    h: 37a70970837e
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r5
    h: 37a70970837e
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-frequency-out-of-range
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r5
    h: 37a70970837e
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r5
    h: 37a70970837e
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  note: Restart once the measured frequency is within limits.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r5
    h: 37a70970837e
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r5
    h: 37a70970837e
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6
    h: a184c25be254
  review: drafted
  review_note: 'support check: partial - Protection type with restart implied, but stopping is not explicitly
    stated.'
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r5
    h: 37a70970837e
  review: drafted
---
