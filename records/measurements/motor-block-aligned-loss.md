---
id: meas:motor-block-aligned-loss
type: Measurement
name: Loss aligned with motor blocks
signals:
- point: model_403.InDCA
  unit: unit:A
  pattern: normalized string current lower in rows near motor block boundaries during morning and afternoon
    backtracking windows
- point: model_160.DCA
  unit: unit:A
  pattern: normalized string current lower in specific tracker blocks or rows, repeatable by time of day
- point: model_103.W
  unit: unit:W
  pattern: normalized inverter output lower for inverters serving affected terrain zones, mostly in morning
    and afternoon backtracking windows
---
This signature is underperformance that clusters along tracker motor block boundaries instead of being scattered randomly across the array. It usually repeats with sun position and is strongest during low sun-angle periods, so compare normalized row or inverter output across morning and afternoon windows. Map underperformance against tracker block IDs, row locations and time of day, then compare the affected zones with topographic survey data, as-built drawings and the terrain assumed in the energy model. Before attributing the loss to geometry, separate backtracking intervals from curtailment, clipping, outages and inverter limits. Drone imagery, row-end angle surveys, tracker command logs and normalized string or inverter output show whether losses line up with grade breaks or motor block edges rather than with equipment failure. The main failure mode is terrain undulation yield loss: a large motor block can drive one command angle across rows that need different backtracking positions, which adds shading loss or cosine loss. Tracker twist can look similar and may lower production across a whole tracker block, so check mechanical row geometry with an angle survey before blaming the controls.

<!-- review notes
- sentence 1: support check: partial - Passages say losses can cluster around motor block boundaries (and concentrate in specific motor blocks), but do not contrast this with random scatter, and 'can cluster' is weaker than a defining signature.
- sentence 6: support check: partial - Passages say larger blocks can force one command angle across rows needing different backtracking, increasing shading or cosine loss, but do not call it 'the main failure mode' and it is stated as 'can', not a certainty.
- sentence 7: support check: partial - Twist can depress production across an entire block and mechanical geometry should be verified before blaming controls, but the passages do not say it looks similar to terrain undulation specifically, and the angle survey is mentioned only for validation/detection, not framed as a comparison to terrain loss.
-->
