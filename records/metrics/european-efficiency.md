---
id: metric:european-efficiency
type: Metric
name: European efficiency
aliases:
- Euro efficiency
- EU efficiency
- European weighted efficiency
category: Inverters
claims:
- claim_id: c1
  rel: subclass_of
  target: metric:inverter-conversion-efficiency
  note: European efficiency is a weighted average of the inverter conversion efficiency (AC fundamental
    output power over DC input power), taken at several partial-load points.
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: sec=h55
    h: 044763d7329c
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
European efficiency is a single figure for comparing inverters. It averages the inverter's conversion efficiency over a spread of power levels that matches the climate at a central European site. Conversion efficiency is the fundamental component of the AC output power divided by the DC input power. It changes with DC input power, operating voltage, ambient temperature and irradiance, which is why a weighted average is used rather than one operating point. The formula multiplies the efficiency measured at each partial load by a weight and adds the results. The weights are 0.03 at 5 percent of nominal power, 0.06 at 10 percent, 0.13 at 20 percent, 0.1 at 30 percent and 0.48 at 50 percent, plus one more term weighted 0.2. The heavy weight at mid-load reflects that most energy in central Europe is produced in the middle of the module power range. Californian efficiency is built on the same idea but is calibrated for sites with higher average irradiance. Manufacturers are expected to measure efficiency according to IEC 61683. A typical European efficiency is around 95 percent, while peak efficiency can reach up to 98 percent. Transformerless inverters reach the highest efficiencies. Datasheets usually list it next to maximum efficiency. For example, Sunny Island battery inverters list 94.0 to 94.3 percent against a maximum of 95.3 to 95.8 percent. Some datasheets add measurement conditions. Sunny Central UP-US units, for example, give 98.6 or 98.7 percent measured without energy self-sufficiency, and Delta M-series string inverters list a Euro efficiency of 98.4 or 98.5 percent.

<!-- review notes
- sentence 2: support check: partial - Definition and dependencies are stated, but the passage does not explicitly say the dependencies are why a weighted average is used (that causal link is inferred).
- sentence 3: support check: partial - Weights are listed and the central-Europe mid-range rationale is stated, but the final 0.2 term is truncated and the heavy 0.48 weight is not explicitly tied to the rationale; also 'efficiency measured at each' is fine.
- sentence 6: support check: partial - Sunny Island figures (94.0–94.3 vs 95.3–95.8) match, though the 94.1 value is within range; the claim that datasheets usually list it next to maximum efficiency is a generalization from only these examples.
-->
