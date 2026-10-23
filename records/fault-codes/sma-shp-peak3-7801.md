---
id: fc:sma-shp-peak3-7801
type: FaultCode
name: SMA PEAK3-US 7801
aliases:
- '7801'
- SMA 7801
- Fault overvoltage protector
category: Inverters
make: sma
make_name: SMA
model_family: shp-peak3
family_name: Sunny Highpower PEAK3 (SHP 125-172-US)
code: '7801'
code_key: '7801'
display_message: Fault overvoltage protector
page: 67
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-shpxxx-us-21-be-en-11
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.28
    h: 91a758e0f041
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h410
    h: b4b644f21aa3
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:spd-alarm
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h283
    h: 3b4b16a8ddf5
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h584
    h: 1718152fab8b
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h411
    h: 7fa9a44c84e0
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:surge-protector-exhausted
  note: Holds when arresters have tripped rather than being only incorrectly inserted.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h283
    h: 3b4b16a8ddf5
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r2
    h: 8244493e7bdc
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:surge-protection-device
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h283
    h: 3b4b16a8ddf5
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r2
    h: 8244493e7bdc
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h584
    h: 1718152fab8b
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:spd-reseating
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h284
    h: 7803693381dd
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h585
    h: 963697bd3c79
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h412
    h: 7803693381dd
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:spd-replacement
  note: Replace only arresters that have tripped.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h284
    h: 7803693381dd
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h585
    h: 963697bd3c79
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h412
    h: 7803693381dd
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r2
    h: 8244493e7bdc
  review: drafted
---
