---
id: meas:energy-ratio-out-of-range
type: Measurement
name: Energy ratio out of range
aliases:
- Past 24h Actual vs Expected
signals:
- point: model_103.WH
  unit: unit:W-HR
  pattern: daily inverter energy outside the accepted band of model-expected energy
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: measured irradiance input to the expected-energy model
---
The energy ratio compares the daily energy a device actually produced with the energy the full PV model expects from measured irradiance and temperature. Each inverter and each production meter is checked on its own. In this monitoring tool, a device passes when its energy is between 70% and 110% of expected. A ratio outside that band is out of range and points to a problem. The check is switched off during snow, so snow days should not raise this flag. The expected value is only trustworthy with a well-tuned PV model and accurate irradiance and temperature data. Before you look for a plant fault, check the model and the sensors. A slow decline in the energy ratio over several days is how soiling losses are detected. This usually needs 5 or more days of data, and soiling is not detected over spans shorter than 4 days. Monitoring dashboards may also show the ratio of actual to expected energy for the last 24 hours. A monthly site-level version, IEER, takes the ratio of measured to estimated AC energy and divides it by the ratio of measured to estimated insolation.

<!-- review notes
- sentence 2: support check: partial - The 70%-110% pass band is stated, but the passage doesn't say an out-of-range ratio points to a problem.
- sentence 3: support check: partial - The title says 'Disabled by snow', but the passage doesn't explain that snow days won't raise the flag.
- sentence 4: support check: partial - The passage says a well-tuned model and accurate irradiance and temperature data are required for accurate expected values; the advice to check the model and sensors before looking for plant faults is not stated.
- sentence 5: support check: partial - The passage supports detection via energy ratio showing gradual loss, 5 or more days typically, and no detection under 4 days; it doesn't say 'slow decline over several days' exactly but this is close, though the claim that this is how soiling is detected is stated.
-->
