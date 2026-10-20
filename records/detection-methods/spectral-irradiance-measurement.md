---
id: method:spectral-irradiance-measurement
type: DetectionMethod
name: Spectral irradiance measurement
claims:
- claim_id: c1
  rel: produces
  target: meas:air-mass-correlated-residual
  note: The residual is also checked against precipitable water and aerosol optical depth. The plant may
    look like it is underperforming or overperforming after ordinary irradiance and temperature corrections.
  cite:
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=h6
    h: 172487c8868e
  - src: src:pv-root-cause-spectral-effect-losses
    loc: sec=h4
    h: eb8006cfb637
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
  review_note: 'support check: partial - Residual vs air mass/season/time of day after removing effects,
    and the overstating of broadband irradiance, are supported, but the passages never say spectral irradiance
    measurement itself produces this residual, and the signal point details are not stated.'
---
Spectral irradiance measurement records the spectrum of the light that reaches the modules. It is used together with technology-specific spectral response data to judge how much irradiance the cells can actually use. A broadband sensor alone cannot show a spectral shift: pyranometers are almost spectrally unselective and measure across roughly 280 to 2800 nm. The method confirms Spectral Effect Yield Losses, where the plant appears to underperform or overperform after ordinary irradiance and temperature corrections because the module's spectral response does not match the prevailing spectrum. It matters most when comparing module technologies, when evaluating tests run during narrow weather windows, and for tandem devices, where the spectrum also affects current matching between subcells. For IV testing, the reference device should have the same or a similar spectral response to the module under test, to minimize spectral mismatch. Measuring the module's spectral response before IV testing is strongly recommended. Where no spectral measurements are available, validated spectral model inputs can be used instead. Spectral effects must still be separated from temperature, soiling, degradation and irradiance sensor bias.

<!-- review notes
- sentence 1: support check: partial - Use of spectral measurements with technology-specific response data is stated, but the passages don't explicitly say the measurement records the spectrum or that the cells' usable irradiance is judged this way.
- sentence 2: support check: partial - Pyranometers being almost spectrally unselective across 280-2800 nm is stated, and broadband alone can understate spectral effects, but 'cannot show a spectral shift' is an inference not directly stated.
- sentence 3: support check: partial - The appearance of under/overperformance due to spectral response mismatch is stated, but the passages don't say a method 'confirms' it; they describe a diagnostic comparison.
- sentence 6: support check: partial - Validated spectral model inputs as an alternative and separating spectral effects from temperature, soiling, degradation and sensor bias are stated, but 'where no measurements are available' is only implied by 'where available'.
-->
