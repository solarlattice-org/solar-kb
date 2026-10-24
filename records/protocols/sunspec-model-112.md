---
id: proto:sunspec-model-112
type: Protocol
name: SunSpec model 112 Inverter (Split Phase) FLOAT
aliases:
- SunSpec 112
- model 112
- inverter_split_phase_float
category: Communication
protocol_kind: information-model
---
SunSpec arranges device registers into defined groups called models, and each model starts with a header that identifies it and gives its length. A device reports which inverter model family it implements through the C_SunSpec_DID register, where 102 means split phase, 101 means single phase and 103 means three phase. SMA lists model 102 split phase AC monitoring as supported but recommends model 701 instead, because the 100 series is now marked as outdated in favour of the 700 series. Inverters support only the models and registers their vendor map lists, and unsupported registers are marked Reserved, so check the map before polling.

<!-- review notes
- sentence 4: support check: partial - Passage says only listed models and supported registers are supported, unsupported ones are Reserved, and to use only supported registers; 'check the map before polling' is advice implied but the claim is for a specific vendor (SOLECTRIA) generalized to inverters.
-->
