---
id: meas:external-source-out-of-threshold
type: Measurement
name: External source outside thresholds
status: proposed
signals:
- point: model_103.PhVphA
  unit: unit:V
  pattern: external-source phase voltage above the configured maximum or below the minimum threshold
- point: model_103.Hz
  unit: unit:HZ
  pattern: external-source frequency outside the configured generator frequency window
---
