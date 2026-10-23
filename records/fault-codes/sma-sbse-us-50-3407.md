---
id: fc:sma-sbse-us-50-3407
type: FaultCode
name: SMA SBSE-US-50 3407
aliases:
- '3407'
- SMA 3407
- DC overvoltage > Disconnect generator
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '3407'
code_key: '3407'
display_message: DC overvoltage > Disconnect generator
page: 105
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.25
    h: dabd4b7dd6f6
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h543
    h: 41676f7fb1bd
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h258
    h: 33883a354598
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h260
    h: 587cea85589b
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h272
    h: 41676f7fb1bd
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h273
    h: f9c84c143221
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h543
    h: 41676f7fb1bd
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h544
    h: f9c84c143221
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h258
    h: 33883a354598
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h261
    h: 5bf6ccea6e5e
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h274
    h: 33b43893fe4d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h545
    h: 33b43893fe4d
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h258
    h: 33883a354598
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h261
    h: 5bf6ccea6e5e
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h274
    h: 33b43893fe4d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h545
    h: 33b43893fe4d
  review: drafted
  review_note: 'support check: partial - The passages check the DC voltage but do not say detection is
    by DC voltage measurement.'
- claim_id: c5
  rel: mitigated_by
  target: mit:string-voltage-margin-design
  note: When DC voltage exceeds the inverter maximum input voltage
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h258
    h: 33883a354598
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h261
    h: 5bf6ccea6e5e
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h274
    h: 33b43893fe4d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h545
    h: 33b43893fe4d
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Escalation if the message recurs frequently
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h258
    h: 33883a354598
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h261
    h: 5bf6ccea6e5e
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h274
    h: 33b43893fe4d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h545
    h: 33b43893fe4d
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h258
    h: 33883a354598
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h260
    h: 587cea85589b
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h261
    h: 5bf6ccea6e5e
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h273
    h: f9c84c143221
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h274
    h: 33b43893fe4d
  review: drafted
  review_note: 'support check: partial - A fault is implied by the destruction risk and the disconnection
    instruction, but it is not stated.'
- claim_id: c8
  rel: has_recovery
  target: ec:manual-reset
  note: Operator disconnects, verifies DC voltage and reconnects; service if frequent
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h258
    h: 33883a354598
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h261
    h: 5bf6ccea6e5e
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h274
    h: 33b43893fe4d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h545
    h: 33b43893fe4d
  review: drafted
---
