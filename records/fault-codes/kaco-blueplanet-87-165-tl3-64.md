---
id: fc:kaco-blueplanet-87-165-tl3-64
type: FaultCode
name: KACO new energy blueplanet TL3 64
aliases:
- '64'
- KACO new energy 64
- Output current limitation
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '64'
code_key: '64'
display_message: Output current limitation
page: 105
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r3
    h: 7c9703d3cbb9
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-power-derating
  note: Per-phase feed-in current reached its maximum
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r3
    h: 7c9703d3cbb9
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:derate
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r3
    h: 7c9703d3cbb9
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r3
    h: 7c9703d3cbb9
  review: drafted
---
