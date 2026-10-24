---
id: func:closed-loop-plant-control
type: Function
name: Closed-loop plant control
aliases:
- power plant controller
- PPC
- closed-loop control at POI
- plant-level active/reactive power control
category: Control
function_kind: control
claims:
- claim_id: c1
  rel: requires
  target: func:ramp-rate-control
  scope:
    products:
    - prod:sma-data-manager-m
    - prod:sma-sunny-tripower-core2
  note: For closed-loop operation of Data Manager M with Sunny Tripower CORE2, the active power gradient
    must be set on every inverter. CORE2 firmware 1.00.08.R or higher and Data Manager M firmware 1.12.07.R
    or higher are needed.
  cite:
  - src: src:sma-kb-closed-loop-control-of-active-and-reactive-power-with-data-manager-m
    loc: sec=h1
    h: 55b212204b2b
  review: drafted
  review_note: 'support check: partial - Passage gives firmware versions and says gradient must be set
    on every inverter, but doesn''t say closed-loop requires a ''ramp rate control'' function as such
    (gradient is the same idea, roughly implied).'
- claim_id: c2
  attr: setting_range
  value:
    min: 0
    max: 1
    unit: unit:NUM
  scope:
    products:
    - prod:tesla-megapack-platform
  conditions: Closed Loop Control Enable parameter (Modbus register 21401, int16, read/write); 0 disables
    and 1 enables closed-loop control
  cite:
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=124
    h: dd8a7c4b40d6
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=149
    h: dd8a7c4b40d6
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=124.r1
    h: 3b623da6a9ac
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=179
    h: dd8a7c4b40d6
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=149.r1
    h: 3b623da6a9ac
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=179.r1
    h: 3b623da6a9ac
  review: drafted
---
Closed-loop plant control measures real and reactive power at the plant meter or point of interconnection. It uses that feedback to correct the plant's power commands so the requested value is actually met at the meter. Open-loop control does not feed back the actual value. Closed-loop control uses the values measured at the point of interconnection, so it can also make up for line and transformer effects. SMA recommends closed-loop control for active power limitation in systems with self-consumption, and for reactive power control in most systems. Open-loop control is preferred where heavy reactive loads without compensation would leave the inverters unable to hold the setpoints. The SMA Cluster Controller and SMA Data Manager M offer a closed-loop operating mode. It needs the measured active power at the grid connection point, and Data Manager M can run it with Sunny Tripower CORE2 inverters. With Data Manager M, slow the meter reading to keep the loop stable. For an SMA meter, change the update cycle from 200 ms to 600 ms or 1000 ms. Janitza meters need a custom Modbus profile. Also set the active power gradient on every inverter. In Tesla Megapack sites, the Tesla System Controller adds the closed-loop correction in its Combiner. On co-located plants, the correction only applies at each metered battery sub-site. On Tesla sites, closed-loop control is off by default at commissioning so that wiring errors in the meter's current or potential transformers do not cause wind-up. Turn it on with the Closed Loop Control Enable setting only after the meter readings match the battery power command. For large or complex SMA plants, the SMA Hybrid Controller or a Data Manager L can control the Power Plant Manager. If both are connected, only one of them may be set up as the active controller.

<!-- review notes
- sentence 8: support check: partial - Passage says both can be used and HYCON for complex requirements, only one active if both connected; but it says the Data Manager L is the default, and 'large' plants and Data Manager L for complex are not exactly stated.
-->
