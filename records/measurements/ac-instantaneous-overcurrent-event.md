---
id: meas:ac-instantaneous-overcurrent-event
type: Measurement
name: AC instantaneous overcurrent event
status: proposed
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
