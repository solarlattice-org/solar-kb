---
id: fc:kaco-blueplanet-87-165-tl3-36
type: FaultCode
name: KACO new energy blueplanet TL3 36
aliases:
- '36'
- KACO new energy 36
- Protection shutdown HW
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '36'
code_key: '36'
display_message: Protection shutdown HW
page: 102
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=73.r3
    h: 521185df11f4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:ac-overcurrent
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=73.r3
    h: 521185df11f4
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter-bridge
  note: The AC IGBTs are monitored for saturation.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=73.r3
    h: 521185df11f4
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=73.r3
    h: 521185df11f4
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: This is a group shutdown; the specific cause usually shows up first.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=73.r3
    h: 521185df11f4
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=73.r3
    h: 521185df11f4
  review: drafted
---
