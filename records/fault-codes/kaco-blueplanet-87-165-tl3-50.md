---
id: fc:kaco-blueplanet-87-165-tl3-50
type: FaultCode
name: KACO new energy blueplanet TL3 50
aliases:
- '50'
- KACO new energy 50
- Grid failure average voltage
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '50'
code_key: '50'
display_message: Grid failure average voltage
page: 104
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r1
    h: 69718aae125b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  note: Average grid voltage per EN 50160 above the permitted limit
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r1
    h: 69718aae125b
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r1
    h: 69718aae125b
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - The row calls it a fault but gives no device behavior; classification
    is only loosely implied.'
- claim_id: c4
  rel: detected_by
  target: method:inverter-settings-review
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r1
    h: 69718aae125b
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:grid-settings-check
  note: Also check software versions and AC cable cross-section
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r1
    h: 69718aae125b
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=75.r1
    h: 69718aae125b
  review: drafted
---
