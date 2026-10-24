---
id: proto:sunspec-modbus
type: Protocol
name: SunSpec Modbus
aliases:
- SunSpec
- SunSpec Modbus profile
- SunSpec Modbus interface
category: Communication
protocol_kind: application
claims:
- claim_id: c1
  rel: subclass_of
  target: proto:modbus
  note: A device-specific Modbus profile that defines which data sit in which register areas, which the
    base Modbus specification leaves open.
  cite:
  - src: src:eq-equip-inverters-sma-communications-sma-sunspec-modbus-techinfo
    loc: sec=3.1
    h: 939ea2e6239b
  - src: src:eq-equip-inverters-sma-communications-sma-sunspec-modbus-techinfo
    loc: sec=3.2
    h: 2ec39a1c71ae
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
SunSpec Modbus is a standardized profile from the SunSpec Alliance. It defines a broad set of measured values and parameters for devices in decentralized generation systems, such as inverters, energy meters and weather stations. It sits on top of the Modbus application protocol. Modbus itself does not say which data go in which register area, so profiles like SunSpec define that, and a Modbus client such as a SCADA system reads from or writes to the device acting as server. Registers are grouped into models. Each model starts with a header that gives its identity and length, and registers a device does not support are marked Reserved and should not be used. On SMA products the SunSpec profile starts at register 40001. The profile version (2.0, 1.1 or 1.0) is chosen automatically when the country data set is set during commissioning. The SMA Data Manager M uses its Modbus client interface (Modbus TCP/RTU) to work with SunSpec devices. Compatible devices are integrated into the system automatically. The FIMER PVS-60-TL-US and PVS-166/175-TL-US string inverters provide SunSpec-compliant Modbus RTU/TCP. On the PVS-166/175, inverter parameters can be upgraded remotely over Ethernet or WLAN using SunSpec Modbus. The CPS SCH100/125KTL-DO and SCH125KTL-AIO inverters support SunSpec and Modbus over RS485, and they can use either SunSpec or CPS Modbus data mapping. On the SMA STS60-10 storage system, the inverter manager answers SunSpec Modbus on unit ID 125. Write the active power setpoint to register 40349, negative to charge and positive to discharge, and leave at least 200 ms between Modbus accesses.

<!-- review notes
- sentence 5: support check: partial - Client interface and automatic integration are stated, but the passages don't name the Data Manager M.
- sentence 8: support check: partial - Unit ID 125, register 40349, sign convention and 200 ms are stated, but the passage also requires Peak Load Shaving and Time of Use to be enabled, which is omitted.
-->
