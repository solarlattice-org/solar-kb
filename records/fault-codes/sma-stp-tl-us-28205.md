---
id: fc:sma-stp-tl-us-28205
type: FaultCode
name: SMA STP-TL-US 28205
aliases:
- '28205'
- SMA 28205
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: '28205'
code_key: '28205'
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=21.r15
    h: 02d1b2b0f754
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=21.r15
    h: 02d1b2b0f754
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:arc-fault-detector
  note: Reports successful completion of the arc fault detection self-test
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=21.r15
    h: 02d1b2b0f754
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-stp-tl-us
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=21.r15
    h: 02d1b2b0f754
  review: drafted
---
