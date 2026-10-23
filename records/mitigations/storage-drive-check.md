---
id: mit:storage-drive-check
type: Mitigation
name: Removable drive check
aliases:
- Check the USB thumb drive
- check USB flash drive
---
On Fronius Galvo, Primo and Symo inverters, checking the removable USB drive is the first step for storage warnings shown on the display. These are 731 (drive not supported), 733 (no drive inserted), 736 (read or write error), 738 (log file not saved), 743 (error during an update) and 745 (defective update file). Make sure a drive is inserted and seated. Check its file system and the files on it, and replace the drive if it is not supported or keeps failing. If the log file cannot be saved, the drive may be full or write-protected: free up space and remove the write protection, then check or replace the drive if needed. If an update fails, run the update again and check the drive. If the update file is defective, download it again before checking or replacing the drive. Wait until OK shows or the Data Transfer LED has stopped flashing and is off before you pull the drive. Removing it earlier can lose data. If the status code stays after these checks, call a Fronius-trained service technician.

<!-- review notes
- sentence 1: support check: partial - The codes, descriptions and USB-drive checks are in the rows, but nothing says checking the drive is the 'first' step. Also, 738's first remedy is freeing memory, and 'Galvo, Primo and Symo' is not stated.
- sentence 2: support check: partial - Inserting or checking the drive, checking the file system and files, and replacing the drive are supported. 'Seated' and 'keeps failing' are not stated.
- sentence 4: support check: partial - The 743 remedy (repeat the update, check the drive) is supported. For 745 the remedy lists downloading the file again and checking or replacing the drive, but the passages don't say the download must come before the check.
- sentence 5: support check: partial - The OK and LED conditions for removal are supported by u8 and the 736 rows. 'Removing it earlier can lose data' is only implied by 'without losing data'.
-->
