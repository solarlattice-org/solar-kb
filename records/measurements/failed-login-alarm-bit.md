---
id: meas:failed-login-alarm-bit
type: Measurement
name: Failed login alarm bit
aliases:
- Unauthorized Network Access Fault
- WARN-30
- Unauthorized Network Access
---
This signature is a warning flag in the inverter status data that sets when someone tries to get onto the inverter network without authorization. The Modbus map labels this bit an Unauthorized Network Access Fault. When the bit is set, the manuals tell you to check whether anyone has made malicious attempts to access the inverter network. On SMA devices, a similar event is logged when a login for the NSD function on a device fails.

<!-- review notes
- sentence 1: support check: partial - Passages describe an unauthorized network access attempt, but nothing says it is a warning flag in status data (the code is only listed as 30).
- sentence 4: support check: partial - The passage shows an event 'Login for NSD function on device failed' but does not mention SMA or state it is similar or logged as an event.
- sentence 1: review: partial - The rows describe code 30 as an unauthorized attempt to access the network, but they do not say it is a warning flag or bit in the inverter status data.
-->
