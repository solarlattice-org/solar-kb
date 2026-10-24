---
id: prod:axis-t8144
type: Product
name: AXIS T8144 60 W midspan
aliases:
- T8144
category: Security
make: axis
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:axis
  cite:
  - src: src:eq-equip-cameras-axis-axis-t8144-60w-midspan-user-manual
    loc: sec=h23
    h: e50e44cc6c59
  review: drafted
- claim_id: c2
  attr: rated_power
  value:
    max: 60
    unit: unit:W
  conditions: Power over Ethernet output, single port, at 55 V DC output
  cite:
  - src: src:eq-equip-cameras-axis-axis-t8144-60w-midspan-cut-sheet
    loc: tbl=1.r8
    h: 15a260307c9d
  - src: src:eq-equip-cameras-axis-axis-t8144-60w-midspan-cut-sheet
    loc: sec=h2
    h: 08bde1a7d49e
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c3
  attr: max_input_voltage
  value:
    min: 20
    max: 60
    unit: unit:V
  conditions: DC input voltage range (dual DC inputs); input power up to 72 W
  cite:
  - src: src:eq-equip-cameras-axis-axis-t8144-60w-midspan-cut-sheet
    loc: tbl=1.r7
    h: b98c410cec31
  - src: src:eq-equip-cameras-axis-axis-t8144-60w-midspan-cut-sheet
    loc: sec=h2
    h: 08bde1a7d49e
  review: drafted
- claim_id: c4
  attr: operating_temperature
  value:
    min: -40
    max: 75
    unit: unit:DEG_C
  conditions: Operating temperature range per cut sheet
  cite:
  - src: src:eq-equip-cameras-axis-axis-t8144-60w-midspan-cut-sheet
    loc: sec=h2
    h: 08bde1a7d49e
  review: drafted
---
The AXIS T8144 60 W Industrial Midspan is an industrial-grade single-port midspan from Axis that supplies Power over Ethernet to network devices. It is built to mount inside cabinets or on DIN rails and is intended for harsh environments. It takes two DC inputs for power redundancy, each accepting 20 to 60 V DC, and draws at most 72 W. The output is 55 V DC with up to 60 W of PoE power. The rated operating temperature is -40 °C to 75 °C. Axis describes it as plug-and-play and widely compatible with Axis PoE devices.

<!-- review notes
- sentence 3: support check: partial - Dual DC inputs for redundancy, 20-60 V DC and max 72 W are stated, but the passages don't say that each input separately accepts 20-60 V.
-->
