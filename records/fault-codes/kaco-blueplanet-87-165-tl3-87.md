---
id: fc:kaco-blueplanet-87-165-tl3-87
type: FaultCode
name: KACO new energy blueplanet TL3 87
aliases:
- '87'
- KACO new energy 87
- Protection shutdown over-current L1
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '87'
code_key: '87'
display_message: Protection shutdown over-current L1
page: 106
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r8
    h: 6690ba2c14b7
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:ac-overcurrent
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r8
    h: 6690ba2c14b7
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r8
    h: 6690ba2c14b7
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r8
    h: 6690ba2c14b7
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-installer
  note: Only on repeated occurrence.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=77.r8
    h: 6690ba2c14b7
  review: drafted
---
