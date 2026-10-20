---
id: meas:pr-drop-low-profile-angle
type: Measurement
name: PR drop at low profile angle
aliases:
- PRdrop
signals:
- point: model_103.W
  unit: unit:W
  pattern: output relative to irradiance drops when the sun profile angle falls below the row shading
    angle
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: reference irradiance used to normalize output into PR
---
This signature is a lower average performance ratio during periods when the sun's profile angle is below the shading angle of the module rows. The profile angle is the sun elevation projected onto a vertical plane at right angles to the row azimuth. The shading angle is the smallest profile angle at which the rows are still unshaded. To get the drop, average the PR separately for unshaded periods (profile angle above the shading angle) and for shaded periods, then subtract the shaded value from the unshaded one. The shading angle depends on the system layout. One reference system, with a 27 degree slope and modules in portrait, had a shading angle of 19 degrees. The drop also includes losses other than shading, such as the modules' low-light behaviour and the inverter's part-load efficiency. Use it as an estimate for comparing systems, not as a direct measure of shading loss. Comparing the measured drop with a row-shading simulation fed by measured plane-of-array irradiance and module temperature shows how accurate the simulation is for this loss. In the reference analysis, intervals with very low sun elevation or very low AC power were removed, along with days with system downtime. Inter-row shading produces this pattern because the row in front blocks direct light and part of the sky's diffuse light from the row behind.

<!-- review notes
- sentence 4: support check: partial - The System 1 row gives slope 27°, portrait, shading angle 19°, but the passages do not state that shading angle depends on system layout (only implied by the definition).
- sentence 8: support check: partial - The passages say the row in front obscures part of the sky's diffuse light and direct shading occurs, but they do not explicitly state the mechanism as causing the lower-PR pattern; it is a reasonable inference.
-->
