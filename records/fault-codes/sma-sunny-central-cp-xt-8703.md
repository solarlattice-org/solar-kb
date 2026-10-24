---
id: fc:sma-sunny-central-cp-xt-8703
type: FaultCode
name: SMA SC-CP-XT 8703
aliases:
- '8703'
- SMA 8703
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '8703'
code_key: '8703'
page: 40
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r6
    h: f52a146dca89
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:invalid-power-setpoint
  note: Concerns the power factor of the external reactive power setpoint.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r6
    h: f52a146dca89
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r6
    h: f52a146dca89
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r6
    h: f52a146dca89
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r6
    h: f52a146dca89
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r6
    h: f52a146dca89
  review: drafted
---
