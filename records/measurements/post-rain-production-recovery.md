---
id: meas:post-rain-production-recovery
type: Measurement
name: Production recovery after rain
status: proposed
signals:
- point: model_307.Rain
  unit: unit:MilliM
  pattern: meaningful or heavy rainfall event recorded
- point: model_103.W
  unit: unit:W
  pattern: irradiance-normalized output declines gradually over dry period, then steps up after rain
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: used to normalize output; no matching irradiance change explains the step
---
