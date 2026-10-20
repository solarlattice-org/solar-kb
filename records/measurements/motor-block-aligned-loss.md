---
id: meas:motor-block-aligned-loss
type: Measurement
name: Loss aligned with motor blocks
status: proposed
signals:
- point: model_403.InDCA
  unit: unit:A
  pattern: normalized string current lower in rows near motor block boundaries during morning and afternoon
    backtracking windows
- point: model_160.DCA
  unit: unit:A
  pattern: normalized string current lower in specific tracker blocks or rows, repeatable by time of day
- point: model_103.W
  unit: unit:W
  pattern: normalized inverter output lower for inverters serving affected terrain zones, mostly in morning
    and afternoon backtracking windows
---
