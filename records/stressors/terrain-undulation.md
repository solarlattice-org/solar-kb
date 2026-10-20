---
id: stressor:terrain-undulation
type: Stressor
name: Undulating terrain
aliases:
- Rolling terrain
- Terrain undulations
---
Undulating terrain means local grade changes across a single-axis tracker field, so the built array no longer matches the simplified geometry assumed by backtracking and energy-yield models. It changes row geometry, backtracking behavior and inter-row shading. The result is terrain undulation yield losses, which can be recovered and are often concentrated in specific motor blocks. A row that backtracks correctly for flat or average slope can still shade its neighbor, or be turned further off sun than needed. Large motor blocks make this worse because they force one angle onto rows that sit on different terrain. Losses repeat with sun position and are strongest at low sun angles. They cluster at motor block boundaries, grade breaks, swales and rolling sections. To find them, map underperformance by block, row and time of day and compare it with topographic surveys and the model's terrain. Then exclude curtailment, clipping, outages and inverter limits, and check with drone images, row angle surveys and tracker command logs.
