---
id: fc:sma-sunny-central-cp-xt-3502
type: FaultCode
name: SMA SC-CP-XT 3502
aliases:
- '3502'
- SMA 3502
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '3502'
code_key: '3502'
page: 36
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r2
    h: c8d350ec3a48
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:ground-fault
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r2
    h: c8d350ec3a48
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:ground-fault-detector
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r2
    h: c8d350ec3a48
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r2
    h: c8d350ec3a48
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:fault-localization
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r2
    h: c8d350ec3a48
  review: drafted
  review_note: 'support check: partial - Check PV array for ground faults implies localization but not
    explicitly stated as detection method.'
- claim_id: c6
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r2
    h: c8d350ec3a48
  review: drafted
---
