---
id: fc:sma-stp-core1-us-901
type: FaultCode
name: SMA CORE1-US 901
aliases:
- '901'
- SMA 901
- Grounding connection missing > Check connection
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '901'
code_key: '901'
display_message: Grounding connection missing > Check connection
page: 48
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h254
    h: 667ca1664a7c
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h255
    h: 260925fde74a
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h171
    h: 667ca1664a7c
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h172
    h: 260925fde74a
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h256
    h: 667ca1664a7c
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h257
    h: 260925fde74a
  review: drafted
- claim_id: c4
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
  review: drafted
- claim_id: c5
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
