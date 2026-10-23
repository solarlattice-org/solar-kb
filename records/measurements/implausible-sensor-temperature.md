---
id: meas:implausible-sensor-temperature
type: Measurement
name: Implausible sensor temperature value
status: proposed
signals:
- point: model_103.TmpCab
  unit: unit:DEG_C
  pattern: internal temperature stuck at an implausible fixed low value (e.g. -25C) that does not follow
    ambient or load
- point: model_103.TmpSnk
  unit: unit:DEG_C
  pattern: heat sink temperature stuck at an implausible fixed value that does not track AC power or ambient
    temperature
---
