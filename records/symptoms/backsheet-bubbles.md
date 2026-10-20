---
id: symptom:backsheet-bubbles
type: Symptom
name: Backsheet bubbles or ripples
aliases:
- blisters
- bumps
claims:
- claim_id: c1
  rel: observed_as
  target: meas:backsheet-surface-outlier
  note: Optical profilometry scans of the backsheet, analysed by a machine-learning algorithm, fit the
    backsheet surface and mark outliers from it. These outliers are cracks, bubbles or delamination. This
    is a lab or survey image signature, not a monitoring-data channel.
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h57
    h: 6959b882ad79
  review: drafted
  review_note: 'support check: partial - Passage says profilometry with ML finds outliers that are cracks,
    bubbles or delamination, but doesn''t mention ''ripples'' or the lab/survey-not-monitoring note, and
    bubbles are only one of the outlier types.'
---
On the rear of the module the backsheet looks wavy, with local bumps, bubbles or ripples. This happens where the backsheet separates from the module or where its own layers separate, and in the worst case one or more layers peel off. The main way to find it is visual inspection. Field module surveys record bubbles larger than 5 mm as a defective backsheet. Most often it points to backsheet delamination. Its causes include thermo-mechanical stress from layers that expand at different rates with heat, incompatible materials, attack by heat, UV and moisture, external mechanical stress, or a lamination process that was too short. It is more common in hot, humid climates. Blisters can also form behind a vapour barrier such as aluminium foil. Bubbles over cell surfaces can come from poor adhesion, flux residue or gas released during manufacture. A bubble that has burst counts as backsheet cracking. Deep cracks or burst bubbles can come from local hotspots or burn marks, so check for burn marks and heating at any opened bubble. Bubbles in the open centre of the back are not an immediate safety risk, although that area runs slightly hotter. Bubbles near the module edge can let water in and create a path to ground. Bubbles near the junction box can loosen it, break the bypass diode connection and cause an arc. First check where the bubbles are and whether the junction box is still firmly attached. Then run insulation and wet-leakage tests: replace modules that fail or that pose a direct safety risk, and keep inspecting the rest regularly. Do not confuse these with front delamination: there the bubbles or bright milky areas sit in the encapsulant and are seen from the front of the module.

<!-- review notes
- sentence 2: support check: partial - Detection is listed as VI (with INS in brackets) and bubbles >5 mm count as defect backsheet in documentation, but 'field module surveys record' and 'main way' are only loosely stated.
- sentence 3: support check: partial - Causes and hot/humid frequency are stated, but the claim that bubbles 'most often' point to delamination is not stated (and other causes like flux/gas appear elsewhere).
- sentence 5: support check: partial - Burst bubbles are listed as backsheet cracking and may result from hotspots/burn marks, but the advice to check burn marks and heating at opened bubbles is not stated.
- sentence 7: support check: partial - Replacement of modules with direct safety risk or failing insulation/wet-leakage tests and regular inspections are stated, but the ordering and checking bubble location and junction box attachment first are not prescribed.
- sentence 8: support check: partial - Front delamination is described as bubbles or bright milky areas in the encapsulant, but 'seen from the front' and the warning not to confuse with backsheet bubbles are not explicit.
-->
