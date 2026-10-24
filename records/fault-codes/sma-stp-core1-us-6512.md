---
id: fc:sma-stp-core1-us-6512
type: FaultCode
name: SMA CORE1-US 6512
aliases:
- '6512'
- SMA 6512
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '6512'
code_key: '6512'
page: 49
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r9
    h: 8843401dd059
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r9
    h: 8843401dd059
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r9
    h: 8843401dd059
  review: drafted
- claim_id: c4
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
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c5
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
- claim_id: c6
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
- claim_id: c7
  rel: applies_to
  target: prod:sma-stp-core1-us
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
  review: drafted
---
