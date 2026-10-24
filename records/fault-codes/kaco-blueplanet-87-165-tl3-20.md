---
id: fc:kaco-blueplanet-87-165-tl3-20
type: FaultCode
name: KACO new energy blueplanet TL3 20
aliases:
- '20'
- KACO new energy 20
- Power rampup active
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '20'
code_key: '20'
display_message: Power rampup active
page: 101
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r5
    h: ca0bb0b9f7bc
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r5
    h: ca0bb0b9f7bc
  review: drafted
  review_note: 'support check: partial - Ramp-up is a status-like state, but informational is not explicitly
    stated.'
- claim_id: c3
  rel: reports
  target: symptom:inverter-power-derating
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r5
    h: ca0bb0b9f7bc
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:derate
  note: stated as a curve or ramp, not a single value
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r5
    h: ca0bb0b9f7bc
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Output ramps back up on its own after the triggering event.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r5
    h: ca0bb0b9f7bc
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r5
    h: ca0bb0b9f7bc
  review: drafted
---
