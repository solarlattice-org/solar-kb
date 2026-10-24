---
id: fc:kaco-blueplanet-87-165-tl3-17
type: FaultCode
name: KACO new energy blueplanet TL3 17
aliases:
- '17'
- KACO new energy 17
- 'HMI1: "Powador-protect dis-connection" HMI2: "External grid protection shutdown"'
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '17'
code_key: '17'
display_message: 'HMI1: "Powador-protect dis-connection" HMI2: "External grid protection shutdown"'
page: 101
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r3
    h: 20bdadeae792
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-parameters-out-of-range
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r3
    h: 20bdadeae792
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r3
    h: 20bdadeae792
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:grid-protection-device
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r3
    h: 20bdadeae792
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c5
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r3
    h: 20bdadeae792
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  note: Check the protection device's power supply and cabling.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r3
    h: 20bdadeae792
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:kaco-blueplanet-87-165-tl3
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r3
    h: 20bdadeae792
  review: drafted
---
