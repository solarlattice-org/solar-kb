---
id: fc:kaco-blueplanet-87-165-tl3-107
type: FaultCode
name: KACO new energy blueplanet TL3 107
aliases:
- '107'
- KACO new energy 107
- Check surge protection device
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '107'
code_key: '107'
display_message: Check surge protection device
page: 107
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r4
    h: a2d1f75b07bd
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:spd-alarm
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r4
    h: a2d1f75b07bd
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:surge-protector-exhausted
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r4
    h: a2d1f75b07bd
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:surge-protection-device
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r4
    h: a2d1f75b07bd
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:visual-inspection
  note: Check the module's function display for red indication.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r4
    h: a2d1f75b07bd
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:spd-replacement
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r4
    h: a2d1f75b07bd
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r4
    h: a2d1f75b07bd
  review: drafted
  review_note: 'support check: partial - The device continues to feed the grid, which fits a warning,
    but the passages do not use the word warning.'
- claim_id: c8
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r4
    h: a2d1f75b07bd
  review: drafted
- claim_id: c9
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r4
    h: a2d1f75b07bd
  review: drafted
  review_note: 'support check: partial - The module must be checked and replaced if necessary, so service
    is only partly implied, and no KACO Service contact…'
---
