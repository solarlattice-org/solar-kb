---
id: fm:terrain-undulation-yield-losses
type: FailureMode
name: Terrain Undulation Yield Losses
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:terrain-undulation
  note: Local grade changes make the built tracker field differ from the simplified geometry assumed in
    backtracking and yield models.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=front
    h: 52c6d93eccc6
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h4
    h: 7ebb164fa9e1
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h5
    h: 206561d63ce8
  review: drafted
- claim_id: c2
  rel: caused_by
  target: stressor:oversized-motor-block
  note: One control group spanning several terrain conditions forces a single command angle onto rows
    that would need different backtracking positions, raising shading or cosine loss.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h5
    h: 206561d63ce8
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h7
    h: e0c095063407
  review: drafted
- claim_id: c3
  rel: caused_by
  target: stressor:inaccurate-model-input
  note: A terrain model or backtracking algorithm that is too coarse can make the commanded angle itself
    the source of loss.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h7
    h: e0c095063407
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h4
    h: 7ebb164fa9e1
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:low-sun-angle
  note: Losses are usually strongest during low sun-angle periods.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h4
    h: 7ebb164fa9e1
  review: drafted
  review_note: 'support check: partial - Low sun angle is stated as when losses are strongest, not as
    a cause of the loss.'
- claim_id: c5
  rel: affects
  target: comp:single-axis-tracker
  note: Row geometry and backtracking behavior of single-axis trackers are disturbed.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h5
    h: 206561d63ce8
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=front
    h: 52c6d93eccc6
  review: drafted
- claim_id: c6
  rel: presents_as
  target: symptom:spatially-uneven-loss
  note: Losses concentrate in specific motor blocks and cluster near block boundaries, grade breaks, swales
    and rolling sections.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=front
    h: 52c6d93eccc6
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h4
    h: 7ebb164fa9e1
  review: drafted
- claim_id: c7
  rel: presents_as
  target: symptom:sun-position-repeatable-loss
  note: The production signature typically repeats with sun position, especially morning and afternoon.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h4
    h: 7ebb164fa9e1
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=front
    h: 52c6d93eccc6
  review: drafted
- claim_id: c8
  rel: presents_as
  target: symptom:inter-row-shading
  note: A row that backtracks correctly under a flat-slope assumption may still shade its neighbor.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h4
    h: 7ebb164fa9e1
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h5
    h: 206561d63ce8
  review: drafted
- claim_id: c9
  rel: presents_as
  target: symptom:nonuniform-tracker-angles
  note: Rows follow commands but terrain produces uneven apparent row spacing and tracker angles.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h4
    h: 7ebb164fa9e1
  review: drafted
- claim_id: c10
  rel: detected_by
  target: method:topographic-survey-comparison
  note: Compare affected zones with topographic survey, as-builts and the terrain used in the original
    energy model.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h6
    h: c071b96206e3
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=front
    h: 52c6d93eccc6
  review: drafted
- claim_id: c11
  rel: detected_by
  target: method:string-inverter-trend
  note: Normalized row, string or inverter output across morning and afternoon windows, mapped to tracker
    blocks.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h6
    h: c071b96206e3
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=front
    h: 52c6d93eccc6
  review: drafted
- claim_id: c12
  rel: detected_by
  target: method:constrained-interval-classification
  note: Separate backtracking intervals from curtailment, clipping, outages and inverter limits.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h6
    h: c071b96206e3
  review: drafted
- claim_id: c13
  rel: detected_by
  target: method:drone-inspection
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h6
    h: c071b96206e3
  review: drafted
- claim_id: c14
  rel: detected_by
  target: method:row-angle-survey
  note: Row-end angle surveys show whether losses follow grade breaks.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h6
    h: c071b96206e3
  review: drafted
- claim_id: c15
  rel: detected_by
  target: method:tracker-command-log-review
  note: Following the commanded angle does not prove correct performance.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h6
    h: c071b96206e3
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h7
    h: e0c095063407
  review: drafted
- claim_id: c16
  rel: detected_by
  target: method:shade-model-comparison
  note: Compare backtracking settings and shade-model output with measured behavior.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=front
    h: 52c6d93eccc6
  review: drafted
- claim_id: c17
  rel: mitigated_by
  target: mit:backtracking-tuning
  note: Refine backtracking parameters per terrain zone.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=front
    h: 52c6d93eccc6
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h2
    h: 0eaaad46eb44
  review: drafted
- claim_id: c18
  rel: mitigated_by
  target: mit:motor-block-sizing-review
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=front
    h: 52c6d93eccc6
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h2
    h: 0eaaad46eb44
  review: drafted
- claim_id: c19
  rel: mitigated_by
  target: mit:grading-correction
  note: Where practical.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=front
    h: 52c6d93eccc6
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h2
    h: 0eaaad46eb44
  review: drafted
- claim_id: c20
  rel: mitigated_by
  target: mit:tracker-geometry-correction
  note: Where practical.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=front
    h: 52c6d93eccc6
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h2
    h: 0eaaad46eb44
  review: drafted
- claim_id: c21
  rel: mitigated_by
  target: mit:energy-model-update
  note: Update models with measured row-level behavior.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=front
    h: 52c6d93eccc6
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h2
    h: 0eaaad46eb44
  review: drafted
---
Terrain undulation losses happen when rolling ground makes the real tracker rows differ from the simple geometry assumed by backtracking and yield models. Trackers can be working and following their commands, yet the command itself causes inter-row shading or drives rows further off sun than needed. Large motor blocks make it worse because one command angle is applied across rows sitting on different terrain. Expect losses that repeat with sun position, peak at low sun angles, and cluster around motor block boundaries, grade breaks and swales. To confirm, map underperformance by tracker block, row and time of day, and compare it with topographic survey, as-builts and the terrain used in the energy model. Separate backtracking periods from curtailment, clipping, outages and inverter limits, then use drone imagery, row-end angle surveys, tracker command logs and normalized string or inverter output to tie losses to terrain rather than equipment faults. Fixes include tuning backtracking per terrain zone, checking motor block sizing, correcting grading or tracker geometry where practical, and updating energy models with measured row behavior.
