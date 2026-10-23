---
id: fc:sma-stp-core1-us-7619
type: FaultCode
name: SMA CORE1-US 7619
aliases:
- '7619'
- SMA 7619
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '7619'
code_key: '7619'
page: 52
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r9
    h: 9888d3b90b8b
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r9
    h: 9888d3b90b8b
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=22.r9
    h: 9888d3b90b8b
  review: drafted
- claim_id: c4
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
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c5
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
- claim_id: c6
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
---
