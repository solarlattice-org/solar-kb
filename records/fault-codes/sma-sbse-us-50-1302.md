---
id: fc:sma-sbse-us-50-1302
type: FaultCode
name: SMA SBSE-US-50 1302
aliases:
- '1302'
- SMA 1302
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '1302'
code_key: '1302'
page: 103
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.19
    h: 3f1d9dfc7644
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-loss
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h249
    h: 386bbb27f481
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h514
    h: 386bbb27f481
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:phase-loss
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h194
    h: 3f7cf298cc7a
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h443
    h: e314a6e53a42
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h310
    h: 1e5c00decc77
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h195
    h: 31f1a10ae8da
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h250
    h: f9a04e763a75
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h515
    h: f9a04e763a75
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h311
    h: 12ba84b8cd7e
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h444
    h: f910b6ee313a
  review: drafted
  review_note: 'support check: partial - The passages say the grid monitor detects the unconnected conductors
    and list AC voltage measurements as corrective steps; they don''t…'
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h195
    h: 31f1a10ae8da
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=14.r4
    h: 683394f59a4a
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h250
    h: f9a04e763a75
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h515
    h: f9a04e763a75
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h444
    h: f910b6ee313a
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h311
    h: 12ba84b8cd7e
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c7
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h444
    h: f910b6ee313a
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:ground-conductor-check
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h444
    h: f910b6ee313a
  review: drafted
- claim_id: c9
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=14.r4
    h: 683394f59a4a
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h443
    h: e314a6e53a42
  review: drafted
- claim_id: c10
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=14.r4
    h: 683394f59a4a
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h443
    h: e314a6e53a42
  review: drafted
- claim_id: c11
  rel: applies_to
  target: prod:sma-sbse-us-50
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.19
    h: 3f1d9dfc7644
  review: drafted
---
