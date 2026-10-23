---
id: fc:kaco-blueplanet-87-165-tl3-58
type: FaultCode
name: KACO new energy blueplanet TL3 58
aliases:
- '58'
- KACO new energy 58
- Control board overtemp.
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '58'
code_key: '58'
display_message: Control board overtemp.
page: 104
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r3
    h: b21b7be70c53
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r3
    h: b21b7be70c53
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r3
    h: b21b7be70c53
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r3
    h: b21b7be70c53
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:fan-function-check
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r3
    h: b21b7be70c53
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:ambient-temperature-check
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r3
    h: b21b7be70c53
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r3
    h: b21b7be70c53
  review: drafted
  review_note: 'support check: partial - Heat sink covered check is implied, but cleaning is not explicitly
    stated.'
- claim_id: c8
  rel: mitigated_by
  target: mit:adequate-cooling
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r3
    h: b21b7be70c53
  review: drafted
---
