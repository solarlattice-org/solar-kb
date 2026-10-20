---
id: meas:ir-hotspot
type: Measurement
name: Localized IR hotspot
aliases:
- hot-spots
- Hotspot
signals:
- point: model_403.InDCA
  unit: unit:A
  pattern: string current lower than peer strings when severe hotspots are present
---
In an infrared image, a localized hotspot shows up as one or more cells or substrings running hotter than the rest of the module while it is under load. The heating builds up where a cell is driven into reverse bias and junction breakdown, where a solder bond's contact resistance has risen or the bond is fatigued, or where separated pieces of a cracked cell still touch. Typical causes are cracked cells, solder bond defects, shadows from soiling, bypass diode behaviour and mismatch, so the pattern points to failure modes such as module hotspot from cell damage, cell cracks and bypass diode failure. Hot spots can also come from broken front glass or external shading, and a loose connection inside a junction box can make the box itself show as hot. Scan with the inverter running, at high irradiance (above 600 W/m²), in steady weather with no clouds and low wind, and give the module 5 to 15 minutes to settle after conditions change. Avoid reflections from clouds, buildings or trees, because they can look like thermal anomalies; wait for steadier conditions or move the camera. One thermal anomaly is only a screening result. Check that it repeats and that it affects electrical output before replacing anything, and raise the priority if it stays stable across inspections or appears on several modules in the same string.

<!-- review notes
- sentence 6: support check: partial - u19 says to avoid cloud/building/tree reflections as they may distort the evaluation and to wait or move the camera, but doesn't say they look like thermal anomalies.
-->
