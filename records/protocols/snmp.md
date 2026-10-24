---
id: proto:snmp
type: Protocol
name: SNMP
aliases:
- Simple Network Management Protocol
category: Communication
protocol_kind: application
---
SNMP is an application-level network management protocol. An SNMP agent in a device exchanges data with an SNMP manager, also called a management station. The Accuenergy AXM-WEB2 and AXM-WEB-PUSH meter modules use SNMP to report metering data to a management station. By default they communicate on port 161 and use the public community string for read-only access. On the AXM-WEB2, open Settings, then Communications, then the SNMP tab. There you enable SNMP, pick SNMPv2c or SNMPv3, set the port (161 or a value from 16100 to 16199) and change the read-only community string, which works like a password. Save, then reboot the module for the changes to take effect. The meter modules can also send traps, which are unsolicited messages triggered by events such as a change in digital input status. Traps go to up to four stations, each set by IP address and port. A buffer holds up to 30 notifications, and a hold time of 0 to 30 seconds sets how long each one waits before it is sent.

<!-- review notes
- sentence 1: support check: partial - Passages mention an SNMP agent and manager and management stations, but none define SNMP as an application-level protocol or say the agent exchanges data with the manager (also called a management station).
- sentence 3: support check: partial - Navigation, enable, version, port, community string and the save and reboot step are stated for the AXM-WEB2. However, the passages don't say the community string can be changed (only that it defaults to Public), and the reboot can be immediate or later.
-->
