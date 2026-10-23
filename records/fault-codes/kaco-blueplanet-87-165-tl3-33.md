---
id: fc:kaco-blueplanet-87-165-tl3-33
type: FaultCode
name: KACO new energy blueplanet TL3 33
aliases:
- '33'
- KACO new energy 33
- DC feed-in error
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '33'
code_key: '33'
display_message: DC feed-in error
page: 101
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r7
    h: 3386cfc45aca
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-injection-high
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r7
    h: 3386cfc45aca
  review: drafted
- claim_id: c3
  rel: has_recovery
  target: ec:auto-reset
  note: May come from grid conditions; call an electrician only if it keeps happening.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r7
    h: 3386cfc45aca
  review: drafted
  review_note: 'support check: partial - Grid-condition cause and call-if-repeated are stated, but self-clearing
    is not explicitly stated.'
---
