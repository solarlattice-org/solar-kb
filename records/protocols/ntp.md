---
id: proto:ntp
type: Protocol
name: NTP
aliases:
- Network Time Protocol
- SNTP
- Simple Network Time Protocol
category: Communication
protocol_kind: application
---
NTP is a network protocol a device uses to set its internal clock from the time of day that an NTP server provides. SNTP is a simplified version of it. SMA inverters log event 10114 when they cannot get time from the configured NTP server. Check that the server is set correctly and that the inverter is on a local network with Internet access.

<!-- review notes
- sentence 2: support check: partial - Passage gives event 10114 and the corrective measures, but doesn't say 'SMA inverters log' it explicitly (implied by the row), and 'Internet access' matches; minor framing of logging is implied rather than stated.
-->
