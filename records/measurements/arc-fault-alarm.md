---
id: meas:arc-fault-alarm
type: Measurement
name: Arc fault alarm
status: proposed
signals:
- point: model_103.W
  unit: unit:W
  pattern: AC power falls to zero when the inverter shuts down on arc detection
- point: model_103.DCA
  unit: unit:A
  pattern: DC input current stops at the moment of the arc fault shutdown
---
