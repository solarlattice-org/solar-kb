---
id: method:weather-normalized-comparison
type: DetectionMethod
name: Weather-normalized production comparison
aliases:
- irradiance-normalized output
- weather-normalized production
- normalized production
- energy performance index
claims:
- claim_id: c1
  rel: produces
  target: meas:post-cleaning-production-step
  note: A repeatable step up in weather-normalized production after cleaning, especially where rain had
    not restored the expected output, points to biological soiling.
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h8
    h: d54a5f534d87
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=front
    h: c791ea65d1df
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-19
- claim_id: c2
  rel: produces
  target: meas:snow-production-residual
  note: 'Production residuals line up with snowfall and snow depth: an abrupt drop after snowfall and
    gradual recovery during melt or slide-off while irradiance sensors still show usable resource.'
  cite:
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h6
    h: 0935b66311ac
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=h4
    h: 0f32a669be34
  - src: src:pv-root-cause-snow-accumulation-losses
    loc: sec=front
    h: ef48f3c9a102
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c3
  rel: produces
  target: meas:performance-index-below-unity
  note: Measured power or energy is divided by expected values from measured weather and an agreed performance
    model; healthy systems sit close to unity.
  cite:
  - src: src:nrel-om-best-practices-pv-ess
    loc: sec=h89
    h: a3ff7fef5764
  - src: src:iea-pvps-t13-07-2017
    loc: sec=h29
    h: 6f1b20e5a0bf
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Passages say expected values come from measured weather and an
    agreed model and indices should be near unity, but do not state that falling below 1 is the signal/ratio
    definition explicitly.'
---
This method compares measured plant output with the output you would expect for the measured weather and irradiance, using a performance model the stakeholders agree on. Line up SCADA production with irradiance, rainfall, cleaning logs and, in winter, snowfall, snow depth and module temperature, and check how the normalized output changes around these events. If normalized output falls slowly during dry periods and comes back after rain or washing, the cause is likely granular dust soiling. If the shortfall stays after rain but output steps up after manual cleaning, the cause is more likely widespread fungal soiling, which you can confirm by close inspection or handheld microscopy. Residuals that line up with snowfall and recover slowly during melt point to snow accumulation losses, and you can compare them with the snow-loss model. Before you blame soiling or snow, remove periods affected by outages, clipping, curtailment, inverter behaviour in cold weather, sensor icing or irradiance sensor problems. Never rely on one dirty irradiance sensor, because sensor drift or local obstruction can produce what looks like a soiling signature. Small losses such as minor shading may not show clearly in yield or performance-ratio comparisons, so you may need other signals as well.

<!-- review notes
- sentence 6: support check: partial - Passages support filtering clipping, curtailment, availability, sensor issues and cold-weather inverter behavior, but outages for snow are only implied via availability and 'never/before blaming' is a stronger framing.
-->
