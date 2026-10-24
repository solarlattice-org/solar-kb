---
id: fc:sma-sunny-central-cp-xt-3512
type: FaultCode
name: SMA SC-CP-XT 3512
aliases:
- '3512'
- SMA 3512
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '3512'
code_key: '3512'
page: 36
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r7
    h: 2b0e4bbdf412
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:ground-fault
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r7
    h: 2b0e4bbdf412
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r7
    h: 2b0e4bbdf412
  review: drafted
  review_note: 'support check: partial - PV array appears only in the corrective measure, not as the affected
    component.'
- claim_id: c4
  rel: detected_by
  target: method:fault-localization
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r7
    h: 2b0e4bbdf412
  review: drafted
  review_note: 'support check: partial - Implied by check for ground faults, not stated as a method.'
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r7
    h: 2b0e4bbdf412
  review: drafted
---
