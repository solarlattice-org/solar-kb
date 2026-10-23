---
id: meas:sd-card-status-message
type: Measurement
name: SD card status message
aliases:
- CardStt
- SD memory card status
---
On Sunny Island battery inverters, the SD card status is read from the parameter CardStt, numbered 312.07 or 312.11 depending on the model. On some models the Sunny Remote Control works out the card status and shows it on its display. Normal values include Operational (busy), Mount (initialization) and Parameter (writing a parameter set). The display can also show the card being accessed or log data being written. Off means no SD card is inserted. Incomp means the card has an incompatible file system. ParamFailed means a parameter set could not be written. The display also reports cards that are full, have an invalid file format or are incompatible, and failed parameter loads. On SMA string inverters, event 7101 reports a defective SD card, which means the card is not formatted. The fix is to reformat the card and save the files to it again. Event 27108 is only a status message that the inverter is reading the card. Event 27109 means the update file on the card has already been used.

<!-- review notes
- sentence 2: support check: partial - The passages say the Sunny Remote Control determines the SD card status, but don't say it applies only to some models or that it shows the status on its display.
- sentence 7: support check: partial - The passages say 27108 is the inverter reading the card and 27109 is an update file already used, but nothing states that 27108 is 'only' a status message.
- sentence 1: review: partial - The passages show CardStt as 312.07 and 312.11 (07) for the SD card status, but no quoted text names Sunny Island battery inverters, and the link from number to model is only implied by the source ids.
-->
