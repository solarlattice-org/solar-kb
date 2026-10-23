---
id: fc:sma-sunny-central-cp-xt-6405
type: FaultCode
name: SMA SC-CP-XT 6405
aliases:
- '6405'
- SMA 6405
category: Inverters
make: sma
make_name: SMA
model_family: sunny-central-cp-xt
family_name: Sunny Central 500CP XT-1000CP XT
code: '6405'
code_key: '6405'
page: 37
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-sccpxt-e7-wa-en-37
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r12
    h: 6ae12d09ad40
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-bus-overvoltage
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r12
    h: 6ae12d09ad40
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h516
    h: 749a6098bfa9
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r12
    h: 6ae12d09ad40
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:dc-connector
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h517
    h: a1d43f878551
  review: drafted
  review_note: 'support check: partial - DC plug connections are listed as possible error sources, but
    the passage doesn''t say the event affects the connector directly.'
- claim_id: c5
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h517
    h: a1d43f878551
  review: drafted
  review_note: 'support check: partial - DC cabling is listed as a possible error source; the link is
    indirect.'
- claim_id: c6
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h517
    h: a1d43f878551
  review: drafted
  review_note: 'support check: partial - PV modules are listed as a possible error source and array rating
    is mentioned, but no explicit statement that the…'
- claim_id: c7
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: When the event occurs frequently.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h517
    h: a1d43f878551
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h517
    h: a1d43f878551
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if the event persists after successful checks.
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h517
    h: a1d43f878551
  review: drafted
- claim_id: c10
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=36.r12
    h: 6ae12d09ad40
  review: drafted
- claim_id: c11
  rel: has_recovery
  target: ec:auto-reset
  note: 'Rare occurrence needs no action; frequent: check array design and DC wiring, then replace assembly
    or inverter.'
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h517
    h: a1d43f878551
  review: drafted
  review_note: 'support check: partial - Rare occurrences needing no action hints at self-clearing, but
    auto-reset is not stated, and the table row shows a 30…'
---
