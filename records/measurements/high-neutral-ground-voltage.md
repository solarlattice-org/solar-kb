---
id: meas:high-neutral-ground-voltage
type: Measurement
name: High neutral-to-ground voltage
aliases:
- N-G voltage
- Neutral-Ground
---
This signature is a voltage between the neutral conductor and ground that is higher than it should be on the AC side of the system. Some surge protective devices have built-in neutral-to-ground voltage indicators: when they sense excessive voltage, the red service LED blinks and the audible alarm cycles. Inside such a device, a differential voltage circuit watches the neutral-to-ground voltage. A sustained excess slowly overheats a resistor until its heat-shrink sleeve shrinks, but brief transient spikes do not cause this. A common cause is a missing XO or neutral-to-ground bonding jumper, which leaves the system ungrounded and can lead to abnormally high line-to-ground voltages. This is an installation error. It needs immediate attention, because the surge protective device keeps reacting to the overvoltage until it fails. During an inverter inspection, measure neutral-to-ground voltage together with line-to-line, line-to-neutral and line-to-ground voltage while the AC is on, but only if it is safe to do so. Before working on the AC terminals, use a voltage detector to confirm there is no voltage from neutral to ground, phase to ground and phase to neutral.

<!-- review notes
- sentence 1: support check: partial - Passages say excessive N-G voltage is detected, but not that it is on the AC side or defined as a signature; "higher than it should be" is a loose paraphrase of "excessive".
- sentence 3: support check: partial - Differential circuit, resistor overheating, shrink wrap, and no effect from transients are stated, but "sustained" and "slowly" are only implied by "eventually".
- sentence 7: support check: partial - The passages say to check absence of voltage with a voltage detector on the AC terminal blocks between those pairs, but do not say "before working on" them.
-->
