---
id: fc:solis-s5-gc-us-gridintf
type: FaultCode
name: Solis S5-GC GRID-INTF
aliases:
- GRID-INTF
- gridintf
- Solis GRID-INTF
- Grid unstable
category: Inverters
make: solis
make_name: Solis
model_family: s5-gc-us
family_name: Solis S5-GC(75-125)K-US
code: GRID-INTF
code_key: gridintf
display_message: Grid unstable
page: 70
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r5
    h: dc004aa7f58f
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-instability
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r5
    h: dc004aa7f58f
  review: drafted
- claim_id: c3
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
- claim_id: c4
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r5
    h: dc004aa7f58f
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c5
  rel: detected_by
  target: method:waveform-spectrum-analysis
  note: Harmonic distortion test of the AC line.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r5
    h: dc004aa7f58f
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: mitigated_by
  target: mit:impedance-matching
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r5
    h: dc004aa7f58f
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
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
- claim_id: c8
  rel: applies_to
  target: prod:solis-s5-gc-us
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r5
    h: dc004aa7f58f
  review: drafted
---
