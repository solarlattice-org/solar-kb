---
id: func:low-voltage-ride-through
type: Function
name: Low-voltage ride-through
aliases:
- LVRT
- DLVT
category: Grid support
function_kind: grid-support
claims:
- claim_id: c1
  rel: part_of
  target: func:voltage-ride-through
  note: LVRT is the low-voltage side of voltage ride-through; HVRT is the high-voltage side.
  cite:
  - src: src:schneider-conext-cl125-power-control-app-note
    loc: sec=h20
    h: c1568a5f209f
  review: drafted
- claim_id: c2
  attr: trip_threshold
  value:
    nominal: 0.88
    unit: unit:UNITLESS
  scope:
    regions:
    - region:us-pa
    valid_from: '2023-11-30'
  conditions: PPL EU UV1 shall-trip setting, per unit of nominal voltage; shall ride-through and shall
    trip curves overlap
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=2
    h: 6b5ff525c1bf
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: sec=h12
    h: d057eb0e1b32
  review: drafted
  review_note: 'support check: partial - UV1 0.88 p.u. with overlapping curves is stated, but the region
    (PA) and effective date 11/30/2023 are only partly evidenced (PPL EU, rev 04 effective 11/30/2023;
    PA not stated).; possible conflict with c4 (same source; check the conditions)'
- claim_id: c3
  attr: trip_time
  value:
    nominal: 2.1
    unit: unit:SEC
  scope:
    regions:
    - region:us-pa
    valid_from: '2023-11-30'
  conditions: PPL EU UV1 shall-trip time at 0.88 p.u.
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=2
    h: 6b5ff525c1bf
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: sec=h12
    h: d057eb0e1b32
  review: drafted
  review_note: 'support check: partial - UV1 time 2.1 s at 0.88 p.u. is in the table; the Pennsylvania
    scope is not stated, though the effective date matches.; possible conflict with c5 (same source; check
    the conditions)'
- claim_id: c4
  attr: trip_threshold
  value:
    nominal: 0.5
    unit: unit:UNITLESS
  scope:
    regions:
    - region:us-pa
    valid_from: '2023-11-30'
  conditions: PPL EU UV2 shall-trip setting, per unit of nominal voltage
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=2
    h: 6b5ff525c1bf
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: sec=h12
    h: d057eb0e1b32
  review: drafted
  review_note: 'support check: partial - UV2 0.5 p.u. is in the table; the Pennsylvania region is not
    stated.; possible conflict with c2 (same source; check the conditions)'
- claim_id: c5
  attr: trip_time
  value:
    nominal: 0.6
    unit: unit:SEC
  scope:
    regions:
    - region:us-pa
    valid_from: '2023-11-30'
  conditions: PPL EU UV2 shall-trip time at 0.5 p.u.
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=2
    h: 6b5ff525c1bf
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: sec=h12
    h: d057eb0e1b32
  review: drafted
  review_note: 'support check: partial - UV2 time 0.6 s at 0.5 p.u. is in the table; the Pennsylvania
    region is not stated.; possible conflict with c3 (same source; check the conditions)'
- claim_id: c6
  attr: setting_range
  value:
    min: 0
    max: 100
    unit: unit:PERCENT
  scope:
    products:
    - prod:chint-sca-36ktl
    - prod:chint-sca-50-60ktl
  conditions: LVRTVolt threshold points 1 to 8, IEEE 1547-2018, Rule 21 and ISO-NE settings
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=12
    h: f8e320e808dc
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=36
    h: f8e320e808dc
  review: drafted
  review_note: 'support check: partial - The table gives 0-100 % for LVRTVolt in all three settings, but
    the passages do not name the Chint products.'
- claim_id: c7
  attr: setting_range
  value:
    min: 0
    max: 655
    unit: unit:SEC
  scope:
    products:
    - prod:chint-sca-36ktl
    - prod:chint-sca-50-60ktl
  conditions: LVRTTime points 1 to 8, IEEE 1547-2018, Rule 21 and ISO-NE settings
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=12
    h: f8e320e808dc
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=36
    h: f8e320e808dc
  review: drafted
  review_note: 'support check: partial - The table gives 0-655 s for LVRTTime, but the passages do not
    name the Chint products.'
- claim_id: c8
  attr: default_value
  value:
    nominal: 50
    unit: unit:PERCENT
  scope:
    products:
    - prod:chint-sca-36ktl
    - prod:chint-sca-50-60ktl
  conditions: LVRTVolt points 3 and 4, IEEE 1547-2018 and Rule 21 settings
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=12
    h: f8e320e808dc
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=36
    h: f8e320e808dc
  review: drafted
  review_note: 'support check: partial - Default 50 % for LVRTVolt (3,4) under IEEE1547-2018 and Rule21
    is in the table; the products are not named.; possible conflict with c9 (same source; check the conditions);
    possible conflict with c10 (same source; check the conditions)'
- claim_id: c9
  attr: default_value
  value:
    nominal: 70
    unit: unit:PERCENT
  scope:
    products:
    - prod:chint-sca-36ktl
    - prod:chint-sca-50-60ktl
  conditions: LVRTVolt points 5 and 6, IEEE 1547-2018 and Rule 21 settings
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=12
    h: f8e320e808dc
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=36
    h: f8e320e808dc
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=12.r5
    h: 44ecb07b86bb
  review: drafted
  review_note: 'support check: partial - Default 70 % for LVRTVolt (5,6) under IEEE1547-2018 and Rule21
    is in the table; the products are not named.; possible conflict with c8 (same source; check the conditions);
    possible conflict with c10 (same source; check the conditions)'
- claim_id: c10
  attr: default_value
  value:
    nominal: 88
    unit: unit:PERCENT
  scope:
    products:
    - prod:chint-sca-36ktl
    - prod:chint-sca-50-60ktl
  conditions: LVRTVolt points 7 and 8, IEEE 1547-2018 and Rule 21 settings; also point 8 under ISO-NE
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=12
    h: f8e320e808dc
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=36
    h: f8e320e808dc
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=12.r7
    h: 44db7998dcb2
  review: drafted
  review_note: 'support check: partial - Default 88 % for LVRTVolt (7,8) under IEEE1547-2018 and Rule21,
    and 88 for ISO-NE point 8, are in the table; the products are not named.; possible conflict with c8
    (same source; check the conditions); possible conflict with c9 (same source; check the conditions)'
- claim_id: c11
  attr: default_value
  value:
    nominal: 20
    unit: unit:SEC
  scope:
    products:
    - prod:chint-sca-36ktl
    - prod:chint-sca-50-60ktl
    standard: std:ieee-1547-2018
  conditions: LVRTTime points 7 and 8, IEEE 1547-2018 setting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=12
    h: f8e320e808dc
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=36
    h: f8e320e808dc
  review: drafted
  review_note: 'support check: partial - IEEE1547-2018 default of 20 s for LVRTTime (7,8) is in the table;
    the products are not named.'
- claim_id: c12
  attr: default_value
  value:
    nominal: 20.5
    unit: unit:SEC
  scope:
    products:
    - prod:chint-sca-36ktl
    - prod:chint-sca-50-60ktl
    standard: std:cpuc-rule-21
  conditions: LVRTTime points 7 and 8, Rule 21 setting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=12
    h: f8e320e808dc
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=36
    h: f8e320e808dc
  review: drafted
  review_note: 'support check: partial - Rule21 default of 20.5 s for LVRTTime (7,8) is in the table;
    the products are not named.'
- claim_id: c13
  attr: default_value
  value:
    nominal: 3.05
    unit: unit:SEC
  scope:
    products:
    - prod:chint-sca-36ktl
    - prod:chint-sca-50-60ktl
    regions:
    - region:iso-ne
  conditions: LVRTTime point 7, ISO-NE setting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=12
    h: f8e320e808dc
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=36
    h: f8e320e808dc
  review: drafted
  review_note: 'support check: partial - ISO-NE default of 3.05 s for point 7 is in the table; the products
    are not named.; possible conflict with c14 (same source; check the conditions)'
- claim_id: c14
  attr: default_value
  value:
    nominal: 3.25
    unit: unit:SEC
  scope:
    products:
    - prod:chint-sca-36ktl
    - prod:chint-sca-50-60ktl
    regions:
    - region:iso-ne
  conditions: LVRTTime point 8, ISO-NE setting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=12
    h: f8e320e808dc
  - src: src:chint-cps-sca36-50-60ktl-dous-480-user-manual-rev-4-0
    loc: tbl=36
    h: f8e320e808dc
  review: drafted
  review_note: 'support check: partial - ISO-NE default of 3.25 s for point 8 is in the table; the products
    are not named.; possible conflict with c13 (same source; check the conditions)'
---
Low-voltage ride-through keeps the inverter online and supplying output current when grid voltage briefly drops below a preset low threshold, so it does not disconnect. After the voltage dip, the inverter changes its reactive current reference according to the country-specific grid code. Utilities publish their own settings. For example, PPL EU sets its low-voltage shall ride-through and shall trip curves to be identical, with points UV1 and UV2.
