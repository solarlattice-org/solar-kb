---
id: meas:array-ratio-out-of-range
type: Measurement
name: Array ratio out of range
aliases:
- AR
signals:
- point: model_103.W
  unit: unit:W
  pattern: power relative to irradiance falls outside the valid range learned by regression for several
    consecutive samples
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: used as the irradiance reference for the ratio; data with low irradiance filtered out
---
The array ratio compares an array's measured power with the irradiance it receives. Its valid range is learned from that array's own history. In the cited approach, regression on three months of past power and irradiance data sets the normal range for each array. A fault is flagged when the array ratio stays outside its normal range for a set number of readings in a row, not after a single outlier. Power and irradiance were sampled every 5 minutes. Readings taken at irradiance below 250 W/m2, or during abrupt changes, were filtered out before the check. The method needs only irradiance and power data, with no extra sensors, so faults can be detected in near real time. A rule-based system then diagnoses the cause. Causes it covers include partial shading, an inverter fault, an inverter booting late, an overheated inverter, a blown fuse and an open string circuit. For a new plant with no history yet, expected power is estimated from the past few days of measurements with a nearest-neighbour method.

<!-- review notes
- sentence 1: support check: partial - Valid range learned from the array's own past data is stated, but the passage never defines the array ratio as measured power compared with received irradiance (it only lists power and irradiance as the inputs).
-->
