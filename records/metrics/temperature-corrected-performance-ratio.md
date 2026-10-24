---
id: metric:temperature-corrected-performance-ratio
type: Metric
name: Temperature-corrected performance ratio
aliases:
- temperature-corrected PR
- weather-corrected performance ratio
- PR STC
- PRTcorr
- PRTC,ref
- PRTO
- temperature-corrected PR to STC
category: Performance
claims:
- claim_id: c1
  rel: subclass_of
  target: metric:performance-ratio
  note: A performance ratio adjusted for module temperature using the module power temperature coefficient,
    so that it reflects operation at a reference temperature (often the STC 25 °C).
  cite:
  - src: src:iea-pvps-t13-22-2021
    loc: sec=1.3.2
    h: 86c1ba054558
  - src: src:iea-pvps-t13-25-2022
    loc: sec=h23
    h: 844d07b9d0e3
  - src: src:trn-oandm-spe-o-and-m-best-practice-guidelines-v-5-0-a07c44238b
    loc: sec=h180
    h: af1a5029e7ee
  review: drafted
---
The temperature-corrected performance ratio is a performance ratio adjusted to show the yield the plant would have had if its modules ran at an agreed reference temperature. That reference is often the STC value of 25 °C. It removes most of the normal seasonal swing in plain PR, which reads higher in cold months and lower in hot months because hot modules are less efficient. Formula: take the specific yield for the period, divide it by the reference yield times a temperature factor of one minus the module temperature coefficient multiplied by the average module temperature minus 25 °C, then multiply by 100. The inputs are the plant specific yield, the reference yield, the plant peak DC power, the temperature coefficient of the installed modules in percent per °C, and the measured module temperature. Log module temperature at intervals of 15 minutes or shorter. Average it over the period weighted by the specific yield of each interval (or by irradiance), so the hottest, most productive hours count the most. It is the recommended practice when PR has to be measured over a short window, such as two weeks or a month during a commissioning test or a handover between O&M providers. The correction should follow IEC procedures, and IEC 61724-1 gives the preferred form of the equation. Some seasonal variation remains because of angle-of-incidence and spectral effects, and a biased temperature coefficient can add its own seasonal pattern.

<!-- review notes
- sentence 2: support check: partial - Passages say the seasonal variation (higher PR in cold, lower in hot due to module temperature) can be significantly reduced, but not that most is removed; u4 says seasonal fluctuations remain.
- sentence 3: support check: partial - The formula is PR_TC = Yf/(Yr×[1−β/100×(Tmod−25)])×100, matching the statement, but the temperature used is weighted by specific yield; the 'average' is not qualified, and the multiplication by β in percent is implicit.
- sentence 4: support check: partial - Yf, Yr, β and module temperature are listed inputs, and P0 is defined, but P0 does not visibly appear in the formula, so calling it an input is questionable.
- sentence 5: support check: partial - Passages support up-to-15-minute logging and yield-weighted (or irradiance-weighted) averaging, but the claim that hottest hours count the most is not stated; the weighting is by yield, not temperature.
-->
