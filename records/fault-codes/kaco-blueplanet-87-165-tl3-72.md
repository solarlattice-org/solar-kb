---
id: fc:kaco-blueplanet-87-165-tl3-72
type: FaultCode
name: KACO new energy blueplanet TL3 72
aliases:
- '72'
- KACO new energy 72
- Fault in fan 3
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '72'
code_key: '72'
display_message: Fault in fan 3
page: 105
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r7
    h: 7d2182fefc27
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:fan-fault-alarm
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r7
    h: 7d2182fefc27
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:fan-failure
  note: Second external fan or its tacho signal
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r7
    h: 7d2182fefc27
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r7
    h: 7d2182fefc27
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:no-production-effect
  note: No direct reduction; temperature derating may follow
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r7
    h: 7d2182fefc27
  review: drafted
---
