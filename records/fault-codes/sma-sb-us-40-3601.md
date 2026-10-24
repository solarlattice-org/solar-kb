---
id: fc:sma-sb-us-40-3601
type: FaultCode
name: SMA SB-US-40 3601
aliases:
- '3601'
- SMA 3601
- High discharge curr. > Check generator
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-40
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP/1TP-US-40)
code: '3601'
code_key: '3601'
display_message: High discharge curr. > Check generator
page: 50
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-40-ba-en-13
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h206
    h: 0d56d0395662
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h207
    h: 25822f0edd59
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:high-leakage-current
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h207
    h: 25822f0edd59
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15.r4
    h: 6c9d17bd013d
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h281
    h: 0b5c74e1ef37
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h567
    h: ed7be7f637ea
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h461
    h: 0b5c74e1ef37
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h325
    h: 0b5c74e1ef37
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ground-fault
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h207
    h: 25822f0edd59
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15.r4
    h: 6c9d17bd013d
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h281
    h: 0b5c74e1ef37
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h207
    h: 25822f0edd59
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15.r4
    h: 6c9d17bd013d
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h568
    h: 0818fdbe4234
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:ground-conductor-check
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r11
    h: 5b2731fd0ecd
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h207
    h: 25822f0edd59
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15.r4
    h: 6c9d17bd013d
  review: drafted
- claim_id: c8
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h207
    h: 25822f0edd59
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15.r4
    h: 6c9d17bd013d
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h281
    h: 0b5c74e1ef37
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h461
    h: 0b5c74e1ef37
  review: drafted
- claim_id: c9
  rel: has_recovery
  target: ec:auto-reset-limited
  note: Reconnects automatically; after five occurrences in a day feed-in is terminated.
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=15.r4
    h: 6c9d17bd013d
  review: drafted
- claim_id: c10
  rel: applies_to
  target: prod:sma-sb-us-40
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h206
    h: 0d56d0395662
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h207
    h: 25822f0edd59
  review: drafted
---
