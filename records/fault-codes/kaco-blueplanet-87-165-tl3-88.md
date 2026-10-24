---
id: fc:kaco-blueplanet-87-165-tl3-88
type: FaultCode
name: KACO new energy blueplanet TL3 88
aliases:
- '88'
- KACO new energy 88
- Protection shutdown over-current L2
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '88'
code_key: '88'
display_message: Protection shutdown over-current L2
page: 106
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r9
    h: 49854e331c41
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:ac-overcurrent
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r9
    h: 49854e331c41
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r9
    h: 49854e331c41
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Label states a protection shutdown on phase L2.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r9
    h: 49854e331c41
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r9
    h: 49854e331c41
  review: drafted
---
