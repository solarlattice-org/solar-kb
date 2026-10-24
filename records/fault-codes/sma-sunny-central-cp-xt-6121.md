---
id: fc:sma-sunny-central-cp-xt-6121
type: FaultCode
name: SMA SC-CP-XT 6121
aliases:
- '6121'
- SMA 6121
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '6121'
code_key: '6121'
page: 37
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r8
    h: 3fd754c46607
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  note: Watchdog gives no response.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r8
    h: 3fd754c46607
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r8
    h: 3fd754c46607
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r8
    h: 3fd754c46607
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r8
    h: 3fd754c46607
  review: drafted
---
