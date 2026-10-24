---
id: fc:sma-sunny-central-cp-xt-3515
type: FaultCode
name: SMA SC-CP-XT 3515
aliases:
- '3515'
- SMA 3515
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '3515'
code_key: '3515'
page: 36
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r8
    h: 9c2ae6401602
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:ground-fault
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r8
    h: 9c2ae6401602
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r8
    h: 9c2ae6401602
  review: drafted
  review_note: 'support check: partial - PV array appears only in the corrective measure.'
- claim_id: c4
  rel: detected_by
  target: method:fault-localization
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r8
    h: 9c2ae6401602
  review: drafted
  review_note: 'support check: partial - Implied only by the check instruction.'
- claim_id: c5
  rel: has_event_class
  target: ec:warning
  note: The detected ground fault is ignored, so operation continues while flagged.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r8
    h: 9c2ae6401602
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r8
    h: 9c2ae6401602
  review: drafted
---
