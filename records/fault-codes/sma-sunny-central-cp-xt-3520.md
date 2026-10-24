---
id: fc:sma-sunny-central-cp-xt-3520
type: FaultCode
name: SMA SC-CP-XT 3520
aliases:
- '3520'
- SMA 3520
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '3520'
code_key: '3520'
page: 36
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r10
    h: 3baec5b7187e
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  note: Reports an insulation fault that has already been cleared.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r10
    h: 3baec5b7187e
  review: drafted
  review_note: 'support check: partial - The fault was fixed and no action is needed, but the row shows
    behavior W rather than informational.'
- claim_id: c3
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r10
    h: 3baec5b7187e
  review: drafted
---
