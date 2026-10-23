---
id: fc:kaco-blueplanet-87-165-tl3-161
type: FaultCode
name: KACO new energy blueplanet TL3 161
aliases:
- '161'
- KACO new energy 161
- 'Error: Grid relay L2'
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '161'
code_key: '161'
display_message: 'Error: Grid relay L2'
page: 108
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r10
    h: 143de31e90b1
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:self-test-failure
  note: Uses the code 160 description through the table reference.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r10
    h: 143de31e90b1
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79
    h: e08e6eb3b9d3
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:relay-failure
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r10
    h: 143de31e90b1
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79
    h: e08e6eb3b9d3
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:grid-relay
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r10
    h: 143de31e90b1
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r10
    h: 143de31e90b1
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79
    h: e08e6eb3b9d3
  review: drafted
---
