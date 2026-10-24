---
id: fc:sma-sbse-us-50-3523
type: FaultCode
name: SMA SBSE-US-50 3523
aliases:
- '3523'
- SMA 3523
- Start of cyclic insulation test
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '3523'
code_key: '3523'
display_message: Start of cyclic insulation test
page: 106
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.29
    h: 67395b7d9289
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h562
    h: ed2a16179796
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.29
    h: 67395b7d9289
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h562
    h: ed2a16179796
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h456
    h: ed2a16179796
  review: drafted
  review_note: 'support check: partial - Message is the start of a cyclic insulation test, a status message
    that implies informational, but this is not explicitly stated.'
- claim_id: c3
  rel: has_recovery
  target: ec:auto-reset
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.29
    h: 67395b7d9289
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h563
    h: 79ca0bff5d29
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h457
    h: 79ca0bff5d29
  review: drafted
  review_note: 'support check: partial - Inverter restarts once on its own during the test, implying automatic
    resumption, but this is not explicitly stated.'
- claim_id: c4
  rel: applies_to
  target: prod:sma-sbse-us-50
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.29
    h: 67395b7d9289
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h562
    h: ed2a16179796
  review: drafted
---
