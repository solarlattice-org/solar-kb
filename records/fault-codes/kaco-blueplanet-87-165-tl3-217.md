---
id: fc:kaco-blueplanet-87-165-tl3-217
type: FaultCode
name: KACO new energy blueplanet TL3 217
aliases:
- '217'
- KACO new energy 217
- Protect. shutdown HW - 24V supply voltage
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '217'
code_key: '217'
display_message: Protect. shutdown HW - 24V supply voltage
page: 110
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r9
    h: 2ac1d067091d
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:supply-voltage-invalid
  note: Internal 24 V supply above permitted maximum.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r9
    h: 2ac1d067091d
  review: drafted
  review_note: 'support check: partial - Supply voltage exceeding its maximum is stated, but ''24 V''
    appears only in the title, not as the exceeded value;…'
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r9
    h: 2ac1d067091d
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r9
    h: 2ac1d067091d
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r9
    h: 2ac1d067091d
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r9
    h: 2ac1d067091d
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=81.r9
    h: 2ac1d067091d
  review: drafted
---
