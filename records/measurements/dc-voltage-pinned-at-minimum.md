---
id: meas:dc-voltage-pinned-at-minimum
type: Measurement
name: DC voltage pinned at minimum
status: proposed
signals:
- point: model_103.DCV
  unit: unit:V
  pattern: flat at the inverter minimum DC input voltage during high-temperature periods
- point: model_103.DCW
  unit: unit:W
  pattern: below the irradiance-expected value during the same intervals
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: normal irradiance at the same timestamps
---
