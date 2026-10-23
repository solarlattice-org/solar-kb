---
id: meas:inverter-fault-code-display
type: Measurement
name: Inverter fault code display
status: proposed
signals:
- point: model_103.PhVphA
  unit: unit:V
  pattern: inverter AC phase voltage disagrees with the grid-side voltage measurement while a warning
    code is active
- point: model_103.W
  unit: unit:W
  pattern: AC power drops to zero for a short time, then comes back after the inverter restarts
- point: model_103.A
  unit: unit:A
  pattern: AC current falls to zero during the short feed-in stop
---
