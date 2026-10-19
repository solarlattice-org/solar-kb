---
id: fm:granular-dust-soiling-losses
type: FailureMode
name: Granular Dust Soiling Losses
category: Soiling
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:surface-soiling
  note: Granular dust settles on the module glass and builds up between rain or cleaning events.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=front
    h: 931a735f2be9
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h2
    h: 5d4993c87d37
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h5
    h: 43575746a7d7
  review: drafted
- claim_id: c2
  rel: caused_by
  target: stressor:dry-period
  note: Losses build up during dry spells when there is no rain to wash the dust off.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h4
    h: dea316ba61e1
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h6
    h: d8fc1b85b960
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:agricultural-activity
  note: Can make dust loss spatially uneven across the plant.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h4
    h: dea316ba61e1
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:construction-activity
  note: Can make dust loss spatially uneven across the plant.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h4
    h: dea316ba61e1
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-16
- claim_id: c5
  rel: caused_by
  target: stressor:unpaved-roads-exposed-soil
  note: Roads and bare soil nearby can raise local dust deposition.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h4
    h: dea316ba61e1
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Roads and exposed soil are named as causing spatial unevenness,
    but the passages don''t state they raise local deposition.'
- claim_id: c6
  rel: affects
  target: comp:module-glass
  note: Dust deposited on the glass lowers its transmittance.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=front
    h: 931a735f2be9
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h2
    h: 5d4993c87d37
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c7
  rel: affects
  target: comp:solar-cell
  note: Particles scatter and absorb light, so less light reaches the cells.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h4
    h: dea316ba61e1
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h5
    h: 43575746a7d7
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c8
  rel: presents_as
  target: symptom:gradual-performance-decline
  note: Irradiance-normalized production declines gradually through dry periods while the plant stays
    online.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h4
    h: dea316ba61e1
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c9
  rel: presents_as
  target: symptom:recovery-after-rain
  note: Output recovers partly or fully after meaningful rain.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h4
    h: dea316ba61e1
  review: drafted
- claim_id: c10
  rel: presents_as
  target: symptom:post-cleaning-step-change
  note: Output recovers after washing.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h4
    h: dea316ba61e1
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Recovery after washing is stated, but a ''step change'' in production
    is not explicitly described.'
- claim_id: c11
  rel: presents_as
  target: symptom:string-current-low
  note: Dust lowers module and array current.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=front
    h: 931a735f2be9
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h2
    h: 5d4993c87d37
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h5
    h: 43575746a7d7
  review: drafted
- claim_id: c12
  rel: presents_as
  target: symptom:spatially-uneven-loss
  note: The loss is usually broad across a zone, but local dust sources, prevailing wind and row edges
    can make it uneven. Uneven deposition can also cause mismatch between strings or substrings.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h4
    h: dea316ba61e1
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h5
    h: 43575746a7d7
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c13
  rel: detected_by
  target: method:performance-ratio-trend
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
  review: drafted
- claim_id: c14
  rel: detected_by
  target: method:soiling-station
  note: Do not rely on a single dirty irradiance sensor. Drift, poor cleaning practice or a local obstruction
    can mimic soiling.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=front
    h: 931a735f2be9
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h2
    h: 5d4993c87d37
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h7
    h: 445831ccd5f3
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h6
    h: d8fc1b85b960
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c15
  rel: detected_by
  target: method:rainfall-response-review
  note: Check whether output recovers after rain as the soiling model predicts.
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
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c16
  rel: detected_by
  target: method:cleaning-log-review
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
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c17
  rel: detected_by
  target: method:weather-normalized-comparison
  note: Uses irradiance-normalized output during dry accumulation periods.
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
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c18
  rel: detected_by
  target: method:soiling-model-residuals
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
  review: drafted
- claim_id: c19
  rel: detected_by
  target: method:reference-block-comparison
  note: Compare with nearby reference blocks when they are available.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h6
    h: d8fc1b85b960
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c20
  rel: mitigated_by
  target: mit:cleaning-schedule-optimization
  note: Set cleaning triggers by the value of the lost energy.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=front
    h: 931a735f2be9
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h2
    h: 5d4993c87d37
  review: drafted
- claim_id: c21
  rel: mitigated_by
  target: mit:soiling-model-calibration
  note: Calibrate local accumulation and wash-off assumptions against operational data before using the
    model for cleaning economics.
  cite:
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=front
    h: 931a735f2be9
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h2
    h: 5d4993c87d37
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h5
    h: 43575746a7d7
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h6
    h: d8fc1b85b960
  review: drafted
- claim_id: c22
  rel: distinguished_from
  target: fm:grid-curtailment-losses
  by: method:performance-monitoring
  note: Dust loss shows as declining normalized output in dry periods with no matching availability, clipping
    or curtailment events, and it recovers after rain or cleaning.
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
  review: drafted
  review_note: 'support check: partial - Passages say dust decline occurs without curtailment/clipping
    events and recovers after rain, and say to separate from curtailment, but don''t explicitly state
    a comparison with grid curtailment losses via performance monitoring.'
---
Granular dust soiling happens when dust settles on the module glass. The dust lowers how much light the glass lets through, which reduces array current and energy output. It shows as a slow drop in irradiance-normalized production during dry spells. Output often recovers partly or fully after real rain or a wash, and the plant stays online throughout. The loss is usually spread across a whole zone. Roads, bare soil, farming, construction, prevailing wind and row edges can make it uneven, and uneven dust can also cause mismatch between strings or substrings. To confirm it, find dry periods where output falls even though availability, clipping, curtailment and sensors are all fine. Then compare those periods with soiling station data, rainfall, cleaning logs and nearby reference blocks. Do not judge soiling from one dirty irradiance sensor alone, because sensor drift, poor cleaning or a local obstruction can look like soiling. Check that the soiling model matches the recovery you actually see after rain or cleaning. If it does not, update its accumulation and wash-off assumptions, then set cleaning triggers by the value of the lost energy.
