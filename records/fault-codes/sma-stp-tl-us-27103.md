---
id: fc:sma-stp-tl-us-27103
type: FaultCode
name: SMA STP-TL-US 27103
aliases:
- '27103'
- SMA 27103
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: '27103'
code_key: '27103'
page: 55
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=21.r6
    h: a6270650246e
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Status message while parameter changes are being adopted.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=26.r8
    h: c5550759f780
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=15.r8
    h: c5550759f780
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=27.r8
    h: c5550759f780
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=21.r6
    h: a6270650246e
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:sma-stp-tl-us
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=21.r6
    h: a6270650246e
  review: drafted
---
