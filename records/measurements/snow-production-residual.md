---
id: meas:snow-production-residual
type: Measurement
name: Snow-aligned production residual
status: proposed
signals:
- point: model_103.W
  unit: unit:W
  pattern: abrupt drop after snowfall, gradual recovery during melt
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: usable irradiance reported while output stays low
- point: model_303.TmpBOM
  unit: unit:DEG_C
  pattern: module temperature used alongside residuals to follow melt
---
