---
id: fc:sma-stp-tl-us-901
type: FaultCode
name: SMA STP-TL-US 901
aliases:
- '901'
- SMA 901
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: '901'
code_key: '901'
page: 47
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=14.r3
    h: 933298c8de4f
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:missing-ground-connection
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h172
    h: 260925fde74a
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h257
    h: 260925fde74a
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=14.r3
    h: 933298c8de4f
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h498
    h: 57e11449fc02
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h499
    h: 8f0cb2682e47
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: mitigated_by
  target: mit:ground-conductor-check
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h256
    h: 5de48d290b94
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h173
    h: 5de48d290b94
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h258
    h: 33883a354598
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=14.r3
    h: 933298c8de4f
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h500
    h: 5de48d290b94
  review: drafted
---
