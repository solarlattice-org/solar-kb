---
id: fc:sma-sb-us-41-3802
type: FaultCode
name: SMA SB-US-41 3802
aliases:
- '3802'
- SMA 3802
- Residual current too high > Check generator
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '3802'
code_key: '3802'
display_message: Residual current too high > Check generator
page: 59
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.27
    h: e45e5541211a
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h292
    h: 073e91a4217c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r3
    h: 038fc33abdb8
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h293
    h: 41ca4ce6d7cb
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r3
    h: 038fc33abdb8
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Only when the message appears frequently.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.27
    h: e45e5541211a
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h294
    h: f2d5a3b20f78
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: Brief interruption of feed-in.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.27
    h: e45e5541211a
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h293
    h: 41ca4ce6d7cb
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Interruption is brief; resumes on its own.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.27
    h: e45e5541211a
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h293
    h: 41ca4ce6d7cb
  review: drafted
  review_note: 'support check: partial - Brief interruption implies resumption, but not explicitly stated.'
---
