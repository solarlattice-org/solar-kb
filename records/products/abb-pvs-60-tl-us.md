---
id: prod:abb-pvs-60-tl-us
type: Product
name: FIMER PVS-60-TL-US string inverter
aliases:
- PVS-60-TL-US
- PVS-60-TL
- PVS-60-TL-R-US
- PVS-60-TL-S-US
- PVS-60-TL-SC-US
category: Inverters
make: abb
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:fimer
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: sec=h7
    h: 7a30193590f6
  review: drafted
- claim_id: c2
  attr: rated_power
  value:
    nominal: 60
    unit: unit:KiloW
  conditions: Rated active power (Pn); full Pn available with grid voltage between 0.937 and 1.2 times
    Un
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: sec=h59
    h: a6668cf93326
  review: drafted
- claim_id: c3
  attr: nominal_voltage
  value:
    nominal: 480
    unit: unit:V
  conditions: Rated AC output voltage (Un)
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: sec=h59
    h: a6668cf93326
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:modbus-rtu
  note: Listed as SunSpec compliant
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=14.r3
    h: d0d623650c1e
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:modbus-tcp
  note: Listed as SunSpec compliant
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=14.r3
    h: d0d623650c1e
  review: drafted
- claim_id: c6
  rel: uses_protocol
  target: proto:sunspec-modbus
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: tbl=14.r3
    h: d0d623650c1e
  review: drafted
- claim_id: c7
  rel: implements
  target: func:rapid-shutdown
  conditions: PVS-60-TL-R-US variant only (single input channel, screw terminal DC connection)
  note: Quick installation guide lists RSD compatibility as Yes for this variant
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-quick-installation-guide-revc
    loc: tbl=2.r3
    h: 485a03c343b2
  review: drafted
- claim_id: c8
  rel: lacks
  target: func:rapid-shutdown
  conditions: PVS-60-TL-S-US and PVS-60-TL-SC-US variants
  note: Quick installation guide lists RSD compatibility as No for these fused variants
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-quick-installation-guide-revc
    loc: tbl=2.r1
    h: 96ed621d01bf
  - src: src:abb-fimer-pvs-60-tl-us-quick-installation-guide-revc
    loc: tbl=2.r2
    h: 068a9e799cbd
  review: drafted
- claim_id: c9
  rel: implements
  target: func:surge-protection
  conditions: Class II SPD on both DC and AC sides, all listed variants
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-quick-installation-guide-revc
    loc: tbl=2.r3
    h: 485a03c343b2
  - src: src:abb-fimer-pvs-60-tl-us-quick-installation-guide-revc
    loc: tbl=2.r1
    h: 96ed621d01bf
  - src: src:abb-fimer-pvs-60-tl-us-quick-installation-guide-revc
    loc: tbl=2.r2
    h: 068a9e799cbd
  review: drafted
- claim_id: c10
  rel: compatible_with
  target: prod:staubli-mc4
  conditions: PVS-50/60-TL units effective from week 17 of 2020
  cite:
  - src: src:abb-fimer-string-inverter-product-manual-appendix-revg
    loc: tbl=1.r13
    h: 6607f354c456
  review: drafted
---
The PVS-60-TL-US is a FIMER three-phase string inverter family rated at 60 kW active power and 60 kVA apparent power, with a 480 Vac rated output voltage. It is rated for 60 kVAR of reactive power, and the manual says full rated power is available across a grid voltage band around the nominal value. It communicates over Modbus RTU and Modbus TCP, and the manufacturer describes that interface as SunSpec compliant. The R variant has one input channel with screw-terminal DC connections, no string fuses and support for rapid shutdown. The S and SC variants have three input channels, or one if the inputs are paralleled. They have fused positive and negative string inputs, using fuse holders on the S and quick-fit connectors on the SC, and they do not support rapid shutdown. Every variant has a DC switch and Class II surge protection on both the DC and AC sides. From week 17 of 2020, PVS-50/60-TL units ship with Stäubli MC4 DC connectors.

<!-- review notes
- sentence 1: support check: partial - The 60 kW, 60 kVA and 480 Vac values are stated, but "three-phase" is not stated in the passages.
- sentence 1: review: partial - The 480 Vac, 60 kW, 60 kVA and 'string inverters' values are stated, but 'three-phase' (and the FIMER brand) are not in the quoted passages.
-->
