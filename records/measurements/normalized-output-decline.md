---
id: meas:normalized-output-decline
type: Measurement
name: Long-term normalized output decline
status: proposed
signals:
- point: model_103.WH
  unit: unit:W-HR
  pattern: weather-normalized yearly energy declines more than module warranty degradation implies
- point: model_403.InDCA
  unit: unit:A
  pattern: string currents spread apart over years as weaker modules limit strings
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
