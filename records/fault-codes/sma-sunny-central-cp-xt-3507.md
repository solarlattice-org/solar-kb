---
id: fc:sma-sunny-central-cp-xt-3507
type: FaultCode
name: SMA SC-CP-XT 3507
aliases:
- '3507'
- SMA 3507
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '3507'
code_key: '3507'
page: 36
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r4
    h: 34e8393df0af
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:ground-fault
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r4
    h: 34e8393df0af
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r4
    h: 34e8393df0af
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:fault-localization
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r4
    h: 34e8393df0af
  review: drafted
  review_note: 'support check: partial - Only a check of the PV array for ground faults is stated, not
    a localization method.'
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r4
    h: 34e8393df0af
  review: drafted
---
