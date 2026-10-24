---
id: proto:sma-modbus
type: Protocol
name: SMA Modbus profile
aliases:
- SMA Modbus
- SMA Modbus interface
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: subclass_of
  target: proto:modbus
  note: A device-specific Modbus profile. It defines which SMA data sits in which Modbus register, because
    the Modbus specification does not define register content.
  cite:
  - src: src:eq-equip-inverters-sma-communications-sma-sunspec-modbus-techinfo
    loc: sec=3.1
    h: 939ea2e6239b
  - src: src:sma-edmx-modbus-ti-en-16
    loc: sec=3.1
    h: 939ea2e6239b
  - src: src:eq-equip-inverters-sma-data-manager-m-edmm-10-modbus-ti-en-14
    loc: sec=3.1
    h: 939ea2e6239b
  - src: src:eq-equip-inverters-sma-sunny-central-modbus-sc2xxx-ti-en-17
    loc: sec=3.1
    h: 3a199a950273
  review: drafted
---
The SMA Modbus profile is SMA's own register map. It sits on top of the Modbus application protocol and says which SMA device data is stored in which Modbus register. Base Modbus does not say what data goes in which area, so a client such as a SCADA system needs this profile to read from or write to an SMA device acting as a Modbus server. SMA products offer both the SMA Modbus profile and the SunSpec Modbus profile. Not every SMA product supports every register in the SMA profile, so check the register list for the device you are working on. The profile covers values such as total and daily energy, current power, and voltage and current levels. Its register assignments are split into ranges that you reach through unit IDs. Usually the SMA device connects to the utility's or grid operator's SCADA system over Ethernet. The Sunny Tripower X lists SMA Modbus as a data protocol, alongside SunSpec Modbus and Speedwire. On Sunny Central inverters, a user-defined profile lets you move registers to consecutive addresses so they can be read in one block. A master profile extension makes third-party Modbus devices available under unit IDs 16 to 31. If the profile shows measured values that the device does not support, the Modbus configuration may be wrong. Check it against the assignment tables and correct it.

<!-- review notes
- sentence 6: support check: partial - Passages support the consecutive-address reassignment and unit IDs 16 to 31 for third-party devices, but do not mention Sunny Central specifically.
-->
