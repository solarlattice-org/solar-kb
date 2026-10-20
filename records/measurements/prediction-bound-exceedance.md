---
id: meas:prediction-bound-exceedance
type: Measurement
name: Output outside predicted bounds
signals:
- point: model_103.W
  unit: unit:W
  pattern: measured AC power falls below the lower bound (or above the upper bound) of the model-predicted
    normal range
---
This signature shows up when measured AC power falls outside a confidence interval. A trained classifier learns this interval from inverter parameters such as AC voltage and AC current. A fault can be predicted when the AC power keeps drifting further outside the expected interval over time. A single small excursion is not enough. In the prediction method, the energy a system should produce is compared with what it actually delivers. The system is classified as faulty when actual output is significantly below expectation. The prediction comes from a machine-learning model, sometimes combined with a single-diode or double-diode PV model. It uses past electrical behavior and weather data from commercial stations or on-site sensors. The accuracy of the prediction is uncertain, so compare performance with predictions over a period of time before declaring a system underperforming. Predictions are more accurate when output is high. Early morning and late afternoon data may be filtered out or ignored. If the system produces nothing while the model predicts output from incoming irradiance and there is no significant snow, the gap is booked as downtime loss. Once the cause of a flagged deviation is found, the classifier can learn to sort later deviations by fault type.

<!-- review notes
- sentence 1: support check: partial - Passage says classifier learns expected AC power from inverter parameters via a confidence interval and flags deviations, but a fault is predicted from growing deviations over time, not simply any single outside-interval reading.
- sentence 2: support check: partial - Larger and larger deviations over time predict a fault is stated; the claim that a single small excursion is not enough is an inference not explicitly stated.
-->
