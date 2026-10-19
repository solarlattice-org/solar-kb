---
id: meas:performance-ratio-decline
type: Measurement
name: Declining performance ratio
status: proposed
signals:
- point: model_103.W
  unit: unit:W
  pattern: irradiance-normalized output gradually falls during dry periods and recovers after rain or
    cleaning
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: reference irradiance for the normalization
- point: model_307.Rain
  unit: unit:MilliM
  pattern: rain events that line up with recovery steps
---
