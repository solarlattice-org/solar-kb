---
id: meas:negative-string-current
type: Measurement
name: Negative string current
signals:
- point: model_403.InDCA
  unit: unit:A
  pattern: one string on an MPPT shows negative current before the inverter connects to the grid
- point: model_160.DCA
  unit: unit:A
  pattern: negative or reversed current on an input while the strings on that MPPT are unequal
---
A negative string current means that a string on a multi-string MPPT input reads a current flowing the wrong way, seen before the inverter connects to the grid. Inverter manuals read this as a voltage imbalance between the two strings on one MPPT, most likely because one string has more PV modules than the other. Do not open or close fuse holders while this current is flowing. Doing so is the same as switching under load and can damage equipment or injure people. Design guides say every string within one MPPT zone should have the same module type, the same number of modules in series and the same orientation. They also say to avoid unequal string lengths within a zone. To check string currents in normal MPPT operation, put a clip-on ammeter around each string cable and compare matching strings under stable irradiance. Some inverters have a string-failure detection function. It compares the current on each input with the mean and reports an event when one input is above or below the mean by more than a set tolerance. A negative sign on a multimeter's voltage reading between a string's own positive and negative cables is a different finding: it points to reverse polarity, not to a length imbalance.

<!-- review notes
- sentence 1: support check: partial - Passages say negative string current before grid connection means voltage imbalance between two strings of one MPPT, not that the current flows the wrong way on a string per se; framing is slightly different.
- sentence 7: support check: partial - Passages say a negative meter reading across a string indicates reverse polarity, but they do not explicitly contrast it with length imbalance.
- sentence 7: review: partial - The passages say a negative indicator on the meter across a string's positive and negative cables means reverse polarity, but they never contrast this with a length imbalance.
-->
