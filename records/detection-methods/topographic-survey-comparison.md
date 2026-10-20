---
id: method:topographic-survey-comparison
type: DetectionMethod
name: Topographic survey comparison
claims:
- claim_id: c1
  rel: produces
  target: meas:motor-block-aligned-loss
  note: Underperformance mapped by tracker block ID and row location lines up with motor block boundaries
    rather than with failed equipment.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h6
    h: c071b96206e3
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h4
    h: 7ebb164fa9e1
  review: drafted
  review_note: 'support check: partial - Passages say losses can cluster around motor block boundaries
    and be strongest at low sun angle, but the specific signal patterns (string current lower in boundary
    rows, inverter output for blocks with boundary rows) are not stated.'
- claim_id: c2
  rel: produces
  target: meas:grade-break-aligned-loss
  note: When affected zones are overlaid on topographic survey data, losses group around grade breaks,
    swales and rolling sections that differ from the representative slope in the model.
  cite:
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h6
    h: c071b96206e3
  - src: src:pv-root-cause-terrain-undulation-yield-losses
    loc: sec=h4
    h: 7ebb164fa9e1
  review: verified
  verified_by: joshuahamsa
  verified_at: 2026-10-20
  review_note: 'support check: partial - Passages support losses clustering around grade breaks, swales
    and rolling sections and repeating by sun position, but not the specific string current or inverter
    signal wording or morning/afternoon backtracking windows.'
---
Topographic survey comparison lays the map of underperforming zones over the site's survey data, the construction as-builts and the terrain that was used in the original energy model. Begin by mapping underperformance by tracker block ID, row location and time of day, then check where the affected zones fall on the terrain. Before you compare, take out intervals affected by curtailment, clipping, outages and inverter constraints, so that only backtracking periods are left. This method is used to confirm terrain undulation yield losses. These show up as losses that repeat with sun position, are strongest at low sun angles, and group around grade breaks, swales and motor block boundaries. Losses that line up with terrain features or motor block boundaries point to a geometry or model problem rather than an equipment failure. To strengthen the result, combine it with drone imagery, row-end angle surveys, tracker command logs and normalized string or inverter output.

<!-- review notes
- sentence 3: support check: partial - u6 says to isolate backtracking intervals from curtailment, clipping, outages and inverter constraints, and it places this after the mapping step, so the 'before you compare' ordering is the opposite of the passage.
- sentence 4: support check: partial - Signature details are supported by u9, but the passages do not state that this specific method (topographic comparison) confirms the losses; they describe a broader diagnostic workflow.
- sentence 6: support check: partial - u6 lists drone imagery, row-end angle surveys, tracker command logs and normalized output as ways to show alignment, but does not say to combine them to strengthen the topographic comparison result.
-->
