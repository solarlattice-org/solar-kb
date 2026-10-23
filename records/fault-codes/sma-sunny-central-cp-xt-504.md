---
id: fc:sma-sunny-central-cp-xt-504
type: FaultCode
name: SMA SC-CP-XT 0504
aliases:
- '0504'
- '504'
- SMA 0504
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '0504'
code_key: '504'
page: 35
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r4
    h: cc57729321ae
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-underfrequency
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r4
    h: cc57729321ae
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r4
    h: cc57729321ae
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=5.4.3
    h: 162f559707eb
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=33.r4
    h: cc57729321ae
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=5.4.3
    h: 162f559707eb
  review: drafted
  review_note: 'support check: partial - Reconnect after monitoring time implies auto-reset, but manual
    acknowledgment may be needed depending on parameterization.'
---
