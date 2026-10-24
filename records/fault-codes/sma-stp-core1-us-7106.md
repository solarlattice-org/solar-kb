---
id: fc:sma-stp-core1-us-7106
type: FaultCode
name: SMA CORE1-US 7106
aliases:
- '7106'
- SMA 7106
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '7106'
code_key: '7106'
page: 50
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r5
    h: d3bbcbdb79a2
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r5
    h: d3bbcbdb79a2
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r5
    h: d3bbcbdb79a2
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:firmware-update-failure
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r5
    h: d3bbcbdb79a2
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r5
    h: d3bbcbdb79a2
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r5
    h: d3bbcbdb79a2
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r7
    h: 8a58ca7a7ff2
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h332
    h: e86432585b19
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h333
    h: a6066276cd3a
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:memory-card-reformat
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r7
    h: 8a58ca7a7ff2
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:update-file-recopy
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r7
    h: 8a58ca7a7ff2
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:memory-card-replacement
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h332
    h: e86432585b19
  review: drafted
- claim_id: c8
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r5
    h: d3bbcbdb79a2
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r5
    h: d3bbcbdb79a2
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r5
    h: d3bbcbdb79a2
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h333
    h: a6066276cd3a
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c9
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r5
    h: d3bbcbdb79a2
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r5
    h: d3bbcbdb79a2
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r5
    h: d3bbcbdb79a2
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h333
    h: a6066276cd3a
  review: drafted
- claim_id: c10
  rel: applies_to
  target: prod:sma-stp-core1-us
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=19.r5
    h: d3bbcbdb79a2
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=8.r5
    h: d3bbcbdb79a2
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=20.r5
    h: d3bbcbdb79a2
  review: drafted
---
