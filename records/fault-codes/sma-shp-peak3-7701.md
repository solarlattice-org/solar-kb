---
id: fc:sma-shp-peak3-7701
type: FaultCode
name: SMA PEAK3-US 7701
aliases:
- '7701'
- SMA 7701
- Self-diagnosis > Interference device
category: Inverters
make: sma
make_name: SMA
model_family: shp-peak3
family_name: Sunny Highpower PEAK3 (SHP 125-172-US)
code: '7701'
code_key: '7701'
display_message: Self-diagnosis > Interference device
page: 67
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-shpxxx-us-21-be-en-11
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.27
    h: b5a9216bac9c
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h405
    h: 75f49e9e17fb
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.27
    h: b5a9216bac9c
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h405
    h: 75f49e9e17fb
  review: drafted
- claim_id: c3
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.27
    h: b5a9216bac9c
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h406
    h: cca77e1e7cd3
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h407
    h: 417f2f122215
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.27
    h: b5a9216bac9c
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h407
    h: 417f2f122215
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-shp-peak3
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.27
    h: b5a9216bac9c
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h405
    h: 75f49e9e17fb
  review: drafted
---
