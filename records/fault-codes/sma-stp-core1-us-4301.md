---
id: fc:sma-stp-core1-us-4301
type: FaultCode
name: SMA CORE1-US 4301
aliases:
- '4301'
- SMA 4301
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '4301'
code_key: '4301'
page: 49
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r4
    h: 941ab92a0300
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r4
    h: 941ab92a0300
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r4
    h: 93c2d6ff802b
  review: drafted
- claim_id: c4
  rel: defined_in
  target: src:sma-kb-stp-us-41-events-4301-4302
  cite:
  - src: src:sma-kb-stp-us-41-events-4301-4302
    loc: sec=h1
    h: f9c7fab7dc47
  review: drafted
- claim_id: c5
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
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c6
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
- claim_id: c7
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
- claim_id: c8
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
- claim_id: c9
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
- claim_id: c10
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
- claim_id: c11
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
- claim_id: c12
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
- claim_id: c13
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
- claim_id: c14
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
- claim_id: c15
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
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c16
  rel: applies_to
  target: prod:sma-stp-core1-us
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r4
    h: 941ab92a0300
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r4
    h: 941ab92a0300
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r4
    h: 93c2d6ff802b
  - src: src:sma-kb-stp-us-41-events-4301-4302
    loc: sec=h1
    h: f9c7fab7dc47
  review: drafted
---
