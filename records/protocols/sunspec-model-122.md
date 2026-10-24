---
id: proto:sunspec-model-122
type: Protocol
name: SunSpec model 122 Measurements_Status
aliases:
- SunSpec 122
- model 122
- status
- Measurement Status
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Model 122 is listed as one of the SunSpec models in the XGI 1500 SunSpec model overview.
  cite:
  - src: src:eq-equip-inverters-yaskawa-yaskawa-solectria-xgi-1500-programming-docr-071063-xgi-1500-modbus-map-d
    loc: tbl=2
    h: 1c93cb0d72a7
  - src: src:eq-equip-inverters-solectria-xgi-1500-docr-071063-xgi-1500-modbus-map-c
    loc: sec=h4
    h: c413147499ae
  review: drafted
---
SunSpec model 122 is a SunSpec information model that carries measurement and status data. Like every SunSpec model, it starts with a header giving its ID and its length. SolarEdge describes SunSpec as an application-layer protocol for interoperability between distributed energy resource components and smart grid applications. The XGI 1500 maps say to use only the supported registers, because unsupported ones are marked Reserved. SMA inverter firmware notes say the status mapping for PVConn, StorConn and ECPConn in model 122 was adjusted.

<!-- review notes
- sentence 2: support check: partial - The passage describes SunSpec as an application-layer protocol for DER/smart grid interoperability, but nothing attributes it to SolarEdge.
- sentence 4: support check: partial - The passages say the status mapping for PVConn, StorConn and ECPConn in model 122 was adjusted, but they don't name SMA or firmware notes.
-->
