---
id: fc:sma-stp-x-us-50-103
type: FaultCode
name: SMA STP-X-US 0103
aliases:
- '0103'
- '103'
- SMA 0103
- Grid incident
category: Inverters
make: sma
make_name: SMA
model_family: stp-x-us-50
family_name: Sunny Tripower X 13-30-US (STP xx-US-50)
code: '0103'
code_key: '103'
display_message: Grid incident
page: 79
claims:
- claim_id: c1
  rel: defined_in
  target: src:sma-stpxx-us-50-be-en-14
  cite:
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=11.1.3
    h: 73c43bced9d0
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h382
    h: 354164b2f12c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=32.r1
    h: fcb1b5c1077d
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h197
    h: 9d464275e542
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h383
    h: 9d464275e542
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:grid-impedance-high
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h197
    h: 9d464275e542
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h383
    h: 9d464275e542
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h197
    h: 9d464275e542
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h383
    h: 9d464275e542
  review: drafted
  review_note: 'support check: partial - Inverter disconnects from the grid, but the passages do not explicitly
    classify it as a fault versus warning.'
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h197
    h: 9d464275e542
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h383
    h: 9d464275e542
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Reconnects after grid monitoring time; parameterization may require manual acknowledgement
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=32.r1
    h: fcb1b5c1077d
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: sec=5.4.3
    h: 162f559707eb
  review: drafted
- claim_id: c7
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=32.r1
    h: fcb1b5c1077d
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h198
    h: 60749c2f0bc9
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h384
    h: 60749c2f0bc9
  review: drafted
  review_note: 'support check: partial - Overvoltage detection and grid voltage checks are described,
    but a grid voltage measurement as the detection method is only implied.'
- claim_id: c8
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:sma-sccpxt-e7-wa-en-37
    loc: tbl=32.r1
    h: fcb1b5c1077d
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:utility-consultation
  note: When local grid voltage is out of range; contact service if voltage is normal and message persists
  cite:
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h198
    h: 60749c2f0bc9
  - src: src:sma-stpxx-us-50-be-en-14
    loc: sec=h384
    h: 60749c2f0bc9
  review: drafted
---
