---
id: fm:fungal-soiling-losses
type: FailureMode
name: Widespread Fungal Soiling Losses
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    min: 5
    max: 11
    unit: unit:PERCENT
  conditions: Persistent production losses from fungal bio-soiling in humid subtropical regions; reported
    from 2024 field work at North Carolina solar farms
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h2
    h: 201b23e0feff
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h4
    h: 52ca8426fce1
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-16
- claim_id: c2
  attr: typical_power_loss
  value:
    nominal: 5
    unit: unit:PERCENT
  conditions: Average annual bio-soiling loss across the humid subtropical (Cfa) zone, extrapolated from
    more than 120 cleanings of operating solar farms
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h7
    h: e287af93bef3
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c3
  rel: caused_by
  target: stressor:fungal-biofilm-growth
  note: Sub-aerial biofilms, especially black fungi, grow on the glass, form dark masses and trap other
    particles
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h5
    h: 4e874b23e982
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h4
    h: 52ca8426fce1
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:humid-climate
  note: Most reported in humid subtropical climates; humidity suggests the deposits will come back
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h9
    h: 58157da0d37b
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h4
    h: 52ca8426fce1
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Humid climate is listed as a recurrence factor and humid subtropical
    regions are where it''s reported, but nothing about humidity causing growth or deposits coming back
    specifically beyond ''suggest recurrence''.'
- claim_id: c5
  rel: caused_by
  target: stressor:vegetation-proximity
  note: Listed as a factor suggesting bio-soiling will recur
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h9
    h: 58157da0d37b
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c6
  rel: caused_by
  target: stressor:water-proximity
  note: Listed as a factor suggesting bio-soiling will recur
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h9
    h: 58157da0d37b
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c7
  rel: affects
  target: comp:module-glass
  note: Deposits stick to the glass and lower its transmittance
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h5
    h: 4e874b23e982
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h4
    h: 52ca8426fce1
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c8
  rel: presents_as
  target: symptom:dark-surface-deposits
  note: Fungi form dark masses on the module surface; coverage can be patchy across the array
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h5
    h: 4e874b23e982
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h8
    h: d54a5f534d87
  review: drafted
- claim_id: c9
  rel: presents_as
  target: symptom:loss-persists-after-rain
  note: Normalized production deficit does not recover after rain
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h2
    h: 201b23e0feff
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h8
    h: d54a5f534d87
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h4
    h: 52ca8426fce1
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c10
  rel: presents_as
  target: symptom:post-cleaning-step-change
  note: Output steps up repeatably after manual cleaning
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h8
    h: d54a5f534d87
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c11
  rel: detected_by
  target: method:weather-normalized-comparison
  note: Compare normalized production before and after cleanings against cleaning records, SCADA and irradiance
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h2
    h: 201b23e0feff
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h8
    h: d54a5f534d87
  review: drafted
- claim_id: c12
  rel: detected_by
  target: method:rainfall-response-review
  note: Check whether output recovers after rain
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h2
    h: 201b23e0feff
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h8
    h: d54a5f534d87
  review: drafted
- claim_id: c13
  rel: detected_by
  target: method:visual-inspection
  note: Close inspection of several array areas, not just one representative module
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h2
    h: 201b23e0feff
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h8
    h: d54a5f534d87
  review: drafted
- claim_id: c14
  rel: detected_by
  target: method:handheld-microscopy
  note: Direct imaging of the module surface confirms biofilms; it has been used on more than 15 GW of
    assets
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h2
    h: 201b23e0feff
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h6
    h: 27c24638759c
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h8
    h: d54a5f534d87
  review: drafted
- claim_id: c15
  rel: mitigated_by
  target: mit:cleaning-schedule-optimization
  note: Add bio-soiling to site cleaning schedules and treat cleaning as required maintenance
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h2
    h: 201b23e0feff
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h9
    h: 58157da0d37b
  review: drafted
- claim_id: c16
  rel: mitigated_by
  target: mit:manual-cleaning
  note: Targeted manual cleaning is needed to remove the deposits
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h5
    h: 4e874b23e982
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h4
    h: 52ca8426fce1
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c17
  rel: mitigated_by
  target: mit:cleaning-validation
  note: Check how production responds to cleaning
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h2
    h: 201b23e0feff
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c18
  rel: mitigated_by
  target: mit:forecast-update
  note: Update revenue and loss forecasts from site cleaning results instead of assuming rain resets the
    loss
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h2
    h: 201b23e0feff
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h9
    h: 58157da0d37b
  review: drafted
- claim_id: c19
  rel: distinguished_from
  target: fm:granular-dust-soiling-losses
  by: method:rainfall-response-review
  note: Ordinary dust partly washes off in rain. Fungal bio-soiling stays on after rain and recovers only
    after targeted or manual cleaning.
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h5
    h: 4e874b23e982
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h8
    h: d54a5f534d87
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h4
    h: 52ca8426fce1
  review: drafted
---
Fungal bio-soiling happens when biofilms, mainly black fungi, grow on the module glass, form dark masses and trap other dirt, which lowers how much light gets through the glass. Unlike ordinary dust, these deposits stay on after rain, so the loss is easy to mistake for dust, pollen or a weather-normalization error. Reported persistent losses in humid subtropical regions are 5-11%, and the average annual loss across that climate zone is 5%. To confirm it, look for a normalized production deficit that does not recover after rain but steps up repeatably after manual cleaning, and compare cleaning records with SCADA, irradiance and weather-normalized production. Confirm the biofilm itself with close visual inspection or a handheld microscope, and check several array areas because the deposits can be patchy. Clean manually or with targeted cleaning, add bio-soiling to the site cleaning schedule, and check how production responds after each cleaning. Update production forecasts from actual cleaning results instead of assuming rain resets the loss, especially at humid sites or sites near vegetation or water.
