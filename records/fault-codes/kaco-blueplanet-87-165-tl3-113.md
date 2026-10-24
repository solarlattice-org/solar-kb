---
id: fc:kaco-blueplanet-87-165-tl3-113
type: FaultCode
name: KACO new energy blueplanet TL3 113
aliases:
- '113'
- KACO new energy 113
- Grid failure undervoltage L3
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '113'
code_key: '113'
display_message: Grid failure undervoltage L3
page: 107
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r10
    h: 641c400f3218
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r10
    h: 641c400f3218
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r10
    h: 641c400f3218
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78
    h: 814cf8fe747c
  review: drafted
  review_note: 'support check: partial - Via 108''s ''Check connection/cabling'' the AC cabling is implied,
    but the passages never say the fault affects an AC cable.'
- claim_id: c4
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r10
    h: 641c400f3218
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78
    h: 814cf8fe747c
  review: drafted
  review_note: 'support check: partial - The grid voltage on the phase is outside limits, implying voltage
    monitoring, but a grid voltage measurement method is not…'
- claim_id: c5
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r10
    h: 641c400f3218
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78
    h: 814cf8fe747c
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r10
    h: 641c400f3218
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78
    h: 814cf8fe747c
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r10
    h: 641c400f3218
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78
    h: 814cf8fe747c
  review: drafted
  review_note: 'support check: partial - The row defers to 108, which describes a shutdown (a fault).
    Fault is implied, but 113''s own Per s. is…'
- claim_id: c8
  rel: has_production_effect
  target: ec:trip
  note: Row defers to the referenced overvoltage entry, which describes a shutdown when phase voltage
    leaves set limits.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r10
    h: 641c400f3218
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78
    h: 814cf8fe747c
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r10
    h: 641c400f3218
  review: drafted
---
