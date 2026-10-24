---
id: func:frequency-watt
type: Function
name: Frequency-Watt
aliases:
- frequency droop
- frequency-power
- P(f)
- Freq-Watt
- over-frequency power reduction
- DHFW
- DLFW
- Frequency-droop mode
- Set F Derating
- Frequency-Watt Control
category: Grid support
function_kind: grid-support
claims:
- claim_id: c1
  rel: requires
  target: role:grid-guard-code-holder
  scope:
    products:
    - prod:sma-sunny-island
  note: 'Sunny Island: the P(f) overfrequency active power reduction mode is an expert parameter protected
    by SMA Grid Guard.'
  cite:
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=148.r13
    h: a5e54afa1678
  review: drafted
- claim_id: c2
  attr: default_value
  value:
    nominal: 0.036
    unit: unit:HZ
  scope:
    products:
    - prod:chint-sca-25ktl-208
  conditions: Overfrequency droop deadband (FreqDroop_DbOf) in the grid setting table
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=35.r12
    h: 4fc0ff18e54b
  review: drafted
- claim_id: c3
  attr: default_value
  value:
    nominal: 0.036
    unit: unit:HZ
  scope:
    products:
    - prod:chint-sca-25ktl-208
  conditions: Underfrequency droop deadband (FreqDroop_DbUf) in the grid setting table
  cite:
  - src: src:chint-cps-sca25ktl-do-us-208-user-manual-rev-1-2
    loc: tbl=35.r13
    h: 68ec7831bf0b
  review: drafted
- claim_id: c4
  attr: setting_range
  value:
    min: 0
    max: 1800
    unit: unit:SEC
  scope:
    products:
    - prod:yaskawa-solectria-sgi-500-750xtm
  conditions: Freq Watt Time Window Modbus register 40381; default 0
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: tbl=31
    h: ff0870582f8e
  review: drafted
- claim_id: c5
  attr: setting_range
  value:
    min: 0
    max: 64800
    unit: unit:SEC
  scope:
    products:
    - prod:yaskawa-solectria-sgi-500-750xtm
  conditions: Freq Watt Timeout Window Modbus register 40382; default 0
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: tbl=31
    h: ff0870582f8e
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c6
  attr: setting_range
  value:
    min: 0
    max: 600
    unit: unit:SEC
  scope:
    products:
    - prod:yaskawa-solectria-sgi-500-750xtm
  conditions: Freq Watt Ramp Time Modbus register 40383; default 0
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: tbl=31
    h: ff0870582f8e
  review: drafted
- claim_id: c7
  attr: setting_range
  value:
    min: 2
    max: 10
    unit: unit:NUM
  scope:
    products:
    - prod:yaskawa-solectria-sgi-500-750xtm
  conditions: Number of points on the frequency-watt curve, Modbus register 40384
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: tbl=31
    h: ff0870582f8e
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c8
  attr: setting_range
  value:
    min: 2
    max: 10
    unit: unit:NUM
  scope:
    products:
    - prod:yaskawa-solectria-xgi-1500
  conditions: Active points on the Freq-Watt curve; at least 2 required
  cite:
  - src: src:yaskawa-xgi-1500-modbus-map-docr-071063-rev-h
    loc: sec=h23
    h: 007e0baa414d
  review: drafted
---
Frequency-Watt changes the inverter's active power output when grid frequency moves away from nominal, which supports grid frequency. When frequency rises, output power goes down. IEEE 1547-2018 sets frequency droop parameters, including an overfrequency droop value kOF. A default settings document for IEEE 1547-2018 lists frequency-droop mode (Freq-Watt) as ON by default. Tesla controllers set up frequency droop with an enable flag, upper and lower deadbands around the reference frequency, upper and lower proportional gains, and a low-pass filter time response. A read-only register reports the resulting power command. On CSI inverters the Freq-Watt menu uses a start frequency, a power reduction gradient, a stop frequency and a hysteresis option. It applies only when a Rule 21 standard is selected, and it is meant for maintenance personnel only. Change these parameters only when the grid operator asks for it.

<!-- review notes
- sentence 2: support check: partial - Table 38 title and overfrequency droop kOF are given and the default ON is listed, but the passages don't say IEEE 1547-2018 sets these or that the document is a default settings document, though it is implied.
-->
