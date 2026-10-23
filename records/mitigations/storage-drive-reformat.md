---
id: mit:storage-drive-reformat
type: Mitigation
name: Storage drive reformatting
---
Storage drive reformatting means formatting the USB flash drive used by the inverter again so that it has a file system the inverter can read. It applies to Fronius Symo status code 740, which reports an initialization error caused by a fault in the file system of the USB flash drive. While this code is active, the inverter shows a warning message on its display. First check the USB flash drive. Then reformat it on a PC to FAT12, FAT16 or FAT32. If the drive is not supported at all (status code 731), check the file system and, if needed, replace the drive. Reformatting does not fix every drive fault. Other drive errors call for removing and reinserting the drive, freeing up memory, removing write protection or replacing the drive.

<!-- review notes
- sentence 1: support check: partial - Passage says reformat the USB drive on a PC to FAT12/16/32, but doesn't define the term or say 'a file system the inverter can read' explicitly (implied).
- sentence 2: support check: partial - Code 740 and its description are stated, but the passage doesn't name the Fronius Symo model.
-->
