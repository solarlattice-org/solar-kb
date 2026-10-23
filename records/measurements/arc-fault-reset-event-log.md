---
id: meas:arc-fault-reset-event-log
type: Measurement
name: Arc fault reset event entry
aliases:
- AFDD user reset
---
On FIMER PVS inverters, a manual reset of an arc fault error made through the internal webserver shows up as warning W026, AFDD user reset, with no LED. This entry does not mean a new fault. It only records in the inverter event history that the customer or installer cleared the arc fault error. On SMA inverters, events 8206 or 8210 mean the inverter is still waiting to be reset after an arc fault, and the original arc detection appears earlier in the log as event 4301 or 4302. Events 8206 and 8210 are reminders that the arc fault was not reset within 10 minutes. They are not new faults. The reset is done by setting the operating data parameter to reset operation inhibition, or by switching AFCI back on. You can do this from the inverter user interface, a connected Data Manager or Sunny Portal. Some models reset themselves after an arc trip up to five times a day. After that, they stop permanently and need a manual restart. The failure mode behind this entry is an arc fault in the PV strings. Before resetting, check the wiring and array for loose connections, damaged or mismatched DC connectors, and scorched modules, and scan for hotspots with a thermal camera.

<!-- review notes
- sentence 5: support check: partial - The parameter settings and the browser UI, Data Manager and Sunny Portal routes are stated. But the Sunny Portal route is for inverters registered with a Data Manager, and the AFCI toggle is only listed for the user interface method.
- sentence 6: support check: partial - For newer models the passage says up to five auto-resets per sunlight day, then permanent stop until manually cleared. But it does not say this applies to only some models, and other models behave differently.
-->
