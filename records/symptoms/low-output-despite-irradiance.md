---
id: symptom:low-output-despite-irradiance
type: Symptom
name: Low output despite irradiance
aliases:
- underperformance
claims:
- claim_id: c1
  rel: observed_as
  target: meas:dc-voltage-pinned-at-minimum
  note: Points to an inverter voltage floor. One monitored system showed a horizontal line at the lower
    MPPT window boundary, and only at low irradiance.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=2.1
    h: 533a89670aca
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:operating-voltage-above-iv-vmp
  note: Supports a voltage-floor event when the measured operating voltage stays above the IV-derived
    Vmp and the operating power is below the IV-derived Pmp.
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h6
    h: 1a2c2578fa31
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h4
    h: 7023830f6e10
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
- claim_id: c3
  rel: observed_as
  target: meas:flat-output-below-available-power
  note: Signature of grid curtailment. Inverter and tracker availability can look normal.
  cite:
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h4
    h: 576525a653a1
  - src: src:pv-root-cause-grid-curtailment-losses
    loc: sec=h6
    h: 08e6be358742
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c4
  rel: observed_as
  target: meas:stow-event-output-dip
  note: Intermittent and correlated with weather. Rows may enter stow repeatedly in gusty weather.
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h4
    h: 65b80c7f6952
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h6
    h: 733de3a75bd0
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Intermittent, weather-correlated dips during gusty weather are
    stated, but the specific gust-above-stow-threshold signal is only implied (threshold exceedance is
    mentioned, not a gust-vs-threshold condition at the same time exactly).'
- claim_id: c5
  rel: observed_as
  target: meas:snow-production-residual
  note: Drop is abrupt after snowfall and recovery is gradual during melt or slide-off.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h4
    h: 0f32a669be34
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h6
    h: 0935b66311ac
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h2
    h: cf13e86d6896
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Abrupt drop after snowfall and gradual recovery are stated, but
    the cold ambient temperature slowing snow clearing is not stated.'
- claim_id: c6
  rel: observed_as
  target: meas:snow-cover-imagery
  note: Camera, drone or field observations show snow covering the modules.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h6
    h: 0935b66311ac
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h2
    h: cf13e86d6896
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c7
  rel: observed_as
  target: meas:zero-power-at-irradiance
  note: Indicates an outage or downtime. One monitoring rule flags zero production when GHI is at least
    100 W/m2.
  cite:
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: tbl=11.r3
    h: 5690bc5ac9cd
  - src: src:iea-pvps-t13-22-2021
    loc: sec=1.2.2
    h: 362882b92bf7
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c8
  attr: typical_power_loss
  value:
    nominal: 1.2
    unit: unit:PERCENT
  conditions: Average energy loss from inverter voltage flooring in summer 2025 at a 100 MW California
    PV plant
  cite:
  - src: src:pv-root-cause-inverter-voltage-floor-losses
    loc: sec=h5
    h: 43c9f30df704
  review: drafted
- claim_id: c9
  attr: typical_power_loss
  value:
    max: 4
    unit: unit:PERCENT
  conditions: Extra annual production loss from gust-driven tracker stow, compared with models that use
    only hourly wind data
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h5
    h: 3f9ef9562906
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
---
The plant is online and irradiance sensors show usable resource, but delivered power is lower than the irradiance should support. With grid curtailment, output sits flat or at a controlled level below available power, so check plant setpoints, dispatch signals and curtailment flags first. With an inverter voltage floor, inverter DC voltage stays at its minimum limit while the IV-derived Vmp is lower, mostly in hot periods or when reactive power demand is high. Tracker wind stow causes repeated output dips in gusty weather; compare tracker stow logs with high-frequency gust data. Snow accumulation causes an abrupt drop after snowfall and a gradual recovery during melt, and it can make string currents uneven; confirm it with weather data and camera or drone images. Zero production while irradiance is sufficient points to an outage or a communication loss rather than any of these losses. Before blaming one cause, rule out outages, curtailment, clipping, soiling and sensor faults, because these losses can look like each other in monthly reviews.

<!-- review notes
- sentence 3: support check: partial - The passages support voltage pinned at the minimum with Vmp below it and hot or reactive-power conditions, but 'mostly' (hot periods or high reactive power) is stated only as 'most likely' or 'can be amplified'.
- sentence 5: support check: partial - Abrupt drop, gradual recovery, and uneven string currents are stated, and weather data plus camera or drone observations are in the workflow, but 'confirm' with images is a mild extension.
- sentence 6: support check: partial - Zero production at sufficient irradiance is linked to downtime or outage, including non-communication, but the passages do not say it rules out the other losses.
- sentence 7: support check: partial - Passages say to filter out outages, curtailment, clipping, soiling and sensor faults and that losses are misclassified in monthly reviews, but not that these losses look like each other in this broad form.
-->
