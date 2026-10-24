---
id: fc:sma-stp-core1-us-10285
type: FaultCode
name: SMA CORE1-US 10285
aliases:
- '10285'
- SMA 10285
- Wi-Fi connection established
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '10285'
code_key: '10285'
display_message: Wi-Fi connection established
page: 58
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h320
    h: 1ac9890a9d94
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h321
    h: d3a655b7df20
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h237
    h: 1ac9890a9d94
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h238
    h: d3a655b7df20
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h312
    h: 1ac9890a9d94
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h313
    h: d3a655b7df20
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h321
    h: d3a655b7df20
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h238
    h: d3a655b7df20
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h313
    h: d3a655b7df20
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h497
    h: a5ec30164225
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:no-production-effect
  note: Status message confirming Wi-Fi link establishment.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h321
    h: d3a655b7df20
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h238
    h: d3a655b7df20
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h313
    h: d3a655b7df20
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h497
    h: a5ec30164225
  review: drafted
  review_note: 'support check: partial - The passages say only that the connection was established, and
    say nothing about production effect, though it is plausibly none.'
- claim_id: c6
  rel: applies_to
  target: prod:sma-stp-core1-us
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h320
    h: 1ac9890a9d94
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h321
    h: d3a655b7df20
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h237
    h: 1ac9890a9d94
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h238
    h: d3a655b7df20
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h312
    h: 1ac9890a9d94
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h313
    h: d3a655b7df20
  review: drafted
---
