---
id: meas:post-cleaning-production-step
type: Measurement
name: Production step after cleaning
aliases:
- production step-change after cleaning
signals:
- point: model_103.W
  unit: unit:W
  pattern: step increase in normalized output right after a cleaning event
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: irradiance used to normalize production before and after cleaning
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 5
    max: 11
    unit: unit:PERCENT
  conditions: Persistent production loss from fungal bio-soiling in humid subtropical regions, which may
    not recover after rain; this loss is what cleaning can recover.
  quote: Fungal bio-soiling can create persistent 5-11% production losses in humid subtropical regions
    and may not recover after rainfall.
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h2
    h: 201b23e0feff
  review: drafted
  review_note: 'support check: partial - The passage gives persistent 5-11% losses from fungal bio-soiling
    in humid subtropical regions that may not recover after rain, but doesn''t state this as the loss
    recovered by cleaning (the production step after cleaning).'
- claim_id: c2
  attr: typical_power_loss
  value:
    min: 5
    max: 20
    unit: unit:PERCENT
  conditions: Energy yield loss from soiling over one year, depending on module location; soiling is mostly
    reversible by cleaning.
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.6
    h: a3dffa29110f
  review: drafted
  review_note: 'support check: partial - The passage gives 5-20% annual energy yield losses from soiling,
    depending on location, and says soiling is mostly removable by cleaning, but it doesn''t describe
    this as a step in production after cleaning.'
---
The signature is a step up in weather-normalized production right after a cleaning, and it repeats with each cleaning. To find it, line up the cleaning records with SCADA data, irradiance and weather-normalized production for the period before and after each cleaning. Production that steps up after cleaning but did not come back after rain points to fungal or biological soiling, not ordinary dust. With granular dust soiling, check whether the soiling model explains the recovery seen after rain or cleaning. If it does not, update the local accumulation and wash-off assumptions. Soiling is usually reversible and cleaning removes most of it, so a clear jump after cleaning shows how much production soiling was costing. Biological deposits can be patchy. Inspect several array areas, using close visual checks or handheld microscopy, rather than relying on one module. Weather-normalized production comparison is one of the listed ways to detect soiling losses, along with soiling stations and clean/dirty reference sensors.

<!-- review notes
- sentence 2: support check: partial - The passages say to compare cleaning records against SCADA, irradiance and weather-normalized production, and u20 says to compare normalized production before and after cleanings, but the passages don't spell out aligning all data over the period before and after each cleaning.
- sentence 4: support check: partial - The passage covers testing whether the soiling model explains recovery after rain or cleaning, and updating local accumulation and wash-off assumptions if it doesn't, but it doesn't limit this to granular dust soiling.
- sentence 5: support check: partial - u6 says soiling is usually reversible and mostly removed by cleaning, but it doesn't say a jump after cleaning measures the production cost of soiling.
-->
