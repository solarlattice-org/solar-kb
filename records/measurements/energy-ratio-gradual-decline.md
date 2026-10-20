---
id: meas:energy-ratio-gradual-decline
type: Measurement
name: Gradual energy ratio decline
aliases:
- gradual performance loss
signals:
- point: model_103.WH
  unit: unit:W-HR
  pattern: daily AC energy falls steadily relative to model-expected energy over several days
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: measured irradiance used to compute expected energy; no matching irradiance drop
- point: model_303.TmpBOM
  unit: unit:DEG_C
  pattern: module temperature used as model input for expected energy
---
The energy ratio compares each day's measured energy with the expected energy from a full PV model, using measured irradiance and temperature. It is calculated for each inverter and each production meter. This signature is a slow, steady fall of that ratio over many days, not a sudden step. Soiling loss detection looks for this kind of gradual decline in the energy ratio. It typically needs five or more days of data and will not flag spans shorter than four days. Granular dust soiling causes this pattern during dry periods, often with partial or full recovery after real rain or washing, while the plant stays online. Dust loss may be uneven across a site, for example near roads, exposed soil, farming or construction. Over the long term, module aging also lowers energy output gradually. System-level decline can be larger than average module degradation because modules age at different rates and the weaker ones limit string current. The result is only reliable if the PV model is well tuned and the irradiance and temperature data are accurate.

<!-- review notes
- sentence 2: support check: partial - Passages describe soiling as a gradual decline in energy ratio/normalized production, but do not say it is not a sudden step or specify 'many days' for the ratio fall (the 'slow, steady' contrast is not stated).
- sentence 6: support check: partial - Passages support module aging causing energy loss and system decline exceeding average module degradation due to mismatch from weaker modules limiting string current, but 'gradually' for aging is only weakly implied (yearly degrade rate) and is not explicit.
-->
