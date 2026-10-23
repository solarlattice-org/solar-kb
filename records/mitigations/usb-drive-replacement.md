---
id: mit:usb-drive-replacement
type: Mitigation
name: Removable storage drive replacement
aliases:
- replace the USB thumb drive
- replace the USB flash drive
---
This action means swapping the inverter's USB storage stick for a working one when the inverter cannot use the current drive for data logging or file access. On Fronius Primo, Galvo and Symo inverters it is the listed remedy when a read or write error occurs on the USB drive. The inverter shows this as a warning on the display. It also applies when the inverter reports that the inserted USB drive is not supported during initialization. Check the drive's file system before replacing it. If the log file cannot be saved because the drive is full or write-protected, first free up space or remove the write protection. Replace the drive only if needed. Before swapping, check the drive and the files on it. Remove the old stick only when the Data Transfer LED has stopped flashing and is no longer lit, so no data is lost. Replacing the drive does not always clear the warning. If the status code persists, a Fronius-trained service technician should be contacted.

<!-- review notes
- sentence 2: support check: partial - Passages give the replace remedy and display warning for code 736, but the Primo, Galvo and Symo model naming isn't stated in them.
-->
