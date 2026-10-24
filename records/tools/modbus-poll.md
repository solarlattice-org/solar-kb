---
id: tool:modbus-poll
type: Tool
name: Modbus client tool
aliases:
- Modbus Poll
- Modbus scanner
- ModScan
- Modbus program
- Modbus client
category: Software
tool_kind: software
claims:
- claim_id: c1
  rel: uses_protocol
  target: proto:modbus
  note: Used to test a device's Modbus interface by reading simple registers, such as the serial number.
  cite:
  - src: src:sma-doc-278742
    loc: sec=h973
    h: b0a7b18bedc1
  - src: src:sma-doc-240154
    loc: sec=12.1
    h: a0eca17eeb5c
  review: drafted
  review_note: 'support check: partial - Passages state testing the Modbus interface by querying simple
    registers with a Modbus program, but don''t name a ''Modbus client tool'' or explicitly tie it to
    the protocol concept beyond that.'
---
A Modbus client program lets a qualified person check a device's Modbus interface by reading simple registers, such as the serial number. Save the client settings and the registers you queried, for example as screenshots, because SMA Service asks for this information when it helps with a problem. Before a Modbus client can talk to an SMA Cluster Controller, the Modbus server must be turned on in the Cluster Controller's user interface. In supported SMA products, the Modbus TCP and Modbus UDP servers are off by default and must be turned on before use. If the client cannot reach the Cluster Controller, read the controller's IP address and make sure the same address is set in the client. A Modbus client can also send setpoints to network port X13 or X14 on the Cluster Controller.
