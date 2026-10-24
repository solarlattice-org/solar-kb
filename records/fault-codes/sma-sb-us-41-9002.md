---
id: fc:sma-sb-us-41-9002
type: FaultCode
name: SMA SB-US-41 9002
aliases:
- '9002'
- SMA 9002
- Installer code invalid
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '9002'
code_key: '9002'
display_message: Installer code invalid
page: 68
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.63
    h: a509970d73c1
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h422
    h: 7ba5aa81e7dc
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:invalid-access-code
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r2
    h: ac6479fb8aba
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r2
    h: ac6479fb8aba
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h249
    h: e1adee9857f4
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h423
    h: 7b9916244398
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:enter-access-code
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r2
    h: ac6479fb8aba
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r2
    h: ac6479fb8aba
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h250
    h: 49e51ba280f0
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h424
    h: 49e51ba280f0
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:informational
  note: Configuration message; parameters remain protected.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r2
    h: ac6479fb8aba
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r2
    h: ac6479fb8aba
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h249
    h: e1adee9857f4
  review: drafted
  review_note: 'support check: partial - The row shows a status message with parameters still protected,
    which suggests informational, but it never states the classification and…'
- claim_id: c5
  rel: applies_to
  target: prod:sma-sb-us-41
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.63
    h: a509970d73c1
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h422
    h: 7ba5aa81e7dc
  review: drafted
---
