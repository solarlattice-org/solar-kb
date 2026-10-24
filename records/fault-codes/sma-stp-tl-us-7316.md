---
id: fc:sma-stp-tl-us-7316
type: FaultCode
name: SMA STP-TL-US 7316
aliases:
- '7316'
- SMA 7316
category: Inverters
make: sma
make_name: SMA
model_family: stp-tl-us
family_name: Sunny Tripower 12000-30000TL-US (STP xxxxxTL-US-10)
code: '7316'
code_key: '7316'
page: 52
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stptl-us-10-ia-xx-22
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r7
    h: dd239bcb7cd6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:firmware-update-failure
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r7
    h: dd239bcb7cd6
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:communication-module
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r7
    h: dd239bcb7cd6
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:retry-update
  note: Retry first; contact service if failure recurs
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r7
    h: dd239bcb7cd6
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the update failure recurs after retry
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r7
    h: dd239bcb7cd6
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sma-stp-tl-us
  cite:
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: tbl=18.r7
    h: dd239bcb7cd6
  review: drafted
---
