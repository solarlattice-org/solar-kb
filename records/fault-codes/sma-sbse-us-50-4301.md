---
id: fc:sma-sbse-us-50-4301
type: FaultCode
name: SMA SBSE-US-50 4301
aliases:
- '4301'
- SMA 4301
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '4301'
code_key: '4301'
page: 110
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.39
    h: d70ef45db0dc
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:arc-fault
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r4
    h: 941ab92a0300
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r4
    h: 941ab92a0300
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=17.r1
    h: 4dec9b04736e
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h310
    h: 79dcacd8e4a8
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:dc-connector
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.23
    h: 821bd2d816f4
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h481
    h: 0e3f2e989d3e
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.31
    h: ae41cbb4f9d8
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h311
    h: d2a22308378b
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=17.r1
    h: 4dec9b04736e
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h311
    h: d2a22308378b
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.23
    h: 821bd2d816f4
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h482
    h: 74ff13d5a06f
  review: drafted
  review_note: 'support check: partial - Visual inspection of the DC installation is a corrective measure,
    not stated as a detection method for the event.'
- claim_id: c7
  rel: detected_by
  target: method:ir-thermography
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.23
    h: 821bd2d816f4
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h482
    h: 74ff13d5a06f
  review: drafted
  review_note: 'support check: partial - IR camera is only a tip to support inspection during corrective
    measures, not stated as a detection method.'
- claim_id: c8
  rel: mitigated_by
  target: mit:connector-compatibility-check
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.23
    h: 821bd2d816f4
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h482
    h: 74ff13d5a06f
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.31
    h: ae41cbb4f9d8
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h311
    h: d2a22308378b
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h613
    h: d2a22308378b
  review: drafted
- claim_id: c10
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=17.r1
    h: 4dec9b04736e
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r3
    h: 7f1f795c5adb
  review: drafted
- claim_id: c11
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=17.r1
    h: 4dec9b04736e
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r3
    h: 7f1f795c5adb
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h612
    h: e77d95345f8b
  review: drafted
- claim_id: c12
  rel: has_recovery
  target: ec:manual-reset
  note: Manual reset needed when operation inhibition is activated.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r4
    h: 941ab92a0300
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r4
    h: 941ab92a0300
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=16.r3
    h: 7f1f795c5adb
  review: drafted
---
