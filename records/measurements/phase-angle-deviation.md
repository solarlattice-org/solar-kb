---
id: meas:phase-angle-deviation
type: Measurement
name: Phase angle deviation
aliases:
- phase shift
- phase error
---
A phase angle deviation means the measured current or voltage phasor does not sit at the angle you expect relative to a reference phase or to its primary signal. Instrument transformers usually add both a ratio error and a phase shift to the secondary signal, and a current transformer can shift the angle unevenly across its range. A time delay on the voltage transformer measurement path also appears at the meter terminals as a phase shift in the waveform, and it can be corrected with a compensation angle. To check for incorrect CT polarity, compare the angle of each phase against a reference phase. To check the vector-group compensation selection, measure the operating current and phase angle. Near zero power factor, a small phase angle error causes a relatively large error in real power readings, while the reactive power reading barely changes. Meters can correct a known deviation with phase angle compensation settings. For example, a secondary current that leads by 1 degree corresponds to a correction of 60 minutes.

<!-- review notes
- sentence 1: support check: partial - Passages mention phase shift relative to the primary signal and angular comparison against a reference phase, but never define a phase angle deviation as such.
- sentence 3: support check: partial - Passage shows a PT-path time shift producing a phase shift at meter terminals and a correction angle computed from it, but the text is fragmentary and does not explicitly say a compensation angle corrects it.
-->
