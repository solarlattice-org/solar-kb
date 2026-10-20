---
id: meas:high-voc
type: Measurement
name: High open-circuit voltage
---
This signature is a string open-circuit voltage reading that comes out higher than the value expected for that string. Measure each string's open-circuit voltage with suitable test equipment before any switches are closed or string overcurrent protection is fitted. To judge the reading, compare it with a value worked out from the module datasheet or a PV model that accounts for module type, module count and cell temperature. You can also measure one module and scale up to the full string, or, where strings are identical, compare strings with each other. A reference string with its own meter helps when irradiance is unstable. High readings usually come from wiring errors, such as the wrong number of modules connected in series in the string. Open-circuit voltage can also be read from a string I-V curve trace, which gives short-circuit current and fill factor at the same time.

<!-- review notes
- sentence 1: support check: partial - Passage says high voltage readings are usually from wiring errors and readings are compared to expected value, but doesn't define a signature; roughly supported though 'higher than expected' is implied.
- sentence 5: support check: partial - Passage says high readings are usually wiring errors, and mentions wrong number of modules in series as a common error, but doesn't explicitly link it to high readings.
- sentence 6: support check: partial - I-V curve gives Voc, Isc and fill factor, but passage doesn't say they are obtained at the same time (though implied by a single trace).
-->
