---
id: fc:sma-sbse-us-50-7001
type: FaultCode
name: SMA SBSE-US-50 7001
aliases:
- '7001'
- SMA 7001
- Fault sensor interior temperature
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '7001'
code_key: '7001'
display_message: Fault sensor interior temperature
page: 113
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.51
    h: df30af0ec68b
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h669
    h: 43c32662cf90
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
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
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
---
