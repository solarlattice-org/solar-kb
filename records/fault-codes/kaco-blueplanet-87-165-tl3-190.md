---
id: fc:kaco-blueplanet-87-165-tl3-190
type: FaultCode
name: KACO new energy blueplanet TL3 190
aliases:
- '190'
- KACO new energy 190
- Semiconductor module 2 in channel A defective
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '190'
code_key: '190'
display_message: Semiconductor module 2 in channel A defective
page: 109
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r10
    h: 16b60c6be7f5
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:power-stage-fault
  note: Label names a defective semiconductor module.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r10
    h: 16b60c6be7f5
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r10
    h: 16b60c6be7f5
  review: drafted
  review_note: 'support check: partial - The semiconductor module is only implied to be part of the inverter
    bridge, and 189 refers to the filter relay…'
---
