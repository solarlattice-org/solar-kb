---
id: fc:sma-stp-core1-us-10340
type: FaultCode
name: SMA CORE1-US 10340
aliases:
- '10340'
- SMA 10340
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '10340'
code_key: '10340'
page: 59
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=26.r1
    h: b1cc33815f32
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h298
    h: 1dd57fd497da
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h507
    h: d55186395880
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: 'Only if direct portal communication is wanted: re-enable the Webconnect function.'
  cite:
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h298
    h: 1dd57fd497da
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sma-stp-core1-us
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=26.r1
    h: b1cc33815f32
  review: drafted
---
