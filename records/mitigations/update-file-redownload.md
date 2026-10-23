---
id: mit:update-file-redownload
type: Mitigation
name: Update file re-download
---
Downloading the update file again is the remedy when a Fronius inverter reports status code 745, a defective update file. With this code the display shows a warning and the update is cancelled. The same action applies to status code 735, where the update file does not match the device or is too old. Check the file, and if needed download the correct update file for that device, for example from the Fronius website. On the Symo, the manual also says to check or replace the USB flash drive when the update file is reported as defective. For a USB update, the firmware file is named froxxxxx.upd, where xxxxx stands for the version number. This helps confirm you have the right file. If the status code is still shown after a fresh download, contact a Fronius-trained service technician.

<!-- review notes
- sentence 2: support check: partial - 735 is described as stated, but its remedy is to check the file and download the correct one, not to download it again as 'the same action' for 745 implies; the wording is roughly consistent but slightly conflated.
-->
