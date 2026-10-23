---
id: fc:sma-sunny-central-cp-xt-104
type: FaultCode
name: SMA SC-CP-XT 0104
aliases:
- '0104'
- '104'
- SMA 0104
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '0104'
code_key: '104'
page: 34
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=32.r2
    h: 84378c008d45
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=32.r2
    h: 84378c008d45
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:external-fuse-check
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=32.r2
    h: 84378c008d45
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Section context says grid errors shut the inverter down.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=32.r2
    h: 84378c008d45
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=5.4.3
    h: 162f559707eb
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Reconnects after grid monitoring time; depending on parameterization manual acknowledgement may
    be needed.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=32.r2
    h: 84378c008d45
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=5.4.3
    h: 162f559707eb
  review: drafted
---
