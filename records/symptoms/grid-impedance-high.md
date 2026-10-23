---
id: symptom:grid-impedance-high
type: Symptom
name: High grid impedance
aliases:
- G- IMP
- weak grids
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Conext CL125 reports event/alarm code 015 (hex 0x000F), described as grid impedance above the
    inverter's limit; Solis inverters show the alarm G- IMP, described as high grid impedance.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=49.r4
    h: 462781d51469
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=29.r3
    h: d2952de8a0d5
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=9.r6
    h: 25613ca69b72
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=14.r7
    h: a71ef8fdaeaf
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c2
  rel: observed_as
  target: meas:grid-voltage-rise-with-power
  note: Plotting grid voltage against PV feed-in gives a positive slope, and linear regression of that
    slope estimates the equivalent grid impedance. On a weak grid the voltage approaches the trip threshold
    of 1.1 p.u. at high yield, and the inverter trips. Hourly averages can hide these trips.
  cite:
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=h57
    h: '182922548211'
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - Positive slope, regression for impedance, 1.1 p.u. trip and hourly
    averages hiding trips are stated, but the passages don''t link high impedance to specific phase voltage/W
    signal patterns, and nothing is said about approaching the overvoltage limit at ''high output'' with
    W ''sudden trip to zero'' beyond the immediate trip.'
---
The inverter flags that the grid impedance at its connection point is above its limit. On the Conext CL125 this shows as event code 015, and on Solis inverters it shows as the alarm G- IMP. On SMA units the same grid incident covers either too high a grid voltage or too high an impedance, and the inverter disconnects from the utility grid, so AC output drops to zero. In monitoring data, a weak grid shows up as grid voltage rising with exported PV power. The inverter can trip when the voltage reaches the threshold at high yield, and hourly averages may hide these trips. On the CL125, first check that the AC cable type and size and the transformer impedance match the CL125 Solution Guide or local regulations. Then let the inverter recover automatically. For plants with many paralleled inverters, Schneider recommends limiting AC cable impedance and transformer impedance. It also recommends calculating grid impedance at the point of common coupling before design, and avoiding weak, high-impedance grids. On Solis units, the protection limit can be adjusted through the user-defined settings, but only if the electrical company allows it.

<!-- review notes
- sentence 2: support check: partial - SMA text states voltage or impedance too high and disconnection from the grid, but AC output dropping to zero is only implied.
-->
