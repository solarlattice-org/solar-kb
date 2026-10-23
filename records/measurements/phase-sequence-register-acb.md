---
id: meas:phase-sequence-register-acb
type: Measurement
name: Phase sequence register reading
aliases:
- Phase Sequence
- GridPhaseSequence
- Power grid phase sequence
---
Some inverters report the three-phase grid phase sequence in a read-only register in the metering group, at Modicon register 40008 (offset 7). In this register, 0 means the sequence is not locked, 1 means clockwise (ABC) and 2 means counterclockwise (ACB). The SGI XTM inverter also has a separate fault code for incorrect phase sequence, with value 32 decimal (0020 hex).

<!-- review notes
- sentence 3: support check: partial - The passage gives fault value 32 / 0020 hex as Incorrect Phase Sequence, but it doesn't name the SGI XTM inverter.
-->
