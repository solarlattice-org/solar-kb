---
id: proto:eebus
type: Protocol
name: EEBus
category: Communication
protocol_kind: application
---
EEBus is a communication standard that lets devices exchange data automatically so that energy is used efficiently. The SMA Data Manager M can add EEBUS devices to a system, but only one EEBUS device can be connected to it, and at present the only supported device is the Audi e-tron charging system connect. Before you configure it, the EEBUS device must be running and on the local network, and the licensed function must be bought and activated on the Data Manager. In the Data Manager user interface, open Configuration, then Device administration, add a device of type EEBUS devices and fill in the input fields. Write down the SKI device ID, then start the search. Give the device that was found a name. Then finish the coupling on the EEBUS device itself, using the SKI identifier and the device maker's manual. Once that is done, the device shows on the dashboard. SMA lists the use case Limitation of Power Production (LPP), firmware version 1.0.0, as running over EEBUS. SMA also lists Bosch Series 8 and Bosch Home Professional models, plus Siemens iQ500, iQ700, iQ800 and avantgarde models, sold in Germany, Austria or Europe, that use EEBus as their communication standard. For the protocol details, SMA points to the EEBus organisation. SMA also offers SEMP as another protocol interface.

<!-- review notes
- sentence 2: support check: partial - Passage supports the one-device limit and Audi e-tron only, but never names the product 'SMA Data Manager M' (only 'the product' / Data Manager).
- sentence 3: support check: partial - Requirements say the device must be in operation, on the local network, and the license purchased and activated; 'on the Data Manager' is implied, and the passage doesn't say 'before you configure' explicitly beyond 'Requirement'.
-->
