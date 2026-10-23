---
id: fc:kaco-blueplanet-87-165-tl3-204
type: FaultCode
name: KACO new energy blueplanet TL3 204
aliases:
- '204'
- KACO new energy 204
- Protection shutdown grid voltage (effective value) L2
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '204'
code_key: '204'
display_message: Protection shutdown grid voltage (effective value) L2
page: 110
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r2
    h: 4daf20ffe988
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  note: 'Row refers to code 203 description: excessive effective grid voltage on phase L2.'
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r2
    h: 4daf20ffe988
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81
    h: 244f6b44216f
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r2
    h: 4daf20ffe988
  review: drafted
  review_note: 'support check: partial - Protection shutdown implies a fault, but no explicit classification.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r2
    h: 4daf20ffe988
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r2
    h: 4daf20ffe988
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81
    h: 244f6b44216f
  review: drafted
  review_note: 'support check: partial - AC wiring check is advised, but the AC cable is not stated as
    affected.'
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  note: If frequent, installation check; if installation fine, device fault.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r2
    h: 4daf20ffe988
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81
    h: 244f6b44216f
  review: drafted
---
