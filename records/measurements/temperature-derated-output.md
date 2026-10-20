---
id: meas:temperature-derated-output
type: Measurement
name: Temperature-linked output derating
status: proposed
signals:
- point: model_103.W
  unit: unit:W
  pattern: AC power reduced below expected output while temperature is high
- point: model_307.TmpAmb
  unit: unit:DEG_C
  pattern: ambient temperature high when the power reduction occurs
- point: model_103.TmpSnk
  unit: unit:DEG_C
  pattern: heat sink temperature high while power is reduced
- point: model_103.TmpCab
  unit: unit:DEG_C
  pattern: High cabinet temperature at the same time as the stepwise power reduction
---
