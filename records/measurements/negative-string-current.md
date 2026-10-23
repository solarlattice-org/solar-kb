---
id: meas:negative-string-current
type: Measurement
name: Negative string current
status: proposed
signals:
- point: model_403.InDCA
  unit: unit:A
  pattern: one string on an MPPT shows negative current before the inverter connects to the grid
- point: model_160.DCA
  unit: unit:A
  pattern: negative or reversed current on an input while the strings on that MPPT are unequal
---
