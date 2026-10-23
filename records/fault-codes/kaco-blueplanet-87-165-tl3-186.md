---
id: fc:kaco-blueplanet-87-165-tl3-186
type: FaultCode
name: KACO new energy blueplanet TL3 186
aliases:
- '186'
- KACO new energy 186
- Protective shutdown over-current L3 int.
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '186'
code_key: '186'
display_message: Protective shutdown over-current L3 int.
page: 109
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r6
    h: 539d73b4dcde
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:overcurrent
  note: Internal overcurrent on phase L3; full description deferred to another code not in evidence.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r6
    h: 539d73b4dcde
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  note: Label states a protective shutdown.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r6
    h: 539d73b4dcde
  review: drafted
---
