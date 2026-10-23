---
id: fc:sma-sunny-central-cp-xt-6116
type: FaultCode
name: SMA SC-CP-XT 6116
aliases:
- '6116'
- SMA 6116
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '6116'
code_key: '6116'
page: 37
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r4
    h: d440ab114d46
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:clock-time-lost
  note: Real-time clock not initialized.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r4
    h: d440ab114d46
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:real-time-clock
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r4
    h: d440ab114d46
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r4
    h: d440ab114d46
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r4
    h: d440ab114d46
  review: drafted
---
