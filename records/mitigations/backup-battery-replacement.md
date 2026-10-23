---
id: mit:backup-battery-replacement
type: Mitigation
name: Backup battery replacement
aliases:
- buffer battery
- back-up battery
---
This action replaces the small coin cell on the inverter communication board that keeps the clock running. It is of the CR2032 type. It applies when the inverter reports a low backup battery voltage (warning W012, Batt. Low, with a flashing yellow LED), shows an error, or has lost its date and time settings. First set the date and time. Then switch the inverter fully off on both the AC and DC sides, wait a few minutes and restart it. Replace the battery only if the clock has gone back to 01/01/2000. Before you start, fully de-energize the inverter and disconnect the strings. On some versions, DC input voltage is still present on the communication board when only the combined AC+DC switch is open. To reach the battery, open the wiring box cover or remove the plastic cover over the DC high-voltage sections. On some models you must also extract the communication and control board, and the power module cover must stay closed. Wear insulating gloves when handling the new battery so it does not discharge, and match the polarity printed on the board. Afterwards, refit the covers, reconnect the input strings and restart the inverter.

<!-- review notes
- sentence 5: support check: partial - The passages support the wiring box cover, the plastic cover, extracting the board, and keeping the power module cover closed. They don't say the plastic-cover and wiring-box-cover routes are alternatives, and 'on some models' for the extraction is only implied.
- sentence 7: support check: partial - The passages support reconnecting the strings and restarting the inverter, and replacing the plastic cover in one version. Refitting all the covers is not stated for the other versions.
-->
