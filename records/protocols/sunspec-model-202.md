---
id: proto:sunspec-model-202
type: Protocol
name: SunSpec model 202 split single phase (ABN) meter
aliases:
- SunSpec 202
- model 202
- ac_meter_abn
- Split Single Phase (ABN) Meter
- Split Phase Meter
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: One of the meter models (single, split, wye, delta) the SunSpec interoperability specification
    defines; all four share a single Modbus map.
  cite:
  - src: src:eq-equip-inverters-solaredge-sunspec-implementation-technical-note
    loc: sec=h42
    h: c4797ccaca99
  - src: src:eq-equip-inverters-solaredge-sunspec-implementation-technical-note
    loc: sec=h47
    h: 59132b557ead
  review: drafted
---
SunSpec model 202 is the SunSpec information model for a split single phase meter, wired as two lines plus neutral (ABN). It shares one Modbus register map with the single phase, wye and delta meter models. The C_SunSpec_DID register tells them apart: 202 means a split single phase meter. Registers that do not apply to a given meter type return the unsupported value. In the SolarEdge SunSpec implementation, the meter's identification register follows the common block at base-0 address 40188. Further meters appear at 40362 and 40537. For SolarEdge three phase inverters with Synergy technology, add 50 to the default meter addresses on 2-unit models and 70 on 3-unit models. On the Accuenergy Acuvim II power meter, the SunSpec meter ID is a read-only uint16 at decimal address 50069. It is read with function 03H, and the following registers hold currents, voltages, scale factors and frequency. The Veris E51C meters report the meter model ID in register 40070, with a range of 201 to 204.
