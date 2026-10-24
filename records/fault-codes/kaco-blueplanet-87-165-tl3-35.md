---
id: fc:kaco-blueplanet-87-165-tl3-35
type: FaultCode
name: KACO new energy blueplanet TL3 35
aliases:
- '35'
- KACO new energy 35
- Protect. shutdown SW
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '35'
code_key: '35'
display_message: Protect. shutdown SW
page: 102
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=73.r2
    h: 290a7a24de3f
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=73.r2
    h: 290a7a24de3f
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-bus-overvoltage
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=73.r2
    h: 290a7a24de3f
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=73.r2
    h: 290a7a24de3f
  review: drafted
  review_note: 'support check: partial - A protective shutdown stops the device, which implies a fault,
    but the row doesn''t classify it explicitly; the ''K'' code…'
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=73.r2
    h: 290a7a24de3f
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:mv-transformer
  note: Applies where the plant has its own transformer; its short-circuit voltage shows how inductive
    the grid is.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=73.r2
    h: 290a7a24de3f
  review: drafted
  review_note: 'review: partial - The note correctly paraphrases the transformer short-circuit voltage
    check, but the row uses the transformer only as a grid-inductance diagnostic, never says…'
- claim_id: c7
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=73.r2
    h: 290a7a24de3f
  review: drafted
---
