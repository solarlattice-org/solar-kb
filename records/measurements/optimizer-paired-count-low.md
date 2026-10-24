---
id: meas:optimizer-paired-count-low
type: Measurement
name: Low reporting optimizer count
status: proposed
signals:
- point: model_502.W
  unit: unit:W
  pattern: no module-level power from optimizers that are not paired
- point: model_103.W
  unit: unit:W
  pattern: inverter AC power stays at zero until pairing completes and startup begins
---
