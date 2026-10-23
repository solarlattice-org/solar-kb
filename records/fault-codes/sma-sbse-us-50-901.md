---
id: fc:sma-sbse-us-50-901
type: FaultCode
name: SMA SBSE-US-50 901
aliases:
- '901'
- SMA 901
- PE connection missing > Check connection
category: Inverters
make: sma
make_name: SMA
model_family: sbse-us-50
family_name: Sunny Boy Smart Energy 3.8-11.5-US (SBSEx.x-US-50)
code: '901'
code_key: '901'
display_message: PE connection missing > Check connection
page: 102
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbsexx-us-50-be-en-11
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.16
    h: 4b68d34393ad
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h498
    h: 57e11449fc02
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
  review: drafted
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
