---
id: proto:sunspec-model-712
type: Protocol
name: SunSpec model 712 DER Watt-Var
aliases:
- SunSpec 712
- model 712
- DERWattVar
- DER Watt-Var Q(P)
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Listed as model 712 in the SunSpec 700 series of DER information models.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw3-14-05-r-stpxx-us-411-info-sunspec-modbus-documentation
    loc: sec=5
    h: 7d26697c862c
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-sunspecmodbus-ti-en-11
    loc: sec=5
    h: 7d26697c862c
  review: drafted
---
SunSpec model 712, DER Watt-Var Q(P), is one of the 700 series SunSpec information models. These models define how a DER controls reactive power based on its active power output. SunSpec is an application-layer protocol for interoperability between distributed energy resource components and smart grid applications. SunSpec groups registers into models. Each model starts with a header that gives its identity and length, and registers a device does not support are marked Reserved. SMA SunSpec Modbus documentation states that a future firmware version will extend SunSpec profile 2.0 with the 700 series to meet IEEE 1547:2018. The 700 series replaces the 100 series, which still works but SunSpec now marks as outdated. On SMA products the SunSpec Modbus profile begins at register 40001, so a technician should look for model 712 by its header in that register range. Check the firmware support list first, because the 700 series is announced for a future version.

<!-- review notes
- sentence 1: support check: partial - The 712 Watt-Var Q(P) listing in the 700 series is stated, but the passages do not say these models define reactive power control based on active power output.
- sentence 5: support check: partial - The passages state that the profile begins at register 40001 and that the 700 series is announced for a future firmware version. They do not say to find model 712 by its header in that range or to check the firmware support list first, which are advice not in the passages.
-->
