---
id: proto:sunspec-model-121
type: Protocol
name: SunSpec model 121 Basic Settings
aliases:
- SunSpec 121
- model 121
- settings
- Inverter Nameplate settings
- Basic settings
category: Communication
protocol_kind: information-model
claims:
- claim_id: c1
  rel: part_of
  target: proto:sunspec-information-model
  note: Model 121 is listed among the supported SunSpec information models in the 100 series, which SunSpec
    now designates as outdated.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-sunspecmodbus-ti-en-11
    loc: sec=5
    h: 7d26697c862c
  - src: src:eq-equip-inverters-solectria-xgi-1500-docr-071063-xgi-1500-modbus-map-c
    loc: sec=h4
    h: c413147499ae
  - src: src:eq-equip-inverters-yaskawa-yaskawa-solectria-xgi-1500-programming-docr-071063-xgi-1500-modbus-map-d
    loc: sec=h4
    h: 8a537b6f00cb
  review: drafted
---
SunSpec model 121 Basic Settings is one of the SunSpec information models. SunSpec groups registers into models, and each model starts with a header that gives its identity and length. SolarEdge describes SunSpec as an application-layer protocol that lets distributed energy resources work with smart grid applications. The first register at 40212 is a read-only uint16 ID, and its value is 121. The XGI 1500 model 121 block includes read-only scale factors such as VAMax_SF, VArMax_SF, PFMin_SF and ECPNomHz_SF. Unsupported registers are marked Reserved and should not be used. The model also has a ClcTotVA enumerated field, which is documented in its own table. SMA inverter firmware supports model 121 but recommends model 702 instead. The 100 series still works, but SunSpec designates it as outdated. One SMA firmware release changed how MaxRmpRte maps in model 121: it is now given in percent of WGra instead of WMax.

<!-- review notes
- sentence 2: support check: partial - The passage describes SunSpec as an application-layer protocol for DER interoperability, but nothing attributes this description to SolarEdge.
- sentence 5: support check: partial - The table of contents lists ClcTotVA Enumerated and Table 18.18 for it, but the passages don't show the table contents or define it as a field of model 121 explicitly.
- sentence 6: support check: partial - The passage says 121 is supported with 702 recommended and the 100 series is outdated, but the passages don't name SMA as the vendor.
- sentence 7: support check: partial - The passage states the MaxRmpRte mapping change to percent of WGra instead of WMax for model 121, but it names no SMA firmware release or SMA vendor.
-->
