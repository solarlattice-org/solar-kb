---
id: meas:abnormal-temperature-display
type: Measurement
name: Abnormal temperature display reading
aliases:
- TempSensorErr
- Abnormal temperature reading
- Detection of abnormal temperature
signals:
- point: model_103.TmpCab
  unit: unit:DEG_C
  pattern: implausible constant low reading, e.g. pinned at sensor floor
---
This signature is an internal inverter temperature value that looks wrong, and it usually comes with a TempSensorErr alarm. To check it, read or observe the temperature value on the inverter display. On one inverter family, the manual lists a sensor reading of -25C as a possible cause of this alarm. The usual causes are a temperature sensor that makes poor contact at its socket connector, or a damaged sensor. Both causes point to a temperature sensor fault, not real overheating. The recommended step is to switch the inverter off, either at its internal disconnects or at the AC supply, and then switch it back on. If the error does not clear, contact the manufacturer's service team.

<!-- review notes
- sentence 1: support check: partial - Passages describe the TempSensorErr alarm as an abnormal temperature reading, but nothing says a 'signature' of internal temperature 'usually comes with' this alarm.
- sentence 5: support check: partial - Causes are sensor contact/damage, which implies a sensor fault, but the passages never state that it is not real overheating.
-->
