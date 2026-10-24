---
id: fc:sma-sunny-central-cp-xt-3404
type: FaultCode
name: SMA SC-CP-XT 3404
aliases:
- '3404'
- SMA 3404
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '3404'
code_key: '3404'
page: 35
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=34.r2
    h: c18bd86c0be0
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h258
    h: 33883a354598
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h260
    h: 587cea85589b
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=34.r2
    h: c18bd86c0be0
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h258
    h: 33883a354598
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h261
    h: 5bf6ccea6e5e
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=34.r2
    h: c18bd86c0be0
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h258
    h: 33883a354598
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h261
    h: 5bf6ccea6e5e
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=34.r2
    h: c18bd86c0be0
  review: drafted
  review_note: 'support check: partial - The passages say to check the DC voltage but do not say detection
    is by DC voltage measurement; the row…'
- claim_id: c5
  rel: mitigated_by
  target: mit:string-voltage-margin-design
  note: When DC voltage exceeds the inverter maximum input voltage
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h258
    h: 33883a354598
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h261
    h: 5bf6ccea6e5e
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=34.r2
    h: c18bd86c0be0
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=34.r2
    h: c18bd86c0be0
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h258
    h: 33883a354598
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h260
    h: 587cea85589b
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: sec=h261
    h: 5bf6ccea6e5e
  review: drafted
  review_note: 'support check: partial - The passages imply a fault through the destruction risk and disconnection,
    but the class is not stated explicitly, and the…'
- claim_id: c8
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=34.r2
    h: c18bd86c0be0
  review: drafted
---
