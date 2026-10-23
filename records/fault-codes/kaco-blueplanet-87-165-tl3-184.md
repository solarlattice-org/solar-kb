---
id: fc:kaco-blueplanet-87-165-tl3-184
type: FaultCode
name: KACO new energy blueplanet TL3 184
aliases:
- '184'
- KACO new energy 184
- Protective shutdown over-current L1 int.
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '184'
code_key: '184'
display_message: Protective shutdown over-current L1 int.
page: 109
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r4
    h: 1109f9338971
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:overcurrent
  note: Internal overcurrent on phase L1.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r4
    h: 1109f9338971
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  note: The label states a protective shutdown.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r4
    h: 1109f9338971
  review: drafted
---
