---
id: meas:performance-index-below-unity
type: Measurement
name: Performance index below unity
aliases:
- Performance Index
- PI
- energy performance index
- EPI
- power performance index
- Self Health
signals:
- point: model_103.WH
  unit: unit:W-HR
  pattern: ratio of actual to weather-predicted energy falls below 1
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: used as the irradiance input to the model the measured energy is compared against
---
A performance index is measured power or energy divided by expected power or energy. A value below unity means the system produced less than the model predicted. The expected value comes from measured weather and irradiance run through a performance model that the stakeholders have agreed on, often a contractual model or digital twin. A healthy system should show a power or energy performance index close to unity, and the index stays comparable across seasons, locations and unusual weather. Monitoring platforms often calculate the index hourly and raise an alert when it stays below a set threshold for longer than a set number of hours. This flags meters or inverters that are underperforming. Daily or monthly trends of measured energy, modeled energy and the index can be charted to compare a site or component against its expected output. Not every shortfall is a hardware fault. Part of the gap between measured and modeled energy may come from data collection problems such as spikes or communication loss, or from small errors in the model. Do not explain away unexplained underperformance with spectral correction. Use it only when measured or modeled atmospheric conditions support it.

<!-- review notes
- sentence 1: support check: partial - The ratio of measured to expected/modeled power or energy is stated, but the passages never say that a value below unity means the system produced less than predicted (only that values should ideally be near unity).
- sentence 3: support check: partial - Passages say both indices ideally are close to unity and give more consistent metrics across seasons, locations and weather anomalies, but 'healthy system' and 'comparable' are slightly stronger than 'more likely to deliver consistent metrics'.
-->
