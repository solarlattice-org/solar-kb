---
id: meas:battery-undertemperature-message
type: Measurement
name: Battery undertemperature message
aliases:
- BatTmpLoWarn
- Low battery temperature warning
- Battery undertemperature
- Battery undertemperature in charge mode
- XA07DcLoTmpC
---
This signature is an inverter or battery inverter event that reports the battery is too cold. On Sunny Island units it shows up as warning W211, a level 1 low battery temperature warning. When an external battery management system reports the condition over SiCom, it shows up as warnings W940 and W942 at level 1 or as errors F924 and F926 at level 3. The 942 and 926 codes refer to the charge mode. Other SMA inverters log this condition as event 9314, battery undertemperature. For that event the cause has to be found by Service, and the battery manufacturer should be contacted. First check that the battery room is warm enough. If the error comes from the external battery management, clear the cause using the battery manufacturer's documentation.

<!-- review notes
- sentence 4: support check: partial - Event 9314 with Service-determined cause and contacting battery manufacturer is stated, but 'other SMA inverters' is not named in the passages.
-->
