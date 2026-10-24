---
id: fc:kaco-blueplanet-87-165-tl3-205
type: FaultCode
name: KACO new energy blueplanet TL3 205
aliases:
- '205'
- KACO new energy 205
- Protection shutdown grid voltage (effective value) L3
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '205'
code_key: '205'
display_message: Protection shutdown grid voltage (effective value) L3
page: 110
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r3
    h: bb0eb2ed9a60
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  note: 'Row refers to code 203 description: excessive effective grid voltage on phase L3.'
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r3
    h: bb0eb2ed9a60
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81
    h: 244f6b44216f
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r3
    h: bb0eb2ed9a60
  review: drafted
  review_note: 'support check: partial - Protection shutdown implies a fault, but no explicit classification.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r3
    h: bb0eb2ed9a60
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r3
    h: bb0eb2ed9a60
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
    loc: tbl=81.r3
    h: bb0eb2ed9a60
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81
    h: 244f6b44216f
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r3
    h: bb0eb2ed9a60
  review: drafted
---
