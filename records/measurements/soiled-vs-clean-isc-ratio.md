---
id: meas:soiled-vs-clean-isc-ratio
type: Measurement
name: Soiled vs clean Isc ratio
status: proposed
signals:
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: use clear-sky, high-irradiance midday periods only
- point: model_303.TmpBOM
  unit: unit:DEG_C
  pattern: back-of-module temperature used to temperature-correct Isc
---
