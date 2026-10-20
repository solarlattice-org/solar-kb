---
id: meas:inverter-normalized-yield-spread
type: Measurement
name: Spread in normalized inverter yield
status: proposed
signals:
- point: model_103.WH
  unit: unit:W-HR
  pattern: one inverter's energy per installed kWp sits below its peers
- point: model_103.W
  unit: unit:W
  pattern: Irradiance-normalized output differs between inverters or zones of the same plant
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: Used as the normalization reference; irradiance itself is uniform
---
