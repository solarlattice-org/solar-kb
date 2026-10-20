---
id: symptom:nonuniform-tracker-angles
type: Symptom
name: Nonuniform tracker angles
claims:
- claim_id: c1
  rel: observed_as
  target: meas:tracker-angle-mismatch
  note: Measured or reported tracker positions disagree with the commanded angle or the monitoring platform's
    calculated ideal angle; can point to a mechanical or configuration problem that reduces energy harvest.
  cite:
  - src: src:alsoenergy-kb-tracker-config-ideal-tracker-angle-calculation
    loc: sec=front
    h: d9cac50a694b
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=front
    h: 64eaf1450156
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h2
    h: 7af38c6dc2bd
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: tbl=12.r11
    h: 893c0123e9af
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:row-shadow-line-offset
  note: In drone orthomosaic or oblique imagery, the row-end shadow lines differ from those of neighboring
    rows.
  cite:
  - src: src:pv-root-cause-tracker-twist-performance-loss
    loc: sec=h6
    h: 3c47e2464233
  review: drafted
  review_note: 'support check: partial - u18 says to compare row-end shadow lines against neighboring
    rows in drone imagery, but it does not tie this to nonuniform tracker angles as a stated observation
    beyond twisted rows.'
- claim_id: c3
  rel: observed_as
  target: meas:motor-block-aligned-loss
  note: Terrain-driven losses can cluster at motor block boundaries, where one command angle serves rows
    on different terrain.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h4
    h: 7ebb164fa9e1
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=front
    h: 52c6d93eccc6
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h5
    h: 206561d63ce8
  review: drafted
- claim_id: c4
  rel: observed_as
  target: meas:grade-break-aligned-loss
  note: Losses gather around grade breaks, swales and rolling sections that differ from the slope the
    model assumes.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h4
    h: 7ebb164fa9e1
  review: drafted
---
On single-axis tracker sites, rows or sections of rows sit at different tilts, even though they still respond to commands. Monitoring shows the tracker positions do not match the commanded angle or the calculated ideal angle, and the affected rows give less normalized current than neighboring rows. Losses repeat with sun position and are worst at low sun angles. Compare morning, solar-noon and afternoon windows, because a row can look fine at one angle and fail at another. Tracker twist is a defect in which part of a row no longer holds a common plane with the rest because of torque tube, drive, bearing, damper or coupler problems. Confirm it by measuring the angle at the drive end, center and free end under the same command. Terrain undulation losses can happen even when every row follows its command correctly. In that case the losses cluster at motor block boundaries, grade breaks and swales, because the backtracking model assumes a simpler slope than the real ground. Check the mechanical geometry first, using drone shadow lines and field angle checks, before blaming the controls. Controller offsets, bent torque tubes, foundation settlement and loose clamps can all produce similar signatures.

<!-- review notes
- sentence 2: support check: partial - u10 gives the mismatch with commanded/ideal angle and u13 gives lower normalized current in affected rows, but no passage joins them as one monitoring observation.
-->
