---
id: fc:sma-stp-tl-us-1501
type: FaultCode
name: SMA STP-TL-US 1501
aliases:
- '1501'
- SMA 1501
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: '1501'
code_key: '1501'
page: 47
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=14.r5
    h: f1c5403213dc
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:configuration-error
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h197
    h: af6c0cd46cf4
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=14.r5
    h: f1c5403213dc
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h253
    h: 5efba38e0da1
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h519
    h: 5efba38e0da1
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h448
    h: 5efba38e0da1
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h315
    h: 5efba38e0da1
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:inverter-settings-review
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h198
    h: 68a1d91ef915
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=14.r5
    h: f1c5403213dc
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h254
    h: 68a1d91ef915
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h198
    h: 68a1d91ef915
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=14.r5
    h: f1c5403213dc
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h254
    h: 68a1d91ef915
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h520
    h: 68a1d91ef915
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h449
    h: 68a1d91ef915
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h316
    h: 68a1d91ef915
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h197
    h: af6c0cd46cf4
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h253
    h: 5efba38e0da1
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h197
    h: af6c0cd46cf4
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=14.r5
    h: f1c5403213dc
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h253
    h: 5efba38e0da1
  review: drafted
---
