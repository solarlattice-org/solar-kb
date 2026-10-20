---
id: method:bess-charging-review
type: DetectionMethod
name: Battery charging review
aliases:
- BESS charging behavior
claims:
- claim_id: c1
  rel: produces
  target: meas:curtailed-energy-not-stored
  note: At PV-plus-storage sites, the review sorts curtailed PV energy into charged, clipped or abandoned.
    Energy can only be recovered if the battery has capacity, power headroom, control permission and an
    operating objective that values the charge.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h6
    h: 08e6be358742
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h5
    h: d55aa663f3f5
  review: drafted
---
A battery charging review checks how a PV-plus-storage plant's battery behaved during periods when export was curtailed. It is one of the data comparisons used to detect grid curtailment yield losses. Compare battery charging behavior with plant setpoints, inverter active power limits, grid operator dispatch, meter output, available power estimated from irradiance, and curtailment flags. Some curtailed energy can be recovered through DC-coupled or AC-coupled battery charging. This only works if the battery has spare capacity, power headroom, permission from the controls, and an operating objective that values the charge. For each constrained interval, record whether the curtailed PV energy was charged into the battery, clipped, or abandoned. Intervals limited by battery charging should be classified separately from grid dispatch, export limits, economic curtailment, controller behavior, outages, and telemetry errors. Curtailment strongly lowers the performance ratio. Without curtailment-aware metrics, teams may chase equipment faults that do not exist and miss real chances to make better use of the battery. If the review shows the battery was not using curtailed energy, a likely next step is to tune the battery charging strategy.

<!-- review notes
- sentence 1: support check: partial - BESS charging behavior is listed among detection comparisons, but passages don't describe a 'battery charging review' specifically as checking battery behavior during export-curtailed periods.
- sentence 5: support check: partial - Passages say heavy curtailment distorts PR and curtailment-aware KPIs avoid chasing false equipment problems and missing opportunities, but don't say it 'strongly lowers' PR or specifically battery use.
- sentence 6: support check: partial - Mitigation includes tuning BESS charging strategy where applicable, but passages don't link it specifically to a review finding that the battery wasn't using curtailed energy.
-->
