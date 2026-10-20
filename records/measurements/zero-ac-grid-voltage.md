---
id: meas:zero-ac-grid-voltage
type: Measurement
name: Zero AC grid voltage
status: proposed
signals:
- point: model_103.PhVphA
  unit: unit:V
  pattern: AC phase voltage falls to zero during the event
- point: model_103.W
  unit: unit:W
  pattern: AC power at or below zero while the grid voltage is zero
---
