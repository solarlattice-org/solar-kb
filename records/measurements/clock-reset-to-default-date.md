---
id: meas:clock-reset-to-default-date
type: Measurement
name: Clock reset to default date
aliases:
- Invalid date
- DateInvalid
- Bad clock ERR
---
The device reports a system time or date that is invalid or wrong, and some inverters raise an explicit invalid-date event asking for the date and time to be set again. A wrong system time directly corrupts data logging and the recorded energy yield values, so event timestamps and logged data can no longer be trusted. On some inverters an internal real-time clock fault puts the clock module in emergency mode; time then becomes inaccurate or is lost, while feeding power to the grid carries on as normal. In one surge protection device, inaccurate timestamps come from a clock that was never synced or from a backup supercapacitor that drained during an extended power loss. On a data logger, a bad clock error usually means a network problem stopped the unit from getting the date and time from the internet. A factory reset returns a device to its default settings and can delete stored system data, so check the clock again after any reset. Fix it by setting the date and time again on the device, then enable network time sync (SNTP) or check the network connection so the clock stays correct.

<!-- review notes
- sentence 2: support check: partial - u9 says wrong system time directly affects data logging and power generation value; u21 says timestamps inaccurate; but 'event timestamps can no longer be trusted' is a mild extrapolation and 'corrupts' is stronger.
- sentence 6: support check: partial - Passages say reset returns to default settings and deletes stored system data, but nothing says to check the clock after a reset.
-->
