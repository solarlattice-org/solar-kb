---
id: fc:sma-sunny-central-cp-xt-7006
type: FaultCode
name: SMA SC-CP-XT 7006
aliases:
- '7006'
- SMA 7006
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '7006'
code_key: '7006'
page: 39
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r5
    h: ff69c7112d63
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:temperature-sensor-fault
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r5
    h: ff69c7112d63
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:temperature-sensor
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r5
    h: ff69c7112d63
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:wiring-terminal-check
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r5
    h: ff69c7112d63
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Escalation after sensor wiring check.
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r5
    h: ff69c7112d63
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sma-sunny-central-cp-xt
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=38.r5
    h: ff69c7112d63
  review: drafted
---
