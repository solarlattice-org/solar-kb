---
id: fc:kaco-blueplanet-87-165-tl3-160
type: FaultCode
name: KACO new energy blueplanet TL3 160
aliases:
- '160'
- KACO new energy 160
- 'Error: Grid relay L1'
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '160'
code_key: '160'
display_message: 'Error: Grid relay L1'
page: 108
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r9
    h: 24eb0aab7317
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:self-test-failure
  note: Self-test finds the grid-side relay stuck; switch-on is not checked.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r9
    h: 24eb0aab7317
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:relay-failure
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r9
    h: 24eb0aab7317
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:grid-relay
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r9
    h: 24eb0aab7317
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  note: The row reports a device error with a defective relay.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r9
    h: 24eb0aab7317
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r9
    h: 24eb0aab7317
  review: drafted
---
