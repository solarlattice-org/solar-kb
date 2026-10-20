---
id: fc:sma-stp-core1-us-9033
type: FaultCode
name: SMA CORE1-US 9033
aliases:
- '9033'
- SMA 9033
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '9033'
code_key: '9033'
page: 54
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r7
    h: eaf36c5b0c2a
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r7
    h: eaf36c5b0c2a
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:rapid-shutdown
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r7
    h: eaf36c5b0c2a
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r7
    h: eaf36c5b0c2a
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: AC side of the inverter is disconnected.
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r7
    h: eaf36c5b0c2a
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r7
    h: eaf36c5b0c2a
  review: drafted
---
