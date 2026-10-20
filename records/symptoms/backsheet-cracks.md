---
id: symptom:backsheet-cracks
type: Symptom
name: Visible backsheet cracks
aliases:
- torn backsheets
- cracked backsheet
- cracked PA back films
claims:
- claim_id: c1
  rel: observed_as
  target: meas:backsheet-surface-outlier
  note: Optical profilometry with machine learning fits the backsheet surface and flags outliers as cracks,
    bubbles or delamination, then gives crack width and depth. It can find cracks before they are visible
    to the eye.
  cite:
  - src: src:iea-pvps-t13-16-2021
    loc: sec=h57
    h: 6959b882ad79
  - src: src:iea-pvps-t13-16-2021
    loc: fig=66
    h: 7e4162410fbe
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:low-insulation-resistance-alarm
  note: When cracks go through the whole backsheet, insulation resistance collapses, especially when wet.
    Dewy, torn backsheets can cause an insulation fault that stops inverters from starting in the morning,
    which costs yield.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5
    h: cdcdc1167476
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.3
    h: eb148eeff8d7
  review: drafted
  review_note: 'support check: partial - Passages support insulation collapse under wet conditions through
    full-thickness cracks and inverters failing to start in the morning from dewy torn backsheets, but
    nothing on the specific signals (W, POAI, RH) or an alarm measurement; also the cracks being ''visible''
    is not tied.'
- claim_id: c3
  rel: observed_as
  target: meas:busbar-aligned-backsheet-cracks
  note: 'Thermo-mechanical type: cracks start at the outer surface and run lengthwise beneath the busbars.
    They can go through the whole backsheet without any chemical degradation.'
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: fig=51
    h: ccf0b7cffcab
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5
    h: cdcdc1167476
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.3
    h: eb148eeff8d7
  review: drafted
- claim_id: c4
  rel: observed_as
  target: meas:cell-gap-square-cracks
  note: Square cracks under the gaps between cells. They come from acetic acid attack together with thermo-mechanical
    stress, and the crack runs from the encapsulant side toward the air side.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: fig=51
    h: ccf0b7cffcab
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.3
    h: eb148eeff8d7
  review: drafted
  review_note: 'support check: partial - Squared cracks under cell gaps with acetic acid attack and crack
    running encapsulant to air side are stated, but the passage attributes thermo-mechanical stress as
    a driver generally (figure says thermo-mechanical combined with photo-oxidative); acceptable core
    but ''together with thermo-mechanical stress'' is only loosely tied to the acetic acid mechanism.'
---
Backsheet cracking means any visible damage to the module backsheet, either on its surface or through the whole layer stack, showing up as a crack, burst or scratch. The cracks may be local, such as a burst bubble or a scratch, may follow the cell gaps or busbars, or may cover much or all of the module where the surface has become brittle. Squared cracks under the cell gaps and lengthwise cracks under the busbars point to thermo-mechanical cracking. A cracked backsheet under a hot cell points to temperature-induced damage from a hotspot or burn mark. When cracks are found, check whether all modules with the same bill of materials are affected, because this type usually hits a whole plant once operating time builds up. Deep cracks reduce insulation, especially in wet conditions. Look for insulation faults that keep inverters from starting on dewy mornings. Discoloration or heavy chalking of the backsheet can come before cracking. Deep splits are often followed by moisture getting in and corrosion, more so in hot and humid climates. Optical profilometry and image-based deep learning can find and sort cracks, sometimes before they are visible to the eye.

<!-- review notes
- sentence 4: support check: partial - Passage says that when type III occurs, mostly all modules with identical BOM are affected and it occurs with increasing operating time, but the advice to check this is an inference, and it applies to type III specifically.
-->
