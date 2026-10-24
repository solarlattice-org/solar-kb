---
id: func:high-voltage-ride-through
type: Function
name: High-voltage ride-through
aliases:
- HVRT
- DHVT
- High Voltage Ride Through (HVRT)
category: Grid support
function_kind: grid-support
claims:
- claim_id: c1
  rel: subclass_of
  target: func:voltage-ride-through
  note: HVRT is the high-voltage side of voltage ride-through; LVRT is the low-voltage side.
  cite:
  - src: src:schneider-conext-cl125-power-control-app-note
    loc: sec=h20
    h: c1568a5f209f
  review: drafted
- claim_id: c2
  attr: default_value
  value:
    nominal: 125
    unit: unit:PERCENT
  scope:
    products:
    - prod:yaskawa-solectria-pvi-20-25tl-480-r
  conditions: HVRTVoltPara first and second point, IEEE 1547-2018 and Rule 21 settings
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=24
    h: 5e694f669b55
  review: drafted
- claim_id: c3
  attr: default_value
  value:
    nominal: 0.16
    unit: unit:SEC
  scope:
    products:
    - prod:yaskawa-solectria-pvi-20-25tl-480-r
    standard: std:ieee-1547-2018
  conditions: HVRTTimePara second point, IEEE 1547-2018 setting
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=24
    h: 5e694f669b55
  review: drafted
- claim_id: c4
  attr: default_value
  value:
    nominal: 0.11
    unit: unit:SEC
  scope:
    products:
    - prod:yaskawa-solectria-pvi-20-25tl-480-r
    standard: std:cpuc-rule-21
  conditions: HVRTTimePara second point, Rule 21 setting
  cite:
  - src: src:yaskawa-pvi-20-25tl-480-r-iom-docr-071030-a
    loc: tbl=24
    h: 5e694f669b55
  review: drafted
- claim_id: c5
  attr: setting_range
  value:
    min: 100
    max: 135
    unit: unit:PERCENT
  scope:
    products:
    - prod:chint-sca-36ktl
    - prod:chint-sca-50-60ktl
    - prod:chint-sca-25ktl-208
  conditions: HVRTVolt first and second point, IEEE 1547-2018, Rule 21 and ISO-NE settings
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=13
    h: 56689c6ea97f
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=32
    h: 34660d291706
  review: drafted
- claim_id: c6
  attr: default_value
  value:
    nominal: 125
    unit: unit:PERCENT
  scope:
    products:
    - prod:chint-sca-36ktl
    - prod:chint-sca-50-60ktl
    - prod:chint-sca-25ktl-208
  conditions: HVRTVolt first and second point, IEEE 1547-2018 and Rule 21 settings
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=13
    h: 56689c6ea97f
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=32
    h: 34660d291706
  review: drafted
- claim_id: c7
  attr: default_value
  value:
    nominal: 120
    unit: unit:PERCENT
  scope:
    products:
    - prod:chint-sca-36ktl
    - prod:chint-sca-50-60ktl
    - prod:chint-sca-25ktl-208
    standard: std:iso-ne-bulk-system-area-settings
  conditions: HVRTVolt first and second point, ISO-NE setting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=13
    h: 56689c6ea97f
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=32
    h: 34660d291706
  review: drafted
- claim_id: c8
  attr: setting_range
  value:
    min: 0
    max: 655
    unit: unit:SEC
  scope:
    products:
    - prod:chint-sca-36ktl
    - prod:chint-sca-50-60ktl
    - prod:chint-sca-25ktl-208
  conditions: HVRTTime parameters points 1 to 8, all grid settings
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=13
    h: 56689c6ea97f
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=32
    h: 34660d291706
  review: drafted
- claim_id: c9
  attr: default_value
  value:
    nominal: 1.05
    unit: unit:SEC
  scope:
    products:
    - prod:chint-sca-36ktl
    - prod:chint-sca-50-60ktl
    - prod:chint-sca-25ktl-208
    standard: std:iso-ne-bulk-system-area-settings
  conditions: HVRTTime seventh and eighth point, ISO-NE setting
  cite:
  - src: src:chint-cps-sca36-50-60ktl-ops
    loc: tbl=13
    h: 56689c6ea97f
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=32
    h: 34660d291706
  review: drafted
- claim_id: c10
  attr: trip_threshold
  value:
    nominal: 1.1
    unit: unit:UNITLESS
  conditions: PPL EU OV1 shall-trip setting, per unit of nominal voltage; ride-through and trip curves
    overlap
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=3
    h: 55565681d7c1
  review: drafted
  review_note: possible conflict with c12 (same source; check the conditions)
- claim_id: c11
  attr: trip_time
  value:
    nominal: 2.1
    unit: unit:SEC
  conditions: PPL EU OV1 at 1.1 p.u.
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=3
    h: 55565681d7c1
  review: drafted
  review_note: possible conflict with c13 (same source; check the conditions)
- claim_id: c12
  attr: trip_threshold
  value:
    nominal: 1.2
    unit: unit:UNITLESS
  conditions: PPL EU OV2 shall-trip setting, per unit of nominal voltage
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=3
    h: 55565681d7c1
  review: drafted
  review_note: possible conflict with c10 (same source; check the conditions)
- claim_id: c13
  attr: trip_time
  value:
    nominal: 0.16
    unit: unit:SEC
  conditions: PPL EU OV2 at 1.2 p.u.
  cite:
  - src: src:std-standards-ieee-der-ride-through-settings
    loc: tbl=3
    h: 55565681d7c1
  review: drafted
  review_note: possible conflict with c11 (same source; check the conditions)
---
High-voltage ride-through lets an inverter or generator stay online and keep delivering output current while grid voltage is briefly above its preset high threshold, instead of tripping. Utilities can set their own limits. In PPL EU's settings, the high-voltage ride-through curve and the trip curve are the same.

<!-- review notes
- sentence 2: support check: partial - PPL EU ride-through and trip curves being identical is stated, but the general claim that utilities can set their own limits is only implied by the utility-specific settings and country-specific notes.
-->
