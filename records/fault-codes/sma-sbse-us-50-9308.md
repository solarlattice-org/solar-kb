---
id: fc:sma-sbse-us-50-9308
type: FaultCode
name: SMA SBSE-US-50 9308
aliases:
- '9308'
- SMA 9308
- Battery system communication error
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '9308'
code_key: '9308'
display_message: Battery system communication error
page: 120
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.75
    h: 7564469d0705
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h786
    h: 5c402507d020
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:communication-loss
  note: Communication error between inverter and battery system.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h786
    h: 5c402507d020
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h787
    h: 72df990bf2f5
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:communication-cable-check
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h788
    h: 72f0b07cd570
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:ground-conductor-check
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h788
    h: 72f0b07cd570
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:battery-connection-check
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h788
    h: 72f0b07cd570
  review: drafted
  review_note: 'support check: partial - Battery switched on and cable checks are present, but a ''battery
    connection check'' is only loosely implied via communication cable…'
---
