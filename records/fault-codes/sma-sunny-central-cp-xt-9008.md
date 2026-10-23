---
id: fc:sma-sunny-central-cp-xt-9008
type: FaultCode
name: SMA SC-CP-XT 9008
aliases:
- '9008'
- SMA 9008
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '9008'
code_key: '9008'
page: 40
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r8
    h: c54a837019da
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:enclosure-door-open
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r8
    h: c54a837019da
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r8
    h: c54a837019da
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=39.r8
    h: c54a837019da
  review: drafted
---
