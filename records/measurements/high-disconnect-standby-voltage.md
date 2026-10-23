---
id: meas:high-disconnect-standby-voltage
type: Measurement
name: High disconnect switch standby voltage
aliases:
- Standby voltage
---
This signature means the standby voltages of all PV array disconnect switches in one string add up to more than 30 V. The SMA inverter reports it under event 9034, Error in Rapid Shutdown System. The same event also covers a misconfigured Rapid Shutdown function and a PV array that could not be disconnected properly. When this fault is present, voltage may still be applied to the inverter DC inputs after a rapid shutdown, so the rapid shutdown has failed. For the DC conductors to discharge reliably, the summed standby voltage of the string's disconnect switches must be above 3.6 V and below 30 V. To fix it, measure the standby voltage of the disconnect switches in use and bring the string total below 30 V. Also check that the switches work and that the Rapid Shutdown operating mode matches the DC disconnection unit. When rapid shutdown works, the inverter reports event 9035, meaning the DC inputs and AC output were discharged.

<!-- review notes
- sentence 3: support check: partial - The passages say voltage can be applied to the DC inputs when the array could not be disconnected, but this is one listed cause, and they don't say that the rapid shutdown has failed or that it occurs after a rapid shutdown.
- sentence 6: support check: partial - Event 9035 is 'Rapid Shutdown successful' with DC inputs and AC output discharged, but the passages don't state that the inverter reports it each time rapid shutdown works.
-->
