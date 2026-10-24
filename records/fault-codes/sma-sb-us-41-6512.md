---
id: fc:sma-sb-us-41-6512
type: FaultCode
name: SMA SB-US-41 6512
aliases:
- '6512'
- SMA 6512
- Minimum operating temperature not reached
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '6512'
code_key: '6512'
display_message: Minimum operating temperature not reached
page: 61
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.32
    h: d0caa3eea3a3
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h313
    h: c1d23dd7c2d4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-undertemperature
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r9
    h: 8843401dd059
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r9
    h: 8843401dd059
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r9
    h: 8843401dd059
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r6
    h: 907ccf700a69
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h313
    h: c1d23dd7c2d4
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h314
    h: c0ac346a9e3b
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  note: Feed-in is held off while the device is below the minimum operating temperature.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r9
    h: 8843401dd059
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r9
    h: 8843401dd059
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r9
    h: 8843401dd059
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r6
    h: 907ccf700a69
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h314
    h: c0ac346a9e3b
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Feed-in resumes on its own once the temperature reaches at least -25 C.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r9
    h: 8843401dd059
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r9
    h: 8843401dd059
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r9
    h: 8843401dd059
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r6
    h: 907ccf700a69
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h314
    h: c0ac346a9e3b
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-sb-us-41
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.32
    h: d0caa3eea3a3
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h313
    h: c1d23dd7c2d4
  review: drafted
---
