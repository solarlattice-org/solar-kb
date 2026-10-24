---
id: mit:communication-bus-termination
type: Mitigation
name: Communication bus termination and cabling practice
aliases:
- RS485 dial switch SW1
- terminating resistor
- shielded twisted pair
- single-point shield grounding
- RS485 bus termination and cabling practice
- termination resistor
- terminator
- RS485 termination DIP-switch
- Single point ground
---
This action terminates an RS485 communication bus with a termination resistor, typically 120 ohm, at the ends of the line. The resistor is usually switched in with a DIP switch or selector switch on the inverter's communication board. It addresses a communication bus wiring or termination fault. When a device reports a communication fault, check that terminators are fitted at both ends of the bus and that undamaged CAT5e cables are plugged in correctly. In a daisy chain, set the termination switch to ON only on the last device and leave it OFF on every other inverter. OFF is the factory default. Use shielded twisted pair cable and wire it with the correct polarity. Run the shield or drain wire continuously and ground it at one point only. Keep the shield away from the RS485 common and the enclosure ground, and never ground the common. Twisting the data pair reduces interference picked up from outside sources. Route copper communication cables apart from power conductors, or cross them at right angles. Fiber is preferred where a cable has to run alongside power wiring. Termination has limits. It adds load to the line, which weakens the signal, and it changes the bus biasing requirements. Whether to terminate is decided site by site. It is usually not needed at low baud rates such as 9600 or 19200 bps. Some products also limit the total communication bus length to 30 m. Some RS485 sensors normally do not need a terminating resistor.

<!-- review notes
- sentence 5: support check: partial - Twisting and routing apart/at right angles and fiber preference are stated, but the source is SEL Ethernet guidance, not general communication cables, and fiber is recommended for parallel runs or enclosure penetration.
-->
