---
id: func:volt-var
type: Function
name: Volt-VAr
aliases:
- voltage-reactive power mode
- Q(U)
- Q(V)
- volt-var control
- DVVR
category: Grid support
function_kind: grid-support
claims:
- claim_id: c1
  rel: part_of
  target: std:ieee-1547-2018
  note: Specified as one of the voltage and reactive power control functions for Category A and B DER.
  quote: Voltage-reactive power mode may also be commonly referred to as "volt-var" mode.
  quote_source: IEEE 1547-2018 §5.1, Table 6 note a
  cite:
  - src: src:std-standards-ieee-ieee-1547-2018
    loc: sec=5.1
    h: 4851fce19c76
  - src: src:std-standards-ieee-default-ieee1547-2018-settings-requirements-2022-12-13
    loc: tbl=3.r3
    h: 8cb5a25c9800
  review: drafted
  review_note: 'support check: partial - Passages show voltage-reactive power (volt-var) mode in Table
    6 for Category A and B DER, but the table''s contents aren''t shown; the ''one of the functions''
    framing is only implied.'
- claim_id: c2
  attr: default_value
  value:
    nominal: 213
    unit: unit:V
  conditions: Solis inverter, Volt-Var curve voltage point 1, EN50549 grid standard
  cite:
  - src: src:kb-solis-44002460844-how-to-enable-volt-var-q-u-function
    loc: sec=h1
    h: 8a8bc8849d66
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions); possible conflict with c6
    (same source; check the conditions); possible conflict with c8 (same source; check the conditions)
- claim_id: c3
  attr: setting_range
  value:
    min: 210
    max: 230
    unit: unit:V
  conditions: Solis inverter, Volt-Var curve voltage point 1, EN50549 grid standard
  cite:
  - src: src:kb-solis-44002460844-how-to-enable-volt-var-q-u-function
    loc: sec=h1
    h: 8a8bc8849d66
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions)
- claim_id: c4
  attr: default_value
  value:
    nominal: 223
    unit: unit:V
  conditions: Solis inverter, Volt-Var curve voltage point 2, EN50549 grid standard
  cite:
  - src: src:kb-solis-44002460844-how-to-enable-volt-var-q-u-function
    loc: sec=h1
    h: 8a8bc8849d66
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c6
    (same source; check the conditions); possible conflict with c8 (same source; check the conditions)
- claim_id: c5
  attr: setting_range
  value:
    min: 210
    max: 230
    unit: unit:V
  conditions: Solis inverter, Volt-Var curve voltage point 2, EN50549 grid standard
  cite:
  - src: src:kb-solis-44002460844-how-to-enable-volt-var-q-u-function
    loc: sec=h1
    h: 8a8bc8849d66
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions)
- claim_id: c6
  attr: default_value
  value:
    nominal: 236
    unit: unit:V
  conditions: Solis inverter, Volt-Var curve voltage point 3, EN50549 grid standard
  cite:
  - src: src:kb-solis-44002460844-how-to-enable-volt-var-q-u-function
    loc: sec=h1
    h: 8a8bc8849d66
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions); possible conflict with c8 (same source; check the conditions)
- claim_id: c7
  attr: setting_range
  value:
    min: 230
    max: 255
    unit: unit:V
  conditions: Solis inverter, Volt-Var curve voltage point 3, EN50549 grid standard
  cite:
  - src: src:kb-solis-44002460844-how-to-enable-volt-var-q-u-function
    loc: sec=h1
    h: 8a8bc8849d66
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c8
  attr: default_value
  value:
    nominal: 246
    unit: unit:V
  conditions: Solis inverter, Volt-Var curve voltage point 4, EN50549 grid standard
  cite:
  - src: src:kb-solis-44002460844-how-to-enable-volt-var-q-u-function
    loc: sec=h1
    h: 8a8bc8849d66
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions); possible conflict with c6 (same source; check the conditions)
- claim_id: c9
  attr: setting_range
  value:
    min: 240
    max: 265
    unit: unit:V
  conditions: Solis inverter, Volt-Var curve voltage point 4, EN50549 grid standard
  cite:
  - src: src:kb-solis-44002460844-how-to-enable-volt-var-q-u-function
    loc: sec=h1
    h: 8a8bc8849d66
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c5
    (same source; check the conditions)
- claim_id: c10
  attr: default_value
  value:
    nominal: 48
    unit: unit:PERCENT
  conditions: Solis inverter, leading reactive power level of the Volt-Var curve, EN50549 grid standard
  cite:
  - src: src:kb-solis-44002460844-how-to-enable-volt-var-q-u-function
    loc: sec=h1
    h: 8a8bc8849d66
  review: drafted
  review_note: possible conflict with c12 (same source; check the conditions); possible conflict with
    c14 (same source; check the conditions); possible conflict with c15 (same source; check the conditions)
- claim_id: c11
  attr: setting_range
  value:
    min: 0
    max: 60
    unit: unit:PERCENT
  conditions: Solis inverter, leading reactive power level of the Volt-Var curve, EN50549 grid standard
  cite:
  - src: src:kb-solis-44002460844-how-to-enable-volt-var-q-u-function
    loc: sec=h1
    h: 8a8bc8849d66
  review: drafted
- claim_id: c12
  attr: default_value
  value:
    nominal: -48
    unit: unit:PERCENT
  conditions: Solis inverter, lagging reactive power level of the Volt-Var curve, EN50549 grid standard
  cite:
  - src: src:kb-solis-44002460844-how-to-enable-volt-var-q-u-function
    loc: sec=h1
    h: 8a8bc8849d66
  review: drafted
  review_note: possible conflict with c10 (same source; check the conditions); possible conflict with
    c14 (same source; check the conditions); possible conflict with c15 (same source; check the conditions)
- claim_id: c13
  attr: setting_range
  value:
    min: -60
    max: 0
    unit: unit:PERCENT
  conditions: Solis inverter, lagging reactive power level of the Volt-Var curve, EN50549 grid standard
  cite:
  - src: src:kb-solis-44002460844-how-to-enable-volt-var-q-u-function
    loc: sec=h1
    h: 8a8bc8849d66
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c14
  attr: default_value
  value:
    nominal: 20
    unit: unit:PERCENT
  conditions: Solis inverter, P lock-in active power level that turns Q(U) on, EN50549 grid standard
  cite:
  - src: src:kb-solis-44002460844-how-to-enable-volt-var-q-u-function
    loc: sec=h1
    h: 8a8bc8849d66
  review: drafted
  review_note: possible conflict with c10 (same source; check the conditions); possible conflict with
    c12 (same source; check the conditions); possible conflict with c15 (same source; check the conditions)
- claim_id: c15
  attr: default_value
  value:
    nominal: 5
    unit: unit:PERCENT
  conditions: Solis inverter, P lock-out active power level that turns Q(U) off, EN50549 grid standard
  cite:
  - src: src:kb-solis-44002460844-how-to-enable-volt-var-q-u-function
    loc: sec=h1
    h: 8a8bc8849d66
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c10 (same source; check the conditions); possible conflict with
    c12 (same source; check the conditions); possible conflict with c14 (same source; check the conditions)
---
Volt-VAr changes the reactive power output in response to grid voltage, following a programmable curve. It injects reactive power when voltage is below nominal and absorbs it when voltage is above nominal. IEEE 1547-2018 calls this the voltage-reactive power mode. One set of default settings requirements for that standard lists the function as OFF by default. The curve is set with four voltage points (V1 to V4), a reactive power value at each point (Q1 to Q4), and a response time constant for reaching 95% of the requested reactive power. In the Tesla commercial controls manuals, Volt-VAr is an open-loop response to voltage measured at the point of interconnection meter. Its output is added to any direct reactive power command, and the curve can be written over Modbus or DNP3. On Solis inverters using the EN50549 grid standard, you turn Q(U) on from the inverter screen under Working Mode, Mode 2. It can deliver up to 60% reactive power, and P lock-in and lock-out levels switch the mode on and off. With the SMA Data Manager M, Q(U) needs exactly one meter at the point of interconnection, and that meter must measure both voltage and current. Splitting the voltage and current measurements across two meters produces faulty power values.

<!-- review notes
- sentence 6: support check: partial - Passages say only one measuring device is supported at the POI, it must measure both voltage and current, and splitting gives mismatched values; but they don't name Data Manager M's 'exactly one' meter requirement beyond 'Data Manager' and say 'faulty measurements' rather than specifically power values (they do say active/reactive power values), so minor detail on product variant.
-->
