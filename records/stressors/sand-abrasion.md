---
id: stressor:sand-abrasion
type: Stressor
name: Sand abrasion
aliases:
- sand blast
- sand blasting
- environmental abrasion
- blowing sand
claims:
- claim_id: c1
  attr: typical_power_loss
  value:
    max: 5
    unit: unit:PERCENT
  conditions: Long-term abrasion of the module glass surface, judged from laboratory testing results
  note: The source says lab results give no evidence of abrasion loss above 5%. The same 5% figure is
    also the usual qualification pass/fail limit for maximum power.
  cite:
  - src: src:iea-pvps-t13-09-2017
    loc: sec=2.3.6
    h: a3dffa29110f
  review: drafted
---
Sand abrasion happens when wind carries sand and dust against the module, wearing and frosting the front glass surface. It is mostly found at desert sites and where sandstorms are frequent. Abrasion wears away anti-reflective and anti-soiling coatings on the glass, which weakens or removes their benefit. The main failure mode it drives is glass corrosion or abrasion. This lowers optical transmittance and therefore module output, but it is not normally a safety or reliability risk for the glass. Depending on how the modules are installed and how often sandstorms occur, the rear side can also be abraded. Polymer backsheets weather more than glass and may then pose safety and reliability risks. Cleaning while sand is on the glass also causes abrasion. In tests, fine sand wore coatings more than coarse sand, and coated glass was affected much more than uncoated glass. Abrasion is found by visual inspection, with IV checks as support. Short-circuit current follows optical transmittance, so it is a useful measure of the loss. Sand can also get into inverters and damage them. Keep enclosures tightly closed, do not open them during dust storms, and use rain-tight or liquid-tight conduit fittings.

<!-- review notes
- sentence 5: support check: partial - Cleaning abrasion, fine sand abrading more than coarse, and coated glass being affected much more than uncoated are supported, but the passages do not clearly say cleaning must happen with sand on the glass (the tests did use sand-covered glass).
- sentence 7: support check: partial - The passages give the precautions (close enclosures, don't open during dust storms, rain-tight or liquid-tight fittings) and say sand can damage the product, but they never name inverters specifically.
-->
