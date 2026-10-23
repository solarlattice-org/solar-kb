---
id: meas:ac-dc-power-mismatch
type: Measurement
name: AC vs DC power mismatch
status: proposed
signals:
- point: model_103.W
  unit: unit:W
  pattern: AC output power differs from DC input power by more than the inverter allows
- point: model_103.DCW
  unit: unit:W
  pattern: DC input power does not match the measured AC output power
---
