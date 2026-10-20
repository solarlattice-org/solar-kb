---
id: meas:grid-voltage-reading-out-of-limit
type: Measurement
name: Grid voltage outside limits
status: proposed
signals:
- point: model_103.PhVphA
  unit: unit:V
  pattern: AC phase voltage goes above the overvoltage setting or below the undervoltage setting
- point: model_103.W
  unit: unit:W
  pattern: AC power drops to zero while the inverter is disconnected, then comes back once the voltage
    is normal again
---
