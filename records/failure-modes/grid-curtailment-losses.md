---
id: fm:grid-curtailment-losses
type: FailureMode
name: Grid Curtailment Yield Losses
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:grid-operator-dispatch
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h4
    h: 576525a653a1
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-16
- claim_id: c2
  rel: caused_by
  target: stressor:interconnection-constraint
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h4
    h: 576525a653a1
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c3
  rel: caused_by
  target: stressor:plant-controller-command
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h4
    h: 576525a653a1
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c4
  rel: caused_by
  target: stressor:negative-pricing
  note: Economic curtailment as a response to negative prices.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h4
    h: 576525a653a1
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c5
  rel: caused_by
  target: stressor:site-export-cap
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h4
    h: 576525a653a1
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c6
  rel: presents_as
  target: symptom:flat-capped-output
  note: Output sits at a flat or controlled level under the power the irradiance would support.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h4
    h: 576525a653a1
  review: drafted
- claim_id: c7
  rel: presents_as
  target: symptom:low-output-despite-irradiance
  note: Export is held below available plant power while inverter and tracker availability and equipment
    health look normal.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h2
    h: 5fdb7733fc7c
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h4
    h: 576525a653a1
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c8
  rel: presents_as
  target: symptom:low-performance-ratio
  note: Low PR in curtailed hours reflects grid instructions more than module, inverter or tracker health.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h5
    h: d55aa663f3f5
  review: drafted
- claim_id: c9
  rel: detected_by
  target: method:setpoint-dispatch-review
  note: Review plant setpoints, inverter active power limits, grid operator dispatch signals and curtailment
    flags.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h2
    h: 5fdb7733fc7c
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=front
    h: 874f05be8763
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h4
    h: 576525a653a1
  review: drafted
- claim_id: c10
  rel: detected_by
  target: method:available-power-reconstruction
  note: Rebuild available power from irradiance, temperature, inverter status, clipping state and modeled
    capability, then compare with meter output and controller limits.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h6
    h: 08e6be358742
  review: drafted
- claim_id: c11
  rel: detected_by
  target: method:constrained-interval-classification
  note: Assign each constrained interval to grid dispatch, export limit, economic curtailment, controller
    behavior, BESS charging limit, outage or telemetry error.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h6
    h: 08e6be358742
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c12
  rel: detected_by
  target: method:bess-charging-review
  note: At storage sites, check whether curtailed PV energy was charged, clipped or abandoned.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h2
    h: 5fdb7733fc7c
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h6
    h: 08e6be358742
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c13
  rel: mitigated_by
  target: mit:separate-curtailment-tracking
  note: Book curtailment apart from equipment losses.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h2
    h: 5fdb7733fc7c
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=front
    h: 874f05be8763
  review: drafted
- claim_id: c14
  rel: mitigated_by
  target: mit:available-power-estimation
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h2
    h: 5fdb7733fc7c
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=front
    h: 874f05be8763
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c15
  rel: mitigated_by
  target: mit:bess-charging-strategy
  note: Curtailed energy can be partly recovered by DC- or AC-coupled charging only if the battery has
    capacity, power headroom, control permission and an objective that values the charge.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h2
    h: 5fdb7733fc7c
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h5
    h: d55aa663f3f5
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c16
  rel: mitigated_by
  target: mit:curtailment-aware-kpis
  note: Avoids chasing false equipment faults at plants that are often constrained.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h2
    h: 5fdb7733fc7c
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h7
    h: 779bcf6ddc67
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
---
Grid curtailment loss happens when the plant could produce more power than it is allowed to export, so available solar energy goes unused. The limit can come from grid operator dispatch, an interconnection constraint, a plant controller command, a response to negative prices, or a site export cap. In the data it looks like a flat or controlled output level below what irradiance would support, while inverter and tracker availability look normal, so it is easily mistaken for underperformance. To confirm it, reconstruct available power from irradiance, temperature, inverter status, clipping state and modeled capability, and compare it with meter output, plant controller limits, dispatch signals and curtailment flags. Sort each constrained interval by cause, such as grid dispatch, export limit, economic curtailment, controller behavior, battery charging limit, outage or telemetry error, and at storage sites check whether curtailed energy was charged, clipped or abandoned. Track curtailment separately from equipment losses and use performance metrics built for curtailed plants, because a low performance ratio in curtailed hours does not mean the equipment is unhealthy. Where there is a battery, adjust the charging strategy so it can absorb curtailed energy when it has spare capacity and power headroom.

<!-- review notes
- sentence 7: support check: partial - Tuning BESS charging strategy and the recovery conditions (capacity, headroom) are stated, but the passages say only that some curtailed energy may be recoverable, not that the strategy should be adjusted to absorb it whenever spare capacity exists.
-->
