---
id: method:available-power-reconstruction
type: DetectionMethod
name: Available power reconstruction
aliases:
- available-power estimation
claims:
- claim_id: c1
  rel: produces
  target: meas:flat-output-below-available-power
  note: Available power is rebuilt from irradiance, temperature, inverter status, clipping state and modeled
    plant capability, then compared with meter output and plant controller limits. Curtailment shows up
    as exported power held below this estimate, even though availability and equipment health stay normal.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=front
    h: 874f05be8763
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h2
    h: 5fdb7733fc7c
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h6
    h: 08e6be358742
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
---
Available power reconstruction estimates how much power the plant could have produced at a given time, so that this can be compared with what it actually exported. The estimate is built from irradiance, temperature, inverter status, clipping state and the modeled capability of the plant. The result is then compared with meter output and with plant controller limits, plant setpoints, inverter active power limits, grid operator dispatch and curtailment flags. It is the main way to confirm grid curtailment losses, where exported power is held below what the plant could deliver even though availability and equipment health are normal. Once constrained intervals are found, each one should be given a cause: grid dispatch, export limit, economic curtailment, plant controller behavior, battery charging limit, outage or telemetry error. At sites with storage, also check whether the curtailed PV energy was used to charge the battery, was clipped, or was lost. Without this check, a low performance ratio during curtailed hours can be mistaken for a fault in the modules, inverters or trackers, and teams may end up chasing equipment problems that do not exist.

<!-- review notes
- sentence 4: support check: partial - The passages describe the comparison as a detection method for curtailment, but nothing says it is the main way to confirm it.
- sentence 7: support check: partial - The passages say low PR in curtailed hours may reflect grid instructions and that ignoring curtailment-aware KPIs leads to chasing false equipment problems, but they don't tie this to the available-power check specifically.
-->
