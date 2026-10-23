---
id: fc:sma-stp-core1-us-10284
type: FaultCode
name: SMA CORE1-US 10284
aliases:
- '10284'
- SMA 10284
- No Wi-Fi connection possible
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '10284'
code_key: '10284'
display_message: No Wi-Fi connection possible
page: 59
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h308
    h: 4688e4f0fa57
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h310
    h: 0390cded536c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:communication-loss
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h310
    h: 0390cded536c
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h493
    h: 5dea0f4f58c0
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:network-connection-check
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h311
    h: 022c55eb4f81
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h494
    h: 022c55eb4f81
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h310
    h: 0390cded536c
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h493
    h: 5dea0f4f58c0
  review: drafted
  review_note: 'support check: partial - The condition is a lost Wi-Fi connection, but a warning classification
    is only implied, not stated.'
---
