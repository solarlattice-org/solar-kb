---
id: meas:power-irradiance-outlier
type: Measurement
name: Power-irradiance outlier
aliases:
- non-realistic power-irradiance pairs
- outlier in power-irradiance pairs
signals:
- point: model_103.W
  unit: unit:W
  pattern: points lying far off the main power-irradiance cloud
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: irradiance paired with anomalous power
---
Over a wide irradiance range, power follows plane-of-array irradiance almost linearly. A power-irradiance outlier is a data point that falls well away from that line. The pattern is easiest to see on a scatter plot of power against plane-of-array irradiance, whether the irradiance is measured or modelled. Such plots can show many outliers, extreme outliers, and inverter clipping in the same dataset. Sensor shadowing, sensor misalignment and similar measurement problems can create unrealistic pairs of power and irradiance values. During a system outage, power stays low even while irradiance is high. Power readings that are unreasonably high are another kind of outlier. Shading, soiling and snow on the modules can lower power without lowering the reading of an irradiance sensor that is kept clean or cleared of snow. When converted to performance ratio, these periods show up as low outlying values. Analysts usually remove these points with interquartile-range limits around the median or mode of the performance metric. They may also apply a high irradiance cutoff, typically set at 1200 W/m2, to drop measurement errors. Removing these outliers matters most for metrics tied directly to irradiance, such as performance ratio. Otherwise the outliers distort the calculated performance loss rate.

<!-- review notes
- sentence 2: support check: partial - Figure 27 shows power vs POA irradiance plots (measured/modelled) with outliers, extreme outliers and clipping, but 'pattern is easiest to see' on a scatter plot is not stated.
- sentence 7: support check: partial - Passage says outlier accounting is crucial for irradiance-related metrics like PR, but does not explicitly say outliers otherwise distort the PLR.
-->
