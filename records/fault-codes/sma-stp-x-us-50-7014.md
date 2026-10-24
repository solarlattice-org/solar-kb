---
id: fc:sma-stp-x-us-50-7014
type: FaultCode
name: SMA STP-X-US 7014
aliases:
- '7014'
- SMA 7014
- Fault boost converter temperature sensor
category: Inverters
make: sma
make_name: SMA
model_family: stp-x-us-50
family_name: Sunny Tripower X 13-30-US (STP xx-US-50)
code: '7014'
code_key: '7014'
display_message: Fault boost converter temperature sensor
page: 93
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stpxx-us-50-be-en-14
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.40
    h: 8e41a078934f
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h563
    h: 2e521c591546
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:temperature-sensor-fault
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.53
    h: 30978f5c459e
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h679
    h: 2e521c591546
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:temperature-sensor
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.53
    h: 30978f5c459e
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h679
    h: 2e521c591546
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:boost-converter
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.53
    h: 30978f5c459e
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h679
    h: 2e521c591546
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.53
    h: 30978f5c459e
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h681
    h: 417f2f122215
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.53
    h: 30978f5c459e
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h681
    h: 417f2f122215
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:sma-stp-x-us-50
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.40
    h: 8e41a078934f
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h563
    h: 2e521c591546
  review: drafted
---
