---
id: comp:transformer
type: Component
name: Inverter transformer
---
In Sunny Island battery inverters the transformer is an internal part whose temperature is monitored. Transformer overtemperature on the master is reported as F109, and on slave devices 1 to 3 as W110, W111 and W112. Transformer overtemperature is a form of inverter overheating. It happens when the master or slave transformer gets too hot because of overload or high ambient temperature. Before it reaches an overtemperature error, the device reduces battery charging power when the transformer or heat sink is too hot. It reports this derating as W137 to W140. To clear these events: reduce or stagger the connected loads, clean the fans and ventilation grids, then restart the unit once it has cooled. If the message keeps coming back, replace the inverter. In grid-tied plants, a transformer after the inverter raises the inverter output voltage to the level the grid requires. That transformer must be designed for the PV load cycle (loaded by day, no load at night) and protected against overload and short circuit. Its tolerance for faults such as ground faults and voltage dips must be considered. Do not switch the transformer while the inverter is energized. The resulting voltage swings can damage inverter components, so disconnect the inverter first. Distribution transformers are factory tested to ANSI C57.12.00 and C57.12.90. The tests include polarity, ratio, losses, impedance and dielectric checks.

<!-- review notes
- sentence 2: support check: partial - Passages say the master/slave transformer temperature is too high due to overload or ambient temperature, but do not frame it as a form of 'inverter overheating' (minor classification).
- sentence 4: support check: partial - Steps for F109–W112 match (reduce loads, clean fans/grids, restart after cooling, replace if persists), but W137–W140 derating advice differs (no replace; increase power capacity), so the claim over-applies to 'these events'.
- sentence 8: support check: partial - Tests per ANSI C57.12.00/C57.12.90 and the listed checks are stated, but only for GE PROLEC distribution transformers, not distribution transformers generally.
-->
