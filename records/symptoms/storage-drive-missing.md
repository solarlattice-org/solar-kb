---
id: symptom:storage-drive-missing
type: Symptom
name: Removable drive not detected
aliases:
- No USB thumb drive inserted
- No USB flash drive inserted
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Fronius Galvo, Primo and Symo inverters show status code 733 as a warning on the display when
    no USB drive is inserted.
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r5
    h: a6c08679a53f
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r5
    h: a6c08679a53f
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r8
    h: 944ffa749bec
  review: drafted
---
On Fronius Galvo, Primo and Symo inverters, status code 733 means the inverter finds no USB drive in its slot. The inverter shows it only as a warning message on the display. SMA devices report a similar message when no USB data carrier is detected, either because none is plugged in or because the one plugged in is not compatible. Check first that a USB drive is inserted and seated properly. If the code stays, contact a Fronius-trained service technician. Other USB codes point to different problems: 731 means the drive is not supported, so check its file system or replace it, and 732 means overcurrent at the drive. Code 736 is a read or write error, and code 738 means the log file could not be saved, for example because the drive is write-protected or full. Remove the drive only after the Data Transfer LED has stopped flashing and is off.

<!-- review notes
- sentence 4: support check: partial - Insert or check the drive and contact service if it persists are stated, but 'seated properly' is not explicitly stated (only 'insert or check').
-->
