---
id: prod:solis-s6-gc-us
type: Product
name: Solis S6-GC(25-60)K-US
aliases:
- S6-GC25K-US
- S6-GC33K-US
- S6-GC36K-US
- S6-GC40K-US
- S6-GC50K-US
- S6-GC60K-US
- S6-GC30K-LV-US
- S6-GC-30K-LV-US
category: Inverters
make: solis
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:solis
  cite:
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: sec=front
    h: 65d0ffd891c8
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: sec=h2
    h: 18fedeb6b950
  review: drafted
  review_note: 'support check: partial - Passages list the models and the token ''solis'', but nothing
    explicitly states Solis makes them (only a bare name appears).'
- claim_id: c2
  rel: uses_protocol
  target: proto:rs485
  note: Listed as the standard communication connection for every model in the family.
  cite:
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=15.r35
    h: 4b848225bef5
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=18.r35
    h: c47df088d2b1
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=21.r35
    h: c90b3dd44720
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=17.r35
    h: b9d64737dd09
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=16.r35
    h: c2fbab15d501
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=20.r35
    h: 1ca1f7bac673
  review: drafted
  review_note: 'support check: partial - RS485 is listed for six models, but S6-GC50K-US has no communication
    row in the passages, so ''every model'' is not fully covered.; review: partial - Six model rows list
    RS485 as a communication connection, but the passages never call it the standard connection for every
    model, and no row covers S6-GC50K-US.'
- claim_id: c3
  rel: uses_protocol
  target: proto:wifi
  conditions: Optional communication connection
  cite:
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=15.r35
    h: 4b848225bef5
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=18.r35
    h: c47df088d2b1
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=21.r35
    h: c90b3dd44720
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=17.r35
    h: b9d64737dd09
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=16.r35
    h: c2fbab15d501
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=20.r35
    h: 1ca1f7bac673
  review: drafted
  review_note: 'support check: partial - WIFI is listed as optional for six models, but the S6-GC50K-US
    row is missing.'
- claim_id: c4
  rel: uses_protocol
  target: proto:cellular
  conditions: Optional communication connection
  cite:
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=15.r35
    h: 4b848225bef5
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=18.r35
    h: c47df088d2b1
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=21.r35
    h: c90b3dd44720
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=17.r35
    h: b9d64737dd09
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=16.r35
    h: c2fbab15d501
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=20.r35
    h: 1ca1f7bac673
  review: drafted
  review_note: 'support check: partial - Cellular is listed as optional for six models, but the S6-GC50K-US
    row is missing.'
---
The manual's model list prints the low-voltage variant as S6-GC-30K-LV-US, but its spec tables print it as S6-GC30K-LV-US. Every model has an RS485 communication connection as standard. Wi-Fi and cellular connections are listed as options.

<!-- review notes
- sentence 2: support check: partial - RS485 with optional WIFI/Cellular is shown for six models, but not for S6-GC50K-US, so 'every model' is not fully shown; 'standard' is implied by the 'Optional' label.
-->
