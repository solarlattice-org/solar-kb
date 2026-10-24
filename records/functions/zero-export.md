---
id: func:zero-export
type: Function
name: Zero export
aliases:
- zero feed-in
- zero export control
- non-export
- Zero-Net Export
category: Control
function_kind: control
claims:
- claim_id: c1
  rel: subclass_of
  target: func:export-limitation
  note: Zero export is configured as an export limitation with the active power setpoint at 0%.
  cite:
  - src: src:sma-kb-stp-110-60-core-2-export-limit-and-control
    loc: sec=h1
    h: 370ce31aa472
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: requires
  target: prod:sma-data-manager-m
  scope:
    products:
    - prod:sma-sunny-tripower-core2
  note: The Data Manager (EDMM-10) acts as master for the CORE2 inverter.
  cite:
  - src: src:sma-kb-stp-110-60-core-2-export-limit-and-control
    loc: sec=h1
    h: 370ce31aa472
  review: drafted
  review_note: 'support check: partial - Data Manager (EDMM-10) is required and master for CORE2, but
    the passage never says the ''M'' variant is required (it cites EDMM-10 and the M/L articles only loosely).;
    review: partial - The passage says export limitation (including zero export) on CORE2 needs the SMA
    Data Manager (EDMM-10), which acts as master, but it never says EDMM-10 is the ''M'' variant; ''Data
    Manager M'' appears only in the titles of linked articles.'
- claim_id: c3
  rel: requires
  target: prod:sma-energy-meter
  scope:
    products:
    - prod:sma-sunny-tripower-core2
  note: EM-20 shown as example; other meters can also be used.
  cite:
  - src: src:sma-kb-stp-110-60-core-2-export-limit-and-control
    loc: sec=h1
    h: 370ce31aa472
  review: drafted
- claim_id: c4
  rel: requires
  target: prod:sma-energy-meter
  scope:
    products:
    - prod:sma-sunny-tripower-smart-energy
  cite:
  - src: src:sma-doc-259463
    loc: tbl=10.r5
    h: b6b049f7bbc0
  review: drafted
  review_note: 'support check: partial - Zero export is supported by Smart Energy with SMA Energy Meter,
    but the passage doesn''t say it requires the meter (also lists Sunny Home Manager systems).'
- claim_id: c5
  rel: requires
  target: func:closed-loop-plant-control
  note: Active power operating mode set to closed loop control with manual control as signal source in
    the Data Manager.
  cite:
  - src: src:sma-kb-stp-110-60-core-2-export-limit-and-control
    loc: sec=h1
    h: 370ce31aa472
  - src: src:sma-kb-zero-feed-in-zero-export-with-stps60-and-battery
    loc: sec=h1
    h: 75ab8003eb08
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: requires
  target: func:active-power-setpoint
  cite:
  - src: src:sma-kb-stp-110-60-core-2-export-limit-and-control
    loc: sec=h1
    h: 370ce31aa472
  - src: src:sma-kb-zero-feed-in-zero-export-with-stps60-and-battery
    loc: sec=h1
    h: 75ab8003eb08
  review: drafted
- claim_id: c7
  rel: requires
  target: func:system-manager
  note: When several ennexOS devices are installed, the System Manager applies the zero export settings
    to subordinate devices.
  cite:
  - src: src:sma-doc-274308
    loc: sec=6
    h: 2d50844734a3
  review: drafted
  review_note: 'support check: partial - System Manager applying settings to subordinate devices is stated,
    but not that zero export ''requires'' it; it is an optional configuration route.'
---
Zero export stops a PV or storage system from sending active power to the utility grid. Some utilities require it, usually because the local grid is constrained. To set up zero export on a Sunny Tripower CORE2, you need an SMA Data Manager and an energy meter. In the Data Manager, set the active power operating mode to closed loop control, set the signal source to manual control and set the active power setpoint to 0%. In plants that combine a Sunny Tripower Storage 60, a Data Manager and an Inverter Manager on the same grid meter, misaligned settings can stop the battery from charging. Fix this by setting the Data Manager setpoint to 0%, setting all inverters to follow external active power commands and configuring peak load shaving in the Inverter Manager. On the CORE2 inverter, change the normalized active and reactive power limitation parameters from 0 to 1 so the inverter accepts external control. Where possible, turn off the ramp rates and setpoint filters. Sunny Tripower Smart Energy supports zero export with an SMA Energy Meter, and also in advanced systems with a Sunny Home Manager. If several ennexOS devices are installed, you can make the settings in the System Manager, which passes them to all subordinate devices.

<!-- review notes
- sentence 4: support check: partial - Parameters 0 to 1 and disabling ramp rates/filters where possible are stated, but the 'so inverter accepts external control' purpose is only loosely implied, and the reactive/active activation is described as external control for active power.
-->
