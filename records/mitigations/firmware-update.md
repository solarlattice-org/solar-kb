---
id: mit:firmware-update
type: Mitigation
name: Firmware update
---
A firmware update installs new device software on an inverter or other plant equipment. Revisions fix software defects; one meter release, for example, fixed settings that reverted to defaults and event report data that became corrupted. On the SMA inverter, the automatic update can be switched on either in the inverter or in the communication product, and the manual recommends the automatic option. If the communication product handles updates, the inverter's own automatic update is off by default. This avoids downloading the same update more than once. A manual update can use an update file loaded through the user interface or from a USB flash drive. You can also have the inverter search for firmware and install it from the user interface. To update through the interface, log in as Installer and open the parameter settings, then Device Configuration. Choose Update firmware from the gear icon, browse to the file and follow the dialog. Afterwards, check the event log to confirm the update finished. A condition-test-failed event means the update package does not suit this inverter. Only a qualified person should carry out the update. Commissioning checklists may record the firmware update as a pass or fail step.

<!-- review notes
- sentence 7: support check: partial - u11 shows a Pass/Fail firmware update step in a checklist, but the 'QUALIFIED PERSON' heading in u7 only loosely supports 'only a qualified person should carry out the update'; it's a label, not an explicit restriction.
-->
