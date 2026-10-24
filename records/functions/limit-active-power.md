---
id: func:limit-active-power
type: Function
name: Limit maximum active power
aliases:
- active power limitation
- power limiting
- curtailment setpoint
- WMaxLimPct
- DWMX
- Set active power limit
- Active Power Limit
- Maximum Active Power Limit
- Active power limit ratio
category: Control
function_kind: control
claims:
- claim_id: c1
  rel: requires
  target: req:ieee-1547-2018-4-6-2
  note: Maximum Active Power setting range is referred to clause 4.6.2.
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=10.6.12
    h: b92b721087a4
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=47.r2
    h: 27491401308b
  review: drafted
- claim_id: c2
  rel: requires
  target: proto:sunspec-model-123
  scope:
    products:
    - prod:kaco-blueplanet-87-165-tl3
  note: External power limitation on the KACO blueplanet is set through WMaxLimPct and WMaxLim_Ena in
    SunSpec model 123.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: tbl=56
    h: 252010cdf85b
  review: drafted
- claim_id: c3
  rel: requires
  target: role:grid-guard-code-holder
  scope:
    products:
    - prod:sma-cluster-controller
  note: Setting inverters to accept Cluster Controller active power limitation setpoints requires installer
    login and an SMA Grid Guard code.
  cite:
  - src: src:sma-doc-240154
    loc: sec=h205
    h: c8f35fb9a618
  review: drafted
  review_note: 'support check: partial - Procedure requires Installer login and Grid Guard code to enable
    inverters to accept Cluster Controller limits; the passage doesn''t say the role ''holder'' explicitly
    but it''s essentially implied.'
- claim_id: c4
  rel: requires
  target: proto:modbus
  scope:
    products:
    - prod:tesla-megapack-platform
  note: Tesla exposes the enable flag and the per-unit limit as read/write Modbus registers 22501 and
    22502.
  cite:
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=121.r2
    h: d3d74ed97163
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=121
    h: 8b9dc5293360
  review: drafted
- claim_id: c5
  attr: setting_range
  value:
    min: 0
    max: 100
    unit: unit:PERCENT
  scope:
    products:
    - prod:sungrow-sg250hx
  conditions: Active power limit ratio, expressed as a percentage of rated power
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=32.r1
    h: fe581bd262e4
  review: drafted
- claim_id: c6
  attr: setting_range
  value:
    min: 0.1
    unit: unit:KiloW
  scope:
    products:
    - prod:huawei-sun2000-45ktl-us-hv-d0
  conditions: Maximum active power parameter; upper bound is Pmax_limit (device upper limit of maximum
    active power)
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=39
    h: 6d3a70d6e031
  review: drafted
- claim_id: c7
  attr: setting_range
  value:
    min: 0.1
    unit: unit:KiloW
  scope:
    products:
    - prod:huawei-sun2000-100ktl-ush0
  conditions: Maximum active power parameter; upper bound is Pmax_limit
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=40.r4
    h: 0b2c40b31556
  review: drafted
---
This function puts a cap on the active power a DER sends out. When it is enabled, the unit's output stays at or below a set maximum. Vendors configure it differently. Sungrow string inverters use an enable switch plus a limit ratio as a percentage of rated power. Huawei SUN2000 inverters take a maximum active power value in kW. SMA inverters use the parameter Set active power limit. On Tesla battery systems, the limit applies in the discharge direction. It is a per-unit fraction of nameplate real power, and both the limit and its enable flag can be read and written over Modbus. The SMA Cluster Controller receives active power limitation setpoints from the grid operator or a direct marketer as digital or analog signals or over Modbus, passes them to the inverters, and reports them back. When the setpoints conflict, it applies the one that limits power most. With self-consumption, the Cluster Controller uses closed-loop control based on the measured feed-in at the grid connection point. The inverters must be set to Act. power lim. via PV system ctrl, which requires installer login with an SMA Grid Guard code.
