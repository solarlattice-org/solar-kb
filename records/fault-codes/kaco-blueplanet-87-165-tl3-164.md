---
id: fc:kaco-blueplanet-87-165-tl3-164
type: FaultCode
name: KACO new energy blueplanet TL3 164
aliases:
- '164'
- KACO new energy 164
- 'Error: Filter relay L1'
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '164'
code_key: '164'
display_message: 'Error: Filter relay L1'
page: 108
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r12
    h: a7b1c88e4616
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:self-test-failure
  note: Uses the code 160 description through the table reference.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r12
    h: a7b1c88e4616
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79
    h: e08e6eb3b9d3
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:relay-failure
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r12
    h: a7b1c88e4616
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79
    h: e08e6eb3b9d3
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:filter-contactor
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r12
    h: a7b1c88e4616
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r12
    h: a7b1c88e4616
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79
    h: e08e6eb3b9d3
  review: drafted
---
