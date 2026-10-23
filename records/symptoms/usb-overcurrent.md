---
id: symptom:usb-overcurrent
type: Symptom
name: USB port overcurrent
aliases:
- Overcurrent at USB thumb drive
- overcurrent at USB flash drive
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Fronius Galvo, Primo and Symo list status code 732 for overcurrent at the USB drive; the Symo
    manual calls it an initialization error.
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r4
    h: 00d0a42ac554
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r4
    h: 00d0a42ac554
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r7
    h: b0a1a955fa5c
  review: drafted
---
On Fronius Galvo, Primo and Symo inverters, status code 732 means too much current is being drawn at the USB drive plugged into the inverter. The Symo manual lists this code as an initialization error, so it shows up when the inverter sets up the USB flash drive. Do not confuse it with the nearby USB codes: 731 means the drive is not supported, and 733 means no drive is inserted. The status code tables give no specific fix for code 732. For the related USB codes, the manuals say to check or replace the drive, check its file system, and call a Fronius-trained service technician if the code persists.

<!-- review notes
- sentence 1: support check: partial - Passages say overcurrent at the USB drive for code 732, but 'plugged into the inverter' and 'too much current drawn' are mild paraphrase; the Galvo/Primo/Symo model attribution isn't explicit in the passages.
- sentence 2: support check: partial - The Symo manual labels it an initialization error, but the passage doesn't say it appears specifically when the inverter sets up the drive; that is an inference.
-->
