---
id: mit:enter-access-code
type: Mitigation
name: Correct access code entry
aliases:
- SMA Grid Guard code
- password
---
This action means entering the correct password or access code to unlock protected functions on a meter, relay or inverter. On SMA STP inverters, event 9002 means the SMA Grid Guard code entered was wrong, so the operating parameters stay protected and cannot be changed. To clear this event, enter the correct SMA Grid Guard code. On SEL meters and relays, you need the correct password to enter every access level except Level 0, which is the entry level. Each higher level unlocks more. Level 1 lets you view settings and meter data, Level E adds demand resets, and Level 2 lets you change configuration settings and reset all data. Use Level C only when an SEL engineer tells you to. Type 2AC to drop back to Level 2. The meter instruction manual lists the factory-default password for each access level.

<!-- review notes
- sentence 7: support check: partial - Table 3.3 lists factory-default passwords per level, but the passages don't identify the source as the meter instruction manual (and Level 0 has N/A).
-->
