---
id: fm:spectral-effect-losses
type: FailureMode
name: Spectral Effect Yield Losses
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:air-mass-variation
  note: The signature often correlates with air mass and season.
  cite:
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=h4
    h: eb8006cfb637
  review: drafted
- claim_id: c2
  rel: caused_by
  target: stressor:atmospheric-water-vapor
  note: The signature often correlates with atmospheric water content.
  cite:
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=h4
    h: eb8006cfb637
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-16
  review_note: 'support check: partial - Passage says the signature correlates with atmospheric water
    content, but doesn''t explicitly state water vapor causes it.'
- claim_id: c3
  rel: caused_by
  target: stressor:atmospheric-aerosols
  note: The signature often correlates with aerosol conditions.
  cite:
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=h4
    h: eb8006cfb637
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Passage says the signature correlates with aerosol conditions,
    but doesn''t explicitly state aerosols cause it.'
- claim_id: c4
  rel: affects
  target: comp:solar-cell
  note: If the spectrum shifts toward wavelengths the cell technology converts poorly, effective irradiance
    at the cell is below what broadband irradiance suggests. In tandem devices it interacts with subcell
    current matching.
  cite:
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=h5
    h: cc75dd4a8e8e
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c5
  rel: presents_as
  target: symptom:expected-vs-measured-gap
  note: The plant may appear to underperform or overperform even after normal irradiance and temperature
    corrections.
  cite:
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=h4
    h: eb8006cfb637
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c6
  rel: presents_as
  target: symptom:capacity-test-bias
  note: Most relevant for tests run during narrow weather windows or when comparing technologies.
  cite:
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=front
    h: 50540480df25
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=h2
    h: 3f9d65519ecf
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=h4
    h: eb8006cfb637
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c7
  rel: detected_by
  target: method:spectral-irradiance-measurement
  note: Use measured spectral irradiance, or validated spectral model inputs, where available.
  cite:
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=h6
    h: 172487c8868e
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=front
    h: 50540480df25
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=h2
    h: 3f9d65519ecf
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c8
  rel: detected_by
  target: method:capacity-test-method-review
  note: First check whether the capacity test or energy model applied a spectral correction.
  cite:
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=h6
    h: 172487c8868e
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:technology-specific-spectral-response
  note: The same atmospheric spectrum gives different effective irradiance for different module designs.
  cite:
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=front
    h: 50540480df25
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=h2
    h: 3f9d65519ecf
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=h6
    h: 172487c8868e
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c10
  rel: mitigated_by
  target: mit:loss-factor-separation
  note: Separate spectral effects from temperature, soiling, degradation and irradiance sensor bias.
  cite:
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=front
    h: 50540480df25
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=h2
    h: 3f9d65519ecf
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c11
  rel: distinguished_from
  target: fm:soiling-losses
  by: method:measured-vs-modeled-reconciliation
  note: Remove soiling effects first. A remaining residual that tracks air mass, precipitable water, aerosol
    optical depth and season points to a spectral cause.
  cite:
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=h6
    h: 172487c8868e
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=front
    h: 50540480df25
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
  review_note: 'support check: partial - Passages say to remove soiling then compare residuals against
    air mass, PW, AOD, season, but don''t explicitly say a remaining residual tracking these points to
    spectral cause.'
---
Spectral effect losses happen when the sunlight reaching the modules has a different spectrum from the reference spectrum used for rating, modeling or capacity testing. If the spectrum shifts toward wavelengths the cell technology converts less well, the cells see less effective irradiance than a broadband sensor reports. As a result, the plant can look like it is underperforming or overperforming even after normal irradiance and temperature corrections, and capacity tests can be biased. The pattern usually follows air mass, season, atmospheric moisture, aerosols and module technology. It matters most for short test windows or when comparing technologies. Use spectral irradiance measurements or validated spectral inputs together with spectral response data for the specific module technology. Apply spectral corrections only when they tie to atmospheric conditions and make the residuals more structured. Do not use them to explain away all underperformance.
