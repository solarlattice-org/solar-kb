---
id: method:reflectance-measurement
type: DetectionMethod
name: Reflectance measurement
aliases:
- hemispherical reflectance
- Spectral reflectance
claims:
- claim_id: c1
  rel: produces
  target: meas:reflectance-increase
  note: In cleaning tests, reflectance rose steadily as cleaning cycles increased, which showed that the
    anti-reflective coating had been removed. Nylon brushes caused a larger rise than polyester brushes,
    and fine sand abraded more than coarse sand.
  quote: For both brushes a continuous increase in reflectance with an increasing number of cycles could
    be observed, indicating that the ARC had been removed.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h80
    h: 8aab36b70d06
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
---
Reflectance measurement checks how much light the front glass of a module reflects. It is used to find damage to the glass surface and its anti-reflective coating. In the laboratory, hemispherical reflectance is measured with an integrating sphere. In the field, a small hand-held spectrometer can be used, but you have to account for how repeatable the reading is. In a typical cleaning durability test, reflectance is measured as a special step after the first visual, power and electroluminescence checks and before the accelerated cleaning. A steady rise in reflectance after repeated cleaning shows that the anti-reflective coating is being worn away. This makes the method a way to confirm glass corrosion or abrasion. Several module types showed large changes in reflection after cleaning, which pointed to loss of the coating. Brush tests on uncoated structured glass showed no measurable effect, while coated glass changed significantly. A maximum reflectance gain has been proposed as a pass or fail limit for cleaning tests. This limit is much stricter than the usual module power-loss limit. Abrasion test rigs that use dry abrasives should be enclosed and ventilated so that operators do not risk silicosis.

<!-- review notes
- sentence 4: support check: partial - Rising reflectance indicating ARC removal is stated, but nothing says the method confirms glass corrosion; abrasion yes, corrosion not mentioned.
-->
