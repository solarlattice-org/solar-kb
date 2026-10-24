---
id: func:enter-service
type: Function
name: Enter service
aliases:
- return to service
- reconnection
- soft start ramp
- reconnect delay
- DCTE
- Return to service after trip
- ES
- Soft Start Ramp Rate
category: Control
function_kind: control
claims:
- claim_id: c1
  attr: setting_range
  value:
    min: 0
    max: 600
    unit: unit:SEC
  scope:
    standard: std:ieee-1547-2018
  conditions: ES Delay (enter service delay) parameter
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=46
    h: 18d199c867fd
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=46.r6
    h: 395d60228815
  review: drafted
- claim_id: c2
  attr: setting_range
  value:
    min: 1
    max: 1000
    unit: unit:SEC
  scope:
    standard: std:ieee-1547-2018
  conditions: ES Randomized Delay (enter service randomized delay) parameter
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=46
    h: 18d199c867fd
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=46.r7
    h: 096fc658df55
  review: drafted
- claim_id: c3
  attr: setting_range
  value:
    min: 1
    max: 1000
    unit: unit:SEC
  scope:
    standard: std:ieee-1547-2018
  conditions: ES Ramp Rate (enter service ramp rate) parameter, expressed as a time
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=46
    h: 18d199c867fd
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=46.r8
    h: 5f28fcefe41a
  review: drafted
- claim_id: c4
  attr: default_value
  value:
    min: 0.917
    unit: unit:UNITLESS
  scope:
    standard: std:ieee-1547-2018
  conditions: Enter service criteria, applicable voltage minimum value, in per unit
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=11.r1
    h: 7c087d142026
  review: drafted
- claim_id: c5
  attr: setting_range
  value:
    min: 0.88
    max: 0.95
    unit: unit:UNITLESS
  scope:
    standard: std:ieee-1547-2018
  conditions: Enter service criteria, applicable voltage minimum value, allowable settings in per unit
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=11.r1
    h: 7c087d142026
  review: drafted
  review_note: possible conflict with c7 (same source; check the conditions)
- claim_id: c6
  attr: default_value
  value:
    max: 1.05
    unit: unit:UNITLESS
  scope:
    standard: std:ieee-1547-2018
  conditions: Enter service criteria, applicable voltage maximum value, in per unit
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=11.r2
    h: 59f76a365a77
  review: drafted
- claim_id: c7
  attr: setting_range
  value:
    min: 1.05
    max: 1.06
    unit: unit:UNITLESS
  scope:
    standard: std:ieee-1547-2018
  conditions: Enter service criteria, applicable voltage maximum value, allowable settings in per unit
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: tbl=11.r2
    h: 59f76a365a77
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions)
- claim_id: c8
  attr: default_value
  value:
    nominal: 0.33
    unit: unit:PERCENT
  scope:
    products:
    - prod:generac-pwrcell-inverter
  conditions: ES_RAMP_RATE enter service soft start ramp rate; unit is percent per second
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=35.r1
    h: fbc96e32d234
  review: drafted
- claim_id: c9
  attr: setting_range
  value:
    min: 0.1
    max: 100
    unit: unit:PERCENT
  scope:
    products:
    - prod:generac-pwrcell-inverter
  conditions: ES_RAMP_RATE enter service soft start ramp rate; unit is percent per second
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=35.r1
    h: fbc96e32d234
  review: drafted
- claim_id: c10
  attr: default_value
  value:
    nominal: 0.33
    unit: unit:PERCENT
  scope:
    products:
    - prod:generac-pwrcell-2
  conditions: ES_Ramp_Rate enter service soft start ramp rate; unit is percent per second
  cite:
  - src: src:generac-generac-pwrcell-2-smart-disconnect-switch-install-manual
    loc: tbl=21.r1
    h: c08277a94c33
  review: drafted
- claim_id: c11
  attr: setting_range
  value:
    min: 0.1
    max: 100
    unit: unit:PERCENT
  scope:
    products:
    - prod:generac-pwrcell-2
  conditions: ES_Ramp_Rate enter service soft start ramp rate; unit is percent per second
  cite:
  - src: src:generac-generac-pwrcell-2-smart-disconnect-switch-install-manual
    loc: tbl=21.r1
    h: c08277a94c33
  review: drafted
- claim_id: c12
  attr: setting_range
  value:
    min: 0.1
    max: 100
    unit: unit:PERCENT
  scope:
    products:
    - prod:yaskawa-solectria-sgi-500-750xtm
  conditions: Soft start ramp rate, percent of rated current per second during startup
  cite:
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: sec=h86
    h: 3cbbaf589250
  review: drafted
---
Enter service sets the conditions a DER must see before it reconnects or returns to service after a trip, then ramps its output back up gradually. The standard requires enter service parameters to be readable and writable over a local DER communication interface: permit service, voltage and frequency high and low limits, a delay, a randomized delay and a ramp rate. In Tesla commercial controls, Enter Service uses meter measurements to enforce reconnect thresholds on the battery system, and is meant for sites where Tesla's islanding controller does not handle site-level reconnection. Tesla inputs include a permit flag, over and under voltage thresholds in per unit, over and under frequency thresholds in Hz, a minimum qualification time and a ramp time, and the Tesla project engineer sets them at commissioning. The Tesla reconnection time and ramp time are read/write Modbus registers starting at 22271 and 22273. Generac PWRcell inverters expose an enter service soft start ramp rate parameter, ES_RAMP_RATE, in percent per second. On the Yaskawa Solectria SGI XTM, the soft start ramp only ramps power up, and when the normal ramp rate is also enabled the inverter uses the lower of the two.

<!-- review notes
- sentence 1: support check: partial - Return to service after trip and ramp are supported, but 'conditions a DER must see' is only loosely supported and the ramping is described only via parameters, not explicitly as gradual ramp-up.
-->
