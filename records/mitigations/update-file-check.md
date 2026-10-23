---
id: mit:update-file-check
type: Mitigation
name: Update file verification
---
Update file verification means checking the firmware update file when the inverter warns that the file is missing, cannot be detected, or does not match the device. For Fronius code 734, check that the update file is present and carries the proper file name. For Fronius code 735, the file is too old or does not fit the device and the update is cancelled; check the file and, if needed, download the correct file for the device from the manufacturer website. When updating SMA products through the user interface, the interface should confirm that the selected file is compatible; if it does not, replace the file before starting the update. SMA inverters log an event when a valid update file is found and another when no update file is found, which helps confirm the result of the check. If the Fronius status code persists after the file has been checked, contact a Fronius-trained service technician. Checking the file does not fix a defective update file: in that case, download the file again or repeat the firmware update.
