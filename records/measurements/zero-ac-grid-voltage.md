---
id: meas:zero-ac-grid-voltage
type: Measurement
name: Zero AC grid voltage
aliases:
- no AC voltage
- NO-GRID
signals:
- point: model_103.PhVphA
  unit: unit:V
  pattern: AC phase voltage falls to zero during the event
- point: model_103.W
  unit: unit:W
  pattern: AC power at or below zero while the grid voltage is zero
---
This signature is an AC grid voltage reading of zero at the inverter or the meter. The inverter is not seeing the utility grid, so it stops producing power. One inverter manual lists an islanding event as a case of no AC voltage. The inverter stays off until the event clears. To confirm it, measure the AC voltage with a CAT III multimeter, or at the inverter test points line to line and line to ground. Compare your reading with the voltage on the inverter display, because a faulty measurement circuit can also show this pattern. If you find no voltage, check the AC fuses and circuit breakers and look for damage on the AC conductors. A waiting-for-grid-voltage or grid failure message can also mean the AC cable is not connected correctly or the country data set is set wrong. On sites with an islanding controller, the grid-side voltage register and the breaker-open status show whether the system is grid-connected or running off-grid. In some monitoring software, when the meter tied to an inverter reads zero AC voltage, the lost energy is filed as grid meter offline loss and not as normal downtime.

<!-- review notes
- sentence 1: support check: partial - Passages say the inverter doesn't detect the grid/no AC voltage and ceases production, but nothing says the reading is zero at 'the inverter or the meter' as a signature definition.
- sentence 7: support check: partial - u12 describes Grid Meter Offline loss as a downtime subcategory when meter AC voltage is zero, but it is PowerTrack-specific and 'some monitoring software' and 'not normal downtime' is roughly supported though it's a subcategory of downtime.
-->
