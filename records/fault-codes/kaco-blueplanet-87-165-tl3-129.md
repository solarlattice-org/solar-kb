---
id: fc:kaco-blueplanet-87-165-tl3-129
type: FaultCode
name: KACO new energy blueplanet TL3 129
aliases:
- '129'
- KACO new energy 129
- Voltage-dependent power reduction
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '129'
code_key: '129'
display_message: Voltage-dependent power reduction
page: 108
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r4
    h: 965cf64daac9
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-power-derating
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r4
    h: 965cf64daac9
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Only if the grid operator has not requested the voltage-dependent function.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r4
    h: 965cf64daac9
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r4
    h: 965cf64daac9
  review: drafted
---
