---
id: concept:modbus-addressing
type: Concept
name: Modbus addressing
aliases:
- Modbus unit ID
- slave address
- Modbus address
- Unit ID
- slave individual addresses
category: Communication
concept_kind: technology
claims:
- claim_id: c1
  rel: part_of
  target: proto:modbus
  note: Addressing rules are defined in the Modbus over serial line specification.
  cite:
  - src: src:ref-communications-comms-modbus-modbus-over-serial-line-v1
    loc: sec=2.2
    h: 4a57a8226320
  - src: src:ref-communications-comms-modbus-modbus-over-serial-line-v1-02
    loc: sec=2.2
    h: 4a57a8226320
  review: drafted
  review_note: 'support check: partial - Passages give the addressing rules under MODBUS, but nothing
    states they come from the serial line specification or that addressing is part of proto:modbus in
    that way.'
- claim_id: c2
  rel: related_to
  target: proto:sma-modbus
  note: SMA Modbus profile defines 247 unit IDs, 245 assignable to individual devices, with some IDs reserved.
  cite:
  - src: src:eq-equip-inverters-sma-sunny-central-modbus-sc2xxx-ti-en-17
    loc: sec=3.6.1
    h: 6e316b9706dd
  review: drafted
- claim_id: c3
  rel: related_to
  target: proto:modbus-tcp
  note: ABB FENA module address mode maps inverter parameters to holding registers in the 0...65535 range.
  cite:
  - src: src:eq-equip-inverters-abb-mfa-scada-modbustcp-link-ds-magnolia-default
    loc: sec=2.3
    h: e02eab8fc342
  review: drafted
- claim_id: c4
  rel: related_to
  target: fm:duplicate-communication-address
  note: Each slave address must be unique on a Modbus serial bus; installers set a unique Modbus address
    per device.
  cite:
  - src: src:ref-communications-comms-modbus-modbus-over-serial-line-v1
    loc: sec=2.2
    h: 4a57a8226320
  - src: src:ref-communications-comms-modbus-modbus-over-serial-line-v1-02
    loc: sec=2.2
    h: 4a57a8226320
  - src: src:eq-equip-das-alsoenergy-alsoenergy-installation-manual-pv-rev-13
    loc: tbl=3.r9
    h: 5de0aac0ff5d
  review: drafted
  review_note: 'support check: partial - Uniqueness of slave address on a serial bus is stated, but installers
    setting a unique address is only a table-of-contents heading, and duplicate-fault relation isn''t
    stated.'
---
Modbus addressing is how a master picks out one device on a shared Modbus link, using a slave address (also called a unit ID). On a serial bus the address space has 256 addresses, and address 0 is reserved for broadcasts that every slave must recognise. The master needs no address of its own, but every slave needs one, and it must be unique on that serial bus. That is why installers program a unique Modbus address into each device. In the SMA Modbus profile, the unit ID is the top-level address. The profile has 247 unit IDs, and 245 of them can be assigned to individual devices. SMA reserves some unit IDs, such as 2 for system parameters and 3 for the inverter, and automatic system detection skips the reserved ranges. Register addressing is a separate layer. Within a device, registers are addressed from 0 to 0xFFFF, which gives 65536 addresses.

<!-- review notes
- sentence 3: support check: partial - Master has no address and slave addresses must be unique are stated; installers programming unique addresses is only implied by a heading, and the causal 'that is why' is not stated.
- sentence 6: support check: partial - Range 0 to 0xFFFF with 65536 addresses is stated for registers, but 'separate layer' and 'within a device' are not explicitly stated.
-->
