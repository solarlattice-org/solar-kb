---
id: meas:ten-minute-average-overvoltage
type: Measurement
name: Ten-minute average overvoltage
aliases:
- 10-minute grid overvoltage
signals:
- point: model_103.PhVphA
  unit: unit:V
  pattern: Rolling ten-minute average of the phase voltage stays above the allowed upper limit
---
This signature appears when the inverter's ten-minute average of grid voltage moves outside the permitted range. One manufacturer reports it as fault code 014, meaning the grid voltage has stayed above the inverter's preset AC voltage for a long time. The usual cause is grid voltage or grid impedance that is too high at the connection point. The voltage can rise because the distribution grid has high resistance compared with the PV capacity nearby, or because the wiring between the inverter and the grid connection has too much resistance. To protect power quality, the inverter disconnects from the utility grid when this happens. After a disconnection the voltage falls and the inverter reconnects. The voltage can then climb again, so the trips may repeat after seconds, minutes or longer. On some inverters the moving-average voltage limits can be configured. The default upper limit is 110 percent, and the default trip time on the low-voltage side is 600 seconds. Wait for the inverter to return to normal. If the fault keeps coming back, contact the manufacturer.

<!-- review notes
- sentence 7: support check: partial - Default VoltMax 110% is stated, but the 600 s default is for MinTripT (min voltage trip time), and 'configurable on some inverters' is only implied; 'low-voltage side' matches Min, so mostly fine, but upper limit/ percent range details are covered; the setting is listed per standards only.
-->
