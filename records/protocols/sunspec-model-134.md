---
id: proto:sunspec-model-134
type: Protocol
name: SunSpec model 134 Freq-Watt Crv
aliases:
- SunSpec 134
- model 134
- freq_watt
category: Communication
protocol_kind: information-model
---
SunSpec arranges device registers into numbered groups called models, and each model opens with a header that gives its identifier and length. An inverter supports only the models its vendor lists, and registers it does not implement within a model are marked Reserved and should not be used. SunSpec is described as an application-layer protocol that lets distributed energy resources interoperate with smart grid applications. SMA inverter documentation notes that SunSpec profile 2.0 dropped the older frequency-watt model 127 and replaced it with model 711, so check which profile the device firmware uses before mapping curve registers. In a vendor map such as the Yaskawa Solectria SGI XTM, a frequency-watt curve is written as a number of points from 2 to 10 with paired frequency and watt percentages, plus ramp time and time window settings.

<!-- review notes
- sentence 4: support check: partial - Passages state model 127 is replaced by 711 in profile 2.0, but nothing attributes this to SMA documentation or advises checking firmware profile before mapping.
- sentence 4: review: partial - The SMA passages state 127 Frequency-Watt is replaced by 711 in profile 2.0, but the advice to check the firmware profile before mapping registers is not in them.
-->
