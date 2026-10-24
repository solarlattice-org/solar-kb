---
id: fc:sma-stp-core1-us-10283
type: FaultCode
name: SMA CORE1-US 10283
aliases:
- '10283'
- SMA 10283
- Wi-Fi module faulty
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '10283'
code_key: '10283'
display_message: Wi-Fi module faulty
page: 57
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h313
    h: e17725fe4d5b
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h314
    h: d241890c1ecd
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h230
    h: e17725fe4d5b
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h231
    h: d241890c1ecd
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r5
    h: 68438bf07570
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:wifi-module-failure
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h314
    h: d241890c1ecd
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h231
    h: d241890c1ecd
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r5
    h: 68438bf07570
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h286
    h: 28c64004ee11
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h488
    h: 4bffee8554ae
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:wifi-module
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h314
    h: d241890c1ecd
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h231
    h: d241890c1ecd
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r5
    h: 68438bf07570
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h286
    h: 28c64004ee11
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h315
    h: c87e8fc90a2c
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h232
    h: c87e8fc90a2c
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r5
    h: 68438bf07570
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h287
    h: e01a67e73baf
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h315
    h: c87e8fc90a2c
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h232
    h: c87e8fc90a2c
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r5
    h: 68438bf07570
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h287
    h: e01a67e73baf
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:sma-stp-core1-us
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h313
    h: e17725fe4d5b
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h314
    h: d241890c1ecd
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h230
    h: e17725fe4d5b
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h231
    h: d241890c1ecd
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=25.r5
    h: 68438bf07570
  review: drafted
---
