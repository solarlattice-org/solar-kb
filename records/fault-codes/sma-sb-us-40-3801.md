---
id: fc:sma-sb-us-40-3801
type: FaultCode
name: SMA SB-US-40 3801
aliases:
- '3801'
- SMA 3801
- DC overcurrent > Check generator
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-40
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP/1TP-US-40)
code: '3801'
code_key: '3801'
display_message: DC overcurrent > Check generator
page: 50
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-40-ba-en-13
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h212
    h: a17802b02abd
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h213
    h: c6f15c03c258
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r2
    h: 8a977edfc09d
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r2
    h: 8a977edfc09d
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h213
    h: c6f15c03c258
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h289
    h: 41ca4ce6d7cb
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h212
    h: a17802b02abd
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h213
    h: c6f15c03c258
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h214
    h: 3246bbb16318
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Only when the message appears frequently.
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h214
    h: 3246bbb16318
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h290
    h: f2d5a3b20f78
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: Brief interruption of feed-in.
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h213
    h: c6f15c03c258
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h289
    h: 41ca4ce6d7cb
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Interruption is brief; resumes on its own.
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h213
    h: c6f15c03c258
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h289
    h: 41ca4ce6d7cb
  review: drafted
  review_note: 'support check: partial - Brief interruption implies resumption, but self-resumption is
    not explicitly stated.'
---
