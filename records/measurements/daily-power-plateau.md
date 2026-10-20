---
id: meas:daily-power-plateau
type: Measurement
name: Flat plateau at power peak
status: proposed
signals:
- point: model_103.W
  unit: unit:W
  pattern: flat plateau at the inverter AC rating around midday peaks
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: irradiance keeps rising while AC power stays flat
- point: model_103.DCW
  unit: unit:W
  pattern: available DC power exceeds the inverter AC rating; inverter limits DC production
---
