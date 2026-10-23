---
id: symptom:meter-wiring-reversed
type: Symptom
name: Meter wiring reversed
aliases:
- reversed CT polarity
claims:
- claim_id: c1
  rel: observed_as
  target: meas:low-meter-power-factor
  note: 'AlsoEnergy guidance: when current and voltage look normal but power is lower than expected, check
    the reported power factor against 0.9. If two phases show power factors of 0.5 and -0.5, those two
    phases are swapped with each other. This is a voltage-reference/CT phase mismatch.'
  cite:
  - src: src:alsoenergy-alsoenergy-installation-manual-pv-rev-15-1
    loc: sec=5.5.3
    h: 3a15a4765001
  review: drafted
  review_note: 'support check: partial - The passage covers the PF check against 0.9 and the 0.5/-0.5
    swapped phases, but it doesn''t say that ''meter wiring reversed'' is observed as low power factor.
    It describes a phase mismatch, not reversal.'
---
The meter or its current transformers have been wired the wrong way round, for example with the meter's input and output connections swapped. First check whether the meter is connected correctly and whether its input and output wiring is reversed. If an existing system is enabled, also check the rated power setting of the existing inverter. A related wiring error is a voltage reference that does not match its CT phase. Current and voltage then read normal, but power comes out lower than expected. In that case, check the power factor in the monitoring portal. Two phases reading 0.5 and -0.5 means those two phases are swapped. Trace the wiring between the meter and the feeder against the wiring diagram. Do not rely on meter validity alarms to catch this: some controllers do not detect reversed CT polarity, so check meter wiring at commissioning.

<!-- review notes
- sentence 5: support check: partial - The note says Meter Invalid doesn't address reversed CT polarity and that wiring should be validated at commissioning. The claim that 'some controllers' don't detect it is a generalization, since the note is about the Tesla controller.
-->
