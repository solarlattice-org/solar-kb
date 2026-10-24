---
id: fc:sma-sunny-central-cp-xt-6404
type: FaultCode
name: SMA SC-CP-XT 6404
aliases:
- '6404'
- SMA 6404
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '6404'
code_key: '6404'
page: 37
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r11
    h: fd9ded8e4809
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:ac-overcurrent
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r11
    h: fd9ded8e4809
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h511
    h: c6e376e4d4de
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h511
    h: c6e376e4d4de
  review: drafted
  review_note: 'support check: partial - The inverter disconnects from the grid, which implies a fault,
    but the passage doesn''t explicitly classify it as a fault.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h511
    h: c6e376e4d4de
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Occasional occurrence needs no action; permanent presence requires assembly or inverter replacement.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h512
    h: 99fdc49ecb5f
  review: drafted
  review_note: 'support check: partial - Occasional occurrence needing no action is stated, but auto-reset
    is not explicitly stated.'
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  note: When the event is permanently present.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h512
    h: 99fdc49ecb5f
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r11
    h: fd9ded8e4809
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r11
    h: fd9ded8e4809
  review: drafted
---
