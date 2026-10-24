---
id: fc:solis-s6-eh3p-30-60k-us-batnamefail
type: FaultCode
name: Solis S6-EH3P30-60K BatName-FAIL
aliases:
- BatName-FAIL
- batnamefail
- Solis BatName-FAIL
- Wrong battery brand selection
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-30-60k-us
family_name: Solis S6-EH3P(30-60)K-NV-YD-H-US
code: BatName-FAIL
code_key: batnamefail
display_message: Wrong battery brand selection
page: 93
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r1
    h: 8c7f6906ffcd
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=27.r1
    h: 8c7f6906ffcd
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:configuration-error
  note: Selected battery model differs from installed battery
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r1
    h: 8c7f6906ffcd
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r1
    h: 8c7f6906ffcd
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r1
    h: 8c7f6906ffcd
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-settings-review
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r1
    h: 8c7f6906ffcd
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r1
    h: 8c7f6906ffcd
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r1
    h: 8c7f6906ffcd
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:solis-s6-eh3p-30-60k-us
  cite:
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r1
    h: 8c7f6906ffcd
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20251202
    loc: tbl=27.r1
    h: 8c7f6906ffcd
  review: drafted
---
