---
id: func:low-frequency-ride-through
type: Function
name: Low-frequency ride-through
aliases:
- LFRT
- DLFT
category: Grid support
function_kind: grid-support
claims:
- claim_id: c1
  rel: part_of
  target: func:frequency-ride-through
  note: Yaskawa describes frequency ride-through as covering low (LFRT) and high (HFRT) frequency conditions,
    and the two can be enabled separately.
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: sec=4.2.9
    h: 6725a5e5cc15
  review: drafted
- claim_id: c2
  attr: trip_threshold
  value:
    nominal: 58.5
    unit: unit:HZ
  scope:
    valid_from: '2023-11-30'
  conditions: PPL EU required under-frequency shall-trip setting UF1
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=4
    h: d45e5447a687
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: sec=h16
    h: 10cf6c57a237
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions)
- claim_id: c3
  attr: trip_time
  value:
    nominal: 301
    unit: unit:SEC
  scope:
    valid_from: '2023-11-30'
  conditions: PPL EU UF1 clearing time at 58.5 Hz
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=4
    h: d45e5447a687
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: sec=h16
    h: 10cf6c57a237
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions)
- claim_id: c4
  attr: trip_threshold
  value:
    nominal: 56.5
    unit: unit:HZ
  scope:
    valid_from: '2023-11-30'
  conditions: PPL EU required under-frequency shall-trip setting UF2
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=4
    h: d45e5447a687
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: sec=h16
    h: 10cf6c57a237
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions)
- claim_id: c5
  attr: trip_time
  value:
    nominal: 0.2
    unit: unit:SEC
  scope:
    valid_from: '2023-11-30'
  conditions: PPL EU UF2 clearing time at 56.5 Hz
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=4
    h: d45e5447a687
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: sec=h16
    h: 10cf6c57a237
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
  review_note: possible conflict with c3 (same source; check the conditions)
- claim_id: c6
  attr: setting_range
  value:
    max: 10
    unit: unit:NUM
  scope:
    products:
    - prod:yaskawa-solectria-sgi-500-750xtm
  conditions: Number of [%Frequency, Time] ordered pairs defining the LFRT must-ride-through curve on
    Yaskawa SGI XTM
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: sec=4.2.9
    h: 6725a5e5cc15
  review: drafted
- claim_id: c7
  attr: trip_time
  value:
    nominal: 1
    unit: unit:SEC
  scope:
    products:
    - prod:yaskawa-solectria-sgi-500-750xtm
  conditions: Minimum time for the Yaskawa SGI XTM to trip on abnormal frequency, firmware D002
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: sec=4.2.9
    h: 6725a5e5cc15
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions)
- claim_id: c8
  attr: trip_time
  value:
    nominal: 0.5
    unit: unit:SEC
  scope:
    products:
    - prod:yaskawa-solectria-sgi-500-750xtm
  conditions: Minimum time for the Yaskawa SGI XTM to trip on abnormal frequency, firmware D003
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: sec=4.2.9
    h: 6725a5e5cc15
  review: drafted
  review_note: possible conflict with c7 (same source; check the conditions)
- claim_id: c9
  attr: response_time
  value:
    max: 500
    unit: unit:MilliSEC
  scope:
    products:
    - prod:yaskawa-solectria-sgi-500-750xtm
  conditions: Yaskawa SGI XTM recovery after an abnormal frequency event that did not require a trip
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: sec=4.2.9
    h: 6725a5e5cc15
  review: drafted
  review_note: 'support check: partial - Passage says it will recover within 500 ms if not required to
    trip; this matches ''up to 500 ms'', though it is not specific to low frequency, which is minor.'
- claim_id: c10
  attr: response_time
  value:
    max: 2
    unit: unit:SEC
  scope:
    products:
    - prod:yaskawa-solectria-sgi-500-750xtm
  conditions: Yaskawa SGI XTM time to reach full output power after momentary cessation, firmware D003
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: sec=4.2.9
    h: 6725a5e5cc15
  review: drafted
---
Low-frequency ride-through keeps a DER online and synchronized with the grid during a temporary underfrequency event, rather than tripping straight away. During such an event the DER must not reduce active power below the value set for its performance category, though output may drop in proportion to grid voltage if the voltage is below the continuous operating level. The Eversource CT technical requirements apply no ride-through requirements below 57.0 Hz. PPL EU's required under-frequency settings, effective 11/30/2023, are a 58.5 Hz trip with a 301 s clearing time and a 56.5 Hz trip with a 0.2 s clearing time. On the Yaskawa SGI XTM, LFRT is set over Modbus with up to 10 [%Frequency, Time] points that define the must-ride-through curve. Enter the points in ascending time order, then enable and trigger the function using bit 1 of the control and trigger registers. When LFRT is enabled on the SGI XTM, it overrides the UL1741/IEEE1547 under-frequency protection setpoints. The over-frequency setpoints stay unchanged unless HFRT is also enabled.

<!-- review notes
- sentence 1: support check: partial - Ride-through is defined as withstanding disturbances and the IEEE text requires maintaining synchronism, but 'staying online rather than tripping straight away' is only implied.
-->
