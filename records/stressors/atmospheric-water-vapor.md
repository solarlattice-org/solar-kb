---
id: stressor:atmospheric-water-vapor
type: Stressor
name: Atmospheric water vapor
aliases:
- precipitable water
- atmospheric water content
---
Water vapor in the atmosphere changes the spectrum of the light that reaches the module. Spectral effect losses occur when that light differs from the reference spectrum used to rate, model or test the module. Modules convert some wavelengths better than others. When the spectrum shifts toward wavelengths a technology converts poorly, the cell receives less effective irradiance than a broadband sensor suggests. This stressor drives Spectral Effect Yield Losses. After normal irradiance and temperature corrections, the plant can still look like it is underperforming or overperforming, and the deviation tends to follow atmospheric water content, air mass, season, aerosols and module technology. The effect can bias capacity tests and shift the energy a plant actually yields. It matters most when you compare module technologies or judge tests run during narrow weather windows. To check for it, first remove clipping, curtailment, temperature, soiling and availability effects. Then compare the remaining residuals against precipitable water, air mass, aerosol optical depth, season and time of day. The atmosphere cannot be controlled, so the effect is managed instead. Apply spectral corrections in testing and modeling, and use spectral irradiance measurements and spectral response data for the specific module technology. Do not use spectral correction to explain away every shortfall. The correction should be tied to measured or modeled atmospheric conditions and should make the residuals more orderly.

<!-- review notes
- sentence 1: support check: partial - Passages say spectral losses occur when light differs from the reference spectrum and correlate with atmospheric water content, but don't explicitly state that water vapor changes the spectrum.
- sentence 6: support check: partial - Mitigation items (corrections, spectral irradiance measurements, technology-specific response data) are supported, but the framing that the atmosphere can't be controlled so it is managed is not stated.
-->
