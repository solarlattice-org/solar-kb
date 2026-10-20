---
id: comp:anti-reflective-coating
type: Component
name: Anti-reflective coating
aliases:
- ARC
- antireflection coating
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    max: 4
    unit: unit:PERCENT
  conditions: Power loss from corrosion of the anti-reflective coating; bounded by the coating's initial
    improvement
  quote: The power loss caused by the corrosion of the antireflection coating is usually limited to 4%
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: sec=5.2.4
    h: 9ce8dc98ece9
  review: drafted
---
An anti-reflective coating is a thin layer that cuts reflection. Most manufacturers put one on the module front glass to improve efficiency and appearance. Coated modules can deliver about 1-3% more power than modules with uncoated glass. The coating is affected by glass corrosion or abrasion. Humidity combined with pollutants, salt or ammonia, unsuitable cleaning methods or agents, and wind-blown sand in deserts can reduce the coating's benefit or remove it completely. In brush cleaning tests, coated glass lost coating and its reflectance rose, while uncoated glass showed no measurable effect. Reflectance measurement, in the lab or with a hand-held spectrometer in the field, can detect this loss. Power loss from a corroded coating is usually limited to about the gain the coating first gave, around 4%. At cell level, the anti-reflective layer's thickness, uniformity and Si/N ratio affect potential induced degradation. A higher refractive index of silicon nitride lowers this degradation but increases reflection losses. Discolored anti-reflection layers are listed among cell defects. Abrasion of coated glass has been tested with brushes following ASTM D2486. A cleaning test standard, DINspec4867, is being developed from ISO 20566.

<!-- review notes
- sentence 4: support check: partial - Brush tests showed coated glass lost ARC with reflectance rising and uncoated glass no effect, and lab/hand-held spectrometer reflectance measurement is stated; but the uncoated no-effect result was in a test without abrasive, and 'detect this loss' is only implied.
- sentence 8: support check: partial - Brush abrasion per ASTM D2486 and DINspec4867 under development based on ISO 20566 are stated, but 'cleaning test standard' for ISO 20566 is for car coatings; the ASTM test is shown only for a linear abrasion in a figure caption, which roughly supports it.
-->
