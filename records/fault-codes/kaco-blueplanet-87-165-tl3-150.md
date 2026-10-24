---
id: fc:kaco-blueplanet-87-165-tl3-150
type: FaultCode
name: KACO new energy blueplanet TL3 150
aliases:
- '150'
- KACO new energy 150
- Protective shutdown drop reference ADC
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '150'
code_key: '150'
display_message: Protective shutdown drop reference ADC
page: 108
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r6
    h: ea1313fd3bad
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reference-voltage-out-of-tolerance
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r6
    h: ea1313fd3bad
  review: drafted
  review_note: 'support check: partial - Row only names a protective shutdown on dropped reference ADC
    for measurement accuracy; out-of-tolerance reference voltage is inferred.'
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r6
    h: ea1313fd3bad
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r6
    h: ea1313fd3bad
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r6
    h: ea1313fd3bad
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r6
    h: ea1313fd3bad
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r6
    h: ea1313fd3bad
  review: drafted
---
