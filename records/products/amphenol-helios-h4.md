---
id: prod:amphenol-helios-h4
type: Product
name: Amphenol Helios H4 PV connector
aliases:
- Helios H4
- H4_Assembly
- H4 PV Connector
- Amphenol H4
- H4
category: Connectors and cable
make: amphenol
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:amphenol
  cite:
  - src: src:eq-connectors-amphenol-ids-17-helios-h4
    loc: sec=h2
    h: 9fe05aed4c0e
  - src: src:eq-connectors-amphenol-ids-17-helios-h4
    loc: sec=h1
    h: 966f5c4f79d2
  - src: src:eq-connectors-amphenol-h4-assembly-instructions
    loc: sec=h1
    h: 6680d05e01a8
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:dc-connector
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=51.r4
    h: 6e1ed26141c1
  - src: src:eq-equip-inverters-huawei-huawei-sun2000-45ktl-us-hv-datasheet-us-06-20170106
    loc: tbl=1.r46
    h: 2b76e6b7efb5
  - src: src:eq-connectors-amphenol-ids-17-helios-h4
    loc: sec=h2
    h: 9fe05aed4c0e
  review: drafted
- claim_id: c3
  rel: compatible_with
  target: prod:huawei-sun2000-25-30ktl-us
  note: Listed as the inverter DC connector.
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=51.r4
    h: 6e1ed26141c1
  review: drafted
- claim_id: c4
  rel: compatible_with
  target: prod:huawei-sun2000-45ktl-us-hv-d0
  note: Listed as the inverter DC input terminal.
  cite:
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=65.r6
    h: 1e62c9d02d93
  - src: src:eq-equip-inverters-huawei-huawei-sun2000-45ktl-us-hv-datasheet-us-06-20170106
    loc: tbl=1.r46
    h: 2b76e6b7efb5
  review: drafted
- claim_id: c5
  rel: compatible_with
  target: prod:solaredge-power-optimizer
  conditions: Optimizer models with Amphenol H4 input connectors (Pxxx-5xH4xxx)
  cite:
  - src: src:eq-equip-inverters-solaredge-design-installation-power-optimizer-input-connector-compatibility-v1-3
    loc: tbl=1.r4
    h: 189bfd09aa75
  review: drafted
  review_note: 'support check: partial - The passage only shows an ''Amphenol H4 | Pxxx-5xH4xxx'' entry,
    implying optimizer models with H4 connectors, but is terse and doesn''t name SolarEdge optimizers
    explicitly.'
- claim_id: c6
  rel: requires
  target: tool:connector-unlocking-tool
  note: A special tool is needed to un-mate, such as the H4TW0001 wrench or the H4TU0000 universal tool.
  cite:
  - src: src:eq-connectors-amphenol-ids-17-helios-h4
    loc: tbl=1.r7
    h: 1f11e8d38785
  - src: src:eq-connectors-amphenol-h4-assembly-instructions
    loc: sec=h15
    h: 104359589f50
  - src: src:eq-equip-inverters-huawei-huawei-sun2000-33-36-40ktl-us-manual
    loc: tbl=18.r6
    h: 7b823465ec9a
  review: drafted
- claim_id: c7
  rel: has_hazard
  target: hazard:disconnecting-under-load
  note: Do not unplug under load; switch off the converter or open the DC circuit interrupter first.
  cite:
  - src: src:eq-connectors-amphenol-h4-assembly-instructions
    loc: sec=h1
    h: 6680d05e01a8
  review: drafted
  review_note: 'support check: partial - Passage says do not unplug under load and how to de-energize,
    but never mentions arcing.'
- claim_id: c8
  rel: has_hazard
  target: hazard:electric-shock
  note: Connectors must be isolated from the supply during assembly or disassembly.
  cite:
  - src: src:eq-connectors-amphenol-h4-assembly-instructions
    loc: sec=h1
    h: 6680d05e01a8
  review: drafted
- claim_id: c9
  attr: rated_output_current
  value:
    nominal: 25
    unit: unit:A
  conditions: Rated current with 2.5 mm2 / 14 AWG cable, datasheet specification table
  cite:
  - src: src:eq-connectors-amphenol-ids-17-helios-h4
    loc: tbl=1.r3
    h: e4f72d13256f
  review: disputed
  review_note: possible conflict with c10 (same source; check the conditions); possible conflict with
    c11 (same source; check the conditions)
  conflicts_with:
  - prod:amphenol-helios-h4#c12
  - prod:amphenol-helios-h4#c13
  - prod:amphenol-helios-h4#c14
  - prod:amphenol-helios-h4#c15
- claim_id: c10
  attr: rated_output_current
  value:
    nominal: 35
    unit: unit:A
  conditions: Rated current with 4.0 mm2 / 12 AWG cable, datasheet specification table
  cite:
  - src: src:eq-connectors-amphenol-ids-17-helios-h4
    loc: tbl=1.r3
    h: e4f72d13256f
  review: disputed
  review_note: possible conflict with c9 (same source; check the conditions); possible conflict with c11
    (same source; check the conditions)
  conflicts_with:
  - prod:amphenol-helios-h4#c12
  - prod:amphenol-helios-h4#c13
  - prod:amphenol-helios-h4#c14
  - prod:amphenol-helios-h4#c15
- claim_id: c11
  attr: rated_output_current
  value:
    nominal: 45
    unit: unit:A
  conditions: Rated current with 6.0 mm2 / 10 AWG cable, datasheet specification table
  cite:
  - src: src:eq-connectors-amphenol-ids-17-helios-h4
    loc: tbl=1.r3
    h: e4f72d13256f
  review: disputed
  review_note: possible conflict with c9 (same source; check the conditions); possible conflict with c10
    (same source; check the conditions)
  conflicts_with:
  - prod:amphenol-helios-h4#c12
  - prod:amphenol-helios-h4#c13
  - prod:amphenol-helios-h4#c14
  - prod:amphenol-helios-h4#c15
- claim_id: c12
  attr: rated_output_current
  value:
    nominal: 40
    unit: unit:A
  conditions: Rated current with 2.5 mm2 cable, per assembly instructions
  cite:
  - src: src:eq-connectors-amphenol-h4-assembly-instructions
    loc: sec=h1
    h: 6680d05e01a8
  review: disputed
  conflicts_with:
  - prod:amphenol-helios-h4#c9
  - prod:amphenol-helios-h4#c10
  - prod:amphenol-helios-h4#c11
  review_note: possible conflict with c13 (same source; check the conditions); possible conflict with
    c14 (same source; check the conditions); possible conflict with c15 (same source; check the conditions)
- claim_id: c13
  attr: rated_output_current
  value:
    nominal: 48
    unit: unit:A
  conditions: Rated current with 4 mm2 cable, per assembly instructions
  cite:
  - src: src:eq-connectors-amphenol-h4-assembly-instructions
    loc: sec=h1
    h: 6680d05e01a8
  review: disputed
  conflicts_with:
  - prod:amphenol-helios-h4#c9
  - prod:amphenol-helios-h4#c10
  - prod:amphenol-helios-h4#c11
  review_note: possible conflict with c12 (same source; check the conditions); possible conflict with
    c14 (same source; check the conditions); possible conflict with c15 (same source; check the conditions)
- claim_id: c14
  attr: rated_output_current
  value:
    nominal: 56
    unit: unit:A
  conditions: Rated current with 6 mm2 cable, per assembly instructions
  cite:
  - src: src:eq-connectors-amphenol-h4-assembly-instructions
    loc: sec=h1
    h: 6680d05e01a8
  review: disputed
  conflicts_with:
  - prod:amphenol-helios-h4#c9
  - prod:amphenol-helios-h4#c10
  - prod:amphenol-helios-h4#c11
  review_note: possible conflict with c12 (same source; check the conditions); possible conflict with
    c13 (same source; check the conditions); possible conflict with c15 (same source; check the conditions)
- claim_id: c15
  attr: rated_output_current
  value:
    nominal: 60
    unit: unit:A
  conditions: Rated current with 10 mm2 cable, per assembly instructions
  cite:
  - src: src:eq-connectors-amphenol-h4-assembly-instructions
    loc: sec=h1
    h: 6680d05e01a8
  review: disputed
  conflicts_with:
  - prod:amphenol-helios-h4#c9
  - prod:amphenol-helios-h4#c10
  - prod:amphenol-helios-h4#c11
  review_note: possible conflict with c12 (same source; check the conditions); possible conflict with
    c13 (same source; check the conditions); possible conflict with c14 (same source; check the conditions)
- claim_id: c16
  attr: operating_temperature
  value:
    min: -40
    max: 85
    unit: unit:DEG_C
  conditions: Ambient temperature range, product datasheet
  cite:
  - src: src:eq-connectors-amphenol-ids-17-helios-h4
    loc: tbl=1.r12
    h: 4f549b78cd0d
  - src: src:eq-connectors-amphenol-ids-17-helios-h4
    loc: tbl=1.r13
    h: 2f29da8bbb28
  review: drafted
- claim_id: c17
  attr: operating_temperature
  value:
    min: -40
    max: 90
    unit: unit:DEG_C
  conditions: Ambient temperature range, per assembly instructions
  cite:
  - src: src:eq-connectors-amphenol-h4-assembly-instructions
    loc: sec=h1
    h: 6680d05e01a8
  review: drafted
---
The Amphenol Helios H4 is a PV DC connector family from Amphenol Industrial Solar Technologies, used on modules, inverters and optimizers. It is rated 1000 V under UL and up to 1500 V under IEC. Its current rating depends on cable size, and the datasheet and the assembly instructions give different figures. Mated connectors are rated IP68 and safety class II, with a flame class of UL94 V-0. The ambient range starts at -40°C and goes up to 85°C or 90°C, depending on the document. The snap-lock meets NEC 2008 690.33, so you need a tool such as the H4TW0001 wrench or the H4TU0000 universal tool to un-mate it. Never unplug it under load. First switch off the converter or open the DC circuit, and isolate the connector from the supply before assembling or taking it apart. Fit sealing caps on unmated connectors. Avoid non-tinned H07RN-F cable, because oxidised copper can push crimp contact resistance past its limits.

<!-- review notes
- sentence 1: support check: partial - Passages support Amphenol AIST H4 PV connector used on inverters and optimizers, but use on modules is not clearly stated (u5 only lists connector types).
- sentence 2: support check: partial - Voltage ratings 1000V UL and 1500V IEC and differing current figures are shown, but u9 says 1000V IEC and 'up to' framing is mixed; mostly supported.
-->
