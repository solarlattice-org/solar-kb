---
id: meas:pr-drop-low-profile-angle
type: Measurement
name: PR drop at low profile angle
status: proposed
signals:
- point: model_103.W
  unit: unit:W
  pattern: output relative to irradiance drops when the sun profile angle falls below the row shading
    angle
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: reference irradiance used to normalize output into PR
---
