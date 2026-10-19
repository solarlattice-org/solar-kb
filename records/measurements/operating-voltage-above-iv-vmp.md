---
id: meas:operating-voltage-above-iv-vmp
type: Measurement
name: Operating voltage above Vmp
status: proposed
signals:
- point: model_103.DCV
  unit: unit:V
  pattern: stays at or near the inverter minimum DC voltage and above the IV-derived Vmp
- point: model_103.DCW
  unit: unit:W
  pattern: below the IV-derived Pmp during the same intervals
- point: model_160.DCV
  unit: unit:V
  pattern: above the expected Vmp at the module temperature
- point: model_303.TmpBOM
  unit: unit:DEG_C
  pattern: high module temperature that lowers Vmp
---
