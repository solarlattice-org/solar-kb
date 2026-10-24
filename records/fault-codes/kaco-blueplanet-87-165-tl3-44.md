---
id: fc:kaco-blueplanet-87-165-tl3-44
type: FaultCode
name: KACO new energy blueplanet TL3 44
aliases:
- '44'
- KACO new energy 44
- Grid failure overvoltage L2
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '44'
code_key: '44'
display_message: Grid failure overvoltage L2
page: 102
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=73.r8
    h: 981151f50995
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  note: Taken from the label; the row's description says undervoltage, which looks like a copy error.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=73.r8
    h: 981151f50995
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=73.r8
    h: 981151f50995
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-installer
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=73.r8
    h: 981151f50995
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=73.r8
    h: 981151f50995
  review: drafted
---
