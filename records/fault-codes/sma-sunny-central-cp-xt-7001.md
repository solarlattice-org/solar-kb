---
id: fc:sma-sunny-central-cp-xt-7001
type: FaultCode
name: SMA SC-CP-XT 7001
aliases:
- '7001'
- SMA 7001
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '7001'
code_key: '7001'
page: 39
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r2
    h: b7d1a0eff81a
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:temperature-sensor-fault
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r2
    h: b7d1a0eff81a
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h670
    h: b75389760f61
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h559
    h: 908d66c12c90
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h358
    h: b75389760f61
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:temperature-sensor
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r2
    h: b7d1a0eff81a
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h670
    h: b75389760f61
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h559
    h: 908d66c12c90
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h358
    h: b75389760f61
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h670
    h: b75389760f61
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h559
    h: 908d66c12c90
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h358
    h: b75389760f61
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: String inverter manuals state feed-in interruption; central inverter table lists differing behavior.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h670
    h: b75389760f61
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h559
    h: 908d66c12c90
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h358
    h: b75389760f61
  review: drafted
  review_note: 'support check: partial - String inverter passages state feed-in interruption, but the
    note about the central inverter table differing is not in these passages.'
- claim_id: c6
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h671
    h: 417f2f122215
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h560
    h: ff23a0a8f6f6
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h359
    h: 417f2f122215
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:wiring-terminal-check
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r2
    h: b7d1a0eff81a
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r2
    h: b7d1a0eff81a
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h671
    h: 417f2f122215
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h359
    h: 417f2f122215
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r2
    h: b7d1a0eff81a
  review: drafted
---
