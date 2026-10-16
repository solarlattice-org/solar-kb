---
id: fm:tracker-wind-stow-losses
type: FailureMode
name: Tracker Wind Stow Production Losses
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:high-wind
  note: Stow is triggered when measured wind or short-duration gusts exceed the tracker controller threshold;
    hourly averages may stay below it.
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h4
    h: 65b80c7f6952
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h5
    h: 3f9ef9562906
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-16
- claim_id: c2
  rel: affects
  target: comp:single-axis-tracker
  note: Rows move to a protective high-tilt or safe angle and capture less irradiance until they return
    to tracking.
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h4
    h: 65b80c7f6952
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c3
  rel: presents_as
  target: symptom:low-output-despite-irradiance
  note: Intermittent, weather-correlated dips, especially when rows stow repeatedly in gusty weather.
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h4
    h: 65b80c7f6952
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c4
  rel: detected_by
  target: method:wind-gust-data-review
  note: Three-second gusts, one-minute moving averages or met mast data explain tracker behavior better
    than hourly averages.
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h2
    h: 3c102c6647a1
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h6
    h: 733de3a75bd0
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c5
  rel: detected_by
  target: method:performance-monitoring
  note: Compare SCADA production and POA irradiance-normalized output during windy periods against stow
    events.
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h2
    h: 3c102c6647a1
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h6
    h: 733de3a75bd0
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:energy-model-update
  note: Model stow losses with high-frequency gust statistics and reconcile actual stow hours against
    P50/P90 assumptions.
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h2
    h: 3c102c6647a1
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h7
    h: 47f98047fafd
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c7
  rel: mitigated_by
  target: mit:forecast-update
  note: Update forecasts when recurring gust-driven stow was not represented in the original model.
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h7
    h: 47f98047fafd
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c8
  rel: mitigated_by
  target: mit:tracker-stow-strategy
  note: Verify wind thresholds and return-to-track logic; change thresholds only if the tracker supplier
    and structural engineer confirm it stays within the design envelope.
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h2
    h: 3c102c6647a1
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h7
    h: 47f98047fafd
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c9
  rel: mitigated_by
  target: mit:loss-factor-separation
  note: Track stow loss as a defined tracker operating mode rather than lumping it into availability,
    curtailment or weather variance.
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h4
    h: 65b80c7f6952
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h7
    h: 47f98047fafd
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c10
  rel: distinguished_from
  target: fm:inverter-clipping
  by: method:tracker-command-log-review
  note: Aligning stow events with SCADA production, irradiance and inverter status separates stow loss
    from clipping.
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h6
    h: 733de3a75bd0
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c11
  rel: distinguished_from
  target: fm:grid-curtailment-losses
  by: method:tracker-command-log-review
  note: Stow loss coincides with logged stow commands and high wind; curtailment shows in inverter or
    grid status without stow events.
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h6
    h: 733de3a75bd0
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Separation from curtailment via aligned logs is stated, but the
    specific signature (curtailment shows in inverter or grid status without stow events) is not.'
- claim_id: c12
  attr: typical_power_loss
  value:
    max: 4
    unit: unit:PERCENT
  conditions: Additional annual production loss when gust-driven tracker response is accounted for, compared
    with models using hourly wind data only (2026 kWh Analytics Solar Risk Assessment).
  cite:
  - src: src:pv-root-cause-tracker-wind-stow-losses
    loc: sec=h5
    h: 3f9ef9562906
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
---
Wind stow losses happen when single-axis trackers move to a protective safe angle because measured wind is above the controller threshold. While the rows are off-angle they capture less sunlight. In the data you see intermittent output dips during gusty weather even though irradiance is good. These losses are easy to miss when they get lumped in with availability, curtailment or weather variance. Energy models built on hourly wind data can understate this loss, because controllers react to short gusts that hourly averages smooth out. Counting gust-driven stow can raise annual production losses by up to 4%. To confirm it, pull the tracker controller logs showing stow commands, return-to-track events, wind speed and the active threshold. Line these up with SCADA production, irradiance and inverter status so you can rule out clipping, curtailment, outages and sensor faults. Where you can, use high-frequency wind data such as three-second gusts or met mast records instead of hourly averages. Check the wind thresholds and the return-to-track logic. Do not lower stow thresholds to win back energy unless the tracker supplier and the structural engineer confirm the change stays within the design limits. Compare actual stow hours with the energy model assumptions, then update forecasts and variance reporting so the loss is tracked in its own category.
