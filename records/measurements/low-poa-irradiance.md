---
id: meas:low-poa-irradiance
type: Measurement
name: Low plane-of-array irradiance
aliases:
- POA
- POAI
- In-plane irradiance
- GI
signals:
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: irradiance stays well below normal daytime levels, as at dawn, dusk or under low light
- point: model_302.GHI
  unit: unit:W-PER-M2
  pattern: low horizontal irradiance during the same periods
---
This signature is a low reading of solar irradiance measured in the plane of the PV array, reported in W/m2. Plane-of-array irradiance is measured on site with at least one irradiance sensor that meets ISO 9060:2018, and the pyranometer class sets the measurement uncertainty. Best practice is to fit two pyranometers in the array plane and one horizontal, with at least one per array orientation, and to use satellite irradiance data as a backup and for accuracy checks. When irradiance is low, IV curves measured at low power can be inaccurate at both the low and high ends of the curve. To avoid this, take IV curve measurements only when irradiance is high enough for the array to produce at least 50 % of nominal power. Performance analyses filter out data below a minimum plane-of-array irradiance, so that differences in low-irradiance losses stay small.

<!-- review notes
- sentence 1: support check: partial - Passages define plane-of-array irradiance in W/m2, but nothing says this signature is a 'low reading' (the low-condition aspect is not stated).
-->
