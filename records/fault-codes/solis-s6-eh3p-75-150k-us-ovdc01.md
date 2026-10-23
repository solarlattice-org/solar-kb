---
id: fc:solis-s6-eh3p-75-150k-us-ovdc01
type: FaultCode
name: Solis S6-EH3P75-150K OV-DC01
aliases:
- OV-DC01
- ovdc01
- Solis OV-DC01
- DC 1 input overvoltage
category: Inverters
make: solis
make_name: Solis
model_family: s6-eh3p-75-150k-us
family_name: Solis S6-EH3P(75-150)K10-NV-YD-H-US
code: OV-DC01
code_key: ovdc01
display_message: DC 1 input overvoltage
page: 117
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r6
    h: 9d0cced047a5
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r6
    h: 4b1baa8d81f4
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r6
    h: 9d0cced047a5
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r6
    h: 9d0cced047a5
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r6
    h: 4b1baa8d81f4
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r6
    h: 9d0cced047a5
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r6
    h: 9d0cced047a5
  review: drafted
  review_note: 'support check: partial - The passages say to check PV voltage, which implies PV input,
    but the PV array is not named.'
- claim_id: c4
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r6
    h: 4b1baa8d81f4
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r6
    h: 9d0cced047a5
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r6
    h: 9d0cced047a5
  review: drafted
  review_note: 'support check: partial - The passages say to check whether PV voltage is abnormal, but
    do not name DC voltage measurement.'
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Restart after checking PV voltage
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r6
    h: 4b1baa8d81f4
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r6
    h: 9d0cced047a5
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r6
    h: 9d0cced047a5
  review: drafted
---
