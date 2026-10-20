---
id: method:normalized-output-trend
type: DetectionMethod
name: Normalized output trend analysis
aliases:
- normalized production trends
- long-term normalized plant output
claims:
- claim_id: c1
  rel: produces
  target: meas:normalized-output-decline
  note: Long-term normalized plant output that falls faster than the average module degradation points
    to mismatch-driven system degradation.
  cite:
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=front
    h: ff0c8c5f07cc
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h2
    h: 14c4627b4866
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h5
    h: 994460afbabc
  review: drafted
  review_note: 'support check: partial - Passages say long-term normalized output is compared to separate
    mismatch-driven system degradation from module degradation, but don''t mention the specific signals
    (WH, POAI) or irradiance/installed-power normalization details.'
- claim_id: c2
  rel: produces
  target: meas:normalized-voltage-deviation
  note: Array voltage normalized to MPP voltage and plotted against module temperature; samples falling
    below the usual linear relationship showed partial shading that yield and PR plots did not reveal.
  cite:
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=h53
    h: 349876638b16
  review: drafted
- claim_id: c3
  rel: produces
  target: meas:inverter-normalized-yield-spread
  note: Output is normalized to module area or installed power so that inverters or sub-arrays can be
    compared. A unit that departs from the others is flagged.
  cite:
  - src: src:iea-pvps-t13-07-2017
    loc: sec=1
    h: 6071f58ccb27
  - src: src:iea-pvps-t13-19-2021
    loc: sec=h92
    h: 4c7181b84063
  review: drafted
- claim_id: c4
  attr: degradation_rate
  value:
    nominal: 0.1
    unit: unit:PERCENT-PER-YR
  conditions: Extra system degradation that some independent engineers add on top of the module degradation
    rate to cover mismatch from uneven module aging. It is a modeling allowance, not a universal rule.
  cite:
  - src: src:pv-root-cause-system-vs-module-degradation
    loc: sec=h6
    h: 03fbe99d08d3
  review: drafted
---
Normalized output trend analysis follows plant, inverter or string output over a long period after scaling it so that the values can be compared. Output is normalized by dividing it by the module area or the installed power, which lets inverters of different size or loading be compared directly. Used together with string or inverter trends, IV curve data and module test results, it helps separate average module degradation from the extra system degradation caused by mismatch. Comparing units only with each other means the environmental conditions cancel out, so the method is not thrown off by sensor drift or missing sensor data. Normalized trends also show soiling losses: look for output falling during dry periods that availability, clipping, curtailment or irradiance sensor problems do not explain. Small shading effects may not show up in yield or performance ratio trends, so normalized array voltage plotted against module temperature can be a more sensitive check. Before trusting the results, check the data quality, meaning the outliers, missing points and gaps, because these can make some analyses unreliable or impossible.
