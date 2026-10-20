---
id: fc:sma-stp-core1-us-10109
type: FaultCode
name: SMA CORE1-US 10109
aliases:
- '10109'
- SMA 10109
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '10109'
code_key: '10109'
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r7
    h: ab83d466a536
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r7
    h: ab83d466a536
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r7
    h: ab83d466a536
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r7
    h: ab83d466a536
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c4
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r7
    h: ab83d466a536
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r7
    h: ab83d466a536
  review: drafted
  review_note: 'support check: partial - No production effect is implied but not stated.'
---
