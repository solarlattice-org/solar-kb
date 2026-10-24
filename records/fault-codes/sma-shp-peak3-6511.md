---
id: fc:sma-shp-peak3-6511
type: FaultCode
name: SMA PEAK3-US 6511
aliases:
- '6511'
- SMA 6511
- Self-diagnosis > Overtemperature
category: Inverters
make: sma
make_name: SMA
model_family: shp-peak3
family_name: Sunny Highpower PEAK3 (SHP 125-172-US)
code: '6511'
code_key: '6511'
display_message: Self-diagnosis > Overtemperature
page: 64
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-shpxxx-us-21-be-en-11
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.14
    h: 0b341f6aee89
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h344
    h: 359fae7aa468
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.44
    h: 182a40e4635a
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h636
    h: 359fae7aa468
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h637
    h: 84181f7ce1f3
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.36
    h: ba7369fcfe16
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h546
    h: 84181f7ce1f3
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.14
    h: 0b341f6aee89
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h345
    h: 84181f7ce1f3
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:choke
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.44
    h: 182a40e4635a
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h637
    h: 84181f7ce1f3
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.36
    h: ba7369fcfe16
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h546
    h: 84181f7ce1f3
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.14
    h: 0b341f6aee89
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h345
    h: 84181f7ce1f3
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.44
    h: 182a40e4635a
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h638
    h: b29c5b38718e
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.36
    h: ba7369fcfe16
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h547
    h: b59ca5d82fe4
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.14
    h: 0b341f6aee89
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h346
    h: b59ca5d82fe4
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:adequate-cooling
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.44
    h: 182a40e4635a
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h638
    h: b29c5b38718e
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.36
    h: ba7369fcfe16
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h547
    h: b59ca5d82fe4
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.14
    h: 0b341f6aee89
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h346
    h: b59ca5d82fe4
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:direct-sun-avoidance
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.36
    h: ba7369fcfe16
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h547
    h: b59ca5d82fe4
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.14
    h: 0b341f6aee89
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h346
    h: b59ca5d82fe4
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:sma-shp-peak3
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.14
    h: 0b341f6aee89
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h344
    h: 359fae7aa468
  review: drafted
---
