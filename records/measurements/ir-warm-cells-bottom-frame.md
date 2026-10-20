---
id: meas:ir-warm-cells-bottom-frame
type: Measurement
name: Warm cells at bottom frame
aliases:
- PID-s IRT patterns
- PID patterns
---
In an infrared image, single cells look warmer than the rest, and the cells in the lower part of the module next to the frame run hotter than those in the upper and middle parts. The pattern shows up in IR thermography of modules working in direct sunlight close to their maximum power point. Clear-sky imaging during operation is the main field method for finding shunting-type potential induced degradation (PID-s). The operating point matters: at open circuit the cell temperatures are even and no pattern appears, while at short circuit the image is dominated by heating from reverse-biased cells. If current is injected in the dark, either in the lab or into a string at night, the affected cells appear cooler than the healthy ones instead of warmer. The usual cause is Potential Induced Degradation, specifically massive shunts from PID and/or polarization. The pattern is stronger in modules close to one pole of the string, typically the negative pole, and the number of warm cells tracks the module power loss along the string. Electrically, module power and fill factor are reduced, and low-light performance suffers more than performance at STC. Use IV measurements or EL imaging to confirm the diagnosis.

<!-- review notes
- sentence 6: support check: partial - The passages support a stronger pattern near the negative pole and warm-cell count agreeing with power loss, but 'typically negative pole' is only partly stated, since u7 says 'one of the poles'.
-->
