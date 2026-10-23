---
id: fc:sma-stp-tl-us-7326
type: FaultCode
name: SMA STP-TL-US 7326
aliases:
- '7326'
- SMA 7326
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: '7326'
code_key: '7326'
page: 53
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r1
    h: debdf2bb6512
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:firmware-update-failure
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r1
    h: debdf2bb6512
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:communication-module
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r1
    h: debdf2bb6512
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:retry-update
  note: Retry first; contact service if failure recurs
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r1
    h: debdf2bb6512
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the update failure recurs after retry
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=19.r1
    h: debdf2bb6512
  review: drafted
---
