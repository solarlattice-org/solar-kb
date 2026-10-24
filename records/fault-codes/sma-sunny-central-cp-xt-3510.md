---
id: fc:sma-sunny-central-cp-xt-3510
type: FaultCode
name: SMA SC-CP-XT 3510
aliases:
- '3510'
- SMA 3510
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '3510'
code_key: '3510'
page: 36
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r5
    h: 2010696eba68
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:low-insulation-resistance
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r5
    h: 2010696eba68
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r5
    h: 2010696eba68
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:fault-localization
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r5
    h: 2010696eba68
  review: drafted
  review_note: 'support check: partial - Check PV array for ground faults implies localization but not
    explicitly.'
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=35.r5
    h: 2010696eba68
  review: drafted
---
