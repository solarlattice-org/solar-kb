---
id: fc:sma-sunny-central-cp-xt-8702
type: FaultCode
name: SMA SC-CP-XT 8702
aliases:
- '8702'
- SMA 8702
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '8702'
code_key: '8702'
page: 40
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r5
    h: a8a9b15963e6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:conflicting-power-setpoints
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r5
    h: a8a9b15963e6
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r5
    h: a8a9b15963e6
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r5
    h: a8a9b15963e6
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r5
    h: a8a9b15963e6
  review: drafted
---
