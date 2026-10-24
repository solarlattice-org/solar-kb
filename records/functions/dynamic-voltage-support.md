---
id: func:dynamic-voltage-support
type: Function
name: Dynamic voltage support
aliases:
- dynamic reactive current
- dynamic grid support
- K-factor reactive current
- Full dynamic grid support
- Dynamic Reactive Current Support
- k-factor
category: Grid support
function_kind: grid-support
claims:
- claim_id: c1
  attr: response_time
  value:
    nominal: 100
    unit: unit:MilliSEC
  conditions: Fastest inverter response stated for dynamic reactive current support against short AC voltage
    fluctuations
  note: Source says the response can be as fast as this value.
  cite:
  - src: src:book-nrel-pv-integration-handbook-for-dist-n-engineers-63114
    loc: sec=3.2.2.3.7
    h: 2b9e8e36858e
  review: drafted
---
During low-voltage and high-voltage ride-through, dynamic voltage support has the inverter inject current, mostly fast reactive current, into the grid to hold up or pull down the voltage. On SMA inverters the dynamic grid support mode can be set to Off, Limited or Complete (full). Limited mode stops current feed-in while staying connected to the grid. Full mode feeds reactive current along a droop when the voltage leaves a band or jumps suddenly. Full mode sets the size of its response with gradient K parameters for undervoltage, overvoltage and negative sequence. Each K gives extra reactive current, relative to nominal current, per unit of voltage deviation. Start voltages set where each droop begins. Other SMA settings cover hysteresis voltage, zero-current thresholds and delays, voltage-leap height, and whether detection uses the nominal or an averaged grid voltage. Default thresholds come from the selected country data set. The NREL handbook describes dynamic reactive current support as a fast response to short voltage fluctuations and flicker. Its curve can include hysteresis and a dead band.

<!-- review notes
- sentence 1: support check: partial - Passages say DER supplies current during LVRT/HVRT for dynamic voltage support, and SMA feeds reactive current; but 'mostly fast reactive current' and 'hold up or pull down' are not explicitly stated (the IEEE says rapid reactive power exchanges in a footnote).
- sentence 5: support check: partial - Passage supports fast response to short voltage fluctuations and optional hysteresis/dead band, but it does not identify the source as an NREL handbook, and flicker is mentioned only generally.
-->
