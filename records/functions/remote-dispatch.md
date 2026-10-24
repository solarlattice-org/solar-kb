---
id: func:remote-dispatch
type: Function
name: Remote dispatch
aliases:
- VPP dispatch mode
- aggregator control
- remote control
- Remote dispatch mode
- Remote electric dispatch
- Remote communication control
category: Energy management
function_kind: energy-management
claims:
- claim_id: c1
  attr: default_value
  value:
    nominal: 0
    unit: unit:UNITLESS
  scope:
    products:
    - prod:chint-sch-350ktl
  conditions: RemoteControlEn parameter, same default under the IEEE 1547-2018, Rule 21 and ISO-NE grid
    codes; 0 means dispatch mode disabled
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=29.r3
    h: 5d472d47048c
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions)
- claim_id: c2
  attr: setting_range
  value:
    min: 0
    max: 1
    unit: unit:UNITLESS
  scope:
    products:
    - prod:chint-sch-350ktl
  conditions: RemoteControlEn parameter under the IEEE 1547-2018, Rule 21 and ISO-NE grid codes
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=29.r3
    h: 5d472d47048c
  review: drafted
- claim_id: c3
  attr: default_value
  value:
    nominal: 0
    unit: unit:UNITLESS
  scope:
    products:
    - prod:yaskawa-solectria-pvi-50-60tl
  conditions: CTRMODE active power control mode (0 disable dispatch, 1 remote dispatch, 2 local control)
  cite:
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: tbl=37.r7
    h: e2da73b41355
  review: drafted
  review_note: 'support check: partial - Evidence shows CTRMODE default 0 but columns are unlabeled and
    the product/grid-code context is not explicit; the 0/1/2 meanings are stated.'
- claim_id: c4
  attr: setting_range
  value:
    min: 0
    max: 2
    unit: unit:UNITLESS
  scope:
    products:
    - prod:yaskawa-solectria-pvi-50-60tl
  conditions: CTRMODE active power control mode (0 disable dispatch, 1 remote dispatch, 2 local control)
  cite:
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: tbl=37.r7
    h: e2da73b41355
  review: drafted
  review_note: 'support check: partial - Range 0 to 2 appears with the mode meanings, but the columns
    are unlabeled, so the min/max assignment is implied rather than stated.'
- claim_id: c5
  attr: setting_range
  value:
    min: 0
    max: 110
    unit: unit:PERCENT
  scope:
    products:
    - prod:chint-sch-350ktl
  conditions: PSet remote electric dispatch active power setpoint, same under IEEE 1547-2018, Rule 21
    and ISO-NE
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=16
    h: 345e14c9f741
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c6
  attr: default_value
  value:
    nominal: 110
    unit: unit:PERCENT
  scope:
    products:
    - prod:chint-sch-350ktl
  conditions: PSet remote electric dispatch active power setpoint, same under IEEE 1547-2018, Rule 21
    and ISO-NE
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=16
    h: 345e14c9f741
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions)
- claim_id: c7
  attr: setting_range
  value:
    min: -60
    max: 60
    unit: unit:PERCENT
  scope:
    products:
    - prod:chint-sch-350ktl
  conditions: QSet remote electric dispatch reactive power setpoint, same under IEEE 1547-2018, Rule 21
    and ISO-NE
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=16
    h: 345e14c9f741
  review: drafted
- claim_id: c8
  attr: default_value
  value:
    nominal: 0
    unit: unit:PERCENT
  scope:
    products:
    - prod:chint-sch-350ktl
  conditions: QSet remote electric dispatch reactive power setpoint
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=16
    h: 345e14c9f741
  review: drafted
  review_note: possible conflict with c6 (same source; check the conditions)
- claim_id: c9
  attr: default_value
  value:
    nominal: 1
    unit: unit:UNITLESS
  scope:
    products:
    - prod:chint-sch-350ktl
  conditions: PFSet remote electric dispatch power factor setpoint
  cite:
  - src: src:chint-cps-sch350ktl-do-us-800-user-manual-rev-2-2
    loc: tbl=16
    h: 345e14c9f741
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions)
- claim_id: c10
  rel: requires
  target: proto:cellular
  note: Tesla SCADA design manual lists cellular as the standard remote connection for diagnostics and
    dispatch; VPN or jump server login is the alternative
  cite:
  - src: src:tesla-scada-design-manual-v3-4
    loc: tbl=6.r4
    h: 6aff85fd9f78
  - src: src:tesla-scada-design-manual-v3-4
    loc: tbl=6.r6
    h: f6bdfb0bdc56
  review: drafted
  review_note: 'support check: partial - Cellular is listed as the standard connection for diagnostics
    and dispatch, but VPN or jump server is an alternative, so cellular is not strictly required.; review:
    partial - The passages list cellular as the standard connection for diagnostics and dispatch with
    VPN/jump server as an alternative, so ''requires'' overstates it, though the note correctly mentions
    the alternative.'
- claim_id: c11
  rel: requires
  target: proto:modbus
  note: CPS inverters expose the remote dispatch enable and setpoints as Modbus registers
  cite:
  - src: src:chint-cps-350kw-modbus-map-2024-12-04
    loc: tbl=35.r4
    h: 15c48f67a955
  - src: src:chint-cps-25kw-480-modbus-map-fw-v5-00
    loc: tbl=57.r1
    h: 22919b17d429
  review: drafted
  review_note: 'support check: partial - Modbus-style registers exist for RemoteDispatchEn and setpoints,
    but the passages never name the Modbus protocol or say dispatch requires it.'
---
Remote dispatch lets an outside controller, such as monitoring or SCADA software, set an inverter's active power, reactive power or power factor instead of using locally stored values. On CPS inverters, a control mode parameter picks between disabled dispatch, remote dispatch and local control. This applies to active power and to reactive power. On older CPS 100kW units, ActivePower and PowerFactor can be set from the LCD for local dispatch or through remote monitoring software for remote dispatch. Tesla's SCADA design manual uses cellular as the standard connection for diagnostics and dispatch, with VPN or jump server remote login as the alternative.

<!-- review notes
- sentence 1: support check: partial - Remote monitoring software can adjust ActivePower and PowerFactor, but the passages do not mention reactive power or SCADA or say it replaces locally stored values.
- sentence 3: support check: partial - LCD and remote software setting of ActivePower and PowerFactor is stated, but the passages never mention 100kW units or that they are older.
- sentence 1: review: partial - Remote setting of active power, power factor and reactive power through monitoring software is supported, but SCADA is not mentioned and no passage frames remote dispatch as replacing locally stored values.
-->
