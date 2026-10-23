---
id: fc:kaco-blueplanet-87-165-tl3-105
type: FaultCode
name: KACO new energy blueplanet TL3 105
aliases:
- '105'
- KACO new energy 105
- Relay plausibility error
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '105'
code_key: '105'
display_message: Relay plausibility error
page: 107
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r3
    h: d543da602dfa
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:relay-voltage-mismatch
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r3
    h: d543da602dfa
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: affects
  target: comp:grid-relay
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r3
    h: d543da602dfa
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r3
    h: d543da602dfa
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Full AC and DC power-off first; recurrence indicates a device fault needing service.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r3
    h: d543da602dfa
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=78.r3
    h: d543da602dfa
  review: drafted
---
