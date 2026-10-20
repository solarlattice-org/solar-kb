---
id: meas:firmware-integrity-check-abort
type: Measurement
name: Firmware integrity check abort
---
This signature is an error message in the device web interface saying that the codepack integrity check stopped a firmware update. It appears during a multiple-image firmware update when any one of the images in the package is corrupt. A related message reports that the codepack integrity check failed because an image in the codepack file is corrupt. For both messages, the listed action is to re-install the firmware. A third message says the final integrity check is invalid. Its listed cause is only multiple reasons, and no action is given. On some inverters, the way to confirm a firmware update finished correctly is to open the user interface afterwards and check the event log.

<!-- review notes
- sentence 6: support check: partial - Passages say to open the user interface and check the events to see whether the update completed; 'event log' and 'some inverters' are minor paraphrases/unstated scope, core is supported.
-->
