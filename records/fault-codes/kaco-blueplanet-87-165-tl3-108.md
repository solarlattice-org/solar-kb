---
id: fc:kaco-blueplanet-87-165-tl3-108
type: FaultCode
name: KACO new energy blueplanet TL3 108
aliases:
- '108'
- KACO new energy 108
- Grid failure overvoltage L1
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '108'
code_key: '108'
display_message: Grid failure overvoltage L1
page: 107
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r5
    h: 082fbd8a6ff0
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r5
    h: 082fbd8a6ff0
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r5
    h: 082fbd8a6ff0
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r5
    h: 082fbd8a6ff0
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r5
    h: 082fbd8a6ff0
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r5
    h: 082fbd8a6ff0
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r5
    h: 082fbd8a6ff0
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r5
    h: 082fbd8a6ff0
  review: drafted
---
