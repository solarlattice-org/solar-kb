---
id: fc:sma-sb-us-41-8503
type: FaultCode
name: SMA SB-US-41 8503
aliases:
- '8503'
- SMA 8503
- Self-diagnosis > Input C defective
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '8503'
code_key: '8503'
display_message: Self-diagnosis > Input C defective
page: 67
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.59
    h: 7f47f389a8ba
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h408
    h: 16ef08f54652
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h409
    h: dfc876236682
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h714
    h: dfc876236682
  review: drafted
  review_note: 'support check: partial - Passages say ''Polarity error on the inverter'', which suggests
    but doesn''t explicitly say reverse polarity.'
- claim_id: c3
  rel: affects
  target: comp:pv-input-terminal
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h243
    h: e74ae3113377
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h408
    h: 16ef08f54652
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h713
    h: 16ef08f54652
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h410
    h: 9f2382017faa
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h715
    h: 9f2382017faa
  review: drafted
  review_note: 'support check: partial - Check whether a string is connected to input C is a wiring check
    but only loosely; also reset string-failure detection.'
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h410
    h: 9f2382017faa
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h715
    h: 9f2382017faa
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h410
    h: 9f2382017faa
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h715
    h: 9f2382017faa
  review: drafted
---
