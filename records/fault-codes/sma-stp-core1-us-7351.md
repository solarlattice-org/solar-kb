---
id: fc:sma-stp-core1-us-7351
type: FaultCode
name: SMA CORE1-US 7351
aliases:
- '7351'
- SMA 7351
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '7351'
code_key: '7351'
page: 52
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r3
    h: fb36bcc7e0da
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r3
    h: fb36bcc7e0da
  review: drafted
- claim_id: c3
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=22.r3
    h: fb36bcc7e0da
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r3
    h: fb36bcc7e0da
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=22.r3
    h: fb36bcc7e0da
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=19.r2
    h: 576c7d273e37
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c5
  rel: affects
  target: comp:wifi-module
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r3
    h: fb36bcc7e0da
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=22.r3
    h: fb36bcc7e0da
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: tbl=19.r2
    h: 576c7d273e37
  review: drafted
---
