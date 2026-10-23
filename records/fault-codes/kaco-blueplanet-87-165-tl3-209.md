---
id: fc:kaco-blueplanet-87-165-tl3-209
type: FaultCode
name: KACO new energy blueplanet TL3 209
aliases:
- '209'
- KACO new energy 209
- 'Detection of hardware de-tection failed: AC relay board'
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '209'
code_key: '209'
display_message: 'Detection of hardware de-tection failed: AC relay board'
page: 110
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r7
    h: 89bb2d6ff4a5
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:memory-error
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r7
    h: 89bb2d6ff4a5
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:grid-relay
  note: Erroneous data stored on the AC relay board.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r7
    h: 89bb2d6ff4a5
  review: drafted
  review_note: 'support check: partial - The AC relay board is named, but a grid tie relay component is
    not explicitly stated; the board is not…'
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r7
    h: 89bb2d6ff4a5
  review: drafted
  review_note: 'support check: partial - Hardware detection failure needing a restart implies a fault,
    but the row doesn''t state a classification explicitly.'
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r7
    h: 89bb2d6ff4a5
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r7
    h: 89bb2d6ff4a5
  review: drafted
---
