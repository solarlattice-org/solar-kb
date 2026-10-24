---
id: metric:specific-yield
type: Metric
name: Specific yield
aliases:
- final yield
- Yf
- specific annual yield
- kWh/kWp
- specific system yield
- system yield
category: Performance
claims:
- claim_id: c1
  rel: part_of
  target: std:solarpower-europe-om-guidelines
  note: Defined in section 10.3.2 of the guidelines.
  cite:
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: sec=10.3.2
    h: 61435db5a239
  - src: src:solarpower-europe-om-guidelines
    loc: sec=10.3.2
    h: d4bc2c904336
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: tbl=2.r37
    h: ecf4a0d71b30
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
Specific yield is the total energy a plant generates over a given period, divided by its installed peak DC power. Formula: specific yield for a period equals the plant energy produced or metered in kWh divided by the plant's nominal peak DC power in kWp. The result is stated in kWh/kWp or in peak sun hours. The period can be chosen freely, for example one month or one year. Because the energy is normalised to nominal power, you can compare plants of different sizes or technologies, and also individual inverters with different nominal powers. Its value depends on the irradiation at the site, ambient temperature, shading, the tilt and azimuth of the modules, and the module and inverter types. To judge a system's efficiency, compare its specific yield with the specific annual yield for its location. The specific annual yield is an average taken from irradiation maps. Expected yield is the reference yield multiplied by the expected performance ratio. It gives the specific yield that was expected for a period. Monitoring portals such as Sunny Portal let you switch the display between absolute yield and specific yield.

<!-- review notes
- sentence 8: support check: partial - Passage shows a portal area to select absolute or specific yield display, but doesn't name Sunny Portal or say 'monitoring portals such as' generally.
-->
