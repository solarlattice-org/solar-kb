---
id: fc:kaco-blueplanet-87-165-tl3-31
type: FaultCode
name: KACO new energy blueplanet TL3 31
aliases:
- '31'
- KACO new energy 31
- AFI module fault
category: Inverters
make: kaco
make_name: KACO new energy
model_family: blueplanet-87-165-tl3
family_name: KACO blueplanet 87.0-165 TL3
code: '31'
code_key: '31'
display_message: AFI module fault
page: 101
claims:
- claim_id: c1
  rel: defined_in
  target: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r6
    h: 3d221759beda
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r6
    h: 3d221759beda
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:residual-current-device-failure
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r6
    h: 3d221759beda
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:ground-fault-detector
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=72.r6
    h: 3d221759beda
  review: drafted
---
