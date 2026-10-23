---
id: fc:sma-stp-tl-us-27325
type: FaultCode
name: SMA STP-TL-US 27325
aliases:
- '27325'
- SMA 27325
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: '27325'
code_key: '27325'
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=21.r13
    h: edc0b7ade51e
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=21.r13
    h: edc0b7ade51e
  review: drafted
  review_note: 'support check: partial - Row is a status message (updating), implying informational, but
    classification not explicitly stated.'
- claim_id: c3
  rel: affects
  target: comp:communication-module
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=21.r13
    h: edc0b7ade51e
  review: drafted
---
