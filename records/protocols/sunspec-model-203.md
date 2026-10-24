---
id: proto:sunspec-model-203
type: Protocol
name: SunSpec model 203 wye-connect three phase (abcn) meter
aliases:
- SunSpec 203
- model 203
- ac_meter_abcn
- WYE-Three Phase (ABCN)
- WYE (4-wire) Meter
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: One of four SunSpec meter models (201 to 204) that share a single Modbus register map; 203 is
    the wye (4-wire) three-phase variant.
  cite:
  - src: src:eq-equip-inverters-solaredge-sunspec-implementation-technical-note
    loc: sec=h42
    h: c4797ccaca99
  - src: src:eq-equip-inverters-solaredge-sunspec-implementation-technical-note
    loc: sec=h47
    h: 59132b557ead
  - src: src:eq-equip-inverters-solaredge-sunspec-implementation-technical-note
    loc: tbl=13.r11
    h: 66f56e78a6c7
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
  review_note: 'support check: partial - Passages list 203 as Wye-Connect three-phase meter in a shared
    map, but ''four of 201-204'' and ''proto:sunspec-information-model'' classification are only implied.'
---
SunSpec model 203 is the SunSpec information model for a wye-connected, four-wire (ABCN) three-phase meter. It is read over Modbus registers. The single, split-phase, wye and delta meter models all share one SunSpec meter register map. Each type uses only part of that map, and the C_SunSpec_DID register shows which type the meter is: a value of 203 means a wye meter. Registers that do not apply to the meter's connection type return the unsupported value. In the SolarEdge SunSpec implementation, the meter model ID follows the meter's common block, for example at address 40188 (base 0). For three-phase Synergy inverters, add 50 to the default meter addresses on 2-unit models and 70 on 3-unit models. On the Veris E51C meters, register 40070 holds the SunSpec meter ID (201 to 204) and sets the meter configuration. The wye model also gives phase-to-neutral voltages, such as phase C to neutral at register 40080. The Accuenergy Acuvim II meter reports the SunSpec meter ID at register 50069 as a uint16, which is read with function 03H. The registers after it give per-phase currents, phase and line voltages, scale factors and frequency. Before you set the meter to 203, check that the site wiring really is three-phase four-wire wye, for example a Form 9 four-wire wye meter with three PTs and three CTs.

<!-- review notes
- sentence 4: support check: partial - Address 40188 (base 0) for DID and the +50/+70 offsets are stated, but the 'follows the common block' ordering is only shown by table, and the offsets apply to the meters' base address on Synergy inverters; mostly fine though the SolarEdge attribution is not explicit.
- sentence 7: support check: partial - u11 states three-phase four-wire needs Form 9 wye with 3 PTs and 3 CTs, and u4 shows 203 is wye, but the instruction to check wiring before setting is not stated (and the register is read-only).
- sentence 7: review: partial - The Tesla row ties three-phase four-wire wiring to a Form 9 wye meter with 3 PTs and 3 CTs, but no passage gives the instruction to check wiring before setting 203, and the Veris register is read-only.
-->
