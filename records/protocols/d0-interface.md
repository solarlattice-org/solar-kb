---
id: proto:d0-interface
type: Protocol
name: D0 optical meter interface
aliases:
- D0
- IEC 62056-21 optical interface
- D0 interface
category: Communication
protocol_kind: transport
---
D0 is an energy meter interface. An SMA configuration table offers it as one way to connect a meter, next to the S0 pulse interface. For a standard energy meter with a D0 interface, the technician selects D0 in the connected meter type drop-down list. For a bidirectional meter with a D0 interface that measures both supply and feed-in, the technician selects D0 and also activates the Bidirectional meter field. When the bidirectional option is active, the second meter input area is no longer available. The D0 setup needs no pulse rate. The S0 option instead asks for the meter's pulses per kWh, taken from the meter manual.

<!-- review notes
- sentence 5: support check: partial - S0 requires pulses/kWh from the meter manual, but the passages never state explicitly that D0 needs no pulse rate (only implied by its steps omitting it).
-->
