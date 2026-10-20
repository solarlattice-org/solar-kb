---
id: symptom:capacity-test-bias
type: Symptom
name: Biased capacity test result
claims:
- claim_id: c1
  rel: observed_as
  target: meas:air-mass-correlated-residual
  note: After irradiance and temperature corrections, and after removing clipping, curtailment, soiling
    and availability effects, the performance residual follows air mass, precipitable water, aerosol conditions,
    season and time of day. The plant may look like it is underperforming or overperforming.
  cite:
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=h6
    h: 172487c8868e
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=h4
    h: eb8006cfb637
  review: drafted
  review_note: 'support check: partial - Residuals correlating with air mass, season, time of day, and
    over/underperformance after removing other effects are stated, but the signal specifics (flat ratio
    drifting, POAI alone not explaining deviation) are not in the passages.'
---
A capacity test can show the plant as underperforming or overperforming when the incoming sunlight's spectrum differs from the reference spectrum used for rating, and the module's spectral response does not match. The error can remain even after the usual irradiance and temperature corrections. It shows up as residuals that track air mass, season, atmospheric water content and aerosols. The risk is highest when a test runs during a narrow weather window or when different module technologies are being compared. First, check whether the capacity test or energy model applied a spectral correction. Where available, use spectral irradiance measurements or validated spectral model inputs, plus spectral response data for the specific module technology. The same sky spectrum gives different effective irradiance for different module designs. Keep spectral effects separate from temperature, soiling, degradation and irradiance sensor bias. Accept a spectral explanation only if it improves the structure of the residuals and is tied to measured or modeled atmospheric conditions.

<!-- review notes
- sentence 3: support check: partial - u10 says it can be especially important for comparing technologies or narrow weather window tests, but not that risk is 'highest' in those cases; close paraphrase though.
-->
