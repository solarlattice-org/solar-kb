---
id: concept:shading-loss
type: Concept
name: Shading loss
aliases:
- inter-row shading
- near shading
- row-to-row shading
- Shade loss
- mutual shading
category: Design
concept_kind: physics
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 1
    max: 5
    unit: unit:PERCENT
  conditions: Typical cumulative annual shading loss of PV systems
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h54
    h: df63666c4734
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h78
    h: df63666c4734
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions)
- claim_id: c2
  attr: typical_power_loss
  value:
    min: 20
    max: 30
    unit: unit:PERCENT
  conditions: Energy losses observed up to this level on rooftop or facade systems
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h54
    h: df63666c4734
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h78
    h: df63666c4734
  review: disputed
  review_note: possible conflict with c1 (same source; check the conditions)
  conflicts_with:
  - concept:shading-loss#c3
- claim_id: c3
  attr: typical_power_loss
  value:
    max: 1
    unit: unit:PERCENT
  conditions: Annual shading loss below which row spacing is generally considered acceptable in utility-scale
    design
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=7.2.3
    h: e4ddc70cfb8d
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
  review_note: 'support check: partial - Passage says less than 1% annual loss may deem row spacing acceptable,
    but not specifically ''utility-scale'' or ''generally'' considered; roughly matches.; review: the
    compiler-flagged conflict (concept:shading-loss#c2) is a scenario difference, resolved at review'
- claim_id: c4
  rel: related_to
  target: concept:ground-coverage-ratio
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=7.2.3
    h: e4ddc70cfb8d
  - src: src:alsoenergy-kb-additional-information-on-pv-system-model-processing
    loc: sec=front
    h: 53994d8c99ff
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:backtracking
  cite:
  - src: src:trn-training-industry-reports-and-guides-nrel-one-axis-trackers-improved-reliability-durability-perf
    loc: fig=50
    h: 9689b67c3732
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h5
    h: 206561d63ce8
  review: drafted
- claim_id: c6
  rel: related_to
  target: concept:half-cut-cells
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h103
    h: 5b4f784910a6
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h54
    h: df63666c4734
  review: drafted
- claim_id: c7
  rel: related_to
  target: concept:energy-loss-waterfall
  cite:
  - src: src:alsoenergy-kb-vi-performance-waterfall-overview
    loc: sec=h8
    h: 30e070dc9187
  - src: src:alsoenergy-kb-energy-loss-waterfall
    loc: sec=front
    h: b18a92c492b3
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c8
  rel: related_to
  target: concept:plane-of-array-irradiance
  cite:
  - src: src:man-alsoenergy-pv-model-powertrack-pv-shading-model
    loc: sec=h2
    h: 95447420b92d
  - src: src:man-alsoenergy-pv-model-powertrack-additional-info-on-pv-system-model-processing
    loc: sec=h4
    h: 8327a5f077ba
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c9
  rel: related_to
  target: concept:clear-sky-model
  cite:
  - src: src:man-alsoenergy-pv-model-powertrack-pv-shading-model
    loc: sec=h2
    h: 95447420b92d
  review: drafted
  review_note: 'support check: partial - Clear-sky model derives diffuse and albedo components used in
    the shade calculation, but the link is indirect.'
- claim_id: c10
  rel: related_to
  target: concept:expected-energy-model
  cite:
  - src: src:alsoenergy-kb-pv-shading-model
    loc: sec=front
    h: 11ff663ce925
  - src: src:iea-pvps-t13-07-2017
    loc: sec=2.4.1
    h: 641fdfeda657
  review: drafted
- claim_id: c11
  rel: related_to
  target: tool:pvsyst
  cite:
  - src: src:man-alsoenergy-pv-model-powertrack-model-training-article
    loc: sec=h3
    h: fcb1298a8c15
  - src: src:man-alsoenergy-pv-model-powertrack-pv-shading-model
    loc: sec=h1
    h: f71c92d11c6c
  review: drafted
- claim_id: c12
  rel: related_to
  target: arch:module-level-power-electronics
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h54
    h: df63666c4734
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h78
    h: df63666c4734
  review: drafted
- claim_id: c13
  rel: related_to
  target: comp:bypass-diode
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h54
    h: df63666c4734
  - src: src:iea-pvps-t13-19-2021
    loc: sec=2.2
    h: 97a00d084029
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c14
  rel: explains
  target: fm:bypass-diode-failure
  note: Hot spots from prolonged shading can lead to follow-up failures such as bypass diode failures.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h54
    h: df63666c4734
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h78
    h: df63666c4734
  review: drafted
- claim_id: c15
  rel: related_to
  target: stressor:partial-shading
  cite:
  - src: src:man-alsoenergy-pv-model-powertrack-pv-shading-model
    loc: sec=h2
    h: 95447420b92d
  - src: src:sma-doc-stpxx-us-41-iv-curve-ti-en-11
    loc: sec=h16
    h: 94bf052364e4
  review: drafted
- claim_id: c16
  rel: related_to
  target: symptom:inter-row-shading
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=7.2.3
    h: e4ddc70cfb8d
  - src: src:man-alsoenergy-pv-model-powertrack-model-training-article
    loc: sec=h3
    h: fcb1298a8c15
  review: drafted
- claim_id: c17
  rel: related_to
  target: meas:pr-drop-low-profile-angle
  cite:
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=4.2.1
    h: fc5f258c95cb
  review: drafted
- claim_id: c18
  rel: related_to
  target: fm:terrain-undulation-yield-losses
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h5
    h: 206561d63ce8
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=front
    h: 52c6d93eccc6
  review: drafted
- claim_id: c19
  rel: related_to
  target: mit:vegetation-management
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=50
    h: 91760d2225a2
  review: drafted
---
Shading loss is the energy lost when objects keep sunlight from reaching the modules, for example far horizons, trees, buildings, cabling, chimneys, or the next row of modules. Because cells and modules are wired in series, the power lost is much larger than the shaded area alone would suggest, and the actual result depends on string layout, MLPE, inverter MPPT behavior and shade-tolerant module types such as half-cut cells. Some inter-row shading always remains in large plants because shadows get very long early and late in the day, so row pitch and tilt are chosen as a trade-off against land use. The ground coverage ratio is part of that trade-off. On single-axis trackers, backtracking avoids east-west row shading, but uneven terrain can upset the backtracking geometry so that rows still shade each other. Monitoring platforms model shading as a reduction of plane-of-array irradiance, using either a shade table imported from PVsyst or a simple inter-row model built from pitch, tilt and module size. These irradiance-based models leave out the electrical effect of partial shading on modules and strings, so the energy loss they calculate is only approximate. In the field you can find shading by visual inspection, by comparing shaded and unshaded strings in monitoring data, or with shading simulations. Shade patterns change with the time of day and the season, and over the years as vegetation grows or new buildings go up. Shading on its own is not a safety problem. Prolonged shading can cause hot spots, though, which lead to burn marks, bypass diode failures or faster aging, so trimming vegetation and doing a shading analysis at the design stage are recommended.
