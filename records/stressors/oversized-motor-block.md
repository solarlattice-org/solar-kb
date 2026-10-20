---
id: stressor:oversized-motor-block
type: Stressor
name: Oversized motor blocks
---
On single-axis trackers, a motor block is a group of rows driven by one actuator or control group. When it is oversized, that block can cover several different terrain conditions. A large block forces every row in it to the same command angle, even where individual rows would do better at different backtracking positions. This raises either shading loss or cosine loss. Oversized motor blocks contribute to terrain undulation yield losses, which can be recovered and tend to concentrate in specific motor blocks. Trackers can follow their commanded angle correctly and still lose yield, because the command itself is wrong when the motor block layout is too coarse for the terrain. To find these losses, compare motor block boundaries, backtracking settings and shade-model output with normalized row or inverter production in the morning and afternoon. To reduce the losses, check the assumptions behind the motor block sizing, tune backtracking parameters for each terrain zone, and correct grading or tracker geometry where practical.

<!-- review notes
- sentence 3: support check: partial - Passages say losses are recoverable and concentrated in specific motor blocks, and mention validating block sizing, but don't explicitly say oversized blocks contribute to them.
-->
