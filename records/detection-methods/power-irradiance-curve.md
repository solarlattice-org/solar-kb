---
id: method:power-irradiance-curve
type: DetectionMethod
name: Power vs irradiance analysis
aliases:
- performance curves
claims:
- claim_id: c1
  rel: produces
  target: meas:temperature-derated-output
  note: An overheating inverter cuts its power or shuts off to protect itself, often without reporting
    a derating status message. Analysing the power vs irradiance curve brings this behaviour to light.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=51.r1
    h: 52f99f2ab326
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=33.r1
    h: 44fc567b4d48
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c2
  rel: produces
  target: meas:power-irradiance-plateau
  note: Plotting measured AC output against in-plane irradiance shows inverter power limitation (clipping)
    as a flat cap above a certain specific irradiance level.
  cite:
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=4.2.2
    h: baaa36bbb1c3
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: fig=52
    h: 42f871f06665
  - src: src:iea-pvps-t13-22-2021
    loc: sec=B.2
    h: 5c54e661da25
  review: drafted
  review_note: 'support check: partial - Passages show inverter power limitation visible above an irradiance
    level in power vs irradiance plots, but don''t explicitly describe a flat constant ceiling.'
- claim_id: c3
  rel: produces
  target: meas:power-irradiance-outlier
  note: A scatter plot of power against plane-of-array irradiance reveals outlier data pairs. These can
    be removed by statistical filtering.
  cite:
  - src: src:iea-pvps-t13-22-2021
    loc: sec=B.2
    h: 5c54e661da25
  - src: src:iea-pvps-t13-22-2021
    loc: sec=h17
    h: 5714454c65c6
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c4
  attr: typical_power_loss
  value:
    nominal: 0.05
    unit: unit:PERCENT
  conditions: Annual energy loss from inverter power limitation, deduced by PR extrapolation from measured
    5-min power vs irradiance data (PR 200-900 W/m² vs 900-1200 W/m²) for one example system
  cite:
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=4.2.2
    h: baaa36bbb1c3
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c5 (same source; check the conditions)
- claim_id: c5
  attr: typical_power_loss
  value:
    nominal: 0.03
    unit: unit:PERCENT
  conditions: Inverter limitation loss predicted by simulation for the same example system at a PV to
    inverter power ratio of 1.12
  cite:
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=4.2.2
    h: baaa36bbb1c3
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions)
---
Power vs irradiance analysis plots the measured output power of an inverter or plant against the in-plane irradiance measured at the same time, using monitoring data. It is the recommended way to check for inverter overheating. An overheating inverter reduces its power or shuts off to protect itself and does not always report a power reduction or derating message. Inverter power limitation, or clipping, shows up as a flat cap in the curve above a certain irradiance level. The loss from this limitation cannot be measured directly. It can be estimated from measured values by comparing the performance ratio in the low and high irradiance ranges. The same plot also shows outliers in the power-irradiance data, which should be filtered out before further analysis. Monitoring is the main way to detect inverter overheating, with IV curve tracing and infrared thermography as additional checks. The result depends on irradiance sensor quality, so follow the recommended limits on irradiance uncertainty and sensor alignment.

<!-- review notes
- sentence 3: support check: partial - Limitation is said to be visible above an irradiance level and clipping is detected, but 'flat cap' shape is not explicitly stated.
- sentence 5: support check: partial - Outliers are shown in power-irradiance plots and statistical filtering is described, but the 'before further analysis' for this same plot is only loosely supported (in PLR context).
- sentence 7: support check: partial - The table gives irradiance uncertainty and sensor alignment limits, but nothing states the result depends on sensor quality for this analysis.
-->
