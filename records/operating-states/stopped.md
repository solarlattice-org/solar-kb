---
id: state:stopped
type: OperatingState
name: Stopped
aliases:
- shutdown
- manual stop
- stop
- 'off'
- Stop status
category: Inverters
---
Stopped means the inverter is not running. Some manuals call this state Stop or shutdown, and the Sunny Island calls it Shutdown. On SMA devices an operator usually starts a stop from the user interface by setting the general operating state parameter to Stop. Setting the operating mode to Stop withdraws permission to operate, so the device does not feed in even when DC voltage is present. A manual stop is logged as a change from operation to standby. A stop sent through the system control is logged separately as an external stop. Some parameters can only be changed while the device is stopped. If you try to change them during operation, the device reports that the setting failed and must be stopped first. On Solis inverters the OPERATION light is off when the inverter has stopped operating. A commanded stop is different from a stop caused by an error. On SMA inverters a steady red LED together with an event message means operation stopped because of an error, and the error needs to be fixed. In a Sunny Island cluster, the whole cluster stops if a slave unit has a fault status. In that case, look for the fault on the slave.

<!-- review notes
- sentence 2: support check: partial - Passage shows setting general operating state to Stop in the UI, but not that this is 'usually' how an operator starts a stop on SMA devices generally (it's only one procedure).
- sentence 3: support check: partial - Passage says OpMod=Stop withdraws permission to operate with DC present (OFF>LOCKED), but doesn't explicitly state the device doesn't feed in.
- sentence 5: support check: partial - Message exists saying setting failed and device must be stopped first, but passages don't state that some parameters can only be changed when stopped or that this occurs during operation.
- sentence 7: support check: partial - Red LED plus event message means operation stopped by error, but the passages don't contrast with commanded stop or say the error needs to be fixed.
- sentence 8: support check: partial - Passages say cluster is stopped when a slave has a fault, but don't instruct to look for the fault on the slave (though implied).
- sentence 7: review: partial - The rows support that a glowing red LED with an event message means operation stopped because of an error, but they do not say steady, do not contrast this with a commanded stop, and do not say the error needs…
-->
