---
id: meas:inverter-temperature-high
type: Measurement
name: High inverter internal temperature
status: proposed
signals:
- point: model_103.TmpCab
  unit: unit:DEG_C
  pattern: cabinet temperature runs high or keeps rising during high-load, hot periods
- point: model_103.TmpSnk
  unit: unit:DEG_C
  pattern: heat sink temperature high compared with normal operation
---
