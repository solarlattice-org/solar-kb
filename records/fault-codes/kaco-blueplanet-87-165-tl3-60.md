---
id: fc:kaco-blueplanet-87-165-tl3-60
type: FaultCode
name: KACO new energy blueplanet TL3 60
aliases:
- '60'
- KACO new energy 60
- Excessive generator voltage / excessive battery voltage
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '60'
code_key: '60'
display_message: Excessive generator voltage / excessive battery voltage
page: 104
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r5
    h: 966ce76fe056
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r5
    h: 966ce76fe056
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  note: Feed-in does not start while PV voltage is too high
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r5
    h: 966ce76fe056
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Feed-in begins once PV voltage falls below the threshold
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r5
    h: 966ce76fe056
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r5
    h: 966ce76fe056
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r5
    h: 966ce76fe056
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: When strings were wired in series instead of parallel
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r5
    h: 966ce76fe056
  review: drafted
---
