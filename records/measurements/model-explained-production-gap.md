---
id: meas:model-explained-production-gap
type: Measurement
name: Model-explained production gap
status: proposed
signals:
- point: model_103.W
  unit: unit:W
  pattern: Measured AC power stays persistently below the modeled baseline; the shortfall shrinks or disappears
    when the module file parameters are varied in sensitivity cases
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: Plane-of-array irradiance used as model input for the sensitivity cases; no irradiance anomaly
    explains the gap
---
