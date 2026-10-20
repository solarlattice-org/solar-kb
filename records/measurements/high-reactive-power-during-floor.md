---
id: meas:high-reactive-power-during-floor
type: Measurement
name: Elevated reactive power dispatch
status: proposed
signals:
- point: model_103.VAr
  unit: unit:V-A_Reactive
  pattern: High reactive power output at the same timestamps as DC voltage floor events
- point: model_103.PF
  unit: unit:UNITLESS
  pattern: Power factor away from unity during suspected voltage-floor intervals
- point: model_103.PhVphA
  unit: unit:V
  pattern: AC voltage level or hysteresis behavior coinciding with DC voltage pinned at the minimum
---
