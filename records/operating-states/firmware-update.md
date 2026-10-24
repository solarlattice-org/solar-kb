---
id: state:firmware-update
type: OperatingState
name: Firmware update in progress
aliases:
- update mode
- updating firmware
- Update in process
- Update progress
category: Inverters
---
On SMA Sunny Boy US inverter displays, the message Update progress means a firmware update is underway, and Update status shows information about the firmware update. In SMA status lists, the status Update in process means the update is still running. An installer usually starts the update from the inverter user interface: open Device Configuration, pick Update firmware for the product, browse to the update file and follow the dialog. You can also have the device check for an update and install it, in which case the firmware updates in the background. If the user interface shows Connection to device lost during the update, log on again. Afterwards, clear the browser cache and log out and back in. When the update has finished, open the user interface and check the events to confirm it completed successfully. When the SMA Inverter Manager updates inverters through the LCS-Tool, an inverter's update is finished once Progress reads 100 %. Any inverter that does not reach 100 % should be updated again on its own, one at a time.

<!-- review notes
- sentence 5: support check: partial - The message and re-logon are stated, but the cache clearing and re-login come after the events check, not specifically as a response to the message, and the passage does not condition them on it.
- sentence 7: support check: partial - Progress 100 % means finished and failed inverters are updated one after another, but 'on its own'/'one at a time' is fine; however the passage says 'nacheinander' for affected inverters, which matches, so only minor wording differences remain.
-->
