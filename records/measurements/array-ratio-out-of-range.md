---
id: meas:array-ratio-out-of-range
type: Measurement
name: Array ratio out of range
status: proposed
signals:
- point: model_103.W
  unit: unit:W
  pattern: power relative to irradiance falls outside the valid range learned by regression for several
    consecutive samples
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: used as the irradiance reference for the ratio; data with low irradiance filtered out
---
