---
id: func:constant-reactive-power
type: Function
name: Constant reactive power mode
aliases:
- constant var
- fixed reactive power
- Q setpoint
- DVAR
- Fixed VAR
- Q Fixed
- Q Set
- Q constant
- Fixed Reactive
- Fixed Reactive Power mode
- Q setting
- Constant Q Mode
category: Grid support
function_kind: grid-support
claims:
- claim_id: c1
  attr: response_time
  value:
    max: 10
    unit: unit:SEC
  scope:
    standard: std:ieee-1547-2018
  conditions: Maximum DER response time to maintain constant reactive power
  quote: The maximum DER response time to maintain constant reactive power shall be 10 s or less.
  quote_source: IEEE 1547-2018 §5.3.5
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=5.3.5
    h: 8631c2630733
  review: drafted
- claim_id: c2
  attr: setting_range
  value:
    min: -60
    max: 60
    unit: unit:PERCENT
  scope:
    products:
    - prod:solis-s6-eh2p-l-us
  conditions: Reactive Power Setting Value (CONST_Q-AS, Modbus register 43051)
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=27
    h: fad5475d5f94
  review: drafted
- claim_id: c3
  attr: default_value
  value:
    nominal: 0
    unit: unit:PERCENT
  scope:
    products:
    - prod:solis-s6-eh2p-l-us
  conditions: Reactive Power Setting Value (CONST_Q-AS, Modbus register 43051); mode enable defaults to
    Disable
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=27
    h: fad5475d5f94
  review: drafted
- claim_id: c4
  attr: setting_range
  value:
    min: -60
    max: 60
    unit: unit:PERCENT
  conditions: CPS single-phase hybrid inverter, L1 and L2 reactive power settings (InvL1CSQPer, InvL2CSQPer);
    same for IEEE 1547-2018, Rule 21 and HECO profiles
  cite:
  - src: src:chint-cps-single-phase-hybrid-inverter-user-manual-apr-2026
    loc: tbl=29
    h: b735d9295310
  review: drafted
- claim_id: c5
  attr: default_value
  value:
    nominal: 0
    unit: unit:PERCENT
  conditions: CPS single-phase hybrid inverter, L1 and L2 reactive power settings; IEEE 1547-2018, Rule
    21 and HECO profiles
  cite:
  - src: src:chint-cps-single-phase-hybrid-inverter-user-manual-apr-2026
    loc: tbl=29
    h: b735d9295310
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions)
- claim_id: c6
  attr: setting_range
  value:
    min: 0.1
    max: 100.1
    unit: unit:PERCENT
  conditions: CPS single-phase hybrid inverter, reactive power response step (QActStep), IEEE 1547-2018
    and HECO profiles
  cite:
  - src: src:chint-cps-single-phase-hybrid-inverter-user-manual-apr-2026
    loc: tbl=29
    h: b735d9295310
  review: drafted
- claim_id: c7
  attr: setting_range
  value:
    min: 0.1
    max: 100
    unit: unit:PERCENT
  conditions: CPS single-phase hybrid inverter, reactive power response step (QActStep), Rule 21 profile
  cite:
  - src: src:chint-cps-single-phase-hybrid-inverter-user-manual-apr-2026
    loc: tbl=29
    h: b735d9295310
  review: drafted
- claim_id: c8
  attr: default_value
  value:
    nominal: 100
    unit: unit:PERCENT
  conditions: CPS single-phase hybrid inverter, reactive power response step (QActStep), all listed profiles
  cite:
  - src: src:chint-cps-single-phase-hybrid-inverter-user-manual-apr-2026
    loc: tbl=29
    h: b735d9295310
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions)
- claim_id: c9
  attr: response_time
  value:
    nominal: 1
    unit: unit:SEC
  scope:
    products:
    - prod:kaco-blueplanet-87-165-tl3
  conditions: Transient time when the reactive power specification is changed; first-order (PT-1) filter
  note: Filter time constant Tau is 200 ms.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: sec=h260
    h: e63851be8b2b
  review: drafted
---
Constant reactive power mode holds the inverter's reactive power at a fixed target level, set as either injection or absorption. The default IEEE 1547-2018 settings list this mode as off by default. The Solis S6-EH2P hybrid uses Modbus registers 43451 for the enable and 43051 for the setpoint, with a range of -60 to 60 percent. The CPS single-phase hybrid takes separate L1 and L2 setpoints plus a reactive power response step. In SMA documentation, the Q setting mode works with active power draw, zero active power and active power output. Cos phi setpoint mode does not work at zero active power.
