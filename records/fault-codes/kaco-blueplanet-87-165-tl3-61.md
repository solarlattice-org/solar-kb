---
id: fc:kaco-blueplanet-87-165-tl3-61
type: FaultCode
name: KACO new energy blueplanet TL3 61
aliases:
- '61'
- KACO new energy 61
- External limit
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '61'
code_key: '61'
display_message: External limit
page: 104
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r6
    h: 357a0d086fb5
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:remote-power-limit
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r6
    h: 357a0d086fb5
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r6
    h: 357a0d086fb5
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:derate
  note: Reduction demanded by grid operator; no value stated
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r6
    h: 357a0d086fb5
  review: drafted
  review_note: 'support check: partial - Power reduction is required by the grid operator, but the row
    says it is a status message and doesn''t explicitly…'
---
