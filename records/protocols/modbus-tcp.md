---
id: proto:modbus-tcp
type: Protocol
name: Modbus TCP
aliases:
- Modbus TCP/IP
- Modbus/TCP
- MODBUS over TCP
- MBAP
category: Communication
protocol_kind: application
claims:
- claim_id: c1
  rel: subclass_of
  target: proto:modbus
  note: Modbus TCP is the Modbus protocol carried over TCP/IP networks, using port 502 by default.
  cite:
  - src: src:eq-equip-das-alsoenergy-locus-edr-grc-moxa-edr-g903-series-manual-4-0
    loc: sec=h692
    h: df79d1e7b097
  - src: src:eq-equip-meters-ion-8650-ion-8650-user-guide
    loc: sec=h264
    h: d0727d822f53
  review: drafted
---
Modbus TCP carries the Modbus protocol over TCP/IP networks, and by default it connects on port 502. The Modbus protocol data unit does not depend on the layers beneath it. On TCP, the client that starts a transaction builds an application data unit, and the function code inside it tells the server what action to take. The packet is close to a Modbus RTU frame, but it adds a six-byte header, drops the CRC and keeps the RTU limit of 256 bytes per packet. The Fronius Datamanager 2.0 offers SunSpec Modbus TCP on its RJ45 Ethernet port and over Wi-Fi, alongside Solar.web and the Fronius Solar API. The FIMER PVS-60-TL-US and PVS-166/175-TL-US inverters support SunSpec-compliant Modbus RTU and TCP. The PVS-60-TL-US runs a Modbus TCP server on port 502. The KACO blueplanet TL3 models list TCP/IP, Modbus TCP and SunSpec as their communication interfaces. The CPS FlexOM Gateway can act as a Modbus TCP server for a third-party SCADA system on the same LAN subnet and forwards its commands to the inverter daisy chain.

<!-- review notes
- sentence 2: support check: partial - PDU independence and function code are stated, but the passage says 'Master' and doesn't say it is on TCP specifically (generic MODBUS), though title is TCP/IP; minor wording difference.
- sentence 5: support check: partial - Modbus RTU/TCP SunSpec is stated for both models, but the port 502 server row isn't tied explicitly to the PVS-60-TL-US.
-->
