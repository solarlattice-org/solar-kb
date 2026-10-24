---
id: proto:sunspec-model-113
type: Protocol
name: SunSpec model 113 Inverter (Three Phase) FLOAT
aliases:
- SunSpec 113
- model 113
- inverter_three_phase_float
category: Communication
protocol_kind: information-model
---
SunSpec model 113 is the three-phase inverter model that uses FLOAT values. It is an information model: it sets out data points, not a transport. The first register of the block is a read-only uint16 ID that holds the value 113. A client can read it to confirm the model number. The block contains an enumerated operating state (St), a vendor operating state (StVnd), an Evt1 event bitfield and two vendor event bitfields (EvtVnd1 and EvtVnd2). The event bit tables in the same map flag conditions such as Over Temp, Over Frequency, Under Frequency and AC Under Voltage.

<!-- review notes
- sentence 1: support check: partial - Passages show model 113 is Inverter (Three-Phase) FLOAT, but nothing says it is an information model that defines data points rather than a transport.
- sentence 4: support check: partial - Bit descriptions for Over Temp, Over Frequency, Under Frequency and AC Under Voltage are listed, but the passages don't say which event table each belongs to or that they are in the same map.
- sentence 1: review: partial - The passages confirm model 113 is Inverter (Three-Phase) FLOAT, but nothing says it is an information model that defines data points rather than a transport.
- sentence 4: review: partial - The Over Temp, Over Frequency, Under Frequency and AC Under Voltage bit rows are quoted, but the passages do not show that table 18 is one of the model's event bit tables.
-->
