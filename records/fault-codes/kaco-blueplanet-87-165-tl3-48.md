---
id: fc:kaco-blueplanet-87-165-tl3-48
type: FaultCode
name: KACO new energy blueplanet TL3 48
aliases:
- '48'
- KACO new energy 48
- Grid failure underfrequency
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '48'
code_key: '48'
display_message: Grid failure underfrequency
page: 103
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74.r4
    h: 3c10d73da350
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-underfrequency
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74.r4
    h: 3c10d73da350
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:inverter-settings-review
  note: Includes checking which country setting is active.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74.r4
    h: 3c10d73da350
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:grid-voltage-measurement
  note: Confirms that all three AC voltages are present.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74.r4
    h: 3c10d73da350
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74.r4
    h: 3c10d73da350
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74.r4
    h: 3c10d73da350
  review: drafted
---
