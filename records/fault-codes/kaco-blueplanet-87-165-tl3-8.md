---
id: fc:kaco-blueplanet-87-165-tl3-8
type: FaultCode
name: KACO new energy blueplanet TL3 8
aliases:
- '8'
- KACO new energy 8
- Self-test in progress
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '8'
code_key: '8'
display_message: Self-test in progress
page: 100
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=71.r3
    h: 3007b4ba272a
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Treated as a device fault only if the self-test stays stuck despite adequate DC voltage.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=71.r3
    h: 3007b4ba272a
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:grid-relay
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=71.r3
    h: 3007b4ba272a
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=71.r3
    h: 3007b4ba272a
  review: drafted
---
