---
id: meas:ir-cold-area
type: Measurement
name: Cold area in IR image
aliases:
- cooler cells
- colder bubbles
---
When current is fed into a module in the dark, cells strongly affected by shunting-type potential induced degradation (PID-s) appear cooler than the other cells in the IR image, matching the darker cells seen in EL. This happens because an injected current heats each cell in proportion to its voltage, and a shunted PID cell has a lower voltage, so it warms up less. In the field, you can inject current into one string at night and look for the cooler cells. Sunlight reflections and shadows do not get in the way, and outdoor EL can be done at the same time. The pattern reverses under sunlight close to the maximum power point, where the same PID cells look warmer, and at open circuit no pattern shows at all, so always record the load condition. In modules aged for many years in the field, delamination can show up in IR as colder bubbles. The camera or software area and spot box tools report minimum, average and maximum temperature for a selected region, which helps you measure a cold area against its surroundings. Measure under steady-state conditions. Set the reflected background temperature correctly, because very cold or very hot objects nearby can shift the apparent temperature of the target.

<!-- review notes
- sentence 4: support check: partial - Reversal near MPP and no pattern at open circuit are stated, but the 'always record the load condition' advice is not explicitly stated (only implied).
-->
