---
id: meas:production-loss-alarm
type: Measurement
name: Production loss alarm
aliases:
- Plant with low PR
- Inverter with low PR
signals:
- point: model_403.InDCA
  unit: unit:A
  pattern: string current drops to zero (open circuit) or falls below its peers
- point: model_160.DCV
  unit: unit:V
  pattern: voltage step down when a substring is shorted
---
A production loss alarm fires when measured output falls below the production the monitoring system calculates from the system parameters, or when the site is producing almost nothing. Typical monitoring checks hourly whether the site is online and producing, and at the end of each day compares daily energy against the expected value, then runs diagnostics and sends an alert if it falls short. As a minimum, the monitoring system should raise alarms for plant shutdowns, inverter stops, and low performance ratio at plant or inverter level; a string without current is a recommended extra alarm. Expected output comes from a PV model driven by measured irradiance and module temperature, so a poorly tuned model or bad sensor data can produce false or missed alarms. Downtime is flagged when there is enough irradiance for the inverter to run but output is zero or below, and the remaining gap between expected and actual output is reported as residual loss. Soiling losses and snow accumulation losses show up as a gap between modeled and actual production, and snow shows up even while irradiance sensors report usable sunlight. Grid curtailment losses produce a flat output below the power the irradiance would support, so check setpoints and dispatch signals before treating the alarm as underperformance. Tracker wind stow losses cause short, weather-linked output dips that monthly reviews may file under availability, curtailment or weather variance, so compare stow telemetry with gust data.

<!-- review notes
- sentence 3: support check: partial - Minimum alarms also include loss of communication, and string without current is listed among best-practice extras; the statement omits loss of communication but is otherwise consistent.
- sentence 4: support check: partial - Passage says model uses measured irradiance and module temperature and needs a well-tuned model and accurate data for accurate results, but does not mention false or missed alarms.
- sentence 5: support check: partial - Downtime definition is stated, but residual loss is the model-vs-measured difference calculated when operating normally (and zero during downtime), not simply the remaining gap after downtime.
-->
