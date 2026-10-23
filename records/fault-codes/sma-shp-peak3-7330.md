---
id: fc:sma-shp-peak3-7330
type: FaultCode
name: SMA PEAK3-US 7330
aliases:
- '7330'
- SMA 7330
- Wait for update conditions
category: Inverters
make: sma
make_name: SMA
model_family: shp-peak3
family_name: Sunny Highpower PEAK3 (SHP 125-172-US)
code: '7330'
code_key: '7330'
display_message: Wait for update conditions
page: 65
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-shpxxx-us-21-be-en-11
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.21
    h: 483d94aa5325
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h376
    h: 42228ca4b612
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:firmware-update-failure
  note: Update package not suitable for this inverter.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=20.r1
    h: bc08bcd11a95
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=9.r1
    h: bc08bcd11a95
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=21.r1
    h: bc08bcd11a95
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h377
    h: d330f7b2eab4
  review: drafted
---
