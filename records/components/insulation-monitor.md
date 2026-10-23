---
id: comp:insulation-monitor
type: Component
name: Insulation monitoring device
aliases:
- Insulation monitoring
- Insulation Monitor/Interruption
- insulation resistance monitoring function
---
The insulation monitoring device checks the resistance between the positive or negative pole of an ungrounded PV array and ground potential. If a DC cable or a faulty module creates a short to ground, the inverter disconnects from the grid. Fronius inverters include insulation monitoring as a safety function required by UL 1741 and the National Electrical Code. Low insulation resistance can defeat protection against electric shock and lead to ground fault currents, electrical fire or device damage. Some medium-voltage inverters therefore monitor it continuously and raise an alarm. These units have automatic and manual modes and leave negative-pole grounding mode while they take the measurement. SMA string inverters set a minimum insulation resistance that depends on the inverter model. The monitor itself can fail. Fronius code 459 reports an error in the measuring signal for the insulation test. SMA central inverter codes 6448 and 6461 report invalid values or a threshold that was not accepted, and call for a check of the device and its cabling. On SMA central inverters, after an insulation error you must switch the monitoring device back on. Then either restart the inverter with the key switch or acknowledge the error in the user interface. Loss of insulation in modules and cables is found by insulation testing, with data monitoring as a supporting method.

<!-- review notes
- sentence 3: support check: partial - Passages say the inverter has insulation monitoring as a safety function required by UL 1741 and NEC, but don't name Fronius.
- sentence 6: support check: partial - Fronius 459 and SMA codes are supported, but 'invalid values or threshold not accepted' fits; 'call for check of device and cabling' is only stated for 6461 (6448 says check insulation monitoring), and brands aren't named in passages.
- sentence 8: support check: partial - Module insulation failure is detected by INS with MON secondary, but cables/interconnectors primary is visual inspection (VI), with INS and MON as secondary.
-->
