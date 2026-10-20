---
id: meas:remote-shutdown-status-point
type: Measurement
name: Remote shutdown status point
signals:
- point: model_103.W
  unit: unit:W
  pattern: AC power falls to zero while the shutdown command is active
---
The Remote Shutdown status point shows that the system is getting a remote shutdown command through the customer's external I/O. The command comes from a pair of terminals in the customer I/O area of the Customer Interface Bay. When remote shutdown is active, the inverter stops operating and the AC bus is isolated from the battery DC source. The unit's AC circuit breaker also opens. Customers may wire these terminals to an E-Stop button that puts the system into standby. The terminals may also be used when the unit is being put into storage. Remote shutdown is a software function and may not meet emergency stop rules everywhere. Check local codes and the AHJ before using it as an E-Stop.
