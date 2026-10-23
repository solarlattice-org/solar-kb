---
id: symptom:unsupported-storage-drive
type: Symptom
name: Unsupported removable storage drive
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Fronius Galvo, Primo and Symo show status code 731, an initialization error, as a warning message
    on the inverter display when the inserted USB drive is not supported.
  quote: Initialization error – USB thumb drive is not supported
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r3
    h: 8b211e171c09
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r3
    h: 8b211e171c09
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r6
    h: 57eda22c1714
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
On Fronius Galvo, Primo and Symo inverters, status code 731 means an initialization error: the inverter does not support the USB drive plugged into it. It shows up as a warning message on the inverter display. Check the USB drive first, including its file system, and replace the drive if needed. It is also separate from code 732, which reports overcurrent at the USB drive. Codes 736 and 738 cover read or write errors and log files that could not be saved, for example because the drive is full or write-protected. On Galvo and Primo units, contact a Fronius-trained service technician if the code stays after the drive has been checked or replaced.

<!-- review notes
- sentence 6: support check: partial - The passages say to contact a Fronius-trained technician if the code persists, but they don't name Galvo and Primo specifically (the u3 row lacks this step).
-->
