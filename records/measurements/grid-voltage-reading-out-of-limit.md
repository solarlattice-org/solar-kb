---
id: meas:grid-voltage-reading-out-of-limit
type: Measurement
name: Grid voltage outside limits
aliases:
- Grid incident
signals:
- point: model_103.PhVphA
  unit: unit:V
  pattern: AC phase voltage goes above the overvoltage setting or below the undervoltage setting
- point: model_103.W
  unit: unit:W
  pattern: AC power drops to zero while the inverter is disconnected, then comes back once the voltage
    is normal again
---
This signature is a grid voltage at the inverter connection point that sits outside the permissible range set in the inverter's grid protection settings. On CPS inverters, the voltage limits are set as a percentage of nominal voltage. The level 1 defaults are 110% for maximum and 88% for minimum, and further levels can be set beyond these. On SMA inverters, a grid incident message appears when the ten-minute average grid voltage leaves the permissible range. The cause is grid voltage or grid impedance at the connection point that is too high, and the inverter disconnects from the grid. Before it trips, the inverter may first reduce its output. With volt-watt enabled, a CPS inverter limits AC output current when the voltage goes above 106% of nominal or below rated voltage. An older CPS 36 kW model delivers full power between 90% and 110% of rated grid voltage and limits current below 90%. Check the voltage at the connection point during feed-in to see whether it stays outside the permissible range all the time. If local grid conditions cause the deviation, contact the grid operator, who must agree to any change in feed-in voltage or monitored limits. If the voltage is within range and the message still appears, contact the manufacturer's service.

<!-- review notes
- sentence 1: support check: partial - Passages only say to check whether grid voltage is in the permissible range and mention monitored operating limits; they don't define the signature or tie the range to the inverter's grid protection settings.
- sentence 2: support check: partial - Defaults of 110% max and 88% min for level 1 and a level 3 max exist, but 'further levels beyond these' is only loosely shown and the 'percentage of nominal voltage' basis is not explicit.
- sentence 4: support check: partial - With Volt-Watt enabled the inverter limits current above 106% Un or below rated voltage, but 'before it trips' is not stated in the passages.
- sentence 5: support check: partial - The SCA36KTL full-power range of 90–110% and current limiting below 90% are stated, but 'older' is not supported.
- sentence 6: support check: partial - Check during feed-in whether voltage is permanently in range is stated, but the statement garbles it to 'stays outside the permissible range all the time'.
-->
