---
id: fc:kaco-blueplanet-87-165-tl3-49
type: FaultCode
name: KACO new energy blueplanet TL3 49
aliases:
- '49'
- KACO new energy 49
- Grid failure overfrequency
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '49'
code_key: '49'
display_message: Grid failure overfrequency
page: 103
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74.r5
    h: 541b41c674b3
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overfrequency
  note: Taken from the label; the row's description says below the limit, which conflicts with the label.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74.r5
    h: 541b41c674b3
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:inverter-settings-review
  note: Uses the code 48 action that the row points to.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74.r5
    h: 541b41c674b3
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74
    h: 25a11d4e57bc
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74.r5
    h: 541b41c674b3
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74
    h: 25a11d4e57bc
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74.r5
    h: 541b41c674b3
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74
    h: 25a11d4e57bc
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74.r5
    h: 541b41c674b3
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74
    h: 25a11d4e57bc
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74.r5
    h: 541b41c674b3
  review: drafted
---
