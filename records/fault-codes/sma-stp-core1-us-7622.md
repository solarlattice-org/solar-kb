---
id: fc:sma-stp-core1-us-7622
type: FaultCode
name: SMA CORE1-US 7622
aliases:
- '7622'
- SMA 7622
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '7622'
code_key: '7622'
page: 52
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r10
    h: beb2c8055c26
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r10
    h: beb2c8055c26
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:communication-loss
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r10
    h: beb2c8055c26
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r10
    h: beb2c8055c26
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:io-module
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r10
    h: beb2c8055c26
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r10
    h: beb2c8055c26
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r10
    h: beb2c8055c26
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r10
    h: beb2c8055c26
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  note: Inverter disconnects from the grid for safety.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r10
    h: beb2c8055c26
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r10
    h: beb2c8055c26
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
