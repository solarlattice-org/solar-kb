---
id: fc:sma-sunny-central-cp-xt-6457
type: FaultCode
name: SMA SC-CP-XT 6457
aliases:
- '6457'
- SMA 6457
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '6457'
code_key: '6457'
page: 38
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r11
    h: 3c99084f0ad9
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:self-test-failure
  note: Capacitor self-test.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r11
    h: 3c99084f0ad9
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r11
    h: 3c99084f0ad9
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r11
    h: 3c99084f0ad9
  review: drafted
---
