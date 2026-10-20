---
id: stressor:atmospheric-aerosols
type: Stressor
name: Atmospheric aerosols
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    max: 7
    unit: unit:PERCENT
  conditions: Persistent soiling loss after a dust and sandstorm event in Portugal, lasting after the
    sky cleared
  note: Loss comes from aerosol particles deposited on the module surface (soiling), not from attenuation
    in the air.
  cite:
  - src: src:iea-pvps-t13-33-2025
    loc: sec=5.2
    h: 8c6ea50ee97c
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
  review_note: possible conflict with c3 (same source; check the conditions)
- claim_id: c2
  attr: typical_power_loss
  value:
    max: 20
    unit: unit:PERCENT
  conditions: Persistent soiling loss after a dust and sandstorm event in Saudi Arabia
  note: Loss comes from deposited particles that stay after the storm.
  cite:
  - src: src:iea-pvps-t13-33-2025
    loc: sec=5.2
    h: 8c6ea50ee97c
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c3
  attr: typical_power_loss
  value:
    nominal: 8
    unit: unit:PERCENT
  conditions: Drop in maximum power output from non-uniform soiling after the February 2017 dust event
    near Evora, Portugal
  note: In the same event the short-circuit current fell by only 3% because bypass diodes activated, so
    Pmax-based soiling measurements are preferred.
  cite:
  - src: src:iea-pvps-t13-33-2025
    loc: sec=5.3.1
    h: 17978c0f428f
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: possible conflict with c1 (same source; check the conditions)
---
Atmospheric aerosols are particles suspended in the air, such as dust, smoke and other particulates, that absorb, reflect and scatter sunlight before it reaches the modules. They change the light spectrum reaching the module, so aerosol conditions are one of the drivers of Spectral Effect Yield Losses, which can make a plant appear to underperform or overperform after normal corrections. During dust and sandstorms the suspended particles can cut global and direct irradiance strongly, and the particles that settle on the glass cause soiling losses that last after the sky clears. Over the long term, the loss from aerosols attenuating light in the air is much smaller than the loss from aerosols deposited on the panels as soiling. Aerosol load is tracked with aerosol optical depth and dust optical depth from ground networks, satellites or reanalysis data, and PM10 and PM2.5 indices can also flag dust storms. When analysing underperformance, compare residuals against aerosol optical depth, air mass and water vapour, and do not use spectral correction as a catch-all explanation. You cannot prevent the airborne effect, but you can reduce deposition with high stow angles away from the wind, anti-soiling coatings and cleaning, and after a storm several cleaning runs may be needed.

<!-- review notes
- sentence 1: support check: partial - Passages describe suspended particles absorbing, reflecting and scattering sunlight and AOD including dust, smoke and other particulates, but don't explicitly define aerosols this way.
- sentence 2: support check: partial - Passage says spectral losses correlate with aerosol conditions and can make plant appear to under/overperform, but doesn't explicitly say aerosols change the spectrum as a driver.
- sentence 7: support check: partial - High stow, coatings, cleaning and multiple cleaning runs are stated, but the claim that the airborne effect cannot be prevented is not stated, and high stow is not always feasible.
-->
