---
id: meas:low-string-isc
type: Measurement
name: Low string short-circuit current
status: proposed
signals:
- point: model_403.InDCA
  unit: unit:A
  pattern: string current persistently below that of peer strings with the same layout at the same irradiance
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: stable irradiance needed so that string current differences can be read as faults
---
