---
id: symptom:inter-row-shading
type: Symptom
name: Inter-row shading
aliases:
- row-to-row shading
- self-shading
- row shading
claims:
- claim_id: c1
  rel: observed_as
  target: meas:ir-hot-cell
  note: IR imaging has shown cells overheating where a neighbouring module row shades them.
  cite:
  - src: src:iea-pvps-t13-ir-el-imaging-2018
    loc: fig=22
    h: 4841e78493a5
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:string-current-below-average
  note: Found by comparing monitoring data from shaded strings against unshaded ones. The shaded strings
    produce less, and the gap moves with the time of day and the season.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h54
    h: df63666c4734
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h78
    h: df63666c4734
  review: drafted
  review_note: 'support check: partial - Passages say shading is seen by comparing monitoring data of
    shaded vs unshaded strings and varies with day/season, but do not mention string current specifically
    or that shaded strings fall below.'
- claim_id: c3
  rel: observed_as
  target: meas:pr-drop-low-profile-angle
  note: Average PR is computed separately for times when the solar profile angle is above the shading
    angle and times when it is below. The difference between the two, called PRdrop, estimates row shading
    loss but also contains low-light and inverter part-load effects.
  cite:
  - src: src:iea-pvps-t13-d2-3-analytical-monitoring
    loc: sec=4.2.1
    h: fc5f258c95cb
  review: drafted
- claim_id: c4
  rel: observed_as
  target: meas:grade-break-aligned-loss
  note: On rolling terrain, losses tend to cluster at grade breaks, swales and rolling sections that differ
    from the slope assumed in the model. They are strongest at low sun angles.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h4
    h: 7ebb164fa9e1
  review: drafted
  review_note: 'support check: partial - Passage describes clustering at grade breaks, swales, rolling
    sections and strongest at low sun, but attributes it to terrain undulation losses; the link to inter-row
    shading is implied only by ''locally excessive shading''.'
- claim_id: c5
  rel: observed_as
  target: meas:motor-block-aligned-loss
  note: A single command angle across a large motor block that spans different terrain can cause extra
    shading of some rows.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h4
    h: 7ebb164fa9e1
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h5
    h: 206561d63ce8
  review: drafted
- claim_id: c6
  rel: observed_as
  target: meas:row-shadow-line-offset
  note: In drone orthomosaic or oblique images, the row-end shadow lines of a twisted tracker row differ
    from those of neighbouring rows.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h6
    h: 3c47e2464233
  review: drafted
  review_note: 'support check: partial - Drone imagery to compare row-end shadow lines against neighbours
    is stated for a twisted row, but the passage doesn''t explicitly say they differ or tie it to inter-row
    shading.'
- claim_id: c7
  rel: observed_as
  target: meas:low-normalized-row-current
  note: Rows affected by tracker twist can show lower normalized current than the rows next to them, mainly
    at low sun angles and during backtracking transitions.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h4
    h: 47d9eb5061f6
  review: drafted
  review_note: 'support check: partial - Passage says affected twisted rows show lower normalized current
    than adjacent rows, mainly at low sun angles/backtracking; it ties this to twist and doesn''t mention
    inter-row shading explicitly.'
- claim_id: c8
  attr: typical_power_loss
  value:
    min: 1
    max: 5
    unit: unit:PERCENT
  conditions: Typical cumulative annual shading loss of PV systems, all shading causes including row-to-row
    self-shading
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h54
    h: df63666c4734
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h78
    h: df63666c4734
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions)
- claim_id: c9
  attr: typical_power_loss
  value:
    min: 20
    max: 30
    unit: unit:PERCENT
  conditions: Energy loss from shading that can be observed on rooftop or facade systems, reported as
    'up to 20-30%'
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h54
    h: df63666c4734
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h78
    h: df63666c4734
  review: drafted
  review_note: 'support check: partial - The 20-30% is stated as ''up to'' for rooftop/facade systems,
    not a typical value, and not specific to inter-row shading.; possible conflict with c8 (same source;
    check the conditions)'
---
Inter-row shading happens when one row of modules casts a shadow on the row behind it. The shadow changes with the time of day and the season. You can see it during a visual inspection. In monitoring data, it shows up when you compare shaded strings with unshaded strings or with a shading simulation. In IR images, the cells shaded by the row in front can appear overheated. Prolonged shading can lead to hot spots, which can cause follow-up damage such as burn marks or bypass diode failures. On tracker sites, the extra shading can come from rolling terrain, which upsets the backtracking geometry. It can also come from tracker twist, where one section of a row sits at the wrong tilt. Terrain-related losses repeat with sun position and cluster at grade breaks and motor block boundaries. Twist shows up as rows whose shadow lines and measured angles differ from their neighbours under the same command. Start by comparing normalized row or inverter output across morning, noon and afternoon windows, since losses tend to peak at low sun angles. A tracker that follows its commanded angle can still lose energy if the terrain model or motor block layout is too coarse. Check the backtracking settings as well as the hardware.

<!-- review notes
- sentence 1: support check: partial - Row-to-row self-shading and changing with day and season are stated, but the explicit definition of one row casting a shadow on the row behind is only implied.
- sentence 5: support check: partial - Terrain losses repeating by sun position and clustering at grade breaks/motor blocks are stated, and shadow-line and angle comparison is described for twist, but the passages don't state that twisted rows' shadow lines and angles differ as a signature explicitly.
-->
