---
id: fc:sma-stp-tl-us-27310
type: FaultCode
name: SMA STP-TL-US 27310
aliases:
- '27310'
- SMA 27310
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: '27310'
code_key: '27310'
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=21.r14
    h: 57eb4f0403d6
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=21.r14
    h: 57eb4f0403d6
  review: drafted
  review_note: 'support check: partial - Status message about updating; informational implied but not
    stated.'
- claim_id: c3
  rel: affects
  target: comp:communication-module
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=21.r14
    h: 57eb4f0403d6
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-stp-tl-us
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=21.r14
    h: 57eb4f0403d6
  review: drafted
---
