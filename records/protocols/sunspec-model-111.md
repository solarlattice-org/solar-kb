---
id: proto:sunspec-model-111
type: Protocol
name: SunSpec model 111 Inverter (Single Phase) FLOAT
aliases:
- SunSpec 111
- model 111
- inverter_single_phase_float
category: Communication
protocol_kind: information-model
---
SunSpec sorts device registers into defined groups called models, and each model starts with a header that gives its identity and its length. SMA calls these register groups information models and lists the ones it supports by model number. A device supports only the models its register map lists, and within a model any register marked Reserved is unsupported and should not be used. The single-phase inverter model with integer values is model 101; its DID register reads 101 for single phase, 102 for split phase and 103 for three phase. SMA marks the 100-series inverter models as outdated in SunSpec and recommends the 700 series, such as model 701 for AC measurement, to meet IEEE 1547-2018.

<!-- review notes
- sentence 4: support check: partial - DID values 101/102/103 for single/split/three phase are stated, but the passage doesn't state that model 101 is the integer single-phase model.
- sentence 4: review: partial - The 101/102/103 DID values are stated, but nothing in the passage says model 101 is the integer-valued single-phase model.
-->
