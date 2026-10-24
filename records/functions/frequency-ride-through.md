---
id: func:frequency-ride-through
type: Function
name: Frequency ride-through
aliases:
- LFRT/HFRT
- LFRT
- HFRT
- Low/High Frequency Ride-Through
- FRT_US
category: Grid support
function_kind: grid-support
claims:
- claim_id: c1
  attr: trip_threshold
  value:
    nominal: 58.5
    unit: unit:HZ
  conditions: PPL EU required under-frequency shall-trip setting UF1
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=4
    h: d45e5447a687
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=4.r3
    h: 51e8170b07de
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c5
    (same source; check the conditions); possible conflict with c7 (same source; check the conditions)
- claim_id: c2
  attr: trip_time
  value:
    nominal: 301
    unit: unit:SEC
  conditions: PPL EU UF1 clearing time at 58.5 Hz
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=4
    h: d45e5447a687
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=4.r3
    h: 51e8170b07de
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions); possible conflict with c8
    (same source; check the conditions)
- claim_id: c3
  attr: trip_threshold
  value:
    nominal: 56.5
    unit: unit:HZ
  conditions: PPL EU required under-frequency shall-trip setting UF2
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=4
    h: d45e5447a687
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=4.r4
    h: 3392dc7c64a1
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c5
    (same source; check the conditions); possible conflict with c7 (same source; check the conditions)
- claim_id: c4
  attr: trip_time
  value:
    nominal: 0.2
    unit: unit:SEC
  conditions: PPL EU UF2 clearing time at 56.5 Hz
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=4
    h: d45e5447a687
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=4.r4
    h: 3392dc7c64a1
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c6
    (same source; check the conditions)
- claim_id: c5
  attr: trip_threshold
  value:
    nominal: 61.2
    unit: unit:HZ
  conditions: PPL EU required over-frequency shall-trip setting OF1
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=5
    h: 356df394eec9
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c7 (same source; check the conditions)
- claim_id: c6
  attr: trip_time
  value:
    nominal: 301
    unit: unit:SEC
  conditions: PPL EU OF1 clearing time at 61.2 Hz
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=5
    h: 356df394eec9
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions); possible conflict with c8
    (same source; check the conditions)
- claim_id: c7
  attr: trip_threshold
  value:
    nominal: 62
    unit: unit:HZ
  conditions: PPL EU required over-frequency shall-trip setting OF2
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=5
    h: 356df394eec9
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=5.r4
    h: 4eda35ca959e
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c5 (same source; check the conditions)
- claim_id: c8
  attr: trip_time
  value:
    nominal: 0.2
    unit: unit:SEC
  conditions: PPL EU OF2 clearing time at 62 Hz
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=5
    h: 356df394eec9
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=5.r4
    h: 4eda35ca959e
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c6
    (same source; check the conditions)
- claim_id: c9
  attr: setting_range
  value:
    min: 0
    max: 10
    unit: unit:NUM
  scope:
    products:
    - prod:yaskawa-solectria-sgi-500-750xtm
  conditions: Number of LFRT or HFRT ordered pairs (registers offset 426 and 467)
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: tbl=32
    h: eb9042cdfdf8
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: sec=4.2.9
    h: 6725a5e5cc15
  review: drafted
- claim_id: c10
  attr: default_value
  value:
    nominal: 2
    unit: unit:NUM
  scope:
    products:
    - prod:yaskawa-solectria-sgi-500-750xtm
  conditions: Factory default number of LFRT and of HFRT ordered pairs
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: tbl=32
    h: eb9042cdfdf8
  review: drafted
- claim_id: c11
  attr: trip_time
  value:
    min: 1
    unit: unit:SEC
  scope:
    products:
    - prod:yaskawa-solectria-sgi-500-750xtm
  conditions: Minimum time required to trip on abnormal frequency, firmware D002
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: sec=4.2.9
    h: 6725a5e5cc15
  review: drafted
- claim_id: c12
  attr: trip_time
  value:
    min: 0.5
    unit: unit:SEC
  scope:
    products:
    - prod:yaskawa-solectria-sgi-500-750xtm
  conditions: Minimum time required to trip on abnormal frequency, firmware D003
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: sec=4.2.9
    h: 6725a5e5cc15
  review: drafted
- claim_id: c13
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
- claim_id: c14
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
Frequency ride-through lets an inverter keep running through abnormally low or high grid frequency for a set time, and disconnect only if the excursion lasts longer than that delay. PPL EU publishes shall-trip settings for frequency ride-through: UF1 at 58.5 Hz and OF1 at 61.2 Hz, each with 301 s clearing, plus UF2 at 56.5 Hz and OF2 at 62 Hz, each with 0.2 s clearing. On the Solectria SGI XTM, LFRT and HFRT are set over Modbus with up to 10 ordered pairs of frequency percent and time. Each can be enabled on its own, and once enabled it overrides the UL1741/IEEE1547 frequency protection setpoints.

<!-- review notes
- sentence 3: support check: partial - Ordered pairs (up to 10), separate enabling and override of UL1741/IEEE1547 setpoints are stated, and registers are Modbus-style offsets, but Modbus is never explicitly named.
-->
