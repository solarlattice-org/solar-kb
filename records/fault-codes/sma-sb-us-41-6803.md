---
id: fc:sma-sb-us-41-6803
type: FaultCode
name: SMA SB-US-41 6803
aliases:
- '6803'
- SMA 6803
- Self-diagnosis > Input A defective
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '6803'
code_key: '6803'
display_message: Self-diagnosis > Input A defective
page: 62
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.35
    h: 8d1881043c6f
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h324
    h: fadd96b1d787
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h325
    h: dfc876236682
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h324
    h: fadd96b1d787
  review: drafted
  review_note: 'support check: partial - The passages say ''Polarity error'' with ''Input A defective'',
    which loosely supports reverse polarity but doesn''t state it explicitly.'
- claim_id: c3
  rel: affects
  target: comp:pv-input-terminal
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h324
    h: fadd96b1d787
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h326
    h: 40f59ef8bd28
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=17.r4
    h: c2b2e23365c6
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:dc-wiring-check
  note: Verify string connection on the input; reset string-failure detection if a string was removed.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h326
    h: 40f59ef8bd28
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=17.r4
    h: c2b2e23365c6
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Escalation if the message recurs frequently.
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h326
    h: 40f59ef8bd28
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=17.r4
    h: c2b2e23365c6
  review: drafted
---
