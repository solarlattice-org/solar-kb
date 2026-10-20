---
id: mit:motor-block-sizing-review
type: Mitigation
name: Motor block sizing review
---
A motor block sizing review checks whether the assumptions behind tracker motor block sizes still hold on undulating terrain. It is one of the listed mitigations for terrain undulation yield losses. It matters because one actuator or control group can cover rows sitting on different terrain conditions. Larger blocks can force a single command angle onto rows that need different backtracking positions, which adds either shading loss or cosine loss. Suspect block sizing when losses repeat with sun position, are strongest at low sun angles, and cluster around motor block boundaries, grade breaks or swales. To review it, map underperformance against tracker block IDs, row locations and time of day, then compare the affected zones with topographic survey data and as-built drawings. Separate backtracking periods from curtailment, clipping, outages and inverter limits first, so that losses lining up with block boundaries are not confused with equipment failure. A tracker that follows its commanded angle can still lose yield, because the command itself may come from a motor block layout that is too coarse. The review is usually paired with refining backtracking by terrain zone, correcting grading or tracker geometry where practical, and updating energy models with measured row behavior.

<!-- review notes
- sentence 1: support check: partial - Validating motor block sizing assumptions is a listed mitigation, but the passages don't define it as checking whether assumptions still hold on undulating terrain (only 'validate motor block sizing assumptions').
- sentence 4: support check: partial - Passages describe repeatability by sun position, strongest at low sun angles, and clustering around block boundaries, grade breaks, swales, but don't explicitly say to suspect block sizing based on these.
- sentence 8: support check: partial - The mitigation list includes these actions together, but 'usually paired' is not stated; they are just listed mitigations.
-->
