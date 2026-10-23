---
id: fc:sma-sb-us-41-9005
type: FaultCode
name: SMA SB-US-41 9005
aliases:
- '9005'
- SMA 9005
- Waiting for main CPU
category: Inverters
make: sma
make_name: SMA
model_family: sb-us-41
family_name: Sunny Boy 3.0-7.7-US (SBx.x-1SP-US-41)
code: '9005'
code_key: '9005'
display_message: Waiting for main CPU
page: 69
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sbxx-us-1xp-41-ba-en-12
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=6.2.65
    h: a6d4421a16f3
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h430
    h: 64047adc4748
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:parameter-change-rejected
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r4
    h: 81f35c20bd2e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r4
    h: 81f35c20bd2e
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=23.r4
    h: 81f35c20bd2e
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h254
    h: 2231dc9042c7
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:insufficient-dc-power
  note: DC voltage too low to run the main CPU.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r4
    h: 81f35c20bd2e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r4
    h: 81f35c20bd2e
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=23.r4
    h: 81f35c20bd2e
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h254
    h: 2231dc9042c7
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=21.r2
    h: c215834d0c43
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:enter-access-code
  note: When the cause is protected parameters.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r4
    h: 81f35c20bd2e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r4
    h: 81f35c20bd2e
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=23.r4
    h: 81f35c20bd2e
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h255
    h: 5915aa3124df
  review: drafted
---
