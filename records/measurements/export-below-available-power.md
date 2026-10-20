---
id: meas:export-below-available-power
type: Measurement
name: Export below available power
signals:
- point: model_103.W
  unit: unit:W
  pattern: AC power stays below the irradiance-supported available power estimate during constrained intervals
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: Plane-of-array irradiance supports more power than is being exported
---
This signature is plant output that holds at a flat or controlled level below the power that the measured irradiance could support. It points to grid curtailment: the plant could produce more, but it is not allowed to export it. The limit may come from grid operator dispatch, an interconnection constraint, a plant controller command, a response to negative prices, or a site export cap. Inverter and tracker availability can look normal during these periods, so the loss is easy to mistake for underperformance or an equipment fault. To confirm it, compare meter output and irradiance-based available power with plant setpoints, inverter active power limits, dispatch signals, curtailment flags and battery charging behavior. Record curtailed energy separately from equipment losses, and use performance metrics designed for heavily curtailed plants.

<!-- review notes
- sentence 4: support check: partial - The passages say availability may look normal and curtailment is easy to misclassify as underperformance, but they do not say it is mistaken for an equipment fault.
-->
