---
id: meas:ir-warm-module
type: Measurement
name: Warm module in IR image
---
In the IR image, a whole module or string looks warmer than the modules around it. Sunlight that is not converted to DC power stays in the module as extra heat. A wide-angle IR camera can pick out modules and strings that are not generating or not connected, because their overall temperature differs noticeably from their neighbours. Inactive modules usually point to disconnected modules or strings, PID or shunted cells, or short-circuited bypass diodes. The temperature rise is only slight and often scales with irradiance, so these faults are hard or even impossible to see under low irradiance. Take images at high irradiance (above 600 W/m²) under stable conditions: no clouds, low wind and steady ambient temperature. A module needs 5 to 15 minutes to settle thermally after conditions change. Natural temperature differences within a module can reach up to 8 K and show as a smooth gradient. A real defect shows as a temperature step from cell to cell, string to string or module to module. With PID, modules near the negative end of the string show warmer cells along the bottom frame or a patchwork pattern.

<!-- review notes
- sentence 6: support check: partial - Passage says up to 8 K from natural inhomogeneity seen as a gradient and defects show cell/string/module-wise steps, but 'smooth' and the 'real defect' framing are slightly stronger than stated.
-->
