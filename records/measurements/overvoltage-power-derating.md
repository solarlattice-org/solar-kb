---
id: meas:overvoltage-power-derating
type: Measurement
name: Volt-watt power derating
status: proposed
signals:
- point: model_103.W
  unit: unit:W
  pattern: AC power falls below available power as AC voltage rises above the derating start voltage
- point: model_103.PhVphA
  unit: unit:V
  pattern: AC voltage elevated into the volt-watt derating band
---
