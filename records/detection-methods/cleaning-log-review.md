---
id: method:cleaning-log-review
type: DetectionMethod
name: Cleaning log review
aliases:
- cleaning records
- cleaning logs
claims:
- claim_id: c1
  rel: produces
  target: meas:post-cleaning-production-step
  note: For dust soiling, output recovers partly or fully after washing. For biological soiling, the step
    after cleaning shows up where rain had not restored output.
  cite:
  - src: src:pv-root-cause-fungal-soiling-losses
    loc: sec=h8
    h: d54a5f534d87
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h6
    h: d8fc1b85b960
  - src: src:pv-root-cause-granular-dust-soiling-losses
    loc: sec=h4
    h: dea316ba61e1
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
---
Cleaning log review means checking the site's records of when modules were washed or cleaned against the plant's production data. Line up the cleaning dates with normalized production trends, SCADA, irradiance and weather data, along with soiling station readings, rainfall and nearby reference blocks if the site has them. Granular dust soiling shows as a slow drop in normalized output during dry periods, followed by partial or full recovery after a real rain or a wash. The key evidence is a repeatable jump in production after cleaning, especially where rain had not brought output back, which points to biological soiling rather than ordinary dust. Use the logged recoveries to check whether the assumed soiling model fits, and update the local buildup and wash-off assumptions before using the model to plan cleaning costs. First rule out other causes of the decline, such as availability problems, clipping, curtailment and irradiance sensor issues. Do not rely on one dirty irradiance sensor: sensor drift, poor cleaning practice and local obstructions can create fake soiling signatures that do not represent the array.

<!-- review notes
- sentence 6: support check: partial - u7 identifies dry-period declines without availability, clipping, curtailment, or sensor issues, implying exclusion, but doesn't explicitly say to rule them out first.
-->
