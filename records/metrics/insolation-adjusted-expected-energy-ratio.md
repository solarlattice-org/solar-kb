---
id: metric:insolation-adjusted-expected-energy-ratio
type: Metric
name: Insolation-adjusted expected energy ratio
aliases:
- IEER
- insolation-adjusted estimated energy ratio
category: Performance
claims:
- claim_id: c1
  rel: subclass_of
  target: metric:performance-ratio
  note: Described as a monthly, weather-adjusted type of performance ratio, calculated at site level.
  cite:
  - src: src:alsoenergy-kb-ieer
    loc: sec=front
    h: c83c6d979313
  - src: src:alsoenergy-kb-ieer-insolation-adjusted-estimated-energy-ratio
    loc: sec=front
    h: 6a5b72830444
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: subclass_of
  target: metric:expected-energy-ratio
  note: IEER takes the expected energy ratio (measured over expected energy) and adjusts it by the ratio
    of measured to expected insolation.
  cite:
  - src: src:alsoenergy-kb-rescheduling-a-legacy-site-performance-yield-report-in-locusnoc
    loc: sec=front
    h: 003faad8cb7c
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
The insolation-adjusted expected energy ratio is a site-level, monthly performance ratio adjusted for weather. It is widely used because the calculation is simple and easy to follow. To calculate it, divide measured AC energy by expected AC energy. Then divide that result by the ratio of measured insolation to expected insolation. Expected energy and expected insolation are long-term values based on a typical meteorological year. The user enters them as monthly values in the site configuration and the weather station configuration. Measured insolation can come from any weather sensor on the site. If no sensor is available, a modeled global horizontal value from satellite-based virtual irradiance can be used. Measured and expected insolation must use the same orientation, so a plane-of-array sensor needs plane-of-array expected values. IEER is reported as a percentage and can be found under Modeled Data in charts, reports and the data API. The result is only as accurate as the original design model. If the design estimate was too high, IEER will read low by about the same amount. The adjustment also tends to be inaccurate on sites with a high DC to AC ratio. GEER is a less flexible version of IEER that always uses virtual irradiance for measured insolation and TMY3 data for expected insolation. The two metrics are offered side by side.

<!-- review notes
- sentence 3: support check: partial - TMY-based long-term values and monthly user entry in site and weather station configuration are stated, but expected values can also come from TMY3 directly rather than always being user-entered.
- sentence 4: support check: partial - Any measured insolation field and modeled GHI fallback are stated, as is the POA needing POA expected values, but 'must' and the satellite description are slightly stronger; the passage says 'not available or deemed inaccurate' and the modeled value requires a US address.
- sentence 5: support check: partial - Percentage and Modeled Data in charts and reports are stated, and the External API is said to include IEER, but the passages do not say it is under Modeled Data in the data API.
- sentence 4: review: partial - The passage supports any measured insolation field, the Modeled GHI fallback from Virtual Irradiance, and POA sensors needing POA expected values, but it does not call the source satellite-based and gives the fallback as 'not available or deemed inaccurate' rather…
-->
