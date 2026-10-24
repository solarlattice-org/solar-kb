---
id: proto:sunspec-model-201
type: Protocol
name: SunSpec model 201 Meter (Single Phase) single phase (AN or AB) meter
aliases:
- SunSpec 201
- model 201
- ac_meter_an_or_ab
category: Communication
protocol_kind: information-model
---
SunSpec model 201 is the SunSpec information model for a single-phase meter connected AN or AB. It is read over Modbus registers. One meter map covers single, split, wye and delta meters. The C_SunSpec_DID register tells them apart, and a value of 201 marks a single-phase meter. A single-phase meter fills in only the summary and phase A values. Registers that do not apply to it return the unsupported value. In the SolarEdge SunSpec meter mapping, a common block comes first with the meter manufacturer, model, serial number and Modbus ID. The meter model ID follows at address 40188 (base 0). On SolarEdge three-phase inverters with Synergy technology, the meter base addresses shift: add 50 for 2-unit models and 70 for 3-unit models. The Veris E51C meters report their model ID, from 201 to 204, in read-only register 40070. The Accuenergy Acuvim II reports it at decimal address 50069.
