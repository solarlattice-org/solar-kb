---
id: method:snow-loss-model-comparison
type: DetectionMethod
name: Loss model comparison
aliases:
- snow loss models
claims:
- claim_id: c1
  rel: produces
  target: meas:snow-production-residual
  note: Measured recovery curves after snow are compared with the energy model's snow-loss assumptions;
    a site clearing slower than modeled may need a revised snow-loss factor even with healthy equipment.
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=front
    h: ef48f3c9a102
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h2
    h: cf13e86d6896
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h6
    h: 0935b66311ac
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
  review_note: 'support check: partial - The comparison of recovery curves with snow-loss assumptions
    and slower clearing needing a revised factor is stated, but the specific signal patterns (POAI present
    with negative residual, low module temperature aligned with slow melt) are not stated in the passages.'
- claim_id: c2
  attr: typical_power_loss
  value:
    max: 42
    unit: unit:PERCENT
  conditions: Annual energy loss predicted by the Marion snow model for a few stations within the Arctic
    Circle; losses are near zero in warmer regions and the Townsend and Powers model predicts far lower
    losses at high latitudes.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=4.2.4
    h: 5ddca0c6f3d8
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Marion model max of 42% for a few Arctic Circle stations, near
    zero in warmer regions, and much lower Townsend and Powers losses are stated, but 42% is a maximum,
    not a typical value.'
---
Next, compare the measured recovery curves with the snow-loss assumptions in the energy model. If a site clears more slowly than modeled, it may need a revised snow-loss factor even when the equipment works normally. Some monitoring platforms detect snow loss by pattern matching against weather conditions and against how similar systems performed in snow. A heated pyranometer gives the best results because the algorithm needs irradiance data. Published snow models can disagree a lot even when they use the same weather files. At one site, one model overestimated the measured loss and the other underestimated it, so model outputs need to be checked against real site data.

<!-- review notes
- sentence 2: support check: partial - Snow loss detection by pattern matching on weather conditions and previously observed similar-system performance, and heated pyranometer for best results because algorithm requires irradiance data are stated; 'best results because' is slightly reworded but essentially present, though 'some monitoring platforms' generalizes a PowerTrack-specific statement.
-->
