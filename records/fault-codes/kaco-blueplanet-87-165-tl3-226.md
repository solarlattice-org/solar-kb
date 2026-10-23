---
id: fc:kaco-blueplanet-87-165-tl3-226
type: FaultCode
name: KACO new energy blueplanet TL3 226
aliases:
- '226'
- KACO new energy 226
- The inverter is disconnected from the grid manually
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '226'
code_key: '226'
display_message: The inverter is disconnected from the grid manually
page: 110
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r11
    h: 436ff261c6ae
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:manual-grid-disconnect
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r11
    h: 436ff261c6ae
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r11
    h: 436ff261c6ae
  review: drafted
  review_note: 'support check: partial - The row describes a manual disconnect status message, which fits
    informational, but the classification is not explicitly stated.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r11
    h: 436ff261c6ae
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Operator reconnects via function button or web interface.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r11
    h: 436ff261c6ae
  review: drafted
---
