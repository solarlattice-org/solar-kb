---
id: meas:normalized-output-decline
type: Measurement
name: Declining normalized output
status: proposed
signals:
- point: model_103.WH
  unit: unit:W-HR
  pattern: energy normalized to irradiance and installed power falls year over year, faster than the module
    degradation rate
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: used as the irradiance reference for normalization
- point: model_103.W
  unit: unit:W
  pattern: Irradiance-normalized AC power falls steadily across dry days
- point: model_307.Rain
  unit: unit:MilliM
  pattern: No rainfall during the declining period
---
