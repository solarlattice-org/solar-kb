---
id: fc:kaco-blueplanet-87-165-tl3-195
type: FaultCode
name: KACO new energy blueplanet TL3 195
aliases:
- '195'
- KACO new energy 195
- DESAT error
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '195'
code_key: '195'
display_message: DESAT error
page: 109
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r15
    h: 78bc0b582eb7
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-overcurrent-overvoltage
  note: IGBT desaturation monitoring tripped.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r15
    h: 78bc0b582eb7
  review: drafted
  review_note: 'support check: partial - DESAT of the IGBTs tripped implies an internal overcurrent, but
    overvoltage is not mentioned and the passage doesn''t say overcurrent.'
- claim_id: c3
  rel: reports
  target: symptom:driver-supply-undervoltage
  note: 'Alternative cause: gate driver 24 V supply too low.'
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r15
    h: 78bc0b582eb7
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=80.r15
    h: 78bc0b582eb7
  review: drafted
---
