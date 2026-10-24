---
id: proto:sunspec-model-802
type: Protocol
name: SunSpec model 802 Battery Base Model
aliases:
- SunSpec 802
- model 802
- battery
category: Communication
protocol_kind: information-model
---
SunSpec is a communication protocol at the application layer. It was designed so that distributed energy resource equipment and smart grid applications can work together. Each model opens with a header that gives its identity and its length. This lets a client walk through the register map one model at a time. In the header, the model ID is read as an unsigned 16-bit register. Models 307 and 160 are examples of how vendor maps show it. A device may implement only some registers inside a model. Registers it does not support are marked Reserved, and only the supported ones should be used. Only the models listed in a vendor's own register map are supported. Check that list before you read battery data from a device, as the Solectria XGI 1500 documents advise. The SunSpec map ends with an end marker of 0xFFFF after the last model.

<!-- review notes
- sentence 2: support check: partial - Header identifying model and its length is stated, but the purpose of letting a client walk the register map model by model is not stated.
- sentence 5: support check: partial - Passages say only models listed in the document are supported by the XGI 1500 and to use supported ones, but say nothing about checking before reading battery data.
-->
