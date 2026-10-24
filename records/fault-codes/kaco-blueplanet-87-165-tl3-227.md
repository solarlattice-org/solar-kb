---
id: fc:kaco-blueplanet-87-165-tl3-227
type: FaultCode
name: KACO new energy blueplanet TL3 227
aliases:
- '227'
- KACO new energy 227
- Protective shutdown current Schutzabschaltung, die bei (hochohmigen)
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '227'
code_key: '227'
display_message: Protective shutdown current Schutzabschaltung, die bei (hochohmigen)
page: 111
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=82.r2
    h: 9b797fb019a7
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:phase-imbalance
  note: Current asymmetry shutdown for high-impedance grid failures.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=82.r2
    h: 9b797fb019a7
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=82
    h: 319281422b79
  review: drafted
  review_note: 'support check: partial - The passage mentions a current asymmetry protective shutdown
    for (high-impedance) grid failures, but the phase imbalance symptom is only loosely…'
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=82.r2
    h: 9b797fb019a7
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=82
    h: 319281422b79
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=82.r2
    h: 9b797fb019a7
  review: drafted
---
