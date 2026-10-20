---
id: fc:sma-stp-core1-us-10118
type: FaultCode
name: SMA CORE1-US 10118
aliases:
- '10118'
- SMA 10118
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '10118'
code_key: '10118'
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r9
    h: 7765fe1a9c08
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r9
    h: 7765fe1a9c08
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r9
    h: 7765fe1a9c08
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r9
    h: 7765fe1a9c08
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r9
    h: 7765fe1a9c08
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r9
    h: 7765fe1a9c08
  review: drafted
  review_note: 'support check: partial - Row implies a status message but never states production effect.'
---
