---
id: meas:dc-voltage-pinned-at-minimum
type: Measurement
name: DC voltage pinned at minimum
signals:
- point: model_103.DCV
  unit: unit:V
  pattern: flat at the inverter minimum DC input voltage during high-temperature periods
- point: model_103.DCW
  unit: unit:W
  pattern: below the irradiance-expected value during the same intervals
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: normal irradiance at the same timestamps
---
This signature appears when the array's maximum power point voltage drops below the lowest DC input voltage the inverter can use, so the inverter's DC operating voltage stays at its floor instead of following the array Vmp. The inverter stays online, but it cannot track the real Vmp. This leaves a gap between the power the array could deliver and the power harvested, and energy that could have been recovered is lost on the DC side. It shows up most often in hot periods, because module voltage falls as cell temperature rises. Higher reactive power demand from the grid or plant can make it worse, because it shifts how the inverter's effective voltage behaves. In production data alone it can look like clipping or general underperformance. Review DC voltage, AC voltage, reactive power and IV-derived Vmp together to tell them apart. To confirm it during suspected events, compare the inverter DC voltage limits, module temperature, in-situ IV curve Vmp and Pmp, and SCADA operating points. The failure mode behind this signature is inverter voltage floor losses.

<!-- review notes
- sentence 1: support check: partial - Passages state Vmp below the inverter minimum usable voltage and that it cannot track Vmp, but do not say the DC operating voltage stays at its floor.
-->
