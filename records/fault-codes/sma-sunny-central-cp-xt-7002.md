---
id: fc:sma-sunny-central-cp-xt-7002
type: FaultCode
name: SMA SC-CP-XT 7002
aliases:
- '7002'
- SMA 7002
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '7002'
code_key: '7002'
page: 39
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r3
    h: a7d5c7e779dc
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
---
