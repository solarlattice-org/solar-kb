---
id: proto:modbus-rtu
type: Protocol
name: Modbus RTU
aliases:
- Modbus RTU over RS-485
category: Communication
protocol_kind: application
claims:
- claim_id: c1
  rel: subclass_of
  target: proto:modbus
  note: The Modbus protocol reference guide lists RTU mode as a transmission mode of the Modbus protocol.
  cite:
  - src: src:ref-communications-comms-modbus-modbus-protocol-ref-guide-pi-mbus-300
    loc: tbl=1.r7
    h: 5c8284ccc5ff
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
Modbus RTU is the RTU transmission mode of the Modbus protocol. It runs over a serial link, for example a two-wire RS-485 bus with D- and D+ data terminals on the Fronius Symo. The FIMER PVS-60-TL-US and PVS-166/175-TL-US string inverters list Modbus RTU/TCP as their communication protocol and state that it is SunSpec compliant. The UNO-DM-PLUS-US inverters list ModBus RTU (SunSpec) next to the Aurora Protocol, and some variants also list ModBus TCP. On the Fronius Datamanager 2.0, the RS485 port carries either SunSpec Modbus RTU or a meter connection. Third-party systems can use it to read inverter data while the system also reports to Fronius Solar.web. The Huawei SmartLogger can connect to one environmental monitoring instrument that supports standard Modbus-RTU. Other third-party Modbus-RTU devices need a .cfg protocol file from Huawei imported into the logger, and you must add them manually. On the Elkor WattsOn Mark II W2-M2, wire the Modbus RTU master to the X. Bus terminal and set the serial format to 115200,N,8,1. The meter answers on any address, and address 1 is recommended.
