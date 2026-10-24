---
id: fc:sma-sunny-central-cp-xt-6443
type: FaultCode
name: SMA SC-CP-XT 6443
aliases:
- '6443'
- SMA 6443
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '6443'
code_key: '6443'
page: 38
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r2
    h: 8cd1c2fdae4c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r2
    h: 8cd1c2fdae4c
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:digital-signal-processor
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r2
    h: 8cd1c2fdae4c
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r2
    h: 8cd1c2fdae4c
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r2
    h: 8cd1c2fdae4c
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r2
    h: 8cd1c2fdae4c
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r2
    h: 8cd1c2fdae4c
  review: drafted
---
