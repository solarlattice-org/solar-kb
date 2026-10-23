---
id: fc:sma-sb-us-41-7106
type: FaultCode
name: SMA SB-US-41 7106
aliases:
- '7106'
- SMA 7106
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '7106'
code_key: '7106'
page: 62
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.37
    h: 8bc7d30d451c
  review: drafted
- claim_id: c2
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
- claim_id: c3
  rel: mitigated_by
  target: mit:memory-card-reformat
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r7
    h: 8a58ca7a7ff2
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:update-file-recopy
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=17.r7
    h: 8a58ca7a7ff2
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:memory-card-replacement
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h332
    h: e86432585b19
  review: drafted
- claim_id: c6
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
  review: drafted
  review_note: 'support check: partial - The update failed while the inverter continues feeding, which
    implies a warning, but the class is not stated.'
- claim_id: c7
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
---
