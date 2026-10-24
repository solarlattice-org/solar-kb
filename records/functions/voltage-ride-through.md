---
id: func:voltage-ride-through
type: Function
name: Voltage ride-through
aliases:
- LVRT/HVRT
- fault ride-through
- FRT
- DVRT
category: Grid support
function_kind: grid-support
claims:
- claim_id: c1
  attr: trip_threshold
  value:
    nominal: 0.88
    unit: unit:UNITLESS
  scope:
    valid_from: '2023-11-30'
  conditions: PPL EU UV1 shall-trip setting, in per unit of nominal voltage; ride-through and trip curves
    overlap
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=2
    h: 6b5ff525c1bf
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=2.r1
    h: 557f3bf8ba1f
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: sec=h12
    h: d057eb0e1b32
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c5
    (same source; check the conditions); possible conflict with c7 (same source; check the conditions)
- claim_id: c2
  attr: trip_time
  value:
    nominal: 2.1
    unit: unit:SEC
  scope:
    valid_from: '2023-11-30'
  conditions: PPL EU UV1 shall-trip time at 0.88 p.u.
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=2
    h: 6b5ff525c1bf
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=2.r1
    h: 557f3bf8ba1f
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: sec=h12
    h: d057eb0e1b32
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
  review_note: possible conflict with c4 (same source; check the conditions); possible conflict with c8
    (same source; check the conditions)
- claim_id: c3
  attr: trip_threshold
  value:
    nominal: 0.5
    unit: unit:UNITLESS
  scope:
    valid_from: '2023-11-30'
  conditions: PPL EU UV2 shall-trip setting, in per unit of nominal voltage
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=2
    h: 6b5ff525c1bf
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=2.r2
    h: 5e826887ed83
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: sec=h12
    h: d057eb0e1b32
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c5
    (same source; check the conditions); possible conflict with c7 (same source; check the conditions)
- claim_id: c4
  attr: trip_time
  value:
    nominal: 0.6
    unit: unit:SEC
  scope:
    valid_from: '2023-11-30'
  conditions: PPL EU UV2 shall-trip time at 0.5 p.u.
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=2
    h: 6b5ff525c1bf
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=2.r2
    h: 5e826887ed83
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: sec=h12
    h: d057eb0e1b32
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c6
    (same source; check the conditions); possible conflict with c8 (same source; check the conditions)
- claim_id: c5
  attr: trip_threshold
  value:
    nominal: 1.1
    unit: unit:UNITLESS
  scope:
    valid_from: '2023-11-30'
  conditions: PPL EU OV1 shall-trip setting, in per unit of nominal voltage; ride-through and trip curves
    overlap
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=3
    h: 55565681d7c1
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: sec=h12
    h: d057eb0e1b32
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c7 (same source; check the conditions)
- claim_id: c6
  attr: trip_time
  value:
    nominal: 2.1
    unit: unit:SEC
  scope:
    valid_from: '2023-11-30'
  conditions: PPL EU OV1 shall-trip time at 1.1 p.u.
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=3
    h: 55565681d7c1
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: sec=h12
    h: d057eb0e1b32
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions); possible conflict with c8
    (same source; check the conditions)
- claim_id: c7
  attr: trip_threshold
  value:
    nominal: 1.2
    unit: unit:UNITLESS
  scope:
    valid_from: '2023-11-30'
  conditions: PPL EU OV2 shall-trip setting, in per unit of nominal voltage
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=3
    h: 55565681d7c1
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: sec=h12
    h: d057eb0e1b32
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c5 (same source; check the conditions)
- claim_id: c8
  attr: trip_time
  value:
    nominal: 0.16
    unit: unit:SEC
  scope:
    valid_from: '2023-11-30'
  conditions: PPL EU OV2 shall-trip time at 1.2 p.u.
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=3
    h: 55565681d7c1
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: sec=h12
    h: d057eb0e1b32
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions); possible conflict with c6 (same source; check the conditions)
- claim_id: c9
  attr: default_value
  value:
    nominal: 10
    unit: unit:MIN
  conditions: SMA parameter FRT_T_U_AVG, the time window used to average pre-fault voltage
  cite:
  - src: src:sma-doc-265222
    loc: sec=4
    h: 40e2303a672a
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c10
  attr: default_value
  value:
    nominal: 0
    unit: unit:UNITLESS
  conditions: SMA parameter FRT_IQ_MODE; mode 0 selects the BDEW Iq(V) characteristic
  cite:
  - src: src:sma-doc-265222
    loc: sec=4
    h: 40e2303a672a
  review: drafted
---
Voltage ride-through lets an inverter stay online and keep delivering output current while grid voltage is briefly outside the normal deadband. A dip below the low threshold is low-voltage ride-through (LVRT), and a rise above the high threshold is high-voltage ride-through (HVRT). Utilities publish their own shall-trip and ride-through settings. In the PPL EU tables the ride-through curve and the trip curve are the same line. On SMA inverters, FRT_MODE selects one of six current feed-in modes, FRT_ULOW and FRT_UUP set the deadband, and FRT_U_BLK with FRT_T_BLK can set a blocking zone where generation stops.

<!-- review notes
- sentence 2: support check: partial - The passages support that the PPL EU ride-through and trip curves are identical. They do not state that utilities in general publish their own settings.
-->
