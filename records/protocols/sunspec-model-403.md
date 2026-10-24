---
id: proto:sunspec-model-403
type: Protocol
name: SunSpec model 403 String Combiner (Current)
aliases:
- SunSpec 403
- model 403
- string_combiner_current_input
category: Communication
protocol_kind: information-model
---
SunSpec sorts device registers into defined groups called models, and each model starts with a header that gives its identity and length. A SunSpec register map begins with the identifier string SunS, and the common model block follows it. A device supports only the SunSpec models listed in its own Modbus map. Registers it does not implement are marked Reserved, so read only the supported registers. SolarEdge describes SunSpec as an application-layer protocol that lets distributed energy resource components work with smart grid applications.

<!-- review notes
- sentence 3: support check: partial - Passages say only models listed in this document are supported (for SOLECTRIA XGI 1500) and unsupported registers are Reserved; generalization to any device's own map is implied but the passages are device-specific.
- sentence 4: support check: partial - The SunSpec description matches, but the passage doesn't attribute it to SolarEdge.
-->
