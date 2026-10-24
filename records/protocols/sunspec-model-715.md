---
id: proto:sunspec-model-715
type: Protocol
name: SunSpec model 715 DERCtl
aliases:
- SunSpec 715
- model 715
- DERCtl
category: Communication
protocol_kind: information-model
---
SunSpec is an application-layer protocol. It is meant to let distributed energy resource equipment work with smart grid applications. SunSpec sorts its registers into groups called models. Each model starts with a header that gives its identity and its length. A device supports only the models listed in its own register map. Registers it does not support are marked Reserved and should not be used. On SMA products the SunSpec Modbus profile starts at register number 40001.

<!-- review notes
- sentence 3: support check: partial - Passages say only models listed in the document are supported by the XGI 1500 and unsupported registers are marked Reserved with 'only use supported registers'; generalization to any device's own register map is not explicit.
-->
