---
id: meas:low-voc
type: Measurement
name: Low open-circuit voltage
aliases:
- Voc
- V oc
---
Low open-circuit voltage is a string or module Voc reading that is well below the expected value. Measure each string's Voc with suitable equipment before any switches are closed or string overcurrent protection is fitted. The reading should typically match the expected value within 5 %. You can get the expected value from the module datasheet, from a PV model that accounts for module type, module count and cell temperature, or by measuring one module and scaling it to the string. Under stable irradiance you can also compare identical strings with each other. Under unstable irradiance, use several meters with one kept on a reference string. A low reading often means modules are missing from the string or the wrong number of modules is interconnected. It can also mean modules are connected with reversed polarity, bypass diodes are shorted, insulation is poor, there is later damage, or water has collected in conduits or junction boxes. A bypass diode can fail short if it is physically shorted in the junction box, mounted the wrong way round, or exposed to lightning or static discharge. An I-V curve trace can replace a separate Voc test. If the trace is only used to get Voc and Isc, you do not need to measure irradiance or cell temperature. Light induced degradation lowers Voc together with short-circuit current, fill factor and maximum power. It appears early in the system's life.

<!-- review notes
- sentence 4: support check: partial - The causes listed (wrong polarity, shorted bypass diodes, poor insulation, damage, water) are in the passage. The passage also says missing interconnections and wrong module counts are common errors the test identifies, but it does not say they cause a low reading. 'Often' is an addition.
-->
