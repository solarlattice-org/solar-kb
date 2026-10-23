---
id: fc:sma-stp-core1-us-3410
type: FaultCode
name: SMA CORE1-US 3410
aliases:
- '3410'
- SMA 3410
- DC overvoltage > Disconnect PV array
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '3410'
code_key: '3410'
display_message: DC overvoltage > Disconnect PV array
page: 49
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h258
    h: 33883a354598
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h260
    h: 587cea85589b
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
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h548
    h: 41676f7fb1bd
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h549
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
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h550
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
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h550
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
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h550
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
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h550
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
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h549
    h: f9c84c143221
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h550
    h: 33b43893fe4d
  review: drafted
  review_note: 'support check: partial - Overvoltage that can destroy the inverter with disconnect instruction
    implies a fault, but the passages never explicitly classify it as fault.'
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
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h550
    h: 33b43893fe4d
  review: drafted
  review_note: 'support check: partial - Operator disconnects, checks DC voltage and reconnects, which
    suggests manual intervention, but no explicit reset or clearing is stated.'
---
