---
id: fc:sma-shp-peak3-10249
type: FaultCode
name: SMA PEAK3-US 10249
aliases:
- '10249'
- SMA 10249
- '|tn4|: network busy'
category: Inverters
make: sma
make_name: SMA
model_family: shp-peak3
family_name: Sunny Highpower PEAK3 (SHP 125-172-US)
code: '10249'
code_key: '10249'
display_message: '|tn4|: network busy'
page: 71
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-shpxxx-us-21-be-en-11
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.40
    h: 5da997984522
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h470
    h: 84154dcf2144
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:communication-loss
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h297
    h: 059ce03933b4
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h214
    h: 059ce03933b4
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h299
    h: 059ce03933b4
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h459
    h: 6781523265db
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h471
    h: 6781523265db
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:network-load-reduction
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h298
    h: d7d9ebc45ca9
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h215
    h: d7d9ebc45ca9
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h300
    h: d7d9ebc45ca9
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h460
    h: d7d9ebc45ca9
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h472
    h: d7d9ebc45ca9
  review: drafted
---
