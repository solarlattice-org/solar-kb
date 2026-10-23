---
id: fc:kaco-blueplanet-87-165-tl3-78
type: FaultCode
name: KACO new energy blueplanet TL3 78
aliases:
- '78'
- KACO new energy 78
- Resid. current shutdown (AFI)
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '78'
code_key: '78'
display_message: Resid. current shutdown (AFI)
page: 105
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r10
    h: 8f3d6cf49f3b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:high-leakage-current
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r10
    h: 8f3d6cf49f3b
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r10
    h: 8f3d6cf49f3b
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r10
    h: 8f3d6cf49f3b
  review: drafted
- claim_id: c5
  rel: indicates
  target: fm:insulation-loss
  note: When the fault tends to occur with precipitation or high humidity.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r10
    h: 8f3d6cf49f3b
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r10
    h: 8f3d6cf49f3b
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=76.r10
    h: 8f3d6cf49f3b
  review: drafted
---
