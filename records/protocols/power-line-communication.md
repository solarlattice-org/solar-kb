---
id: proto:power-line-communication
type: Protocol
name: Power line communication
aliases:
- PLC
- powerline communication
- PLCC
- power line carrier
- Power line
category: Communication
protocol_kind: transport
---
Power line communication works at the transport layer. It puts a high-frequency signal on top of an existing power line, so the power conductors also carry the data. The Enphase IQ Gateway talks to IQ8 Series microinverters, collects system performance data and sends it over the internet to the Enphase Cloud. Utilities use power line carrier on transmission lines. Coupling capacitors inject the carrier signal, and line traps keep it out of the substation. The carrier can be coupled from one phase to ground, between two phases, or on all three phases. Transformers strongly weaken PLC signals, and rain or snow can raise noise levels enough to cause data errors.

<!-- review notes
- sentence 1: support check: partial - Passages say PLC superimposes a high-frequency signal on an existing power line, but nothing says it works at the 'transport layer'; that claim is not supported.
-->
