---
id: fc:kaco-blueplanet-87-165-tl3-148
type: FaultCode
name: KACO new energy blueplanet TL3 148
aliases:
- '148'
- KACO new energy 148
- External memory error 1
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '148'
code_key: '148'
display_message: External memory error 1
page: 108
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r5
    h: 3d2fded5f7eb
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:memory-error
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r5
    h: 3d2fded5f7eb
  review: drafted
  review_note: 'support check: partial - Display says External memory error 1 while description refers
    to permanent internal memory; internal memory error is only loosely supported.'
- claim_id: c3
  rel: affects
  target: comp:memory-unit
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r5
    h: 3d2fded5f7eb
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r5
    h: 3d2fded5f7eb
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r5
    h: 3d2fded5f7eb
  review: drafted
---
