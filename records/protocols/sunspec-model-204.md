---
id: proto:sunspec-model-204
type: Protocol
name: SunSpec model 204 delta-connect three phase (abc) meter
aliases:
- SunSpec 204
- model 204
- ac_meter_abc
- Delta (3-wire) Meter
category: Communication
protocol_kind: information-model
---
SunSpec model 204 is the SunSpec information model for a delta-connected three-phase (ABC, 3-wire) meter, carried over Modbus registers. The SunSpec meter map covers single-phase, split-phase, wye and delta meters in one layout, and the C_SunSpec_DID register says which one is present. A value of 204 means delta. Registers that a given meter type does not use return the unsupported value, so a reading from an unused point should not be taken as a fault. On the Veris E51C series, the meter model ID is in read-only register 40070 and is set by the meter configuration, from 201 to 204. SolarEdge inverters show their meters as SunSpec meter blocks: a common block holds the meter manufacturer, model and serial number, and C_SunSpec_DID follows at addresses such as 40188 (base 0). On SolarEdge three-phase inverters with Synergy technology, add 50 to the default meter addresses for 2-unit inverters and 70 for 3-unit inverters. The Accuenergy Acuvim II puts its SunSpec meter ID at register 50069, read with function 03H. It is followed by phase currents, phase voltages and line-to-line voltages AB, BC and CA, each group with its own scale factor.

<!-- review notes
- sentence 3: support check: partial - Unsupported value return for non-applicable registers is stated, but the advice that such readings should not be taken as a fault is not in the passages.
- sentence 5: support check: partial - Passages show a common block with manufacturer, model, serial and C_SunSpec_DID at 40188 (base 0), but nothing in them names SolarEdge inverters as the device.
- sentence 7: support check: partial - The ID at 50069 with 03H read, the phase currents, phase voltages and line voltages AB/BC/CA with scale factors are shown, but the passages do not name the Accuenergy Acuvim II. Also the scale factors are per group (current, voltage), not per individual quantity.
-->
