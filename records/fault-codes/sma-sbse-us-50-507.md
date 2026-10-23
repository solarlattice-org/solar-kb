---
id: fc:sma-sbse-us-50-507
type: FaultCode
name: SMA SBSE-US-50 507
aliases:
- '507'
- SMA 507
- Active power limit AC frequency
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '507'
code_key: '507'
display_message: Active power limit AC frequency
page: 101
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.13
    h: 4f4907d0a7ee
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h483
    h: 60972b33971a
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overfrequency
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.13
    h: 4f4907d0a7ee
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h483
    h: 60972b33971a
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h484
    h: 8d640405f7e5
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.10
    h: b3049d4e7001
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h418
    h: 8d640405f7e5
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.4
    h: 3b3d813202d3
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h294
    h: 60972b33971a
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h295
    h: 8d640405f7e5
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:derate
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.13
    h: 4f4907d0a7ee
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h484
    h: 8d640405f7e5
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.10
    h: b3049d4e7001
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h418
    h: 8d640405f7e5
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.4
    h: 3b3d813202d3
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h295
    h: 8d640405f7e5
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h485
    h: 3f810abc1c00
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h296
    h: 3f810abc1c00
  review: drafted
  review_note: 'support check: partial - Passages advise checking the grid frequency, but don''t state
    detection by frequency measurement.'
- claim_id: c5
  rel: mitigated_by
  target: mit:utility-consultation
  note: Only when fluctuations and the message occur frequently.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h485
    h: 3f810abc1c00
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h296
    h: 3f810abc1c00
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Only after grid operator approval, coordinated with manufacturer service.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h485
    h: 3f810abc1c00
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h296
    h: 3f810abc1c00
  review: drafted
---
