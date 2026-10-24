---
id: concept:backtracking
type: Concept
name: Backtracking
aliases:
- tracker backtracking
category: Trackers
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: comp:single-axis-tracker
  note: Backtracking is a tracking substate the tracker control unit runs at dawn and dusk to set a tilt
    angle that avoids row-to-row shading.
  cite:
  - src: src:test-cx-manuals-trina-ps-cm-commissioning-manual-vanguard
    loc: sec=10.1
    h: 5e8007b47b9a
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h5
    h: 206561d63ce8
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:shading-loss
  note: Backtracking accepts some loss from pointing off the sun to avoid larger losses from shaded panels.
    Poorly tuned backtracking can cause either shading loss or cosine loss.
  cite:
  - src: src:test-cx-manuals-trina-ps-cm-commissioning-manual-vanguard
    loc: sec=10.1
    h: 5e8007b47b9a
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h5
    h: 206561d63ce8
  review: drafted
- claim_id: c3
  rel: related_to
  target: symptom:inter-row-shading
  note: The purpose of backtracking is to prevent shading between panels on adjacent tracker rows.
  cite:
  - src: src:test-cx-manuals-trina-ps-cm-commissioning-manual-vanguard
    loc: sec=10.1
    h: 5e8007b47b9a
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h2
    h: 0eaaad46eb44
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h5
    h: 206561d63ce8
  review: drafted
- claim_id: c4
  rel: related_to
  target: fm:terrain-undulation-yield-losses
  note: Rolling terrain disturbs the row geometry that backtracking assumes, so energy that could be recovered
    is lost in specific motor blocks.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h2
    h: 0eaaad46eb44
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h5
    h: 206561d63ce8
  review: drafted
- claim_id: c5
  rel: related_to
  target: mit:backtracking-tuning
  note: 'Recommended fix: refine backtracking parameters separately for each terrain zone.'
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h2
    h: 0eaaad46eb44
  review: drafted
  review_note: 'support check: partial - u8 says refine backtracking parameters by terrain zone, but ''separately
    for each'' is slightly stronger than ''by terrain zone'' (minor).'
- claim_id: c6
  rel: related_to
  target: mit:motor-block-sizing-review
  note: A large motor block applies one command angle to rows that each need a different backtracking
    position.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h2
    h: 0eaaad46eb44
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h5
    h: 206561d63ce8
  review: drafted
---
Backtracking is a tracker operating mode used at dawn and dusk, when the sun is low and tracker rows would otherwise shade each other. In this mode the tracker control unit calculates a tilt angle that keeps adjacent rows from shading each other's panels, then moves the tracker to that angle. It is worth doing when the loss from pointing the panels away from the sun is smaller than the loss shading would cause. The calculation relies on geometry: row pitch, tracker angle, module plane and the horizon formed by the neighboring row. On site, row spacing and panel width must be set for each tracker. Backtracking only stops east-west shading between rows. It does not prevent north-south shading. On rolling terrain, a row that backtracks correctly for a flat-ground assumption can still shade its neighbor or be turned further off the sun than needed. Large motor blocks make this worse because they force one angle onto rows that need different ones. To find these losses, compare backtracking settings, motor block boundaries, shade-model output and row-level production in the morning and afternoon. Then tune the backtracking parameters for each terrain zone. During commissioning, check and adjust the backtracking shadow status. Changing backtracking parameters requires a login on the handheld terminal or the computer app.

<!-- review notes
- sentence 1: support check: partial - u4 gives dawn/dusk substate, but 'sun is low' and 'rows would otherwise shade' are only implied, not stated.
- sentence 8: support check: partial - u9 and u5/u16 support the commissioning check and login requirement, but the handheld terminal login path only shows a LOGIN step, not an explicit requirement statement, though it is implied.
-->
