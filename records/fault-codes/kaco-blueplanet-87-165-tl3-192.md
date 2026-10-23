---
id: fc:kaco-blueplanet-87-165-tl3-192
type: FaultCode
name: KACO new energy blueplanet TL3 192
aliases:
- '192'
- KACO new energy 192
- Semiconductor module 1 in channel B defective
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '192'
code_key: '192'
display_message: Semiconductor module 1 in channel B defective
page: 109
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r12
    h: 3e539ec617de
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:power-stage-fault
  note: Label names a defective semiconductor module.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r12
    h: 3e539ec617de
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r12
    h: 3e539ec617de
  review: drafted
  review_note: 'support check: partial - Semiconductor module only implies the inverter bridge; it is
    not stated.'
---
