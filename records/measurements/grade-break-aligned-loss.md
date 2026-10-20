---
id: meas:grade-break-aligned-loss
type: Measurement
name: Loss aligned with grade breaks
signals:
- point: model_403.InDCA
  unit: unit:A
  pattern: Lower normalized string current in rows on grade breaks or swales during morning and afternoon
    backtracking windows
- point: model_103.W
  unit: unit:W
  pattern: Repeatable time-of-day shortfall in normalized output for inverters serving rolling terrain
    sections
- point: model_160.DCW
  unit: unit:W
  pattern: Normalized string or input power lower in rows on grade breaks or swales, repeatable by sun
    position, worst in morning and afternoon
---
This signature is underperformance that clusters at grade breaks, swales, rolling sections and motor block boundaries, where the array departs from the representative slope used in the model. The loss repeats with sun position and tends to be strongest during periods of low sun angle. Rows can be mechanically available and following commands while the loss is present, because the terrain itself causes uneven apparent row spacing, nonuniform tracker angles or local excess shading. To find it, map underperformance against tracker block IDs, row locations and time of day, then compare the affected zones with topographic survey data, as-built drawings and the terrain used in the energy model. Remove curtailment, clipping, outage and inverter-constraint periods so that only backtracking intervals are left. Then use drone imagery, row-end angle surveys, tracker command logs and normalized string or inverter output to check whether the loss follows grade breaks rather than an equipment failure. Comparing normalized row or inverter production between morning and afternoon windows, together with shade-model output and backtracking settings, supports the diagnosis. The main failure mode behind this pattern is Terrain Undulation Yield Losses. Uneven ground disturbs the backtracking geometry, so a row can shade its neighbour or be turned farther off sun than needed, and large motor blocks force one command angle across rows sitting on different terrain.

<!-- review notes
- sentence 5: support check: partial - Passage says to isolate backtracking intervals from the other effects, and the listed tools can show alignment with grade breaks; but 'remove ... leaving only backtracking intervals' and 'check' are roughly right, though it also mentions motor block boundaries and says 'can show', a slight overstatement.
-->
