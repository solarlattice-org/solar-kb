---
id: meas:current-magnitude-mismatch
type: Measurement
name: Expected vs measured current mismatch
aliases:
- Low current
- Current Readings not as Expected
signals:
- point: model_103.A
  unit: unit:A
  pattern: measured phase current magnitude differs from the value expected for the operating point
---
This signature is a gap between the current you expected and the current you actually measured. Several different factors can cause the measured current to differ from the expected value. On PV strings, measure the short-circuit current of each string with suitable test equipment and compare it with the expected value. You can also measure each string's current with a clip-on ammeter while the inverter is tracking the maximum power point, then compare it with the expected value. When identical strings are measured under stable irradiance, their currents should normally agree within about 5 % of the average string current. If irradiance is unstable, you can delay the test, keep one meter on a reference string, or check the readings against an irradiance meter. On a current transformer metering circuit, comparing expected and measured current magnitude can show that the CT is connected to the wrong tap. A negative-sequence current check also helps confirm this.

<!-- review notes
- sentence 1: support check: partial - The passage says low current is a variation between expected and measured current, but the cited text doesn't define 'this signature' as that gap, and the table doesn't state it.
- sentence 7: review: partial - The SEL table supports expected-vs-measured magnitude comparison plus a negative-sequence check for a CT on the wrong tap, but it covers operating current error, not a 'metering circuit' specifically.
-->
