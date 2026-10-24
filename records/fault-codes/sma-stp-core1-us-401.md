---
id: fc:sma-stp-core1-us-401
type: FaultCode
name: SMA CORE1-US 401
aliases:
- '401'
- SMA 401
- Grid incident
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '401'
code_key: '401'
display_message: Grid incident
page: 47
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h241
    h: 27ce43a6ea35
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h242
    h: 00db0741c1e5
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h158
    h: 27ce43a6ea35
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h159
    h: 00db0741c1e5
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h243
    h: 27ce43a6ea35
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h244
    h: 00db0741c1e5
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:islanding-detected
  note: Stand-alone grid or very large grid frequency change detected.
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h159
    h: 00db0741c1e5
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h244
    h: 00db0741c1e5
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h225
    h: f714a156b3c4
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h469
    h: f714a156b3c4
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h403
    h: f714a156b3c4
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h159
    h: 00db0741c1e5
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h244
    h: 00db0741c1e5
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h225
    h: f714a156b3c4
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=13.r2
    h: 7a6d28b76793
  review: drafted
  review_note: 'support check: partial - Passage labeled ''Grid fault'' with feed-in stopped, but fault
    classification is implied rather than stated.'
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h159
    h: 00db0741c1e5
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h244
    h: 00db0741c1e5
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=13.r2
    h: 7a6d28b76793
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h225
    h: f714a156b3c4
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h469
    h: f714a156b3c4
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h403
    h: f714a156b3c4
  review: drafted
- claim_id: c7
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h160
    h: 58ff631dba3d
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h245
    h: 58ff631dba3d
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=13.r2
    h: 7a6d28b76793
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h226
    h: a59ad34e5713
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h470
    h: a59ad34e5713
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h404
    h: a59ad34e5713
  review: drafted
  review_note: 'support check: partial - Passages only say to check the grid connection for frequency
    fluctuations; frequency measurement as the detection method is implied, not stated.'
- claim_id: c8
  rel: mitigated_by
  target: mit:utility-consultation
  note: If a power outage or grid work is suspected.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h226
    h: a59ad34e5713
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h470
    h: a59ad34e5713
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h404
    h: a59ad34e5713
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:sma-stp-core1-us
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h241
    h: 27ce43a6ea35
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h242
    h: 00db0741c1e5
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h158
    h: 27ce43a6ea35
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h159
    h: 00db0741c1e5
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h243
    h: 27ce43a6ea35
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h244
    h: 00db0741c1e5
  review: drafted
---
