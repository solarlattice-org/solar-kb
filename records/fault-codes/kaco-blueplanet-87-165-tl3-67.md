---
id: fc:kaco-blueplanet-87-165-tl3-67
type: FaultCode
name: KACO new energy blueplanet TL3 67
aliases:
- '67'
- KACO new energy 67
- Fehler Leistungsteil 1
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '67'
code_key: '67'
display_message: Fehler Leistungsteil 1
page: 105
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r4
    h: f88e00390eb6
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:power-stage-fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r4
    h: f88e00390eb6
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r4
    h: f88e00390eb6
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:power-board
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r4
    h: f88e00390eb6
  review: drafted
  review_note: 'support check: partial - The fault is in the power section (Leistungsteil), which approximately
    maps to power board, but the row doesn''t name a board.'
- claim_id: c5
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r4
    h: f88e00390eb6
  review: drafted
---
