---
id: fc:sma-stp-core1-us-27301
type: FaultCode
name: SMA CORE1-US 27301
aliases:
- '27301'
- SMA 27301
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '27301'
code_key: '27301'
page: 59
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=26.r11
    h: 8b80a8cadd1e
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=15.r11
    h: 8b80a8cadd1e
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:informational
  note: Status message during the communication component update.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=26.r11
    h: 8b80a8cadd1e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=15.r11
    h: 8b80a8cadd1e
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:communication-processor
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=26.r11
    h: 8b80a8cadd1e
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=15.r11
    h: 8b80a8cadd1e
  review: drafted
---
