---
id: fc:sma-stp-core1-us-3802
type: FaultCode
name: SMA CORE1-US 3802
aliases:
- '3802'
- SMA 3802
- DC overcurrent > Check PV array
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '3802'
code_key: '3802'
display_message: DC overcurrent > Check PV array
page: 49
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r2
    h: 8a977edfc09d
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r2
    h: 8a977edfc09d
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r3
    h: 038fc33abdb8
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r3
    h: 038fc33abdb8
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h293
    h: 41ca4ce6d7cb
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r3
    h: 038fc33abdb8
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Only when the message appears frequently.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.27
    h: e45e5541211a
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h294
    h: f2d5a3b20f78
  review: drafted
- claim_id: c7
  rel: has_production_effect
  target: ec:trip
  note: Brief interruption of feed-in.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.27
    h: e45e5541211a
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h293
    h: 41ca4ce6d7cb
  review: drafted
- claim_id: c8
  rel: has_recovery
  target: ec:auto-reset
  note: Interruption is brief; resumes on its own.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.27
    h: e45e5541211a
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h293
    h: 41ca4ce6d7cb
  review: drafted
  review_note: 'support check: partial - Brief interruption implies resumption, but not explicitly stated.'
---
