---
id: fc:kaco-blueplanet-87-165-tl3-73
type: FaultCode
name: KACO new energy blueplanet TL3 73
aliases:
- '73'
- KACO new energy 73
- Standalone grid error
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '73'
code_key: '73'
display_message: Standalone grid error
page: 105
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r8
    h: 9d8f74d34e77
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-loss
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r8
    h: 9d8f74d34e77
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r8
    h: 9d8f74d34e77
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r8
    h: 9d8f74d34e77
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:grid-voltage-measurement
  note: Verify all three grid phases are present; standalone grid detection only active in some country
    settings.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r8
    h: 9d8f74d34e77
  review: drafted
  review_note: 'support check: partial - Action asks to check that the grid is present on all three phases
    and says detection is country-dependent, but a…'
- claim_id: c6
  rel: mitigated_by
  target: mit:external-fuse-check
  note: Applies when tripped fuses cause missing phases.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r8
    h: 9d8f74d34e77
  review: drafted
---
