---
id: proto:sunspec-model-401
type: Protocol
name: SunSpec model 401 String Combiner (Current)
aliases:
- SunSpec 401
- model 401
- string_combiner_current
category: Communication
protocol_kind: information-model
---
SunSpec sorts device registers into defined groups called models. Each model opens with a header that gives its identity and length. SunSpec as a whole is described as an application-layer protocol for interoperability between distributed energy resource components and smart grid applications. A device may support only some registers within a model, and unsupported ones are marked Reserved, so read only the supported registers. A string combiner box gathers the DC current of several PV strings before it goes on to the inverter. Monitoring platforms such as AlsoEnergy report combiner data as combiner output current and per-string current for each channel.

<!-- review notes
- sentence 5: support check: partial - Passage gives ZoneAmps# as combiner output current and I# as string output current per channel, but doesn't name AlsoEnergy or other platforms explicitly (only implied by the DC string combiner context).
-->
