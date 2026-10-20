---
id: meas:grade-break-aligned-loss
type: Measurement
name: Loss aligned with grade breaks
status: proposed
signals:
- point: model_403.InDCA
  unit: unit:A
  pattern: Lower normalized string current in rows on grade breaks or swales during morning and afternoon
    backtracking windows
- point: model_103.W
  unit: unit:W
  pattern: Repeatable time-of-day shortfall in normalized output for inverters serving rolling terrain
    sections
- point: model_160.DCW
  unit: unit:W
  pattern: Normalized string or input power lower in rows on grade breaks or swales, repeatable by sun
    position, worst in morning and afternoon
---
