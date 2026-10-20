---
id: mit:tracker-geometry-correction
type: Mitigation
name: Tracker geometry correction
---
Tracker geometry correction is a physical repair that brings single-axis tracker rows back to their intended rotational geometry. It addresses performance loss from tracker twist and terrain undulation yield losses. For tracker twist, fix the actuator calibration and the torque tube alignment, repair any bent or loose mechanical parts, and then check the backtracking settings. On rolling terrain, fix the grading or the tracker geometry where this is practical. Pair the fix with backtracking tuned for each terrain zone and a check of the motor block sizing. Confirm the mechanical geometry before blaming the controls, because controller offsets, bad calibration, bent torque tubes, foundation settlement and loose clamps can produce similar production losses. Only treat twist as a defect when sections of the same row disagree by more than the site tolerance under the same command. A row built to follow grade changes is not twisted if it still holds the commanded geometry. After the repair, repeat the angle survey. Compare normalized power against unaffected rows under stable irradiance in both morning and afternoon windows. Limit: a row that follows its command can still lose yield on undulating terrain if the terrain model, the backtracking algorithm or the motor block layout is too coarse. Mechanical correction alone may not recover that loss.

<!-- review notes
- sentence 1: support check: partial - Passages list mitigations like correcting torque tube alignment and tracker geometry, but don't define 'tracker geometry correction' as a physical repair restoring rotational geometry addressing both twist and terrain losses.
- sentence 3: support check: partial - Passages list correcting grading/geometry where practical, refining backtracking by terrain zone and validating motor block sizing, but don't say to pair them as a combined fix.
- sentence 7: support check: partial - The command being too coarse can cause loss despite following it is stated, but the claim that mechanical correction alone may not recover it is an inference not stated.
-->
