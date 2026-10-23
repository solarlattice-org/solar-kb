---
id: fc:sma-sb-us-41-3805
type: FaultCode
name: SMA SB-US-41 3805
aliases:
- '3805'
- SMA 3805
- Residual current too high
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '3805'
code_key: '3805'
display_message: Residual current too high
page: 59
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.28
    h: d9702c65933d
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h296
    h: 01adc959b405
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r3
    h: ded27d4996a4
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r3
    h: ded27d4996a4
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h298
    h: 41ca4ce6d7cb
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r3
    h: ded27d4996a4
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r3
    h: ded27d4996a4
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Only when the message appears frequently.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r3
    h: ded27d4996a4
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r3
    h: ded27d4996a4
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h299
    h: f2d5a3b20f78
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: Brief interruption of feed-in.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r3
    h: ded27d4996a4
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r3
    h: ded27d4996a4
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h298
    h: 41ca4ce6d7cb
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Interruption is brief; resumes on its own.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r3
    h: ded27d4996a4
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r3
    h: ded27d4996a4
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h298
    h: 41ca4ce6d7cb
  review: drafted
  review_note: 'support check: partial - Brief interruption implies resumption, but not explicit.'
---
