---
id: meas:flat-output-below-available-power
type: Measurement
name: Flat output below available power
status: proposed
signals:
- point: model_103.W
  unit: unit:W
  pattern: flat or controlled level below irradiance-supported available power
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: irradiance would support higher output
- point: model_103.DCV
  unit: unit:V
  pattern: May move away from the MPP voltage while output is held down
---
