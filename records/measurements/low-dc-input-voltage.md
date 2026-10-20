---
id: meas:low-dc-input-voltage
type: Measurement
name: Low DC input voltage
status: proposed
signals:
- point: model_103.DCV
  unit: unit:V
  pattern: near zero or well below normal while the status LEDs are dark
- point: model_160.DCV
  unit: unit:V
  pattern: MPPT input voltage absent or low
---
