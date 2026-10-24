---
id: fc:kaco-blueplanet-87-165-tl3-181
type: FaultCode
name: KACO new energy blueplanet TL3 181
aliases:
- '181'
- KACO new energy 181
- Insulation error, centre
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '181'
code_key: '181'
display_message: Insulation error, centre
page: 109
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r1
    h: a4615c726fe3
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:low-insulation-resistance
  note: Fault is located near the centre of the PV string; symmetrical fault resistances are also detected.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r1
    h: a4615c726fe3
  review: drafted
  review_note: 'support check: partial - Insulation error near the string centre and symmetrical fault
    resistances are stated, but low insulation resistance is only implied.'
- claim_id: c3
  rel: indicates
  target: fm:insulation-loss
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r1
    h: a4615c726fe3
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r1
    h: a4615c726fe3
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  note: The fault must be rectified for safe operation.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r1
    h: a4615c726fe3
  review: drafted
  review_note: 'support check: partial - The passage says the faults must be rectified for safe operation,
    but doesn''t explicitly class it as a fault.'
- claim_id: c6
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r1
    h: a4615c726fe3
  review: drafted
---
