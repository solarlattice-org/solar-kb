---
id: stressor:air-mass-variation
type: Stressor
name: Varying air mass
aliases:
- AM
---
Varying air mass changes the spectrum of sunlight that reaches the modules, so it is treated as a parameter that shapes the incident spectrum. How much this matters depends on module technology. The same atmospheric spectrum can give different effective irradiance for different module designs, and the short-circuit response of amorphous silicon modules was seen to vary with air mass. The effect tends to follow air mass, season, time of day, atmospheric water content and aerosols. It matters most when comparing technologies or judging tests run during narrow weather windows. To find it, first remove clipping, curtailment, temperature, soiling and availability effects. Then compare the remaining performance residuals against air mass, which some sites log with local sensors alongside irradiance and module temperature. Air mass itself cannot be avoided. The resulting bias is reduced by applying spectral corrections in testing and modeling and by using technology-specific spectral response data. A spectral correction should improve the structure of the residuals and be linked to measured or modeled atmospheric conditions. It should not be used as a catch-all explanation for underperformance.

<!-- review notes
- sentence 2: support check: partial - The passages support technology-specific effective irradiance and a-Si short-circuit response varying with air mass, but "how much this matters depends on technology" is only implied, and the "variability" is tied to air mass only as modeled.
- sentence 4: support check: partial - Removing the listed effects and comparing residuals against air mass is in u6, and u34 says air mass is recorded by local sensors, but "some sites log" is a loose link and u34 is about a dataset, not detection.
- sentence 5: support check: partial - Mitigation by spectral corrections and technology-specific response data is stated, but the claim that air mass itself cannot be avoided is not in the passages.
-->
