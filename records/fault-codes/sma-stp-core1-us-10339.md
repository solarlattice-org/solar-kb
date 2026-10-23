---
id: fc:sma-stp-core1-us-10339
type: FaultCode
name: SMA CORE1-US 10339
aliases:
- '10339'
- SMA 10339
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '10339'
code_key: '10339'
page: 59
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=26
    h: 9b627983164d
  review: drafted
  review_note: code printed in the table header line
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h297
    h: 637a56d0bb71
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h504
    h: 4959d6f19b9e
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h297
    h: 637a56d0bb71
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h504
    h: 4959d6f19b9e
  review: drafted
  review_note: 'support check: partial - The passages say nothing about production effect, though it is
    plausibly none for enabling Webconnect.'
---
