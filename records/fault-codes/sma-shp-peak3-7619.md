---
id: fc:sma-shp-peak3-7619
type: FaultCode
name: SMA PEAK3-US 7619
aliases:
- '7619'
- SMA 7619
category: Inverters
make: sma
make_name: SMA
model_family: shp-peak3
family_name: Sunny Highpower PEAK3 (SHP 125-172-US)
code: '7619'
code_key: '7619'
page: 67
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-shpxxx-us-21-be-en-11
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.26
    h: 07982b660099
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:communication-loss
  note: Inverter receives no data from the energy meter.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r9
    h: 9888d3b90b8b
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r9
    h: 9888d3b90b8b
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=22.r9
    h: 9888d3b90b8b
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h235
    h: 881ad6c197f7
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h397
    h: 675e88e1fcfd
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h401
    h: 675e88e1fcfd
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:energy-meter
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r9
    h: 9888d3b90b8b
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r9
    h: 9888d3b90b8b
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=22.r9
    h: 9888d3b90b8b
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h235
    h: 881ad6c197f7
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h397
    h: 675e88e1fcfd
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h401
    h: 675e88e1fcfd
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:network-connection-check
  note: Meter must be on the same network; for Wi-Fi, improve link quality or use Ethernet.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r9
    h: 9888d3b90b8b
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r9
    h: 9888d3b90b8b
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=22.r9
    h: 9888d3b90b8b
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h398
    h: 1429c43b5943
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h402
    h: 1429c43b5943
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-shp-peak3
  cite:
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=12.1.26
    h: 07982b660099
  review: drafted
---
