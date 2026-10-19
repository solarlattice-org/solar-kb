---
id: meas:no-recovery-after-rain
type: Measurement
name: No recovery after rain
status: proposed
signals:
- point: model_307.Rain
  unit: unit:MilliM
  pattern: rainfall event recorded
- point: model_103.W
  unit: unit:W
  pattern: normalized production deficit unchanged after rain; step-up only after manual cleaning
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: used to normalize output
---
