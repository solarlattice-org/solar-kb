---
id: fc:sma-stp-tl-us-601
type: FaultCode
name: SMA STP-TL-US 601
aliases:
- '601'
- SMA 601
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: '601'
code_key: '601'
page: 47
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=14.r1
    h: c395530b0b12
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-injection-high
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h165
    h: 2ab8e611c91f
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h185
    h: 493f3196f5e0
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=14.r1
    h: c395530b0b12
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h237
    h: bdf5d0cb813c
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h489
    h: bdf5d0cb813c
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h423
    h: bdf5d0cb813c
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h300
    h: bdf5d0cb813c
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:dc-injection-measurement
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h249
    h: f7988acc8abf
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h166
    h: f7988acc8abf
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h251
    h: f7988acc8abf
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h186
    h: f7988acc8abf
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=14.r1
    h: c395530b0b12
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h490
    h: f7988acc8abf
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h424
    h: f7988acc8abf
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h301
    h: f7988acc8abf
  review: drafted
  review_note: 'support check: partial - Inverter detects DC in grid current, but no explicit measurement
    method is stated; monitoring threshold implies it.'
- claim_id: c4
  rel: mitigated_by
  target: mit:utility-consultation
  note: When the message appears frequently.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h249
    h: f7988acc8abf
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h166
    h: f7988acc8abf
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h251
    h: f7988acc8abf
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h186
    h: f7988acc8abf
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=14.r1
    h: c395530b0b12
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h490
    h: f7988acc8abf
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h424
    h: f7988acc8abf
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h301
    h: f7988acc8abf
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Raising the monitoring threshold, if the grid operator agrees.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h249
    h: f7988acc8abf
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h166
    h: f7988acc8abf
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h251
    h: f7988acc8abf
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h186
    h: f7988acc8abf
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h490
    h: f7988acc8abf
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h424
    h: f7988acc8abf
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h301
    h: f7988acc8abf
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sma-stp-tl-us
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=14.r1
    h: c395530b0b12
  review: drafted
---
