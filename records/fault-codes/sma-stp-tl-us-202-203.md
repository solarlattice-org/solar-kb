---
id: fc:sma-stp-tl-us-202-203
type: FaultCode
name: SMA STP-TL-US 202-203
aliases:
- 202-203
- SMA 202-203
- Grid fault
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: 202-203
code_key: 202-203
code_from: 202
code_to: 203
display_message: Grid fault
page: 45
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h179
    h: 06a2712e0fd4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h179
    h: 06a2712e0fd4
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-loss
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h179
    h: 06a2712e0fd4
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h179
    h: 06a2712e0fd4
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h180
    h: da920c17bb08
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h179
    h: 06a2712e0fd4
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h179
    h: 06a2712e0fd4
  review: drafted
- claim_id: c7
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h180
    h: da920c17bb08
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:ac-connection-check
  note: Check breaker and AC cabling first; grid operator, then service if persistent
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h180
    h: da920c17bb08
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:utility-consultation
  note: When grid voltage is out of range due to local grid conditions
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h180
    h: da920c17bb08
  review: drafted
- claim_id: c10
  rel: applies_to
  target: prod:sma-stp-tl-us
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h179
    h: 06a2712e0fd4
  review: drafted
---
