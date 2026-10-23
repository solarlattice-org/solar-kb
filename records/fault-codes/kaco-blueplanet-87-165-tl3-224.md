---
id: fc:kaco-blueplanet-87-165-tl3-224
type: FaultCode
name: KACO new energy blueplanet TL3 224
aliases:
- '224'
- KACO new energy 224
- External limitation
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '224'
code_key: '224'
display_message: External limitation
page: 110
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r10
    h: bd3845a1600c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:remote-power-limit
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r10
    h: bd3845a1600c
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r10
    h: bd3845a1600c
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:derate
  note: Relative active power setpoint from external source; no value stated.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r10
    h: bd3845a1600c
  review: drafted
---
