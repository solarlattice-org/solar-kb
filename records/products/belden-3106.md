---
id: prod:belden-3106
type: Product
name: Belden 3106 RS-485 cable
aliases:
- 3106A
- 3106DB
category: Connectors and cable
make: belden
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:belden
  cite:
  - src: src:eq-equip-cable-belden-3106a-rs-485
    loc: sec=h13
    h: 8f07556fd213
  - src: src:eq-equip-cable-belden-3106db-rs-485
    loc: sec=h13
    h: 8e767b423ea0
  - src: src:ref-communications-comms-modbus-belden-3106a-rs485-wire-spec
    loc: sec=h15
    h: 7aee2ed17df8
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:communication-cable
  note: Single 22 AWG stranded tinned-copper pair with overall shield plus a 22 AWG drain/common conductor
    and tinned-copper braid.
  cite:
  - src: src:eq-equip-cable-belden-3106db-rs-485
    loc: sec=h6
    h: 94dc73903203
  - src: src:eq-equip-cable-belden-3106a-rs-485
    loc: sec=h6
    h: e9abc4fd76fc
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:rs485
  note: Sold as an EIA industrial RS-485 cable.
  cite:
  - src: src:eq-equip-cable-belden-3106db-rs-485
    loc: sec=h6
    h: 94dc73903203
  - src: src:eq-equip-cable-belden-3106a-rs-485
    loc: sec=h6
    h: e9abc4fd76fc
  - src: src:ref-communications-comms-modbus-belden-3106a-rs485-wire-spec
    loc: sec=h15
    h: 7aee2ed17df8
  review: drafted
---
The Belden 3106 is a family of RS-485 communication cables made by Belden. It includes the 3106A and 3106DB versions. Each cable has one shielded 22 AWG stranded tinned-copper pair with polyethylene insulation, one extra 22 AWG conductor and an overall tinned-copper braid. The 3106A has a PVC jacket. The 3106DB has a CPE jacket and is rated for direct burial. Both are rated CM and PLTC and resist sunlight and oil.
