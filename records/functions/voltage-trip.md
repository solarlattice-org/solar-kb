---
id: func:voltage-trip
type: Function
name: Voltage trip
aliases:
- voltage protection
- must-trip voltage
- over/under-voltage trip
- PTOV
- PTUV
- Shall trip
- over-voltage trip point
- under-voltage trip point
category: Protection
function_kind: protection
claims:
- claim_id: c1
  attr: trip_threshold
  value:
    nominal: 1.2
    unit: unit:UNITLESS
  scope:
    standard: std:ieee-1547-2018
  conditions: OV2 shall-trip function, Category I and Category II; per-unit of nominal voltage; the setting
    is fixed at this value
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=19.r1
    h: 5c143f9ae2f4
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=18.r1
    h: 73372b6054b8
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c7
    (same source; check the conditions); possible conflict with c11 (same source; check the conditions);
    possible conflict with c15 (same source; check the conditions)
- claim_id: c2
  attr: trip_time
  value:
    nominal: 0.16
    unit: unit:SEC
  scope:
    standard: std:ieee-1547-2018
  conditions: OV2 clearing time, Category I and Category II; the setting is fixed at this value
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=19.r1
    h: 5c143f9ae2f4
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=18.r1
    h: 73372b6054b8
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions); possible conflict with c13
    (same source; check the conditions); possible conflict with c16 (same source; check the conditions)
- claim_id: c3
  attr: trip_threshold
  value:
    nominal: 1.1
    unit: unit:UNITLESS
  scope:
    standard: std:ieee-1547-2018
  conditions: OV1 default setting, Category I and Category II; per-unit of nominal voltage
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=19.r2
    h: f1a5814871d8
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=18.r2
    h: c1b4d59b7164
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c7
    (same source; check the conditions); possible conflict with c11 (same source; check the conditions);
    possible conflict with c15 (same source; check the conditions)
- claim_id: c4
  attr: setting_range
  value:
    min: 1.1
    max: 1.2
    unit: unit:UNITLESS
  scope:
    standard: std:ieee-1547-2018
  conditions: OV1 allowable voltage settings, Category I and Category II; per-unit of nominal voltage
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=19.r2
    h: f1a5814871d8
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=18.r2
    h: c1b4d59b7164
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c8 (same source; check the conditions); possible conflict with c12
    (same source; check the conditions)
- claim_id: c5
  attr: trip_time
  value:
    nominal: 2
    unit: unit:SEC
  scope:
    standard: std:ieee-1547-2018
  conditions: OV1 default clearing time, Category I and Category II
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=19.r2
    h: f1a5814871d8
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=18.r2
    h: c1b4d59b7164
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c9
    (same source; check the conditions); possible conflict with c13 (same source; check the conditions)
- claim_id: c6
  attr: setting_range
  value:
    min: 1
    max: 13
    unit: unit:SEC
  scope:
    standard: std:ieee-1547-2018
  conditions: OV1 allowable clearing time settings, Category I and Category II
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=19.r2
    h: f1a5814871d8
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=18.r2
    h: c1b4d59b7164
  review: drafted
- claim_id: c7
  attr: trip_threshold
  value:
    nominal: 0.45
    unit: unit:UNITLESS
  scope:
    standard: std:ieee-1547-2018
  conditions: UV2 default setting, Category I and Category II; per-unit of nominal voltage
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=18.r4
    h: aa8a5dcb31de
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=19.r4
    h: c4ac5639a44b
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c11 (same source; check the conditions);
    possible conflict with c15 (same source; check the conditions)
- claim_id: c8
  attr: setting_range
  value:
    min: 0
    max: 0.5
    unit: unit:UNITLESS
  scope:
    standard: std:ieee-1547-2018
  conditions: UV2 allowable voltage settings, Category I, II and III; per-unit of nominal voltage
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=18.r4
    h: aa8a5dcb31de
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=19.r4
    h: c4ac5639a44b
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=20.r4
    h: 640aaa0fcf7b
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions)
- claim_id: c9
  attr: trip_time
  value:
    nominal: 0.16
    unit: unit:SEC
  scope:
    standard: std:ieee-1547-2018
  conditions: UV2 default clearing time, Category I and Category II
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=18.r4
    h: aa8a5dcb31de
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=19.r4
    h: c4ac5639a44b
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c5 (same source; check the conditions); possible conflict with c13
    (same source; check the conditions); possible conflict with c16 (same source; check the conditions)
- claim_id: c10
  attr: setting_range
  value:
    min: 0.16
    max: 2
    unit: unit:SEC
  scope:
    standard: std:ieee-1547-2018
  conditions: UV2 allowable clearing time settings, Category I and Category II
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=18.r4
    h: aa8a5dcb31de
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=19.r4
    h: c4ac5639a44b
  review: drafted
- claim_id: c11
  attr: trip_threshold
  value:
    nominal: 0.7
    unit: unit:UNITLESS
  scope:
    standard: std:ieee-1547-2018
  conditions: UV1 default setting, Category II; per-unit of nominal voltage
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=19.r3
    h: 62c793611f12
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c7 (same source; check the conditions);
    possible conflict with c15 (same source; check the conditions)
- claim_id: c12
  attr: setting_range
  value:
    min: 0
    max: 0.88
    unit: unit:UNITLESS
  scope:
    standard: std:ieee-1547-2018
  conditions: UV1 allowable voltage settings, Category II; per-unit of nominal voltage
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=19.r3
    h: 62c793611f12
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions)
- claim_id: c13
  attr: trip_time
  value:
    nominal: 10
    unit: unit:SEC
  scope:
    standard: std:ieee-1547-2018
  conditions: UV1 default clearing time, Category II
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=19.r3
    h: 62c793611f12
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c5
    (same source; check the conditions); possible conflict with c9 (same source; check the conditions);
    possible conflict with c16 (same source; check the conditions)
- claim_id: c14
  attr: setting_range
  value:
    min: 2
    max: 21
    unit: unit:SEC
  scope:
    standard: std:ieee-1547-2018
  conditions: UV1 allowable clearing time settings, Category II; also UV2 clearing time range in Category
    III
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=19.r3
    h: 62c793611f12
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=20.r4
    h: 640aaa0fcf7b
  review: drafted
- claim_id: c15
  attr: trip_threshold
  value:
    nominal: 0.5
    unit: unit:UNITLESS
  scope:
    standard: std:ieee-1547-2018
  conditions: UV2 default setting, Category III; per-unit of nominal voltage
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=20.r4
    h: 640aaa0fcf7b
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions); possible conflict with c7 (same source; check the conditions);
    possible conflict with c11 (same source; check the conditions)
- claim_id: c16
  attr: trip_time
  value:
    nominal: 2
    unit: unit:SEC
  scope:
    standard: std:ieee-1547-2018
  conditions: UV2 default clearing time, Category III
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=20.r4
    h: 640aaa0fcf7b
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c9
    (same source; check the conditions); possible conflict with c13 (same source; check the conditions)
- claim_id: c17
  attr: trip_threshold
  value:
    nominal: 1.1
    unit: unit:UNITLESS
  conditions: PPL EU required OV1 shall-trip setting; per-unit of nominal voltage
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=3
    h: 55565681d7c1
  review: drafted
  review_note: possible conflict with c19 (same source; check the conditions); possible conflict with
    c21 (same source; check the conditions); possible conflict with c23 (same source; check the conditions)
- claim_id: c18
  attr: trip_time
  value:
    nominal: 2.1
    unit: unit:SEC
  conditions: PPL EU required OV1 shall-trip time
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=3
    h: 55565681d7c1
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c20 (same source; check the conditions); possible conflict with
    c24 (same source; check the conditions)
- claim_id: c19
  attr: trip_threshold
  value:
    nominal: 1.2
    unit: unit:UNITLESS
  conditions: PPL EU required OV2 shall-trip setting; per-unit of nominal voltage
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=3
    h: 55565681d7c1
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c17 (same source; check the conditions); possible conflict with
    c21 (same source; check the conditions); possible conflict with c23 (same source; check the conditions)
- claim_id: c20
  attr: trip_time
  value:
    nominal: 0.16
    unit: unit:SEC
  conditions: PPL EU required OV2 shall-trip time
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=3
    h: 55565681d7c1
  review: drafted
  review_note: possible conflict with c18 (same source; check the conditions); possible conflict with
    c22 (same source; check the conditions); possible conflict with c24 (same source; check the conditions)
- claim_id: c21
  attr: trip_threshold
  value:
    nominal: 0.88
    unit: unit:UNITLESS
  conditions: PPL EU required UV1 shall-trip setting; per-unit of nominal voltage
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=2
    h: 6b5ff525c1bf
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c17 (same source; check the conditions); possible conflict with
    c19 (same source; check the conditions); possible conflict with c23 (same source; check the conditions)
- claim_id: c22
  attr: trip_time
  value:
    nominal: 2.1
    unit: unit:SEC
  conditions: PPL EU required UV1 shall-trip time
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=2
    h: 6b5ff525c1bf
  review: drafted
  review_note: possible conflict with c20 (same source; check the conditions); possible conflict with
    c24 (same source; check the conditions)
- claim_id: c23
  attr: trip_threshold
  value:
    nominal: 0.5
    unit: unit:UNITLESS
  conditions: PPL EU required UV2 shall-trip setting; per-unit of nominal voltage
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=2.r2
    h: 5e826887ed83
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=2
    h: 6b5ff525c1bf
  review: drafted
  review_note: possible conflict with c17 (same source; check the conditions); possible conflict with
    c19 (same source; check the conditions); possible conflict with c21 (same source; check the conditions)
- claim_id: c24
  attr: trip_time
  value:
    nominal: 0.6
    unit: unit:SEC
  conditions: PPL EU required UV2 shall-trip time
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=2.r2
    h: 5e826887ed83
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=2
    h: 6b5ff525c1bf
  review: drafted
  review_note: possible conflict with c18 (same source; check the conditions); possible conflict with
    c20 (same source; check the conditions); possible conflict with c22 (same source; check the conditions)
- claim_id: c25
  attr: default_value
  value:
    nominal: 110
    unit: unit:PERCENT
  scope:
    products:
    - prod:chint-sca-50-100k-t
  conditions: GridVoltMax1 (level 1 overvoltage) in IEEE 1547, Rule 21 and ISO-NE profiles
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=21
    h: 07e294ff20a2
  review: drafted
  review_note: possible conflict with c30 (same source; check the conditions); possible conflict with
    c33 (same source; check the conditions)
- claim_id: c26
  attr: setting_range
  value:
    min: 0
    max: 655
    unit: unit:SEC
  scope:
    products:
    - prod:chint-sca-50-100k-t
  conditions: VoltMaxTripT1/T2/T3 overvoltage trip times
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=21
    h: 07e294ff20a2
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c27
  attr: trip_time
  value:
    nominal: 13
    unit: unit:SEC
  scope:
    products:
    - prod:chint-sca-50-100k-t
    standard: std:ieee-1547
  conditions: VoltMaxTripT1, IEEE 1547 profile
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=21
    h: 07e294ff20a2
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c28
  attr: trip_time
  value:
    nominal: 12.5
    unit: unit:SEC
  scope:
    products:
    - prod:chint-sca-50-100k-t
    standard: std:cpuc-rule-21
  conditions: VoltMaxTripT1, Rule 21 profile
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=21
    h: 07e294ff20a2
  review: drafted
- claim_id: c29
  attr: trip_time
  value:
    nominal: 2
    unit: unit:SEC
  scope:
    products:
    - prod:chint-sca-50-100k-t
  conditions: VoltMaxTripT1, ISO-NE profile
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=21
    h: 07e294ff20a2
  review: drafted
  review_note: possible conflict with c31 (same source; check the conditions)
- claim_id: c30
  attr: default_value
  value:
    nominal: 120
    unit: unit:PERCENT
  scope:
    products:
    - prod:chint-sca-50-100k-t
  conditions: GridVoltMax2 and GridVoltMax3 in IEEE 1547, Rule 21 and ISO-NE profiles
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=21
    h: 07e294ff20a2
  review: drafted
  review_note: possible conflict with c25 (same source; check the conditions); possible conflict with
    c33 (same source; check the conditions)
- claim_id: c31
  attr: trip_time
  value:
    nominal: 0.16
    unit: unit:SEC
  scope:
    products:
    - prod:chint-sca-50-100k-t
  conditions: VoltMaxTripT2 and VoltMaxTripT3 in IEEE 1547, Rule 21 and ISO-NE profiles
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=21
    h: 07e294ff20a2
  review: drafted
  review_note: possible conflict with c29 (same source; check the conditions)
- claim_id: c32
  attr: setting_range
  value:
    min: 0
    max: 100
    unit: unit:PERCENT
  scope:
    products:
    - prod:chint-sca-50-100k-t
  conditions: GridVoltMin1 level 1 undervoltage trip value, percent of nominal
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=21
    h: 07e294ff20a2
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c33
  attr: default_value
  value:
    nominal: 88
    unit: unit:PERCENT
  scope:
    products:
    - prod:chint-sca-50-100k-t
  conditions: GridVoltMin1 in IEEE 1547, Rule 21 and ISO-NE profiles
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=21
    h: 07e294ff20a2
  review: drafted
  review_note: possible conflict with c25 (same source; check the conditions); possible conflict with
    c30 (same source; check the conditions)
- claim_id: c34
  attr: trip_threshold
  value:
    nominal: 110
    unit: unit:PERCENT
  scope:
    products:
    - prod:generac-pwrmicro
  conditions: OV1 voltage trip, percent of nominal, Generac PWRmicro
  cite:
  - src: src:generac-generac-pwrmicro-installation-manual-a0008718926
    loc: tbl=20.r2
    h: 4df42ceedb23
  review: drafted
- claim_id: c35
  attr: trip_time
  value:
    nominal: 13
    unit: unit:SEC
  scope:
    products:
    - prod:generac-pwrmicro
  conditions: OV1 clearing time, Generac PWRmicro
  cite:
  - src: src:generac-generac-pwrmicro-installation-manual-a0008718926
    loc: tbl=20.r2
    h: 4df42ceedb23
  review: drafted
---
Voltage trip disconnects the inverter from the grid when the voltage stays outside set overvoltage or undervoltage limits for longer than the set clearing time. Utilities can require their own settings. For example, PPL EU sets OV1 at 1.1 p.u. with a 2.1 s trip time and UV2 at 0.5 p.u. with a 0.6 s trip time.

<!-- review notes
- sentence 1: support check: partial - The passages show overvoltage and undervoltage trip thresholds with clearing times and a disconnection due to under-voltage. They do not explicitly describe the mechanism of disconnecting when the voltage stays outside limits for longer than the clearing time.
-->
