---
id: fc:sma-stp-core1-us-10255
type: FaultCode
name: SMA CORE1-US 10255
aliases:
- '10255'
- SMA 10255
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '10255'
code_key: '10255'
page: 58
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r3
    h: b859db5b0b53
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r3
    h: b859db5b0b53
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h282
    h: 4e7842a5ada3
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h482
    h: d3e044ae0206
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r3
    h: b859db5b0b53
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h282
    h: 4e7842a5ada3
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h482
    h: d3e044ae0206
  review: drafted
  review_note: 'support check: partial - The passages say nothing about production effect, though it is
    plausibly none for a network status message.'
---
