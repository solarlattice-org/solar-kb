---
id: fc:sma-sunny-central-cp-xt-3504
type: FaultCode
name: SMA SC-CP-XT 3504
aliases:
- '3504'
- SMA 3504
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '3504'
code_key: '3504'
page: 36
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r3
    h: 5c93c770ad05
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:low-insulation-resistance
  note: Ignored when the insulation-error ignore parameter is enabled.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r3
    h: 5c93c770ad05
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:insulation-monitor
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r3
    h: 5c93c770ad05
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r3
    h: 5c93c770ad05
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:fault-localization
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r3
    h: 5c93c770ad05
  review: drafted
  review_note: 'support check: partial - Check PV array for ground faults implies localization but is
    not stated as detection method.'
- claim_id: c6
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r3
    h: 5c93c770ad05
  review: drafted
---
