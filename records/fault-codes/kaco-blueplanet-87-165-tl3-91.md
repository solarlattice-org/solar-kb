---
id: fc:kaco-blueplanet-87-165-tl3-91
type: FaultCode
name: KACO new energy blueplanet TL3 91
aliases:
- '91'
- KACO new energy 91
- Protective shutdown drop 2.5 V
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '91'
code_key: '91'
display_message: Protective shutdown drop 2.5 V
page: 106
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r11
    h: 035b9967d2b8
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r11
    h: 035b9967d2b8
  review: drafted
  review_note: 'support check: partial - The label says only ''protective shutdown'' and gives no description,
    so the fault class is implied but not stated.'
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  note: Only the label states a protective shutdown; no description given.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r11
    h: 035b9967d2b8
  review: drafted
  review_note: 'review: partial - Only the label ''Protective shutdown drop 2.5 V'' suggests production
    stops; the row gives no description, action or severity to confirm a…'
- claim_id: c4
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r11
    h: 035b9967d2b8
  review: drafted
---
