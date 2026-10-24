---
id: fc:kaco-blueplanet-87-165-tl3-206
type: FaultCode
name: KACO new energy blueplanet TL3 206
aliases:
- '206'
- KACO new energy 206
- Protection shutdown over-current HW
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '206'
code_key: '206'
display_message: Protection shutdown over-current HW
page: 110
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r4
    h: 17c5a0b5d695
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:overcurrent
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r4
    h: 17c5a0b5d695
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r4
    h: 17c5a0b5d695
  review: drafted
  review_note: 'support check: partial - Protection shutdown implies a fault, but no explicit classification.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r4
    h: 17c5a0b5d695
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r4
    h: 17c5a0b5d695
  review: drafted
---
