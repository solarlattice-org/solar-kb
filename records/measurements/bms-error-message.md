---
id: meas:bms-error-message
type: Measurement
name: Battery management error message
aliases:
- Error message via SiCom
- Battery error
---
This signature is an error or warning on the battery inverter that the external battery management system passes over the SiCom link. On SMA Sunny Island units, battery overvoltage reported by the battery management shows as F921 at level 3, with the internal name XA02DcHiVolt. Related SiCom codes cover general errors, undervoltage, over- and undertemperature, charging current too high, short circuit, an error in the battery, and an internal battery management error, which also has a level 1 warning, W947. Separate inverter codes, F208 and W209, flag a battery overvoltage error that the inverter detects itself. A battery error may also mean the external battery management was detected but never configured, the battery management timeout monitor tripped, or the measured battery voltage is outside the measurement range. To fix it, clear the cause in the external battery management system using the battery manufacturer's documentation, and check that the data cable of the lithium-ion battery is connected correctly. Check that the message is plausible before acting, and replace the battery if needed.

<!-- review notes
- sentence 4: support check: partial - F208 and W209 are battery overvoltage errors, but the passages don't say the inverter detects them itself or that they are separate from SiCom.
- sentence 5: support check: partial - Unconfigured BMS, timeout trigger, and out-of-range voltage are stated, but the passages describe the voltage as above or below range, and these are separate battery error variants rather than stated alternate meanings of a single error.
- sentence 1: review: partial - The passages support errors (F9xx) and a warning (W947) sent via SiCom from battery management, but they never say the battery management system is external.
- sentence 4: review: partial - The rows show F208 (level 3) and W209 (level 1) as battery overvoltage errors, but nothing says the inverter detects them itself or that they are separate from the SiCom codes.
-->
