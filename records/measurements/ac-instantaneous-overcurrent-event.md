---
id: meas:ac-instantaneous-overcurrent-event
type: Measurement
name: AC instantaneous overcurrent event
signals:
- point: model_103.A
  unit: unit:A
  pattern: AC output current briefly goes above the inverter's upper limit, then drops to zero when the
    inverter disconnects
- point: model_103.W
  unit: unit:W
  pattern: AC power drops to zero during the fault and comes back after the grid returns to normal and
    the inverter reconnects
---
This signature is an inverter event raised when the AC output current goes above the inverter's upper current limit. The event is tied to grid conditions, and the inverter normally reconnects to the grid on its own once the grid is back to normal. If the event keeps coming back, treat it as a repeated fault rather than a one-off, and contact the manufacturer for service.

<!-- review notes
- sentence 2: support check: partial - The inverter generally reconnects after the grid returns to normal, but the passage doesn't explicitly say the event is tied to grid conditions beyond that implication.
-->
