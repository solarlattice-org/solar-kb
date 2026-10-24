---
id: proto:csip
type: Protocol
name: Common Smart Inverter Profile
aliases:
- CSIP
- SunSpec Common Smart Inverter Profile
category: Communication
protocol_kind: application
---
CSIP, the SunSpec Common Smart Inverter Profile, appears in equipment datasheets as a grid interoperability certification. The Generac PWRcell 2 inverter lists CSIP among its grid certifications, alongside UL 1741 SB, IEEE 1547 and Rule 21. In an Enphase system, the IQ Gateway software runs an IEEE 2030.5 client that exchanges messages with a utility CSIP server. The CSIP server can send a Power Export Limit (PEL) command, and the gateway applies the default PEL to the grid profile. An Enphase gateway release fixed problems where the 2030.5 client stopped responding when the CSIP server did not answer its first message. The same release added timeout and retry handling. The same release also fixed a problem where CSIP PEL commands did not reduce IQ8 output in sites that mix IQ7 and IQ8 microinverters.

<!-- review notes
- sentence 2: support check: partial - Grid certifications list includes CSIP, UL 1741 SB, IEEE 1547 and Rule 21, but the passage doesn't name the product as Generac PWRcell 2.
- sentence 4: support check: partial - Passages mention CSIP PEL commands and default PEL from the server applied to grid profile, but only as a fix for a failure to apply; the described behavior is implied rather than stated as working.
-->
