---
id: meas:low-string-isc
type: Measurement
name: Low string short-circuit current
signals:
- point: model_403.InDCA
  unit: unit:A
  pattern: string current persistently below that of peer strings with the same layout at the same irradiance
- point: model_302.POAI
  unit: unit:W-PER-M2
  pattern: stable irradiance needed so that string current differences can be read as faults
---
This signature is a string short-circuit current that comes in below the expected value, or below the readings of other identical strings measured at the same time. To take the reading, open all switching devices and disconnecting means and isolate each string from the others. Then short the string briefly with a PV tester, a short-circuit cable in an existing load break switch, or a short-circuit switch test box. Read the current with a suitably rated clip-on ammeter, in-line ammeter or tester. Interrupt it with the load break device and confirm it has reached zero before changing any connection. Under stable irradiance, identical strings should match, typically within 5 % of the average string current. If irradiance is unstable, delay the test, put a second meter on a reference string, or use an irradiance meter or a visual check of the sky to judge whether the readings are valid. This check is meant to find wiring faults and major array faults, not to measure performance. Use an I-V curve test to measure performance and to pinpoint module defects or shading. During operation, some inverters can flag a similar pattern with string-failure detection. This feature compares each input's current with the mean of the inputs and reports an event when the difference exceeds a set tolerance. It is off by default.

<!-- review notes
- sentence 1: support check: partial - Passages say strings should match expected value and each other (within ~5%), but don't state a signature of reading below expected; they only speak of comparison, not direction.
-->
