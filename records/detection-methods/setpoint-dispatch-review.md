---
id: method:setpoint-dispatch-review
type: DetectionMethod
name: Setpoint and dispatch review
claims:
- claim_id: c1
  rel: produces
  target: meas:export-below-available-power
  note: When setpoints and dispatch are reviewed, a flat or controlled output level below irradiance-supported
    available power is linked to an active limit. Inverter and tracker availability can still look normal.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h4
    h: 576525a653a1
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=front
    h: 874f05be8763
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h2
    h: 5fdb7733fc7c
  review: drafted
---
Setpoint and dispatch review checks whether low plant output was caused by an imposed limit rather than an equipment problem. The reviewer compares plant setpoints, inverter active power limits, grid operator dispatch and meter output with the available power supported by irradiance, plus battery charging behavior and curtailment flags. Available power is first rebuilt from irradiance, temperature, inverter status, clipping state and modeled plant capability, then checked against meter output and plant controller limits. Each constrained interval is then given a cause: grid dispatch, export limit, economic curtailment, plant controller behavior, battery charging limit, outage or telemetry error. The method confirms grid curtailment yield losses, which show up as a flat or controlled output level below the power the plant could produce. Without this review, curtailment is easy to mistake for underperformance because inverter and tracker availability can look normal. On frequently constrained plants, curtailment-aware performance measures help crews avoid chasing equipment faults that do not exist.

<!-- review notes
- sentence 1: support check: partial - Passages say curtailment is misclassified as underperformance unless setpoints and dispatch are reviewed, but don't explicitly describe the review as checking imposed limit versus equipment problem, though this is strongly implied.
- sentence 5: support check: partial - The signature is described as flat/controlled output below available power, but the passages do not say a method 'confirms' curtailment losses.
-->
