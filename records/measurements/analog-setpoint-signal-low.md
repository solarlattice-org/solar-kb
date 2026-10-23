---
id: meas:analog-setpoint-signal-low
type: Measurement
name: Analog setpoint signal low
aliases:
- AnInFail
signals:
- point: model_103.W
  unit: unit:W
  pattern: AC power stays at the last valid setpoint or at Pmax instead of following the external command
---
On SMA central inverters the reactive power setpoint status reads AnInFail when an analog-input mode such as VArCnstNomAnIn or PFCnstAnIn is selected and the analog input measures less than 2 mA. Analog setpoints reach the Cluster Controller as current signals from 0 mA to 20 mA, used for active power limitation and the reactive power setpoint. The Cluster Controller treats analog input signals as valid up to 21 mA, so a slight overload can be used to reach the maximum setpoint. An invalid input status is only recorded as a fault after the configured failure tolerance time has passed. If the display shows no current signal for the analog signal source or sensor, the source or sensor is probably not connected correctly. The recommended first step is to check that the cable is properly connected to the analog input.

<!-- review notes
- sentence 4: support check: partial - The passage says failure tolerance time indicates the time as of which an invalid input status is recorded as a fault, but doesn't say 'only' after it or that it is configured.
- sentence 6: support check: partial - The corrective measure to check the cable at the analog input is stated for AnInFail, but nothing says it is the recommended first step or ordering.
-->
