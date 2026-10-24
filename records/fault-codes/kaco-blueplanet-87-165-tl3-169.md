---
id: fc:kaco-blueplanet-87-165-tl3-169
type: FaultCode
name: KACO new energy blueplanet TL3 169
aliases:
- '169'
- KACO new energy 169
- 'Error: AFI sensor'
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '169'
code_key: '169'
display_message: 'Error: AFI sensor'
page: 108
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r15
    h: 7df1fc309926
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:residual-current-device-failure
  note: Applies when the residual current sensor cannot be demagnetised before feed-in.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r15
    h: 7df1fc309926
  review: drafted
  review_note: 'review: partial - Row 169 states that the AFI sensor could not be demagnetised and that
    a device error was detected, but calling this a…'
- claim_id: c3
  rel: affects
  target: comp:ground-fault-detector
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r15
    h: 7df1fc309926
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r15
    h: 7df1fc309926
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c5
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=79.r15
    h: 7df1fc309926
  review: drafted
---
