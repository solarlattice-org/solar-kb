---
id: meas:zero-power-at-irradiance
type: Measurement
name: Zero power with irradiance
aliases:
- Downtime Loss
- System outages
signals:
- point: model_103.W
  unit: unit:W
  pattern: zero or very low while irradiance is sufficient
- point: model_302.GHI
  unit: unit:W-PER-M2
  pattern: sufficient irradiance at the same time
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: irradiance remains present while inverter output is zero
---
This signature is output power at or below zero during a period when there is enough irradiance for the inverter to run. One monitoring rule marks an inverter as down when it reports zero energy production, or stops communicating, while GHI is at least 100 W/m2. The rule is skipped for any data point that has no irradiance reading. Monitoring software filters the early morning and evening hours so that low sun is not falsely flagged as downtime. Performance-loss analyses remove these outage periods with a low-power filter. If the AC voltage on the meter linked to the inverter is also zero, the loss is classed as the grid meter being offline rather than as inverter downtime. Inverters shut down automatically when the AC grid fails, when PV voltage and power fall below the set values, or when the ambient temperature goes outside its normal range. An inverter also disconnects from the grid when the grid frequency is outside the permitted range, which gives zero output even in full sun. Check for a manual or app shutdown, or for an active power limit set to zero with the stop option enabled, before assuming a fault.

<!-- review notes
- sentence 2: support check: partial - The rule text supports GHI ≥100 W/m2, not communicating or not producing, and skipping points without irradiance. However, it says the test fails on zero energy production data points, and the 'zero energy production' wording is stated only for the failure, not for stops communicating explicitly in the test.
- sentence 3: support check: partial - Early morning/evening filtering to avoid false downtime is stated, but the passages don't say performance-loss analyses remove outage periods with a low-power filter; the low-power filter is only described as a general data-thresholding method.
- sentence 6: support check: partial - The passages state the inverter disconnects when frequency is out of range, but do not say this gives zero output even in full sun (implied only).
- sentence 7: support check: partial - Passages describe manual/app shutdown and the shutdown-at-0%-power-limit switch, but they don't give the advice to check these before assuming a fault.
-->
