---
id: method:performance-ratio-trend
type: DetectionMethod
name: Performance ratio trend analysis
aliases:
- PR
claims:
- claim_id: c1
  rel: produces
  target: meas:performance-ratio-decline
  note: For soiling, look for output declining in dry periods without availability, clipping or curtailment
    explanations, then recovering after rain or cleaning. Week-by-week regression slopes that shift suddenly
    suggest acute disturbances; a steady drift over several weeks suggests gradual change.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=front
    h: 931a735f2be9
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h2
    h: 5d4993c87d37
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h6
    h: d8fc1b85b960
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=h32
    h: dca3eb3b5322
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=h36
    h: d32e8bcfd2a6
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
  review_note: 'support check: partial - Passages support dry-period output decline without availability/clipping/irradiance-sensor
    explanation and the weekly sudden-vs-gradual slope reading, but recovery after rain/cleaning is only
    implied via the model test, and the specific signals (W, POAI, TmpBOM) are not stated.'
- claim_id: c2
  attr: degradation_rate
  value:
    nominal: -0.9
    unit: unit:PERCENT-PER-YR
  conditions: Assumed linear relative PLR of the EURAC PV system from monthly temperature-corrected PR,
    STL trend plus linear regression; uncertainty ±0.09 %/a
  cite:
  - src: src:iea-pvps-t13-22-2021
    loc: sec=h61
    h: 3df0ed974715
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'possible conflict with c3 (same source; check the conditions); reviewer: the compiler-flagged
    conflict is a different scenario or technology, not disagreement'
- claim_id: c3
  attr: degradation_rate
  value:
    nominal: -1.49
    unit: unit:PERCENT-PER-YR
  conditions: Second segment of a one-change-point model for the EURAC system, spanning 5.5 years after
    a change point at 2.5 years
  cite:
  - src: src:iea-pvps-t13-22-2021
    loc: sec=h61
    h: 3df0ed974715
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'possible conflict with c2 (same source; check the conditions); reviewer: the compiler-flagged
    conflict is a different scenario or technology, not disagreement'
- claim_id: c4
  attr: degradation_rate
  value:
    nominal: -1.01
    unit: unit:PERCENT-PER-YR
  conditions: Overall linear PLR of a multi-crystalline system in Bolzano, Italy over eight years; the
    final multi-step segment was -0.97 %/a
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=4.3.4
    h: 1cd492a25890
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'reviewer: the compiler-flagged conflict is a different scenario or technology, not disagreement'
---
Performance ratio trend analysis follows the plant's performance ratio over time. The performance ratio is the AC yield, normalised for array size, divided by the reference yield from plane-of-array irradiance. The data are quality-checked and filtered to remove outliers and unrepresentative conditions. They are then corrected for module temperature, aggregated to days, weeks or months, and fitted with a statistical trend model such as STL decomposition with linear or change-point regression. PR plotted against module temperature or reference yield can be refitted every week. A sudden shift in slope or intercept points to an acute fault, while a steady drift over several weeks points to gradual change. For granular dust soiling and general soiling losses, look for dry periods where output falls without any availability, clipping, curtailment or irradiance sensor explanation. Then check this against soiling station data, rainfall, cleaning logs and reference blocks. Uncorrected PR is seasonal: it runs higher in cold months and lower in hot months, so temperature correction or a performance index is needed before you read a trend. Results depend on the irradiance reference used. Pyranometer-based PR comes out systematically lower than PR based on silicon reference cells, and a single dirty or drifting irradiance sensor can create a false soiling signature. No single combination of filter, metric and model has been shown to be best. Comparing results from several approaches gives a more robust trend estimate.
