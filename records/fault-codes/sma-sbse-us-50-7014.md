---
id: fc:sma-sbse-us-50-7014
type: FaultCode
name: SMA SBSE-US-50 7014
aliases:
- '7014'
- SMA 7014
- Fault boost converter temperature sensor
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '7014'
code_key: '7014'
display_message: Fault boost converter temperature sensor
page: 114
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.53
    h: 30978f5c459e
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h679
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
---
