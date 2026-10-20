---
id: meas:inverter-normalized-yield-spread
type: Measurement
name: Spread in normalized inverter yield
signals:
- point: model_103.WH
  unit: unit:W-HR
  pattern: one inverter's energy per installed kWp sits below its peers
- point: model_103.W
  unit: unit:W
  pattern: Irradiance-normalized output differs between inverters or zones of the same plant
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: Used as the normalization reference; irradiance itself is uniform
---
Monitoring reports can list each inverter's production next to its predicted and normalized energy and its installed capacity, so inverters can be compared directly. Terrain undulation losses show up as underperformance that repeats with sun position. It is strongest at low sun angles and clusters at motor block boundaries, grade breaks and rolling parts of the array. To check for terrain effects, compare normalized row or inverter output in morning and afternoon windows against motor block boundaries, backtracking settings and the shade model. Before blaming terrain, separate backtracking intervals from curtailment, clipping, outages and inverter constraints. This shows whether the loss follows the terrain rather than an equipment failure. Granular dust soiling can also spread unevenly across a site, for example near roads, exposed soil, farming or construction, and at row edges. Trends at string or inverter level, compared with module test results, help separate average module degradation from extra system degradation caused by mismatch between modules.
