---
id: mit:update-file-recopy
type: Mitigation
name: Update file recopy
---
Recopying the update file means placing the firmware update file on the inverter's memory card again, in the \UPDATE folder. It is the corrective step for event 7110, raised when the inverter finds no new update file on the SD memory card; the update fails, but the inverter keeps feeding power into the grid. It also applies to event 7106, a defective update file; one manual says to reformat the memory card first and then save the files to it again. Other manuals give a shorter instruction for event 7106: run the firmware update again. A defective update file does not stop production: the inverter keeps feeding in while the update is outstanding. If the copy works, event 7112 appears to show that the update file was copied to the inverter's internal memory. For updates done through the user interface, the interface should confirm that the update file is compatible; if it does not, use a different update file.

<!-- review notes
- sentence 3: support check: partial - 7106 evidence says reformat the card and re-save files, but nothing links it to 'recopying the update file' in \UPDATE or says it 'also applies' beyond re-saving files.
- sentence 6: support check: partial - 7112 states the file was copied successfully to internal memory, but the passages don't say it follows a successful copy from the card or 'appears' as a result of the copy step.
-->
