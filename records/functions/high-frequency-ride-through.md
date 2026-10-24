---
id: func:high-frequency-ride-through
type: Function
name: High-frequency ride-through
aliases:
- HFRT
- DHFT
category: Grid support
function_kind: grid-support
claims:
- claim_id: c1
  rel: part_of
  target: func:frequency-ride-through
  note: The Yaskawa frequency ride-through function covers both low (LFRT) and high (HFRT) frequency conditions,
    and each can be enabled on its own.
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: sec=4.2.9
    h: 6725a5e5cc15
  review: drafted
- claim_id: c2
  attr: trip_threshold
  value:
    nominal: 61.2
    unit: unit:HZ
  conditions: PPL EU required over-frequency setting OF1 (shall trip)
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=5
    h: 356df394eec9
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions)
- claim_id: c3
  attr: trip_time
  value:
    nominal: 301
    unit: unit:SEC
  conditions: PPL EU over-frequency setting OF1 clearing time at 61.2 Hz
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=5
    h: 356df394eec9
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions)
- claim_id: c4
  attr: trip_threshold
  value:
    nominal: 62
    unit: unit:HZ
  conditions: PPL EU required over-frequency setting OF2 (shall trip)
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=5
    h: 356df394eec9
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions)
- claim_id: c5
  attr: trip_time
  value:
    nominal: 0.2
    unit: unit:SEC
  conditions: PPL EU over-frequency setting OF2 clearing time at 62 Hz
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=5
    h: 356df394eec9
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions)
- claim_id: c6
  attr: setting_range
  value:
    max: 10
    unit: unit:NUM
  scope:
    products:
    - prod:yaskawa-solectria-sgi-500-750xtm
  conditions: Number of [%Frequency, Time] ordered pairs that define the HFRT must-ride-through curve
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: sec=4.2.9
    h: 6725a5e5cc15
  review: drafted
- claim_id: c7
  attr: trip_time
  value:
    min: 1
    unit: unit:SEC
  scope:
    products:
    - prod:yaskawa-solectria-sgi-500-750xtm
  conditions: Minimum time to trip on abnormal frequency, firmware D002
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: sec=4.2.9
    h: 6725a5e5cc15
  review: drafted
- claim_id: c8
  attr: trip_time
  value:
    min: 0.5
    unit: unit:SEC
  scope:
    products:
    - prod:yaskawa-solectria-sgi-500-750xtm
  conditions: Minimum time to trip on abnormal frequency, firmware D003
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: sec=4.2.9
    h: 6725a5e5cc15
  review: drafted
- claim_id: c9
  attr: response_time
  value:
    max: 500
    unit: unit:MilliSEC
  scope:
    products:
    - prod:yaskawa-solectria-sgi-500-750xtm
  conditions: Recovery after a frequency event when the inverter was not required to trip
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: sec=4.2.9
    h: 6725a5e5cc15
  review: drafted
- claim_id: c10
  attr: response_time
  value:
    max: 2
    unit: unit:SEC
  scope:
    products:
    - prod:yaskawa-solectria-sgi-500-750xtm
  conditions: Time to reach full output power after momentary cessation, firmware D003
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: sec=4.2.9
    h: 6725a5e5cc15
  review: drafted
---
High-frequency ride-through keeps a DER connected and in sync with the grid during a temporary over-frequency disturbance, so it does not trip right away. On the Yaskawa SGI XTM, you set up HFRT over Modbus: control, trigger and status bits, an ordered-pair count, and up to 10 frequency and time points that define the must-ride-through curve. When HFRT is enabled on the SGI XTM, it overrides the UL1741/IEEE1547 over-frequency protection setpoints. It can be enabled separately from LFRT. The inverter keeps exporting power while it is inside the time window. It stops producing only if frequency stays past the setpoint for longer than the set time. Above 70 Hz it goes into momentary cessation and risks damage. PPL EU over-frequency settings use OF1 at 61.2 Hz with a 301 s clearing time and OF2 at 62 Hz with a 0.2 s clearing time.

<!-- review notes
- sentence 1: support check: partial - Ride-through and maintaining synchronism during over-frequency are stated, but the 'does not trip right away' wording is only implied and the definition is general.
- sentence 4: support check: partial - Export during window and cessation only after exceeding time are stated, and cessation and damage warning above 70 Hz are stated, but the damage is 'may result' and the 69.5 Hz D002 threshold differs.
-->
