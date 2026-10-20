---
id: method:shade-model-comparison
type: DetectionMethod
name: Shade model comparison
claims:
- claim_id: c1
  rel: produces
  target: meas:motor-block-aligned-loss
  note: Comparing shade-model output against normalized row or inverter production in morning and afternoon
    windows shows losses that repeat with sun position, peak at low sun angles, and cluster at motor block
    boundaries, grade breaks and swales.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=front
    h: 52c6d93eccc6
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h2
    h: 0eaaad46eb44
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h4
    h: 7ebb164fa9e1
  review: drafted
  review_note: 'support check: partial - Passages support repeatable, low-sun-angle losses clustered at
    motor block boundaries, grade breaks and swales, and comparison of shade-model output with production;
    the specific signal claims (inverter W below shade-model expectation, InDCA lower in rows) are only
    loosely implied.'
- claim_id: c2
  rel: produces
  target: meas:model-explained-production-gap
  note: Actual output is compared with modelled output; consistent repeated underperformance patterns
    are attributed to shading. The shading model reduces expected plane-of-array irradiance as a percentage
    loss.
  cite:
  - src: src:iea-pvps-t13-19-2021
    loc: sec=2.2
    h: 97a00d084029
  - src: src:alsoenergy-kb-pv-shading-model
    loc: sec=front
    h: 11ff663ce925
  review: drafted
---
Shade model comparison checks the output of a shading model against measured row or inverter production. Its purpose is to show whether the losses come from shading geometry. Shading models are usually built during site design. They can be a simple layout of rectangular rows or a full 3D physical model, and a shade table exported from PVsyst can be loaded into the monitoring platform. For terrain undulation yield losses, compare the terrain-following design data, the motor block boundaries, the backtracking settings and the shade-model output. Check these against normalized production in the morning and afternoon windows. A typical finding is a loss that repeats with sun position, is strongest at low sun angles, and clusters near motor block boundaries, grade breaks and swales. Do not assume a tracker is fine just because it follows its commanded angle. On rolling ground, the command itself can cause the loss if the terrain model, the backtracking algorithm or the motor block layout is too coarse. The model calculates shade loss as a percentage of irradiance. It ignores how partially shaded modules interact electrically and how the wiring and inverters respond, so the energy-loss result is only approximate. A shade record made at commissioning gives a baseline for later comparisons. It also confirms whether the design shading assumptions match the built system.

<!-- review notes
- sentence 1: support check: partial - Passages describe comparing shade-model output with normalized row/inverter production, but do not state the purpose as showing whether losses come from shading geometry.
-->
