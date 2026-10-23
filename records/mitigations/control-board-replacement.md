---
id: mit:control-board-replacement
type: Mitigation
name: Control board replacement
aliases:
- SIBUCTRL board
---
Replacing the control board is a corrective step for the CPLD fault, reported as Fault0060, on CPS three-phase string inverters. Restart the inverter before any replacement: turn both the AC and DC switches off, wait one minute so stored energy can discharge, then turn both switches back on. If the restart does not clear the fault, the manuals call for replacing either the control board or the whole inverter. For SMA SIBUCTRL control boards, first resolve any open inverter events using the service knowledge base. Then order the board through the SMA Online Service Center, giving the article number and the remedial actions already taken. Some units have no separate replacement board: SMA states that the entire AS-Box-S has to be replaced. SMA board-swap training also says to disconnect the inverter from all power, secure it so it cannot be switched back on, and confirm there is no voltage with a suitable meter before starting work.

<!-- review notes
- sentence 6: support check: partial - The transcript says to disconnect from power, secure against re-switching on, and check absence of voltage with a suitable device, but it is for a KP Assembly Board replacement, not general SMA board-swap training.
- sentence 1: review: partial - Every row lists replacing the Control Board (or the inverter) as the fix for Fault0060 CPLD Fault on CPS inverters, but the 'three-phase string' scope is not stated.
-->
