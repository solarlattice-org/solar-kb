---
id: fc:kaco-blueplanet-87-165-tl3-194
type: FaultCode
name: KACO new energy blueplanet TL3 194
aliases:
- '194'
- KACO new energy 194
- Semiconductor module 3 in channel B defective
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '194'
code_key: '194'
display_message: Semiconductor module 3 in channel B defective
page: 109
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r14
    h: 3ef01d48d860
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:power-stage-fault
  note: Label names a defective semiconductor module.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r14
    h: 3ef01d48d860
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r14
    h: 3ef01d48d860
  review: drafted
  review_note: 'support check: partial - Semiconductor module only implies the inverter bridge; it is
    not stated.'
- claim_id: c4
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r14
    h: 3ef01d48d860
  review: drafted
---
