---
id: meas:energy-ratio-out-of-range
type: Measurement
name: Energy ratio out of range
status: proposed
signals:
- point: model_103.WH
  unit: unit:W-HR
  pattern: daily inverter energy outside the accepted band of model-expected energy
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: measured irradiance input to the expected-energy model
---
