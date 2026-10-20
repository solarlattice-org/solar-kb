---
id: symptom:dull-rough-surface
type: Symptom
name: Dull or rough surface
claims:
- claim_id: c1
  rel: observed_as
  target: meas:reflectance-increase
  note: On anti-reflective coated glass, reflectance rises steadily with cleaning or abrasion cycles,
    which indicates the coating has been removed. Reflectance can be measured in the field with a small
    hand-held spectrometer. This applies to the glass corrosion or abrasion cause, not to backsheet chalking.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h80
    h: 8aab36b70d06
  review: drafted
  review_note: 'support check: partial - Passages say reflectance rises continuously with cleaning cycles
    indicating ARC removal and handheld spectrometer use, but the link between dull/rough surface and
    reflectance increase, and the exclusion of backsheet chalking, are not stated.'
---
A dull or rough surface shows up in two places on a module: the outer side of the backsheet and the front glass. On the backsheet, a rough or dull look usually comes with a white powder that rubs off on a finger, which points to backsheet chalking. Chalking happens when sunlight and heat break down the polymer in the outer backsheet layer and release the pigment or filler, and a simple wipe test confirms it. On the front glass, a hazy or milky surface that feels rougher than undegraded areas, often with more soiling, points to glass corrosion or abrasion. Glass corrosion comes from humidity combined with pollutants, salt or ammonia; abrasion comes from wind-blown sand and dust, mostly in deserts, or from harsh cleaning methods and agents that wear off the coatings. If the front glass has an anti-reflective coating, measure its reflectance: a rise after cleaning or abrasion shows the coating has been worn away. Chalking does not reduce performance or safety at first, but it may come before backsheet cracking and insulation failures, so keep inspecting affected backsheets regularly and keep ground fault detection active. Whether chalking will lead to cracking cannot be predicted: cracking has been seen with and without chalking.

<!-- review notes
- sentence 6: support check: partial - Passages show rising reflectance with cleaning cycles indicates ARC removal, but do not instruct measuring reflectance as a diagnostic for coated glass; this is largely a test-context inference.
-->
