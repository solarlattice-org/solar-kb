---
id: meas:low-normalized-row-current
type: Measurement
name: Low normalized row current
status: proposed
signals:
- point: model_403.InDCA
  unit: unit:A
  pattern: lower POA-normalized string current than adjacent rows, varying between morning, noon and afternoon
    windows
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: used to normalize string current
- point: model_307.WndSpd
  unit: unit:M-PER-SEC
  pattern: loss more visible during windy intervals
---
