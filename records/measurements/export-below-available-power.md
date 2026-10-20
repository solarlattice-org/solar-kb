---
id: meas:export-below-available-power
type: Measurement
name: Export below available power
status: proposed
signals:
- point: model_103.W
  unit: unit:W
  pattern: AC power stays below the irradiance-supported available power estimate during constrained intervals
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: Plane-of-array irradiance supports more power than is being exported
---
