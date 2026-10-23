---
id: fc:sma-sunny-central-cp-xt-6410
type: FaultCode
name: SMA SC-CP-XT 6410
aliases:
- '6410'
- SMA 6410
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '6410'
code_key: '6410'
page: 37
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r13
    h: 29a79d604337
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:supply-voltage-invalid
  note: 24 V internal supply
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r13
    h: 29a79d604337
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:internal-power-supply-fault
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r13
    h: 29a79d604337
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r13
    h: 29a79d604337
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r13
    h: 29a79d604337
  review: drafted
  review_note: 'support check: partial - The row shows disconnection/wait behavior and a service contact,
    so a fault is implied, but it isn''t explicitly classified.'
- claim_id: c6
  rel: has_recovery
  target: ec:service-required
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r13
    h: 29a79d604337
  review: drafted
---
