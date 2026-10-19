---
id: meas:production-loss-alarm
type: Measurement
name: Production loss alarm
status: proposed
signals:
- point: model_403.InDCA
  unit: unit:A
  pattern: string current drops to zero (open circuit) or falls below its peers
- point: model_160.DCV
  unit: unit:V
  pattern: voltage step down when a substring is shorted
---
