---
id: fm:glass-corrosion-abrasion
type: FailureMode
name: Glass Corrosion or Abrasion
aliases:
- PVFS 1-12
- PVFS 1-12vs.01
category: Modules
claims:
- claim_id: c1
  rel: affects
  target: comp:module-glass
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=35.r3
    h: b0be2238bf5b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=16.r3
    h: b0be2238bf5b
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=35.r5
    h: 60bbe86a9d13
  review: verified
  verified_by: joshuahamsa
  verified_at: &id001 2026-10-20
- claim_id: c2
  rel: affects
  target: comp:anti-reflective-coating
  note: Corrosion or abrasion can reduce or remove the benefit of front-side ARC, anti-soiling or multilayer
    coatings.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=35.r3
    h: b0be2238bf5b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=16.r3
    h: b0be2238bf5b
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h80
    h: 8aab36b70d06
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:moisture-exposure
  note: Atmospheric humidity or dew dissolves sodium ions from the soda lime glass surface. This forms
    an alkali base that attacks the glass silicate.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=35.r3
    h: b0be2238bf5b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=16.r3
    h: b0be2238bf5b
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c4
  rel: caused_by
  target: stressor:atmospheric-pollutants
  note: Gases or particles such as pollutants, salt and ammonia act together with humidity.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=35.r3
    h: b0be2238bf5b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=16.r3
    h: b0be2238bf5b
  review: drafted
- claim_id: c5
  rel: caused_by
  target: stressor:improper-cleaning
  note: Mechanical removal techniques or unsuitable cleaning agents can damage or strip the coatings.
    In brush cleaning tests, coated glass lost its ARC while uncoated glass showed no measurable effect.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=35.r3
    h: b0be2238bf5b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=16.r3
    h: b0be2238bf5b
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h80
    h: 8aab36b70d06
  review: drafted
- claim_id: c6
  rel: caused_by
  target: stressor:sand-abrasion
  note: Mostly seen in deserts, where wind, sand and dust together abrade and frost the glass surface.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=35.r3
    h: b0be2238bf5b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=16.r3
    h: b0be2238bf5b
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c7
  rel: presents_as
  target: symptom:hazy-glass
  note: The colour and transparency of the glass change, either evenly or unevenly.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=16.r1
    h: e6cd75ca03ab
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=35.r1
    h: e6cd75ca03ab
  review: drafted
- claim_id: c8
  rel: presents_as
  target: symptom:dull-rough-surface
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=16.r1
    h: e6cd75ca03ab
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=35.r1
    h: e6cd75ca03ab
  review: drafted
  review_note: 'support check: partial - Rougher appearance is stated, but ''dull'' is not mentioned (hazy/milky
    only).'
- claim_id: c9
  rel: presents_as
  target: symptom:stc-power-drop
  note: Lower glass transmission reduces power.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=35.r5
    h: 60bbe86a9d13
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=12.r8
    h: 85e789978c00
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=12.r7
    h: 33a22e8988ea
  review: drafted
- claim_id: c10
  rel: presents_as
  target: symptom:isc-reduction
  note: Listed for both homogeneous and heterogeneous glass corrosion.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=12.r8
    h: 85e789978c00
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=12.r7
    h: 33a22e8988ea
  review: drafted
- claim_id: c11
  rel: presents_as
  target: symptom:iv-curve-distortion
  note: Heterogeneous glass corrosion is listed with changes in Rsc and with inflection points in the
    IV curve.
  cite:
  - src: src:iea-pvps-t13-01-2014
    loc: tbl=12.r8
    h: 85e789978c00
  review: drafted
- claim_id: c12
  rel: leads_to
  target: fm:soiling-losses
  note: Degraded glass can soil more easily, which can cause losses larger than the usual few percent.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=35.r5
    h: 60bbe86a9d13
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=16.r1
    h: e6cd75ca03ab
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=35.r1
    h: e6cd75ca03ab
  review: drafted
  review_note: 'support check: partial - Passages say increased soiling susceptibility can be observed
    and cause larger losses, but not that it leads to soiling losses as a failure mode in those exact
    terms; reasonably close.'
- claim_id: c13
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=16.r2
    h: 9f71f14c12d8
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=35.r2
    h: 9f71f14c12d8
  review: drafted
- claim_id: c14
  rel: detected_by
  target: method:iv-curve-tracing
  note: Listed in parentheses, as a secondary method.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=16.r2
    h: 9f71f14c12d8
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=35.r2
    h: 9f71f14c12d8
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
- claim_id: c15
  rel: detected_by
  target: method:reflectance-measurement
  note: A rise in reflectance shows ARC removal. It can be measured in the lab with an integrating sphere
    or in the field with a hand-held spectrometer.
  cite:
  - src: src:iea-pvps-t13-21-2022
    loc: sec=h80
    h: 8aab36b70d06
  review: verified
  verified_by: joshuahamsa
  verified_at: *id001
---
Glass corrosion or abrasion is damage to the front glass of a module or to its anti-reflective or anti-soiling coatings. It reduces or removes the benefit those coatings give. Corrosion comes from humidity or dew acting with pollutants, salt or ammonia on soda lime glass. Abrasion comes mostly from wind-blown sand and dust in deserts, and from harsh cleaning methods or cleaning agents. Affected glass changes colour and transparency, evenly or in patches, and can look hazy, milky or rougher than undamaged areas. Lower glass transmission causes a power loss that is usually a few percent and levels off over time. Losses can be larger if the glass starts to soil more easily. Confirm it mainly by visual inspection. IV curve tracing can help as a secondary check, showing lower Pmax and Isc. A reflectance measurement with a hand-held spectrometer can show whether a coating has been worn off. Damage to the glass can also raise operation and maintenance costs.
