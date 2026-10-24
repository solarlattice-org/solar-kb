---
id: fc:sma-sunny-central-cp-xt-7706
type: FaultCode
name: SMA SC-CP-XT 7706
aliases:
- '7706'
- SMA 7706
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '7706'
code_key: '7706'
page: 39
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r16
    h: c8e1d1ec82eb
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:ac-disconnect-open
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r16
    h: c8e1d1ec82eb
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:ac-disconnect
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r16
    h: c8e1d1ec82eb
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r16
    h: c8e1d1ec82eb
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r16
    h: c8e1d1ec82eb
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r16
    h: c8e1d1ec82eb
  review: drafted
---
