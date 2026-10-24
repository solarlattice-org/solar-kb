---
id: fc:sma-sunny-central-cp-xt-204
type: FaultCode
name: SMA SC-CP-XT 0204
aliases:
- '0204'
- '204'
- SMA 0204
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '0204'
code_key: '204'
page: 34
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=32.r4
    h: 84e770a9f9bd
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=32.r4
    h: 84e770a9f9bd
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  note: Section context says grid errors shut the inverter down.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=32.r4
    h: 84e770a9f9bd
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=5.4.3
    h: 162f559707eb
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Depending on parameterization manual acknowledgement may be needed.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=32.r4
    h: 84e770a9f9bd
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=5.4.3
    h: 162f559707eb
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=32.r4
    h: 84e770a9f9bd
  review: drafted
---
