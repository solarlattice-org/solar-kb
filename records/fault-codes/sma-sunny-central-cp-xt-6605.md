---
id: fc:sma-sunny-central-cp-xt-6605
type: FaultCode
name: SMA SC-CP-XT 6605
aliases:
- '6605'
- SMA 6605
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '6605'
code_key: '6605'
page: 39
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r1
    h: c22cba87c04a
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r1
    h: c22cba87c04a
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r1
    h: c22cba87c04a
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Fast stop triggered by switch cabinet overtemperature.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r1
    h: c22cba87c04a
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r1
    h: c22cba87c04a
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r1
    h: c22cba87c04a
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r1
    h: c22cba87c04a
  review: drafted
---
