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
  rel: defined_in
  target: src:sma-stp33-62-us-41-ba-en-14
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r7
    h: 697b7dc0517b
  review: drafted
- claim_id: c4
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r7
    h: fa68e2b51596
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r7
    h: fa68e2b51596
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r7
    h: 697b7dc0517b
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h627
    h: abc29332332d
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r18
    h: 7e495d3b84ea
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:ambient-temperature-check
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=11.1.42
    h: c0bbd8c0ee73
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h628
    h: 3957b3341b69
  review: drafted
  review_note: 'support check: partial - Ensuring max ambient temperature is complied with is a corrective
    measure, not a detection method.'
- claim_id: c7
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
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
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=37.r18
    h: 7e495d3b84ea
  review: drafted
- claim_id: c8
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r7
    h: fa68e2b51596
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r7
    h: fa68e2b51596
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h627
    h: abc29332332d
  review: drafted
- claim_id: c9
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=18.r7
    h: fa68e2b51596
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=7.r7
    h: fa68e2b51596
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=19.r7
    h: 697b7dc0517b
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h627
    h: abc29332332d
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
---
