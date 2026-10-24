---
id: fc:kaco-blueplanet-87-165-tl3-203
type: FaultCode
name: KACO new energy blueplanet TL3 203
aliases:
- '203'
- KACO new energy 203
- Protection shutdown grid voltage (effective value) L1
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '203'
code_key: '203'
display_message: Protection shutdown grid voltage (effective value) L1
page: 110
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r1
    h: bf9cd7e88c2a
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  note: Based on RMS voltage of the phase.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r1
    h: bf9cd7e88c2a
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r1
    h: bf9cd7e88c2a
  review: drafted
  review_note: 'support check: partial - Action says to check AC-side wiring, but the row doesn''t state
    that the AC cable is affected.'
- claim_id: c4
  rel: mitigated_by
  target: mit:ac-connection-check
  note: If recurring, inspect the installation; if installation is fine, device fault is suspected.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r1
    h: bf9cd7e88c2a
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r1
    h: bf9cd7e88c2a
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r1
    h: bf9cd7e88c2a
  review: drafted
  review_note: 'support check: partial - A protective shutdown and device fault are mentioned, but no
    explicit fault classification.'
- claim_id: c7
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r1
    h: bf9cd7e88c2a
  review: drafted
---
