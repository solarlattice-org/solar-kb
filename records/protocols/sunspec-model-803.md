---
id: proto:sunspec-model-803
type: Protocol
name: SunSpec model 803 Lithium-Ion Battery Bank Model
aliases:
- SunSpec 803
- model 803
- lithium_ion_bank
category: Communication
protocol_kind: information-model
---
SunSpec is an application-layer communication protocol. Its purpose is interoperability between distributed energy resource components and smart grid applications. SunSpec groups device registers into defined information models. Each model starts with a header that identifies the model and gives its length. A device may support only some registers within a model. Unsupported registers are marked Reserved, and only supported registers should be used. On SMA inverters, the SunSpec profile includes only the information models the product supports. This keeps PV inverter models out of battery inverters, and battery inverter models out of PV inverters. Within a model, blocks can repeat to hold data areas of different lengths. On SMA battery and hybrid inverters, a lithium-ion battery must be connected to the inverter by a data cable so that battery management can work.
