---
id: fc:sma-sb-us-41-6903
type: FaultCode
name: SMA SB-US-41 6903
aliases:
- '6903'
- SMA 6903
- Self-diagnosis > Input B defective
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '6903'
code_key: '6903'
display_message: Self-diagnosis > Input B defective
page: 62
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.36
    h: f6629d47b6db
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h328
    h: f7315b8a64ea
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h329
    h: dfc876236682
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h328
    h: f7315b8a64ea
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - The passages say ''Polarity error'' with ''Input B defective'',
    which loosely supports reverse polarity but doesn''t state it explicitly.'
- claim_id: c3
  rel: affects
  target: comp:pv-input-terminal
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h328
    h: f7315b8a64ea
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h330
    h: 58ee038e7156
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=17.r5
    h: 3f1b8aab63a7
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:dc-wiring-check
  note: Verify string connection on the input; reset string-failure detection if a string was removed.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h330
    h: 58ee038e7156
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=17.r5
    h: 3f1b8aab63a7
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h330
    h: 58ee038e7156
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=17.r5
    h: 3f1b8aab63a7
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sma-sb-us-41
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.36
    h: f6629d47b6db
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h328
    h: f7315b8a64ea
  review: drafted
---
