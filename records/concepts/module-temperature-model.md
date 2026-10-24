---
id: concept:module-temperature-model
type: Concept
name: Module temperature model
aliases:
- cell temperature model
- module temperature vs wind speed
- thermal model
category: Modules
concept_kind: physics
claims:
- claim_id: c1
  rel: related_to
  target: concept:nominal-operating-cell-temperature
  note: Once the Sandia coefficients are fitted, NOCT can be calculated; simple NOCT-based equations also
    estimate module temperature.
  cite:
  - src: src:man-nrel-sandia-photovoltaic-array-performance-model-sand2004-3535-2004
    loc: sec=h19
    h: 0afd83588cac
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.2.2
    h: d5c12dd63efd
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:ptc-rating
  note: The fitted thermal model gives the module temperature at PVUSA Test Conditions.
  cite:
  - src: src:man-nrel-sandia-photovoltaic-array-performance-model-sand2004-3535-2004
    loc: sec=h19
    h: 0afd83588cac
  review: drafted
- claim_id: c3
  rel: related_to
  target: metric:temperature-corrected-performance-ratio
  note: A fitted thermal model can be used to temperature-normalize performance data; the reference temperature
    for corrected PR is often a module temperature taken from a standard model.
  cite:
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=h50
    h: '206960095731'
  - src: src:iea-pvps-t13-25-2022
    loc: sec=h23
    h: 844d07b9d0e3
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:expected-energy-model
  note: Module temperature estimates feed predictions of annual and operational expected yield.
  cite:
  - src: src:man-nrel-sandia-photovoltaic-array-performance-model-sand2004-3535-2004
    loc: sec=h19
    h: 0afd83588cac
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=h50
    h: '206960095731'
  review: drafted
- claim_id: c5
  rel: related_to
  target: concept:temperature-coefficient
  note: Estimated module temperature is combined with the power temperature coefficient to estimate efficiency.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.2.2
    h: d5c12dd63efd
  - src: src:iea-pvps-t13-25-2022
    loc: sec=h23
    h: 844d07b9d0e3
  review: drafted
- claim_id: c6
  rel: related_to
  target: method:ir-thermography
  note: NOCT-based temperature equations help choose weather conditions in which IR imaging can detect
    inactive module parts.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.2.2
    h: d5c12dd63efd
  review: drafted
- claim_id: c7
  rel: related_to
  target: std:iec-61215-2016
  note: For modules certified to IEC 61215-2:2016, temperature is stated in terms of the Faiman model.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: sec=2.2.2
    h: d5c12dd63efd
  review: drafted
- claim_id: c8
  rel: related_to
  target: tool:anemometer
  note: Standard meteorological practice measures wind speed at a height of 10 m. The fitted coefficients
    depend on where the anemometer is located.
  cite:
  - src: src:man-nrel-sandia-photovoltaic-array-performance-model-sand2004-3535-2004
    loc: sec=h19
    h: 0afd83588cac
  review: drafted
---
A module temperature model estimates how hot a PV module runs from local conditions: irradiance on the module, ambient air temperature, wind speed and sometimes wind direction. Designers need it to predict annual energy production, using hourly irradiance, temperature and wind data from weather databases or models. The Sandia empirical model predicts back-surface module temperature with two fitted coefficients. Coefficient a sets the upper temperature limit at low wind and high irradiance, and coefficient b sets how fast temperature falls as wind increases. The coefficients depend on module construction, mounting style (open rack, close roof mount or insulated back) and where wind is measured, which by standard practice is at a height of 10 m. Cell temperature is found by adding a temperature difference, scaled by irradiance, to the back-surface temperature. This difference is typically 2 to 3 °C for open-rack flat-plate modules and zero for modules with an insulated back. The simple Sandia model is accurate to about ±5°C, which changes predicted power by less than 3%. Other common models are the Ross model, which uses ambient temperature and irradiance, and the Faiman model, which adds cooling by wind. Module temperature matters for service life because it speeds up most degradation processes. After installation, measured module temperature, ambient temperature and wind speed can be used to refit the model for the site. The fitted model then supports temperature normalization, expected-yield calculations and the temperature-corrected performance ratio.
