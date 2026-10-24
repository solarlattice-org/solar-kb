---
id: fc:kaco-blueplanet-87-165-tl3-189
type: FaultCode
name: KACO new energy blueplanet TL3 189
aliases:
- '189'
- KACO new energy 189
- Semiconductor module 1 in channel A defective
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '189'
code_key: '189'
display_message: Semiconductor module 1 in channel A defective
page: 109
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r9
    h: 91b07ffa36c3
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:power-stage-fault
  note: Alternatively the associated filter relay does not close correctly.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r9
    h: 91b07ffa36c3
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r9
    h: 91b07ffa36c3
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:filter-contactor
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r9
    h: 91b07ffa36c3
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r9
    h: 91b07ffa36c3
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: AC and DC disconnection and reconnection.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r9
    h: 91b07ffa36c3
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r9
    h: 91b07ffa36c3
  review: drafted
  review_note: 'support check: partial - Row describes a defect needing power cycle, implying a fault,
    but never states a fault classification explicitly.'
- claim_id: c8
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r9
    h: 91b07ffa36c3
  review: drafted
---
