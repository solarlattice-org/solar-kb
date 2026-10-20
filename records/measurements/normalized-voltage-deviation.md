---
id: meas:normalized-voltage-deviation
type: Measurement
name: Normalized voltage deviation
aliases:
- vDC
signals:
- point: model_103.DCV
  unit: unit:V
  pattern: normalized array voltage drops below the usual linear voltage-temperature relationship
- point: model_303.TmpBOM
  unit: unit:DEG_C
  pattern: module temperature used as the x-axis for the correlation
---
This signature uses the PV array output voltage, either normalized in per-unit or in volts. The array voltage, normalized to the MPP voltage, is plotted against module temperature using 5 or 15 minute averages, with each week shown separately. For crystalline silicon in normal operation, the points follow a tight linear relationship with temperature, so abnormal operation stands out clearly. The fault pattern is a group of samples with much lower array voltage that sit below the usual line, while most samples still follow it. In the documented case, partial shading from a nearby scaffold tower produced this pattern because the array no longer ran at the MPP it would have under even light. Small shading losses like this were hard to spot in plots of system yield against reference yield or performance ratio against temperature, but the voltage deviation showed them clearly. For CIGS modules the voltage depends less on temperature and the scatter is wider, but irregular low-voltage values should still be visible.

<!-- review notes
- sentence 2: support check: partial - Figures 19 and 20 show voltage normalized to MPP vs module temperature, with 5-min and 15-min averages and weekly separation, but the 'or' framing is loose: the two averaging intervals belong to different examples.
-->
