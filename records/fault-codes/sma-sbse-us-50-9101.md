---
id: fc:sma-sbse-us-50-9101
type: FaultCode
name: SMA SBSE-US-50 9101
aliases:
- '9101'
- SMA 9101
- AC voltage calibration failed.
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '9101'
code_key: '9101'
display_message: AC voltage calibration failed.
page: 118
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.70
    h: 5409b2699f5f
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h761
    h: 1a37094c7d50
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:calibration-failure
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h761
    h: 1a37094c7d50
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h762
    h: 5f495eb5f303
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h763
    h: 417f2f122215
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h762
    h: 5f495eb5f303
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h763
    h: 417f2f122215
  review: drafted
---
