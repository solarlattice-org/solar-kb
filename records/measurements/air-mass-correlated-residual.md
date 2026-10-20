---
id: meas:air-mass-correlated-residual
type: Measurement
name: Air-mass-correlated residual
signals:
- point: model_103.W
  unit: unit:W
  pattern: residual against modeled power varies with air mass, season and time of day
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: under- or over-performance remains after ordinary irradiance correction
---
This signature is a pattern in the gap between measured and modeled output that follows air mass. The plant can look like it is producing too little or too much even after the usual irradiance and temperature corrections. The residual often also tracks season, water in the atmosphere, aerosol conditions and module technology. It matters most when comparing different technologies or when a test was run during a narrow weather window. Amorphous silicon modules show this clearly: their short-circuit current per unit irradiance changes with air mass. A model with air mass as a parameter worked well for the month it was fitted to, but its bias grew when it was applied to other months. Filtering data by minimum sun elevation and clear-sky conditions keeps air mass and spectral differences small when comparing performance. Do not treat spectral correction as a catch-all for underperformance nobody can explain. A real spectral correction should make the residual pattern better structured and be tied to measured or modeled atmospheric conditions, using spectral response data for the specific module technology.

<!-- review notes
- sentence 1: support check: partial - Passages say the plant can appear to under- or overperform after irradiance and temperature corrections and that the signature is often correlated with air mass, but not that it is specifically a gap between measured and modeled output that follows air mass (air mass is one of several correlates).
- sentence 3: support check: partial - The passages say a-Si Isc/G varies with air mass and that the air-mass model worked for the fitted month but bias grew in other months, but 'clearly' is loosely supported and the passage frames this as a spectral-response assignment, so it is mostly supported with minor wording differences.
-->
