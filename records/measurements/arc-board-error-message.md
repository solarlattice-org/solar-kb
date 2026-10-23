---
id: meas:arc-board-error-message
type: Measurement
name: Arc board error message
aliases:
- Arcboard Err
- ArcboardErr
- Arc Board Error
- Arc board failure
- AFD board self test failure
---
This signature is an arc board error code shown on the inverter display or in its fault log, for example Arcboard Err or Arc Board Error. It means the internal arc fault detection board failed its own self-check. Manuals give two likely causes: a communication fault between the arc board and the inverter, or an abnormal reading inside the arc board. Some inverters list it as a protection event, while others list it as an alarm. Over Modbus it can appear as an arc board failure bit or as an arc board self-check result register. First, watch the inverter for about five minutes to see if the alarm clears by itself. Then check that the logic connector to the arc board is secure and run the arc fault test from the settings menu. If the error keeps coming back, the arc detection board has probably failed. Replace the arc board or the wiring box, or contact the manufacturer's service team.

<!-- review notes
- sentence 5: support check: partial - Checking the connector and running the arc fault test are stated, but the five-minute observation comes from different manufacturer entries and is not in the same procedure, so the sequence is merged.
- sentence 6: support check: partial - Replacing the arc board or wiring box and contacting service are stated, but 'probably failed' is an inference not explicitly stated.
-->
