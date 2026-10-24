---
id: fc:solis-1p-4g-us-gridintf
type: FaultCode
name: Solis 1P-4G-US GRID-INTF
aliases:
- GRID-INTF
- gridintf
- Solis GRID-INTF
- Grid unstable
category: Inverters
make: solis
make_name: Solis
model_family: 1p-4g-us
family_name: Solis-1P(3.6-10)K-4G-US
code: GRID-INTF
code_key: gridintf
display_message: Grid unstable
page: 62
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=14.r3
    h: 7ed6fd7ac33c
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
  cite:
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=13.r3
    h: 7ed6fd7ac33c
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-instability
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r5
    h: dc004aa7f58f
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:ac-overcurrent
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r16
    h: f4152628ed31
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r16
    h: f91351135bbf
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r16
    h: f91351135bbf
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r5
    h: dc004aa7f58f
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:waveform-spectrum-analysis
  note: Harmonic distortion test of the AC line.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r5
    h: dc004aa7f58f
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:impedance-matching
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r5
    h: dc004aa7f58f
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=16.r16
    h: f4152628ed31
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=27.r16
    h: f91351135bbf
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=28.r16
    h: f91351135bbf
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:solis-1p-4g-us
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=14.r3
    h: 7ed6fd7ac33c
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=13.r3
    h: 7ed6fd7ac33c
  review: drafted
---
