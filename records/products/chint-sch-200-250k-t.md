---
id: prod:chint-sch-200-250k-t
type: Product
name: CPS SCH200K-T-US-480 / SCH250K-T-US-600
aliases:
- SCH 200 K T US 480
- SCH 250 K T US 600
- SCH 200 250 K T
category: Inverters
make: chint
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:chint
  note: Models are branded CPS, and the manual refers fault escalation to CPS Customer Service.
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=45.r29
    h: ca6adb56f2a4
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=41.r1
    h: 77985fbffbd6
  review: drafted
  review_note: 'support check: partial - Passages show CPS branding and CPS Customer Service, but never
    state the maker is CHINT POWER SYSTEMS.'
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=45.r28
    h: e44f4493cfe8
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=45.r13
    h: 439bb1376480
  review: drafted
  review_note: 'support check: partial - Passages describe a transformerless unit with AC output power,
    implying an inverter, but never say it is an inverter explicitly.'
- claim_id: c3
  rel: implements
  target: func:mppt
  note: Each model has a single MPP tracker.
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=45.r6
    h: 257d6eafbd04
  review: drafted
  review_note: 'support check: partial - Single MPP tracker per model is stated, implying MPPT, though
    MPPT is not named explicitly.'
- claim_id: c4
  rel: implements
  target: func:constant-power-factor
  note: Power factor above 0.99 by default, adjustable to ±0.8.
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=45.r22
    h: 75c28bcd594f
  review: drafted
- claim_id: c5
  rel: implements
  target: func:surge-protection
  note: DC side uses Type II MOV surge protection.
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=45.r11
    h: 41a053f375ab
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c6
  rel: implements
  target: func:dc-arc-fault-protection
  note: Arc board, with an arc fault test that can be run from the app Settings menu.
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=43.r7
    h: 29641da34bb0
  review: drafted
- claim_id: c7
  rel: uses_protocol
  target: proto:modbus
  conditions: Modbus map lists firmware V01.15 as applicable for SCH250K-T-US-600 / SCH200K-T-US-480
  cite:
  - src: src:chint-cps-200-250kw-k-t-modbus-map-2026-01-30
    loc: tbl=2.r1
    h: 73fa01820a3d
  review: drafted
  review_note: 'support check: partial - The map lists firmware V01.15 as applicable to both models, but
    the passage doesn''t name Modbus as the protocol.; review: partial - The row only lists applicable
    models and firmware V01.15; Modbus appears only in the source document''s name (a Modbus map), not
    in the passage text.'
- claim_id: c8
  attr: rated_power
  value:
    nominal: 200
    unit: unit:KiloW
  conditions: CPS SCH200K-T-US-480 rated AC output power; subject to AC output derating
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=45.r13
    h: 439bb1376480
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions)
- claim_id: c9
  attr: rated_power
  value:
    nominal: 250
    unit: unit:KiloW
  conditions: CPS SCH250K-T-US-600 rated AC output power; subject to AC output derating
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=45.r13
    h: 439bb1376480
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions)
- claim_id: c10
  attr: efficiency
  value:
    nominal: 98.5
    unit: unit:PERCENT
  conditions: Maximum (peak) efficiency, CPS SCH200K-T-US-480
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=45.r29
    h: ca6adb56f2a4
  review: drafted
  review_note: possible conflict with c11 (same source; check the conditions); possible conflict with
    c12 (same source; check the conditions); possible conflict with c13 (same source; check the conditions)
- claim_id: c11
  attr: efficiency
  value:
    nominal: 98.8
    unit: unit:PERCENT
  conditions: Maximum (peak) efficiency, CPS SCH250K-T-US-600
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=45.r29
    h: ca6adb56f2a4
  review: drafted
  review_note: possible conflict with c10 (same source; check the conditions); possible conflict with
    c12 (same source; check the conditions); possible conflict with c13 (same source; check the conditions)
- claim_id: c12
  attr: efficiency
  value:
    nominal: 98
    unit: unit:PERCENT
  conditions: CEC efficiency, CPS SCH200K-T-US-480
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=45.r30
    h: 42e3440263d5
  review: drafted
  review_note: possible conflict with c10 (same source; check the conditions); possible conflict with
    c11 (same source; check the conditions); possible conflict with c13 (same source; check the conditions)
- claim_id: c13
  attr: efficiency
  value:
    nominal: 98.4
    unit: unit:PERCENT
  conditions: CEC efficiency, CPS SCH250K-T-US-600
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=45.r30
    h: 42e3440263d5
  review: drafted
  review_note: possible conflict with c10 (same source; check the conditions); possible conflict with
    c11 (same source; check the conditions); possible conflict with c12 (same source; check the conditions)
- claim_id: c14
  attr: nominal_voltage
  value:
    nominal: 480
    unit: unit:V
  conditions: Rated AC output voltage, CPS SCH200K-T-US-480
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=45.r15
    h: 068b2178adb6
  review: drafted
  review_note: possible conflict with c15 (same source; check the conditions)
- claim_id: c15
  attr: nominal_voltage
  value:
    nominal: 600
    unit: unit:V
  conditions: Rated AC output voltage, CPS SCH250K-T-US-600
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=45.r15
    h: 068b2178adb6
  review: drafted
  review_note: possible conflict with c14 (same source; check the conditions)
- claim_id: c16
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Rated output frequency, both models
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=45.r20
    h: c031c9413628
  review: drafted
- claim_id: c17
  attr: frequency
  value:
    min: 57
    max: 63
    unit: unit:HZ
  conditions: Output frequency range, both models
  cite:
  - src: src:chint-cps-sch200-250k-t-us-user-manual-aug-2026
    loc: tbl=45.r21
    h: ffe7c7a222a4
  review: drafted
---
This CPS family has two transformerless three-phase string inverters, the SCH200K-T-US-480 and the SCH250K-T-US-600. The 480 V model is rated at 200 kW AC and the 600 V model at 250 kW AC, both at 60 Hz. Output derating applies. Peak efficiency is 98.5% for the 200 kW model and 98.8% for the 250 kW model. CEC efficiency is 98.0% and 98.4%. Each unit has a single MPP tracker that operates from 860 to 1450 Vdc and starts up at 900 V. Power factor is adjustable to ±0.8. The DC side has Type II MOV surge protection and either DC switches or a DC disconnect, depending on the wire box type. An arc board provides DC arc detection. If ArcboardErr appears, check the arc board logic connector, run the arc fault test from the app, and replace the arc board or wire box if the alarm comes back. Common faults include CommErr, an internal communication failure, and ExtFanErr or IntFanErr, a cooling fan failure. For either, wait five minutes, check the fans for foreign objects, and reboot by switching off the three-phase supply before calling CPS service. A Modbus register map covers both models and lists firmware V01.15 as applicable.

<!-- review notes
- sentence 1: support check: partial - Two transformerless models are shown, but 'three-phase' and 'string inverter' are not stated in the passages.
- sentence 8: support check: partial - The passage lists V01.15 as applicable firmware for both models, but doesn't say it is a Modbus register map.
- sentence 1: review: partial - The passages show both models and that they are transformerless, but they do not say three-phase or string inverter.
- sentence 7: review: partial - The fault meanings and steps are supported, but the fan foreign-object check appears only for the fan errors, so 'for either' wrongly applies it to CommErr too.
-->
