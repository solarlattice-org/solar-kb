---
id: mit:memory-card-replacement
type: Mitigation
name: Memory card replacement
---
Memory card replacement means taking out the micro SD card in an SMA inverter and fitting a new one. One SMA document calls for it when event 7101 reports that the micro SD card in the inverter is faulty. Event 7106 means the update file on the memory card is defective, so the firmware update from the card has failed. For event 7106 the listed fixes are to reformat the card, save the files to it again and repeat the firmware update. Replacing the card is not one of the listed steps. Other manuals describe event 7101 as an unformatted SD card. There the fix is also to reformat the card and save the files again, not to replace it. On a Sunny WebBox, the card stops saving data once it is full and the MEMORY LED lights red. At that point, replace the card or format it on a computer. Use SD cards supplied by SMA, because other cards may not be compatible. The Sunny WebBox does not support SDHC cards or cards larger than 2 GB, and the card must be formatted with FAT16. Do not remove the card while the MEMORY LED is flashing orange. Doing so can damage the card's file system and lose data.
