---
id: fc:sma-sunny-central-cp-xt-6427
type: FaultCode
name: SMA SC-CP-XT 6427
aliases:
- '6427'
- SMA 6427
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '6427'
code_key: '6427'
page: 37
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r19
    h: adbb0b3e5531
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:voltage-sensor-fault
  note: DC voltage measurement sensor
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r19
    h: adbb0b3e5531
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r19
    h: adbb0b3e5531
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r19
    h: adbb0b3e5531
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r19
    h: adbb0b3e5531
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r19
    h: adbb0b3e5531
  review: drafted
---
