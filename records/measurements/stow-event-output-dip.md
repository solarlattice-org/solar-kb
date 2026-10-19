---
id: meas:stow-event-output-dip
type: Measurement
name: Output dip during stow
status: proposed
signals:
- point: model_103.W
  unit: unit:W
  pattern: intermittent drop during logged stow intervals while irradiance remains supportive
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: irradiance stays high during the same logged stow intervals
- point: model_307.WndSpd
  unit: unit:M-PER-SEC
  pattern: gusts at or above the active controller wind threshold coincide with logged stow commands
---
