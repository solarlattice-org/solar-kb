---
id: metric:mppt-efficiency
type: Metric
name: MPPT efficiency
aliases:
- MPP adaptation efficiency
- tracking efficiency
- MPP tracking efficiency
- Static MPPT efficiency
- MPPT efficiency, static
category: Inverters
---
MPPT efficiency shows how well an inverter's maximum power point tracker keeps the PV array at its true maximum power point. Maximum power point tracking is the technique an inverter uses to get the most power out of the array. It is needed because the array's output depends in a non-linear way on irradiance, temperature and resistance, which gives the I-V curve its shape. The metric is the array's actual operating power divided by the true maximum power taken from the I-V curve. To check it in the field, run the system under steady conditions and record the array's operating voltage and power. Then disconnect the array straight away and trace its I-V curve to find the true maximum power. Tracking is not equally good on every inverter, so the shortfall shows up as an MPP tracking loss in plant energy-loss accounting. Datasheets give MPPT efficiency as a percentage, often labelled as a static value. One microinverter datasheet gives a weighted static MPPT efficiency and cites EN 50530 as its reference.

<!-- review notes
- sentence 5: support check: partial - u14 says different inverters track with varying efficiency and lists MPP tracking loss, but doesn't explicitly say the shortfall appears as that loss in accounting beyond the loss entry itself.
-->
