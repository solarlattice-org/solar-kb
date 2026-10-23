---
id: meas:battery-voltage-low
type: Measurement
name: Low battery voltage reading
aliases:
- BatVtgLow
- Warning low battery voltage
- OV-Vbatt
- VBATMINSL2
---
The inverter or battery inverter reports that the measured battery voltage is too low, and it flags this as battery undervoltage. In a severe case, the measured battery voltage falls below the range the device can measure, and the device logs a battery error or battery fault. To confirm the reading, measure the battery voltage at the inverter connection point and check that it is within the battery's specified limits. A possible cause is a battery whose usable capacity has become too small, for example through aging. Check that all battery cells work, because faulty cells can pull the measured voltage below the permitted range. A low battery voltage can also show up as a battery connection failure, so also check that the battery switch is closed. Recover by charging the battery in emergency charge mode or with an external charger, and shed DC loads when the state of charge is low.

<!-- review notes
- sentence 5: support check: partial - Check that all battery cells are functional is stated, but the explanation that faulty cells pull voltage low is not explicit.
- sentence 6: support check: partial - Battery connection failure solution lists checking switch closed and low voltage, but doesn't say low voltage shows up as connection failure in the way framed.
-->
