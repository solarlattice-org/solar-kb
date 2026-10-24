---
id: fc:sma-sbse-us-50-7002
type: FaultCode
name: SMA SBSE-US-50 7002
aliases:
- '7002'
- SMA 7002
- Fault sensor interior temperature
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '7002'
code_key: '7002'
display_message: Fault sensor interior temperature
page: 113
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.52
    h: 331044aa14e1
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h674
    h: 43c32662cf90
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:temperature-sensor-fault
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r3
    h: a7d5c7e779dc
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h675
    h: b75389760f61
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:temperature-sensor
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r3
    h: a7d5c7e779dc
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h675
    h: b75389760f61
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h675
    h: b75389760f61
  review: drafted
  review_note: 'support check: partial - The inverter interrupts feed-in and needs Service, implying a
    fault, but the table row shows behavior W (warning); classification not explicit.'
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h675
    h: b75389760f61
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h675
    h: b75389760f61
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h676
    h: 417f2f122215
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:wiring-terminal-check
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r3
    h: a7d5c7e779dc
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r3
    h: a7d5c7e779dc
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h676
    h: 417f2f122215
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:sma-sbse-us-50
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.52
    h: 331044aa14e1
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h674
    h: 43c32662cf90
  review: drafted
---
