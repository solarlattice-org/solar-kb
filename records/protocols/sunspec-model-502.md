---
id: proto:sunspec-model-502
type: Protocol
name: SunSpec model 502 Solar Module
aliases:
- SunSpec 502
- model 502
- solar_module
category: Communication
protocol_kind: information-model
---
SunSpec sorts device registers into defined groups called models. Each model opens with a header that identifies it and gives its length. A device supports only the models listed in its own documentation. Inside a model, registers the device does not support are marked Reserved, and only supported registers should be used. SolarEdge describes SunSpec as an application-layer protocol for interoperability between distributed energy resource components and smart grid applications. On SMA inverters the Modbus interface is off by default. You must turn it on before SunSpec Modbus data can be read, and port 502 is set by default. On SMA products the SunSpec Modbus profile starts at register 40001, and Modbus is offered over both TCP and UDP on port 502.

<!-- review notes
- sentence 2: support check: partial - Passages support Reserved marking and using only supported registers, and that only listed models are supported for this specific inverter; the general claim about any device is an extrapolation from the XGI 1500 text.
- sentence 3: support check: partial - The passage describes SunSpec as an application-layer protocol for DER/smart grid interoperability, but nothing attributes this description to SolarEdge (source unclear).
-->
