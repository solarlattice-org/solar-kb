---
id: fc:kaco-blueplanet-87-165-tl3-11
type: FaultCode
name: KACO new energy blueplanet TL3 11
aliases:
- '11'
- KACO new energy 11
- Power limitation
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '11'
code_key: '11'
display_message: Power limitation
page: 101
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r2
    h: 7dfae2e2c080
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-power-derating
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r2
    h: 7dfae2e2c080
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r2
    h: 7dfae2e2c080
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:derate
  note: Thermal protection limits power; the row gives no limit value.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r2
    h: 7dfae2e2c080
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r2
    h: 7dfae2e2c080
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:installation-clearance
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r2
    h: 7dfae2e2c080
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:adequate-cooling
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r2
    h: 7dfae2e2c080
  review: drafted
---
