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
  rel: reports
  target: symptom:communication-loss
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r9
    h: 9888d3b90b8b
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r9
    h: 9888d3b90b8b
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c4
  rel: affects
  target: comp:energy-meter
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r9
    h: 9888d3b90b8b
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r9
    h: 9888d3b90b8b
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:network-connection-check
  note: Covers meter network integration and Wi-Fi or Ethernet link quality.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r9
    h: 9888d3b90b8b
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r9
    h: 9888d3b90b8b
  review: drafted
---
