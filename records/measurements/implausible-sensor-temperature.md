---
id: meas:implausible-sensor-temperature
type: Measurement
name: Implausible sensor temperature value
aliases:
- TempSensorErr
- Temperature Sensor Failure
- Fault sensor interior temperature
- meas:abnormal-temperature-display
- Abnormal temperature display reading
signals:
- point: model_103.TmpCab
  unit: unit:DEG_C
  pattern: internal temperature stuck at an implausible fixed low value (e.g. -25C) that does not follow
    ambient or load
- point: model_103.TmpSnk
  unit: unit:DEG_C
  pattern: heat sink temperature stuck at an implausible fixed value that does not track AC power or ambient
    temperature
---
The inverter raises a TempSensorErr alarm when its internal temperature reading looks abnormal. One manual names a sensor reading stuck at -25C as a possible cause of the alarm. The usual causes are a temperature sensor socket connector with poor contact or a damaged sensor, which is a temperature sensor fault. To check it, read the temperature on the inverter display, then turn the disconnects off and back on to reboot. If the alarm stays, contact the manufacturer's service team. On some inverters, a temperature sensor failure stops AC production, and the manufacturer recommends a site visit. If a weather station's temperature sensor is not connected correctly, the display shows no measured values for it. A wrong battery temperature reading can make the battery inverter charge at the wrong voltage, and too high a charging voltage can damage the battery. During IV curve tracing, a gap between the real cell temperature and the measured one distorts the curve, so first check that the sensor is still attached to the module.

<!-- review notes
- sentence 4: support check: partial - Display check, disconnect off/on reboot, and contacting service if not cleared appear across passages, but service contact is Solectria-specific and the combined sequence is a synthesis.
- sentence 6: support check: partial - Passage says no measured values shown when the connected temperature sensor isn't correctly connected, but doesn't specify it's a weather station sensor.
-->
