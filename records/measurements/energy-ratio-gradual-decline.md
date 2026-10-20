---
id: meas:energy-ratio-gradual-decline
type: Measurement
name: Gradual energy ratio decline
status: proposed
signals:
- point: model_103.WH
  unit: unit:W-HR
  pattern: daily AC energy falls steadily relative to model-expected energy over several days
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: measured irradiance used to compute expected energy; no matching irradiance drop
- point: model_303.TmpBOM
  unit: unit:DEG_C
  pattern: module temperature used as model input for expected energy
---
