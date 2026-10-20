---
id: fc:sma-stp-core1-us-6502
type: FaultCode
name: SMA CORE1-US 6502
aliases:
- '6502'
- SMA 6502
category: Inverters
make: sma
make_name: SMA
model_family: stp-core1-us
family_name: Sunny Tripower CORE1-US (STP 33/50/62-US-41)
code: '6502'
code_key: '6502'
page: 49
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-13
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r7
    h: fa68e2b51596
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sma-stp33-62-us-41-ops-manual
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r7
    h: fa68e2b51596
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r7
    h: fa68e2b51596
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r7
    h: fa68e2b51596
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r7
    h: fa68e2b51596
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r7
    h: fa68e2b51596
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r7
    h: fa68e2b51596
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r7
    h: fa68e2b51596
  review: drafted
- claim_id: c6
  rel: affects
  target: comp:inverter
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r7
    h: fa68e2b51596
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r7
    h: fa68e2b51596
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:clear-heat-dissipation-path
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r7
    h: fa68e2b51596
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r8
    h: 9db7f3376fec
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r7
    h: fa68e2b51596
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r8
    h: 9db7f3376fec
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:adequate-cooling
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r8
    h: 9db7f3376fec
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r8
    h: 9db7f3376fec
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r7
    h: fa68e2b51596
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r7
    h: fa68e2b51596
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:direct-sun-avoidance
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r8
    h: 9db7f3376fec
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r8
    h: 9db7f3376fec
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r7
    h: fa68e2b51596
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r7
    h: fa68e2b51596
  review: drafted
---
