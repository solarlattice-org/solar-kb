---
id: fc:sma-stp-core1-us-29004
type: FaultCode
name: SMA CORE1-US 29004
aliases:
- '29004'
- SMA 29004
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '29004'
code_key: '29004'
page: 59
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=26.r15
    h: 1851894a0a87
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=15.r15
    h: 1851894a0a87
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=27.r15
    h: 1851894a0a87
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:parameter-change-rejected
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=26.r15
    h: 1851894a0a87
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=15.r15
    h: 1851894a0a87
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=27.r15
    h: 1851894a0a87
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=22.r5
    h: 4a55c0f1a1eb
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=22.r2
    h: 9a60070f2b45
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.107
    h: edd3590f7093
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h582
    h: 978b87543654
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h583
    h: 65873cd56889
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=26.r15
    h: 1851894a0a87
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=15.r15
    h: 1851894a0a87
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=27.r15
    h: 1851894a0a87
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=22.r5
    h: 4a55c0f1a1eb
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=22.r2
    h: 9a60070f2b45
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h583
    h: 65873cd56889
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c6
  rel: applies_to
  target: prod:sma-stp-core1-us
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=26.r15
    h: 1851894a0a87
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=15.r15
    h: 1851894a0a87
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=27.r15
    h: 1851894a0a87
  review: drafted
---
