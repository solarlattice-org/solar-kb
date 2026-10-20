---
id: meas:zero-ac-output
type: Measurement
name: Zero inverter AC output
status: proposed
signals:
- point: model_103.W
  unit: unit:W
  pattern: AC power stays at zero
- point: model_103.WH
  unit: unit:W-HR
  pattern: energy counter stops increasing
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: normal plane-of-array irradiance while the inverter output is zero
---
