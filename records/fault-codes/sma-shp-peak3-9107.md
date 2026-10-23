---
id: fc:sma-shp-peak3-9107
type: FaultCode
name: SMA PEAK3-US 9107
aliases:
- '9107'
- SMA 9107
- Self-diagnosis > Interference device
category: Inverters
make: sma
make_name: SMA
model_family: shp-peak3
family_name: Sunny Highpower PEAK3 (SHP 125-172-US)
code: '9107'
code_key: '9107'
display_message: Self-diagnosis > Interference device
page: 70
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-shpxxx-us-21-be-en-11
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.37
    h: 31f0e7ab671c
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h455
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
---
