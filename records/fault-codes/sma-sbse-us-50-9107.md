---
id: fc:sma-sbse-us-50-9107
type: FaultCode
name: SMA SBSE-US-50 9107
aliases:
- '9107'
- SMA 9107
- Self-diagnosis > Interference device
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '9107'
code_key: '9107'
display_message: Self-diagnosis > Interference device
page: 119
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.72
    h: 825e2018419a
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h771
    h: 75f49e9e17fb
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h771
    h: 75f49e9e17fb
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h455
    h: 75f49e9e17fb
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h773
    h: 417f2f122215
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h457
    h: 417f2f122215
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h772
    h: cca77e1e7cd3
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h773
    h: 417f2f122215
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h456
    h: cca77e1e7cd3
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h457
    h: 417f2f122215
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-sbse-us-50
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.72
    h: 825e2018419a
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h771
    h: 75f49e9e17fb
  review: drafted
---
