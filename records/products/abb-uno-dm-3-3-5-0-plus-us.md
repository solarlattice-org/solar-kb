---
id: prod:abb-uno-dm-3-3-5-0-plus-us
type: Product
name: UNO-DM-3.3/3.8/4.6/5.0-TL-PLUS-US string inverter
aliases:
- UNO-DM-3.3-TL-PLUS
- UNO-DM-3.8-TL-PLUS
- UNO-DM-4.6-TL-PLUS
- UNO-DM-5.0-TL-PLUS
- UNO-DM-3.3-5.0-TL-PLUS-US
- UNO-DM-4.6-PLUS
- UNO-DM-5.0-PLUS
- UNO-DM-3.3-PLUS
- UNO-DM-3.8-PLUS
category: Inverters
make: abb
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:abb
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: sec=h1
    h: 5bda5a0c5340
  review: drafted
- claim_id: c2
  rel: uses_protocol
  target: proto:modbus-rtu
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=11.r3
    h: 3e1610df8945
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:sunspec-modbus
  note: Listed as ModBus RTU (SunSpec).
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=11.r3
    h: 3e1610df8945
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:aurora-protocol
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=11.r3
    h: 3e1610df8945
  review: drafted
- claim_id: c5
  rel: implements
  target: func:dc-arc-fault-protection
  note: AFD listed for the -SB-RA model versions, which also include a DC switch, wiring box and RSD supply
    output.
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=11.r27
    h: 65d2ab8ce41a
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=9.r27
    h: 661f0b626423
  review: drafted
- claim_id: c6
  rel: implements
  target: func:constant-power-factor
  note: Power factor above 0.995, adjustable to +/-0.8.
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=8.r31
    h: 4946bac7c607
  review: drafted
  review_note: 'support check: partial - The passage only gives PF >0.995 adj. ±0.8 for the 3.3/3.8 models,
    not 4.6/5.0, and doesn''t explicitly say constant PF mode.'
- claim_id: c7
  attr: rated_power
  value:
    nominal: 4600
    unit: unit:W
  conditions: UNO-DM-4.6-PLUS, at 240 Vac
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=17.r20
    h: 5524bc870f66
  review: disputed
  review_note: possible conflict with c8 (same source; check the conditions)
  conflicts_with:
  - prod:abb-uno-dm-3-3-5-0-plus-us#c9
  - prod:abb-uno-dm-3-3-5-0-plus-us#c10
- claim_id: c8
  attr: rated_power
  value:
    nominal: 5000
    unit: unit:W
  conditions: UNO-DM-5.0-PLUS, at 240 Vac
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=17.r20
    h: 5524bc870f66
  review: disputed
  review_note: possible conflict with c7 (same source; check the conditions)
  conflicts_with:
  - prod:abb-uno-dm-3-3-5-0-plus-us#c9
  - prod:abb-uno-dm-3-3-5-0-plus-us#c10
- claim_id: c9
  attr: rated_power
  value:
    nominal: 3300
    unit: unit:W
  conditions: UNO-DM-3.3-PLUS, maximum output power at cos phi = 1, 240 Vac (US-Q manual RevB)
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=8.r22
    h: b7ee34723400
  review: disputed
  conflicts_with:
  - prod:abb-uno-dm-3-3-5-0-plus-us#c7
  - prod:abb-uno-dm-3-3-5-0-plus-us#c8
  review_note: possible conflict with c10 (same source; check the conditions)
- claim_id: c10
  attr: rated_power
  value:
    nominal: 4200
    unit: unit:W
  conditions: UNO-DM-3.8-PLUS, maximum output power at cos phi = 1, 240 Vac (US-Q manual RevB)
  cite:
  - src: src:abb-fimer-uno-dm-3-3-5-0-tl-plus-us-q-product-manual-revb
    loc: tbl=8.r22
    h: b7ee34723400
  review: disputed
  conflicts_with:
  - prod:abb-uno-dm-3-3-5-0-plus-us#c7
  - prod:abb-uno-dm-3-3-5-0-plus-us#c8
  review_note: possible conflict with c9 (same source; check the conditions)
- claim_id: c11
  attr: max_input_voltage
  value:
    nominal: 600
    unit: unit:V
  conditions: Absolute maximum DC input voltage (Vmax,abs), UNO-DM-4.6-PLUS and UNO-DM-5.0-PLUS
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=17.r36
    h: a539d4883a61
  review: drafted
  review_note: 'support check: partial - The 600 V appears only as a column label next to the Vmax,abs
    row, without a clear value statement.'
- claim_id: c12
  attr: efficiency
  value:
    nominal: 97
    unit: unit:PERCENT
  conditions: Maximum efficiency, UNO-DM-4.6-PLUS
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=17.r36
    h: a539d4883a61
  review: drafted
  review_note: possible conflict with c13 (same source; check the conditions); possible conflict with
    c14 (same source; check the conditions); possible conflict with c15 (same source; check the conditions);
    possible conflict with c16 (same source; check the conditions)
- claim_id: c13
  attr: efficiency
  value:
    nominal: 97.4
    unit: unit:PERCENT
  conditions: Maximum efficiency, UNO-DM-5.0-PLUS
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=17.r36
    h: a539d4883a61
  review: drafted
  review_note: possible conflict with c12 (same source; check the conditions); possible conflict with
    c14 (same source; check the conditions); possible conflict with c15 (same source; check the conditions);
    possible conflict with c16 (same source; check the conditions); possible conflict with c17 (same source;
    check the conditions)
- claim_id: c14
  attr: efficiency
  value:
    nominal: 96
    unit: unit:PERCENT
  conditions: CEC efficiency, UNO-DM-4.6-PLUS at 208 Vac
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=17.r37
    h: d977f0ab02c0
  review: drafted
  review_note: possible conflict with c12 (same source; check the conditions); possible conflict with
    c13 (same source; check the conditions); possible conflict with c15 (same source; check the conditions);
    possible conflict with c16 (same source; check the conditions); possible conflict with c17 (same source;
    check the conditions)
- claim_id: c15
  attr: efficiency
  value:
    nominal: 96.5
    unit: unit:PERCENT
  conditions: CEC efficiency, UNO-DM-4.6-PLUS at 240 Vac
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=17.r37
    h: d977f0ab02c0
  review: drafted
  review_note: possible conflict with c12 (same source; check the conditions); possible conflict with
    c13 (same source; check the conditions); possible conflict with c14 (same source; check the conditions);
    possible conflict with c17 (same source; check the conditions)
- claim_id: c16
  attr: efficiency
  value:
    nominal: 96.5
    unit: unit:PERCENT
  conditions: CEC efficiency, UNO-DM-5.0-PLUS at 208 Vac
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=17.r37
    h: d977f0ab02c0
  review: drafted
  review_note: possible conflict with c12 (same source; check the conditions); possible conflict with
    c13 (same source; check the conditions); possible conflict with c14 (same source; check the conditions);
    possible conflict with c17 (same source; check the conditions)
- claim_id: c17
  attr: efficiency
  value:
    nominal: 97
    unit: unit:PERCENT
  conditions: CEC efficiency, UNO-DM-5.0-PLUS at 240 Vac
  cite:
  - src: src:abb-uno-dm-3-3-5-0-tl-plus-us-product-manual-reva
    loc: tbl=17.r37
    h: d977f0ab02c0
  review: drafted
  review_note: possible conflict with c13 (same source; check the conditions); possible conflict with
    c14 (same source; check the conditions); possible conflict with c15 (same source; check the conditions);
    possible conflict with c16 (same source; check the conditions)
---
At 240 Vac the 4.6 model is rated 4600 W and the 5.0 model 5000 W. The later manual lists maximum output of 3300 W for the 3.3 model and 4200 W for the 3.8 model. For communication it uses Modbus RTU with SunSpec and the Aurora Protocol. The -SB-RA model versions add a DC switch, a wiring box, arc fault detection and a supply output for rapid shutdown.
