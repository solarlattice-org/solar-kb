---
id: fc:sma-stp-tl-us-7311
type: FaultCode
name: SMA STP-TL-US 7311
aliases:
- '7311'
- SMA 7311
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: '7311'
code_key: '7311'
page: 52
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r6
    h: 49ebca7e1476
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:firmware-update-failure
  note: Language table update
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r6
    h: 49ebca7e1476
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:retry-update
  note: Retry first; contact service if failure recurs
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r6
    h: 49ebca7e1476
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the update failure recurs after retry
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r6
    h: 49ebca7e1476
  review: drafted
---
