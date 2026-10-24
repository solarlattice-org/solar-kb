---
id: fc:sma-sunny-central-cp-xt-6418
type: FaultCode
name: SMA SC-CP-XT 6418
aliases:
- '6418'
- SMA 6418
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '6418'
code_key: '6418'
page: 37
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r15
    h: 4671f9567aa7
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r15
    h: 4671f9567aa7
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r15
    h: 4671f9567aa7
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r15
    h: 4671f9567aa7
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r15
    h: 4671f9567aa7
  review: drafted
  review_note: 'support check: partial - A fault is implied by the behavior and service contact, but it
    isn''t explicitly classified.'
- claim_id: c6
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r15
    h: 4671f9567aa7
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r15
    h: 4671f9567aa7
  review: drafted
---
