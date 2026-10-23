---
id: fc:kaco-blueplanet-87-165-tl3-38
type: FaultCode
name: KACO new energy blueplanet TL3 38
aliases:
- '38'
- KACO new energy 38
- 'Generator voltage too high / fault: Battery overvoltage'
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '38'
code_key: '38'
display_message: 'Generator voltage too high / fault: Battery overvoltage'
page: 102
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=73.r4
    h: 044f3a298ab9
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=73.r4
    h: 044f3a298ab9
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=73.r4
    h: 044f3a298ab9
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=73.r4
    h: 044f3a298ab9
  review: drafted
  review_note: 'support check: partial - The action says to check PV voltage with measuring equipment,
    but the row doesn''t state that detection is by DC…'
- claim_id: c5
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Applies when strings were wired in series where they should be parallel.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=73.r4
    h: 044f3a298ab9
  review: drafted
---
