---
id: fc:yaskawa-solectria-pvi-20-25tl-480-r-pvreverse
type: FaultCode
name: Yaskawa Solectria PVI-25TL-R PV Reverse
aliases:
- PV Reverse
- pvreverse
- Yaskawa Solectria PV Reverse
- PV input reverse connection
category: Inverters
make: yaskawa-solectria
make_name: Yaskawa Solectria
model_family: pvi-20-25tl-480-r
family_name: Solectria PVI 20/25TL-480-R
code: PV Reverse
code_key: pvreverse
display_message: PV input reverse connection
page: 82
claims:
- claim_id: c1
  rel: defined_in
  target: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r4
    h: 44bbc5349a34
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r4
    h: 44bbc5349a34
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r4
    h: 44bbc5349a34
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r4
    h: 44bbc5349a34
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:polarity-correction
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=37.r4
    h: 44bbc5349a34
  review: drafted
---
