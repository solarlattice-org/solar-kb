---
id: fc:kaco-blueplanet-87-165-tl3-47
type: FaultCode
name: KACO new energy blueplanet TL3 47
aliases:
- '47'
- KACO new energy 47
- Grid failure phase-to-phase voltage
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '47'
code_key: '47'
display_message: Grid failure phase-to-phase voltage
page: 103
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74.r3
    h: 597610d0fbde
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-voltage-out-of-range
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74.r3
    h: 597610d0fbde
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:ac-cable
  note: A cable cross-section that is too small can push the voltage up.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74.r3
    h: 597610d0fbde
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74.r3
    h: 597610d0fbde
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:inverter-settings-review
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74.r3
    h: 597610d0fbde
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:fuse-check
  note: AC fuses are checked in case a phase is missing.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74.r3
    h: 597610d0fbde
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74.r3
    h: 597610d0fbde
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74.r3
    h: 597610d0fbde
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=74.r3
    h: 597610d0fbde
  review: drafted
---
