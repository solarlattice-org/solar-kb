---
id: fc:sma-shp-peak3-7349
type: FaultCode
name: SMA PEAK3-US 7349
aliases:
- '7349'
- SMA 7349
- Incorrect login rights for configuration file
category: Inverters
make: sma
make_name: SMA
model_family: shp-peak3
family_name: Sunny Highpower PEAK3 (SHP 125-172-US)
code: '7349'
code_key: '7349'
display_message: Incorrect login rights for configuration file
page: 67
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-shpxxx-us-21-be-en-11
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.25
    h: 29ad142f219a
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h395
    h: 60add4fd3838
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:insufficient-user-rights
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.25
    h: 29ad142f219a
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h395
    h: 60add4fd3838
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h396
    h: 7a3143d1e151
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:login-with-required-rights
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.25
    h: 29ad142f219a
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h397
    h: fcb0ee3d27a7
  review: drafted
---
