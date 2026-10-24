---
id: proto:sunspec-information-model
type: Protocol
name: SunSpec information models
aliases:
- SunSpec models
- SunSpec
- SunSpec Model
category: Communication
protocol_kind: information-model
---
The SunSpec Alliance defines standard information models, built on Modbus, for monitoring and controlling distributed energy resource devices. SunSpec calls itself an application-layer protocol. Its aim is to let DER components and smart grid applications work together. Registers are grouped into models. Each model starts with a header that gives its identity and length. Registers a device does not support are marked Reserved and should not be used. On SMA inverters, SunSpec profile 2.0 is selected automatically when you choose a country data set based on SMA Grid Guard 10. In the installation assistant it appears under Network configuration > Modbus as Standard (recommended). SMA supports the 100-series models, such as 001 Common, 101 to 103 AC monitoring, 120 to 123 nameplate, settings and controls, and 160 DC monitoring. SunSpec now treats the 100 series as outdated, and the 700 series is meant to replace it to meet IEEE 1547-2018. The SMA profile leaves out any model the device does not support. Within a model, blocks repeat so the data area can fit, for example, a different number of DC inputs.
