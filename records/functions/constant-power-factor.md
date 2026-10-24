---
id: func:constant-power-factor
type: Function
name: Constant power factor mode
aliases:
- fixed power factor
- cos phi fixed
- PF mode
- DFPF
- Fixed PF
- Fixed Power Factor mode
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
  conditions: Maximum DER response time to maintain the constant power factor
  quote: The maximum DER response time to maintain constant power factor shall be 10 s or less.
  quote_source: IEEE 1547-2018 §5.3.2
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=5.3.2
    h: 6aaf1eecb7b8
  review: drafted
- claim_id: c2
  attr: setting_range
  value:
    min: 0
    max: 1
    unit: unit:UNITLESS
  scope:
    standard: std:ieee-1547-2018
  conditions: Constant Power Factor setting parameter; excitation set separately as over- or under-excited
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=37
    h: 75588dc5dd29
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=37.r2
    h: ee76f3623026
  review: drafted
- claim_id: c3
  attr: setting_range
  value:
    min: 0.8
    max: 1
    unit: unit:UNITLESS
  scope:
    products:
    - prod:solis-s6-eh2p-l-us
  conditions: Power Factor Setting Value (Modbus register 43054); allowed bands are -1 to -0.8 and +0.8
    to +1
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=26
    h: bc62159b4750
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=26.r2
    h: 4adf0ad1c7cd
  review: drafted
- claim_id: c4
  attr: default_value
  value:
    nominal: 1
    unit: unit:UNITLESS
  scope:
    products:
    - prod:solis-s6-eh2p-l-us
  conditions: Power Factor Setting Value (Modbus register 43054); the Fixed PF mode enable itself defaults
    to Disable
  cite:
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=26
    h: bc62159b4750
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=26.r2
    h: 4adf0ad1c7cd
  review: drafted
- claim_id: c5
  attr: setting_range
  value:
    min: 0.8
    unit: unit:UNITLESS
  scope:
    products:
    - prod:chint-sch-125ktl-aio
    - prod:chint-sch-200-250k-t
    - prod:chint-sca-25ktl-208
    - prod:canadian-solar-23-28ktl-ct
  conditions: Power factor adjustable to 0.8 leading or lagging (listed as plus/minus 0.8 adjustable);
    nominal power factor above 0.99
  cite:
  - src: src:chint-cps-sch125ktl-aio-us-600-sep-2020
    loc: tbl=37.r19
    h: 14255a5f7bdd
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=45.r22
    h: 75c28bcd594f
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=55.r22
    h: 04b64ff5ef58
  - src: src:csi-csi-23-28ktl-ct-inverter-installation-manual
    loc: tbl=32.r10
    h: ad5edc9d8ce8
  review: drafted
- claim_id: c6
  attr: setting_range
  value:
    min: 0.75
    unit: unit:UNITLESS
  scope:
    products:
    - prod:abb-pvs-166-175-tl-us
  conditions: 'PVS-166-TL at Smax: adjustable from 0.75 lead to 0.75 lag; nominal power factor above 0.995'
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=9.r33
    h: ec1fe0973d6f
  review: drafted
- claim_id: c7
  attr: setting_range
  value:
    min: 0.8
    unit: unit:UNITLESS
  scope:
    products:
    - prod:abb-pvs-166-175-tl-us
  conditions: 'PVS-175-TL at Smax: adjustable from 0.8 lead to 0.8 lag; nominal power factor above 0.995'
  cite:
  - src: src:abb-fimer-pvs-166-175-tl-us-a-2-product-manual-reve
    loc: tbl=9.r33
    h: ec1fe0973d6f
  review: drafted
---
Constant power factor mode makes the inverter run at a fixed power factor, so its reactive power follows its active output at a set ratio. In FIMER Aurora Manager LITE, you pick cos-phi fixed as the reactive power regulation mode, enter the over- or under-excited value and confirm with SET. CPS SCH125KTL-AIO, SCH200K/SCH250K-T, SCA25KTL-DO and CSI 23/28KTL-CT inverters list power factor adjustable to plus or minus 0.8. The FIMER PVS-166 adjusts to 0.75 lead or lag, the PVS-175 to 0.8, and the UNO-DM-3.3/3.8-PLUS to plus or minus 0.8.

<!-- review notes
- sentence 1: support check: partial - Constant PF operation is stated, but the reactive power following active output at a set ratio is an inference not explicitly stated.
- sentence 2: support check: partial - Selecting cos-phi fixed, entering over/under-excited value and confirming with SET are stated, but the passages don't name Aurora Manager LITE.
-->
