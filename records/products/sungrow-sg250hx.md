---
id: prod:sungrow-sg250hx
type: Product
name: Sungrow SG250HX-US
aliases:
- SG250HX
- SG250HX-US
category: Inverters
make: sungrow
product_level: family
model_number: SG250HX-US
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sungrow
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=h3
    h: 71a81a880591
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: sec=h5
    h: 1ad69086d46a
  review: drafted
- claim_id: c2
  attr: max_input_voltage
  value:
    max: 1500
    unit: unit:V
  conditions: Maximum PV input voltage
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=47
    h: 980c7f82774f
  review: drafted
- claim_id: c3
  attr: mppt_voltage_range
  value:
    min: 500
    max: 1500
    unit: unit:V
  conditions: Full MPP voltage range
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=47
    h: 980c7f82774f
  review: drafted
- claim_id: c4
  attr: mppt_voltage_range
  value:
    min: 860
    max: 1300
    unit: unit:V
  conditions: MPP voltage range for nominal power
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=47
    h: 980c7f82774f
  review: drafted
- claim_id: c5
  attr: max_input_current
  value:
    nominal: 30
    unit: unit:A
  conditions: Per MPP input (12 independent inputs); also max current per input connector
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=47
    h: 980c7f82774f
  review: drafted
- claim_id: c6
  attr: rated_power
  value:
    nominal: 250
    unit: unit:KiloV-A
  conditions: AC output power at 30 °C ambient
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=47
    h: 980c7f82774f
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
  review_note: possible conflict with c7 (same source; check the conditions); possible conflict with c8
    (same source; check the conditions)
- claim_id: c7
  attr: rated_power
  value:
    nominal: 225
    unit: unit:KiloV-A
  conditions: AC output power at 40 °C ambient
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=47
    h: 980c7f82774f
  review: drafted
  review_note: possible conflict with c6 (same source; check the conditions); possible conflict with c8
    (same source; check the conditions)
- claim_id: c8
  attr: rated_power
  value:
    nominal: 200
    unit: unit:KiloV-A
  conditions: AC output power at 50 °C ambient
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=47
    h: 980c7f82774f
  review: drafted
  review_note: possible conflict with c6 (same source; check the conditions); possible conflict with c7
    (same source; check the conditions)
- claim_id: c9
  attr: rated_output_current
  value:
    max: 180.5
    unit: unit:A
  conditions: Maximum AC output current
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=47
    h: 980c7f82774f
  review: drafted
- claim_id: c10
  attr: nominal_voltage
  value:
    nominal: 800
    unit: unit:V
  conditions: Nominal AC voltage, three-phase plus PE
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=47
    h: 980c7f82774f
  review: drafted
- claim_id: c11
  attr: nominal_voltage
  value:
    min: 680
    max: 880
    unit: unit:V
  conditions: Permitted AC voltage range
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=47
    h: 980c7f82774f
  review: drafted
  review_note: 'support check: partial - The 680–880 V AC voltage range is listed, but it is a range,
    not a nominal voltage; the statement''s wording is loose though its condition says permitted range.'
- claim_id: c12
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Nominal grid frequency
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=47
    h: 980c7f82774f
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c13
  attr: frequency
  value:
    min: 55
    max: 65
    unit: unit:HZ
  conditions: Grid frequency range
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=47
    h: 980c7f82774f
  review: drafted
- claim_id: c14
  attr: efficiency
  value:
    nominal: 99
    unit: unit:PERCENT
  conditions: Maximum efficiency
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=47
    h: 980c7f82774f
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=47.r22
    h: 81e82adda4ef
  review: drafted
  review_note: possible conflict with c15 (same source; check the conditions)
- claim_id: c15
  attr: efficiency
  value:
    nominal: 98.5
    unit: unit:PERCENT
  conditions: European weighted efficiency
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=47
    h: 980c7f82774f
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=47.r22
    h: 81e82adda4ef
  review: drafted
  review_note: possible conflict with c14 (same source; check the conditions)
- claim_id: c16
  rel: uses_protocol
  target: proto:rs485
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=48.r23
    h: 9afb7fef49e4
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c17
  rel: implements
  target: func:mppt
  note: 12 independent MPP inputs
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=47
    h: 980c7f82774f
  review: drafted
- claim_id: c18
  rel: implements
  target: func:reverse-polarity-protection
  note: DC reverse connection protection listed as Yes
  cite:
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=47
    h: 980c7f82774f
  review: drafted
---
The Sungrow SG250HX-US is a grid-connected PV string inverter for three-phase 800 V systems. It accepts up to 1500 V DC on 12 independent MPP inputs, each rated for 30 A, and tracks across 500 V to 1500 V, with full power between 860 V and 1300 V. AC output is 250 kVA at 30 °C, falling to 225 kVA at 40 °C and 200 kVA at 50 °C, and AC current is limited to 180.5 A at a nominal 60 Hz. The datasheet lists 99.0% maximum efficiency and 98.5% European efficiency. It has DC reverse connection protection and grid monitoring, and communicates over RS485. Fault 106, Grounding Cable Fault, means checking the ground cable connection and its insulation from live conductors, then calling Sungrow service if the fault stays. Many codes are grouped as System Fault: open the AC and DC switches, close them again after 15 minutes, and call Sungrow service if the fault comes back.

<!-- review notes
- sentence 6: support check: partial - The passage is truncated and only shows checking ground cable insulation and contacting service, but the check of connection is only implied by the fragment '...connected.'
- sentence 1: review: partial - Grid-connected PV inverter and nominal AC voltage 3/PE, 800 V are supported, but nothing in the cited passages calls it a string inverter.
-->
