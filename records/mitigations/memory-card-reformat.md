---
id: mit:memory-card-reformat
type: Mitigation
name: Memory card reformatting
aliases:
- Re-format the SD card
- Reformat the memory card
---
Reformatting the memory card is a corrective step for SMA inverter events raised during a firmware update from an SD or micro SD card. It applies when event 7106 reports that the update file on the memory card is defective and the update failed. It also applies when event 7101 reports that the SD memory card is defective or not formatted. To do it, reformat the card and then save the update files onto it again. After event 7106, run the firmware update again once the card has been reformatted and reloaded. Reformatting does not always fix the problem: if the card is still faulty, replace it. Some manuals tell you to replace the micro SD card straight away for event 7101.
