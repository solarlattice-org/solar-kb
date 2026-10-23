---
id: fc:sma-shp-peak3-10252
type: FaultCode
name: SMA PEAK3-US 10252
aliases:
- '10252'
- SMA 10252
- '[|tn4|: communication disrupted'
category: Inverters
make: sma
make_name: SMA
model_family: shp-peak3
family_name: Sunny Highpower PEAK3 (SHP 125-172-US)
code: '10252'
code_key: '10252'
display_message: '[|tn4|: communication disrupted'
page: 71
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-shpxxx-us-21-be-en-11
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.42
    h: e5a4c926c4ab
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h480
    h: 0d22961c20a3
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:communication-loss
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h304
    h: c527469c7586
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h480
    h: 0d22961c20a3
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h481
    h: 5a9966a8d705
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:network-cable
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h305
    h: 3e364e48e1a4
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h482
    h: 3e364e48e1a4
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:network-connection-check
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h305
    h: 3e364e48e1a4
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h482
    h: 3e364e48e1a4
  review: drafted
---
