---
id: fc:kaco-blueplanet-87-165-tl3-2
type: FaultCode
name: KACO new energy blueplanet TL3 2
aliases:
- '2'
- KACO new energy 2
- Insufficient generator voltage / insufficient battery voltage!
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '2'
code_key: '2'
display_message: Insufficient generator voltage / insufficient battery voltage!
page: 100
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=71.r1
    h: bbfc085b6270
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-undervoltage
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=71.r1
    h: bbfc085b6270
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:dc-voltage-measurement
  note: Compare displayed voltage with voltage measured at the terminals.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=71.r1
    h: bbfc085b6270
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=71.r1
    h: bbfc085b6270
  review: drafted
  review_note: 'support check: partial - Row says to check for DC polarity reversal but doesn''t state
    a string polarity measurement method.'
- claim_id: c5
  rel: affects
  target: comp:pv-disconnect-switch
  note: Applies to the XL version, where the DC isolator may be switched off.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=71.r1
    h: bbfc085b6270
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=71.r1
    h: bbfc085b6270
  review: drafted
---
