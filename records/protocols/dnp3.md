---
id: proto:dnp3
type: Protocol
name: DNP3
aliases:
- IEEE 1815
- Distributed Network Protocol
- IEEE Std 1815
- IEEE1815
- DNP
- DNP V3.00
category: Communication
protocol_kind: application
---
DNP3, published as IEEE Std 1815, is a protocol for connecting to DER devices. Utility SCADA systems often use it, and application notes exist for monitoring and controlling DER with it. DNP3 uses a simplified three-layer model with application, data link and physical layers. A Transport Function inside the application layer splits large messages into pieces the data link layer can carry. The DNP Users Group maintains the specification in eight volumes. Volume 8, the Interoperability Specification, defines four standard implementation levels. The optional SMA Hybrid Controller supports IEEE1815 (DNP3). On Tesla battery systems, the Watt-Var curve can be changed in real time through Modbus or DNP3 points.

<!-- review notes
- sentence 3: support check: partial - Eight volumes, DNP Users Group maintenance, and Volume 8 Interoperability with four levels are stated, but the passage doesn't mention the 'maintains the specification in eight volumes' beyond that—mostly fine; however the Users Group maintains standards and the volumes are listed, so only minor gaps (Volume 8 title list incomplete).
-->
