---
id: fc:kaco-blueplanet-87-165-tl3-100
type: FaultCode
name: KACO new energy blueplanet TL3 100
aliases:
- '100'
- KACO new energy 100
- Protection shutdown HW overtemperature
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '100'
code_key: '100'
display_message: Protection shutdown HW overtemperature
page: 106
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r13
    h: 7b1326478b21
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r13
    h: 7b1326478b21
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r13
    h: 7b1326478b21
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r13
    h: 7b1326478b21
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: AC and DC power cycle first; service if the restart does not clear it.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r13
    h: 7b1326478b21
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r13
    h: 7b1326478b21
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Escalation when the power cycle fails.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r13
    h: 7b1326478b21
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r13
    h: 7b1326478b21
  review: drafted
---
