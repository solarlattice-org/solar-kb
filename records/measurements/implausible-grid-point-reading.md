---
id: meas:implausible-grid-point-reading
type: Measurement
name: Implausible grid connection reading
---
Active power fed in at the grid connection point is read from a measurement source such as an energy meter. That source must be installed at the grid connection point itself. Transformer-rated meters use external instrument transformers to isolate or step down current or voltage. On these meters the reading is usually in secondary units. Multiply it by the dial multiplier on the meter faceplate to get primary values. Check this before you decide a grid-point value is implausible. SMA inverters can log an event that says they are waiting for grid voltage and reports a grid connection installation failure. The event tells you to check the grid and the fuses. Solis troubleshooting says to measure AC voltage or frequency at the inverter test points and compare it with the display. If the two disagree, the inverter's measurement circuit may be faulty.

<!-- review notes
- sentence 3: support check: partial - Reading in secondary units and multiplying by the dial multiplier on the faceplate are stated, but the advice to check this before judging a grid-point value implausible is not in the passage.
- sentence 5: support check: partial - Passages say to check AC voltage or frequency at the inverter test points and check the LCD reading, which may indicate a bad measurement circuit, but they do not explicitly say to compare the two or that a disagreement means a fault. They also do not name Solis.
-->
