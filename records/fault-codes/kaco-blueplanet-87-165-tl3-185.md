---
id: fc:kaco-blueplanet-87-165-tl3-185
type: FaultCode
name: KACO new energy blueplanet TL3 185
aliases:
- '185'
- KACO new energy 185
- Protective shutdown over-current L2 int.
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '185'
code_key: '185'
display_message: Protective shutdown over-current L2 int.
page: 109
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r5
    h: cdc5373e193c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:overcurrent
  note: Internal overcurrent on phase L2; full description deferred to another code not in evidence.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r5
    h: cdc5373e193c
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  note: Label states a protective shutdown.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r5
    h: cdc5373e193c
  review: drafted
---
