---
id: concept:curtailment
type: Concept
name: Curtailment
aliases:
- grid curtailment
- economic curtailment
category: Grid
concept_kind: market
claims:
- claim_id: c1
  rel: explains
  target: fm:grid-curtailment-losses
  note: Curtailment holds export below what the plant could produce, so realized energy drops even though
    equipment is healthy.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h1
    h: 158275ff7629
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h2
    h: 5fdb7733fc7c
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h4
    h: 576525a653a1
  review: drafted
- claim_id: c2
  rel: explains
  target: meas:flat-output-below-available-power
  note: Under curtailment, output sits flat or at a controlled level below the power the irradiance would
    support.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h4
    h: 576525a653a1
  review: drafted
- claim_id: c3
  rel: explains
  target: symptom:low-performance-ratio
  note: A low PR during curtailed hours may come from grid instructions, not from module, inverter or
    tracker health.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h5
    h: d55aa663f3f5
  review: drafted
- claim_id: c4
  rel: related_to
  target: metric:performance-ratio
  note: The usual approach is to exclude curtailed periods and calculate a non-curtailed PR. This needs
    careful analysis when curtailment applies more than 50% of the time.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h5
    h: d55aa663f3f5
  - src: src:iea-pvps-t13-25-2022
    loc: sec=h24
    h: 68d475d606d5
  review: drafted
- claim_id: c5
  rel: related_to
  target: stressor:grid-operator-dispatch
  note: One possible source of the limit.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h4
    h: 576525a653a1
  - src: src:iea-pvps-t13-25-2022
    loc: sec=h24
    h: 68d475d606d5
  review: drafted
- claim_id: c6
  rel: related_to
  target: stressor:interconnection-constraint
  note: One possible source of the limit.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h4
    h: 576525a653a1
  review: drafted
- claim_id: c7
  rel: related_to
  target: stressor:plant-controller-command
  note: One possible source of the limit.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h4
    h: 576525a653a1
  review: drafted
- claim_id: c8
  rel: related_to
  target: stressor:negative-pricing
  note: Curtailment can be a response to negative prices.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h4
    h: 576525a653a1
  review: drafted
- claim_id: c9
  rel: related_to
  target: stressor:site-export-cap
  note: One possible source of the limit.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h4
    h: 576525a653a1
  review: drafted
- claim_id: c10
  rel: related_to
  target: func:limit-active-power
  note: Curtailment loss occurs when the inverters are commanded to limit their power output.
  cite:
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: tbl=10.r3
    h: 7bfdbf807e8d
  - src: src:man-alsoenergy-pv-model-powertrack-pv-model-losses
    loc: sec=h5
    h: 3b77a534f0f4
  review: drafted
- claim_id: c11
  rel: related_to
  target: fm:inverter-clipping
  note: Both inverter saturation and curtailment produce capped output. Clipping state is one input when
    reconstructing available power.
  cite:
  - src: src:iea-pvps-t13-22-2021
    loc: sec=1.2.3
    h: 426525e43b7d
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h6
    h: 08e6be358742
  review: drafted
  review_note: 'support check: partial - Saturation and curtailment are discussed and clipping state is
    an input to available power reconstruction, but the passages don''t state both produce capped output
    as a relation.'
- claim_id: c12
  rel: related_to
  target: metric:availability
  note: Proactive curtailment can reduce availability.
  cite:
  - src: src:iea-pvps-t13-22-2021
    loc: sec=1.2.3
    h: 426525e43b7d
  review: drafted
- claim_id: c13
  rel: related_to
  target: method:available-power-reconstruction
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h6
    h: 08e6be358742
  review: drafted
- claim_id: c14
  rel: related_to
  target: mit:curtailment-aware-kpis
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h2
    h: 5fdb7733fc7c
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h7
    h: 779bcf6ddc67
  review: drafted
- claim_id: c15
  rel: related_to
  target: mit:available-power-estimation
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h2
    h: 5fdb7733fc7c
  review: drafted
- claim_id: c16
  rel: related_to
  target: mit:bess-charging-strategy
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h2
    h: 5fdb7733fc7c
  review: drafted
- claim_id: c17
  rel: related_to
  target: arch:dc-coupled-storage
  note: Some curtailed energy can be recovered through battery charging if the battery has capacity, headroom,
    control permission and an objective that values the charge.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h5
    h: d55aa663f3f5
  review: drafted
- claim_id: c18
  rel: related_to
  target: arch:ac-coupled-storage
  note: Some curtailed energy can be recovered through battery charging under the same conditions.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h5
    h: d55aa663f3f5
  review: drafted
- claim_id: c19
  rel: related_to
  target: meas:curtailed-energy-not-stored
  note: At storage sites, track whether curtailed PV energy was charged, clipped or abandoned.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h6
    h: 08e6be358742
  review: drafted
- claim_id: c20
  rel: related_to
  target: tool:alsoenergy-powertrack
  note: PowerTrack calculates curtailment loss as expected output minus actual output while the site is
    following the control setpoint.
  cite:
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: tbl=10.r3
    h: 7bfdbf807e8d
  - src: src:man-alsoenergy-pv-model-powertrack-pv-model-losses
    loc: sec=h5
    h: 3b77a534f0f4
  - src: src:alsoenergy-kb-pv-model-losses
    loc: sec=front
    h: 10001d881d82
  review: drafted
---
Curtailment means a PV plant is allowed to export less power than it could actually produce. The limit can come from grid operator dispatch, an interconnection constraint, a plant controller command, a response to negative prices, or a site export cap. In the data, output stays flat or at a controlled level below what the irradiance would support, while inverter and tracker availability look normal. Because the equipment is healthy, curtailment is easy to mistake for underperformance, and it pulls down the performance ratio during the curtailed hours. To diagnose it, rebuild the available power from irradiance, temperature, inverter status and clipping state. Compare that with meter output, setpoints and dispatch signals, then sort each constrained interval by cause. Monitoring tools such as PowerTrack detect curtailment from the control signal sent to the inverters. They count the loss as expected output minus actual output only while the plant is following its setpoint. At PV-plus-storage sites, some curtailed energy can go into a DC-coupled or AC-coupled battery. This only works if the battery has room, power headroom, control permission and an objective that values the charge. Track curtailment separately from equipment loss and use curtailment-aware KPIs, so crews do not chase equipment faults that are not there.
