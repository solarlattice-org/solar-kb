---
id: meas:low-insulation-resistance-alarm
type: Measurement
name: Low insulation resistance alarm
status: proposed
signals:
- point: model_103.W
  unit: unit:W
  pattern: inverter stops exporting while the insulation alarm is active
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: normal morning irradiance while the inverter stays offline
- point: model_307.RH
  unit: unit:PERCENT
  pattern: high humidity or dew at the time the inverter fails to start
---
