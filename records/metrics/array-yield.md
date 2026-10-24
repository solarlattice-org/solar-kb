---
id: metric:array-yield
type: Metric
name: Array yield
aliases:
- Ya
- Instantaneous array yield
category: Performance
---
Array yield describes the output of the PV array on its own, separate from the rest of the system, assuming the MPP tracking is ideal. Working it out requires a measurement of the array's DC output power, which the monitoring parameter list gives as PDC in kW. It appears as a derived parameter next to PV array energy output, reference yield, system yield and the capture and system losses. Array yield over a period is reported in hours, while the instantaneous array yield has no unit. If the array is treated as linear, array yield rises in proportion to reference yield. On a scatter plot of the two, a straight line through the origin fits the points. The slope of that regression line approximates the average array performance ratio. Fitting a new line each week shows sudden changes and longer trends in array performance.

<!-- review notes
- sentence 4: support check: partial - The table gives units '- , h' for array yield (yA, YA), but the passages do not explicitly pair the hours unit with the period value and the dimensionless unit with the instantaneous value. That pairing follows only from the ordering of the symbols and units.
-->
