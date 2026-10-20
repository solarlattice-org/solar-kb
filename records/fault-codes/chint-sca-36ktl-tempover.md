---
id: fc:chint-sca-36ktl-tempover
type: FaultCode
name: CPS SCA36KTL TempOver
aliases:
- TempOver
- tempover
- CPS TempOver
- Over-temperature protection
category: Inverters
make: chint
make_name: CPS
model_family: sca-36ktl
family_name: CPS SCA36KTL-DO/US-480
code: TempOver
code_key: tempover
display_message: Over-temperature protection
vendor_severity: Protection
page: 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r7
    h: 25366f44879a
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  note: from the Type column
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r7
    h: 25366f44879a
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r7
    h: 25366f44879a
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
- claim_id: c4
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r7
    h: 25366f44879a
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:visual-inspection
  note: Check ambient, air inlet, fan and installation location.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r7
    h: 25366f44879a
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r7
    h: 25366f44879a
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
  review_note: 'support check: partial - Checks for blocked inlet/fan are listed, but clearing the blockage
    is not explicitly stated.'
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: If the alarm does not clear after 30 minutes.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r7
    h: 25366f44879a
  review: drafted
- claim_id: c8
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r7
    h: 25366f44879a
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6
    h: a184c25be254
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
  review_note: 'support check: partial - Protection type, but stopping production is not explicitly stated.'
- claim_id: c9
  rel: has_recovery
  target: ec:auto-reset
  note: Alarm expected to clear on its own; service if not corrected.
  cite:
  - src: src:chint-cps-sca36-50-60ktl-fault-and-troubleshooting
    loc: tbl=6.r7
    h: 25366f44879a
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
---
