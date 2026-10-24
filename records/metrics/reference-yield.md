---
id: metric:reference-yield
type: Metric
name: Reference yield
aliases:
- Yr
- Ref_Yield
category: Performance
claims:
- claim_id: c1
  rel: part_of
  target: std:solarpower-europe-om-guidelines
  note: Reference yield is defined in section 10.3.1 of the O&M Best Practice Guidelines.
  cite:
  - src: src:solarpower-europe-om-guidelines
    loc: sec=10.3.1
    h: b7311e894be5
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: sec=10.3.1
    h: a97534593e7e
  review: drafted
---
Reference yield is the energy a PV system could deliver over a given period under standard conditions if it had no losses. It is written Yr. A lowercase yr is used for the instantaneous reference yield. Over a period, reference yield is given in hours. Monitoring platforms can also show it in kWh per kWp, labelled Ref_Yield. You compare reference yield with the final system yield to get the performance ratio. Expected yield for a period is the reference yield multiplied by the expected performance ratio. The irradiance input can come from module-level sensors (high accuracy, high hardware cost), cell sensors (medium accuracy, low cost) or a local comparison (medium-low accuracy, no hardware, but the baseline must be checked). If you plot array yield against reference yield and fit a straight line through the origin, the slope is roughly the average array performance ratio. A change in the weekly slope points to a sudden fault or a trend.

<!-- review notes
- sentence 3: support check: partial - Unit h is stated and Ref_Yield in kWh/kWp is shown, but nothing says monitoring platforms show it that way over a period specifically; the Ref_Yield label is stated though.
-->
